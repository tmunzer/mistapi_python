# tests/unit/test_api_request.py
"""
Comprehensive unit tests for mistapi.__api_request.APIRequest.

Tests cover URL generation, query string encoding, token rotation,
proxy logging, header sanitisation, rate-limit handling, the shared
retry wrapper, and each HTTP-method convenience function.
"""

import json
from unittest.mock import Mock, patch

import pytest
import requests
from requests.exceptions import HTTPError

from mistapi.__api_request import APIRequest
from mistapi.__api_response import APIResponse


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_api_request(cloud_uri="api.mist.com", tokens=None):
    """Create an APIRequest with a mocked session for isolated testing."""
    with patch("mistapi.__api_request.requests.session") as mock_session_cls:
        mock_session = Mock()
        mock_session.headers = {}
        mock_session.proxies = {}
        mock_session.cookies = {}
        mock_session_cls.return_value = mock_session

        req = APIRequest()
        req._session = mock_session
        req._cloud_uri = cloud_uri

        if tokens:
            req._apitoken = list(tokens)
            req._apitoken_index = 0
            req._session.headers.update({"Authorization": "Token " + tokens[0]})
        return req


def _mock_response(
    status_code=200,
    json_data=None,
    headers=None,
    raise_for_status_effect=None,
):
    """Build a mock requests.Response."""
    resp = Mock(spec=requests.Response)
    resp.status_code = status_code
    resp.headers = headers or {}
    resp.json.return_value = json_data if json_data is not None else {}
    resp.content = json.dumps(json_data or {}).encode()

    # For _remove_auth_from_headers — attach a mock PreparedRequest
    prep = Mock()
    prep.headers = {}
    resp.request = prep

    if raise_for_status_effect:
        resp.raise_for_status.side_effect = raise_for_status_effect
    else:
        resp.raise_for_status.return_value = None
    return resp


# ===========================================================================
# Tests
# ===========================================================================


class TestUrl:
    """APIRequest._url() builds the full URL from cloud_uri + uri."""

    def test_basic_url(self):
        req = _make_api_request("api.mist.com")
        assert req._url("/api/v1/self") == "https://api.mist.com/api/v1/self"

    def test_empty_uri(self):
        req = _make_api_request("api.mist.com")
        assert req._url("") == "https://api.mist.com"

    def test_eu_host(self):
        req = _make_api_request("api.eu.mist.com")
        assert req._url("/api/v1/orgs") == "https://api.eu.mist.com/api/v1/orgs"

    def test_uri_with_path_segments(self):
        req = _make_api_request("api.mist.com")
        org_id = "203d3d02-dbc0-4c1b-9f41-76896a3330f4"
        uri = f"/api/v1/orgs/{org_id}/sites"
        assert req._url(uri) == f"https://api.mist.com{uri}"


class TestGenQuery:
    """APIRequest._gen_query() builds URL-encoded query strings."""

    def test_none_returns_empty(self):
        req = _make_api_request()
        assert req._gen_query(None) == ""

    def test_empty_dict_returns_empty(self):
        req = _make_api_request()
        assert req._gen_query({}) == ""

    def test_single_param(self):
        req = _make_api_request()
        assert req._gen_query({"page": "2"}) == "?page=2"

    def test_multiple_params(self):
        req = _make_api_request()
        result = req._gen_query({"page": "1", "limit": "100"})
        assert result.startswith("?")
        assert "page=1" in result
        assert "limit=100" in result

    def test_special_chars_encoded(self):
        req = _make_api_request()
        result = req._gen_query({"filter": "name=hello world&foo"})
        assert "?" in result
        # urllib.parse.urlencode encodes spaces as + and & as %26
        assert "hello+world" in result or "hello%20world" in result
        assert "%26" in result

    def test_preserves_insertion_order(self):
        req = _make_api_request()
        # dict preserves insertion order in Python 3.7+
        result = req._gen_query({"a": "1", "b": "2", "c": "3"})
        assert result == "?a=1&b=2&c=3"


class TestNextApiToken:
    """APIRequest._next_apitoken() rotates through tokens and raises
    RuntimeError when only one token is available."""

    def test_rotates_to_next_token(self):
        req = _make_api_request(tokens=["tok_aaa1", "tok_bbb2", "tok_ccc3"])
        req._apitoken_index = 0
        req._next_apitoken()
        assert req._apitoken_index == 1
        assert req._session.headers["Authorization"] == "Token tok_bbb2"

    def test_wraps_around_to_first_token(self):
        req = _make_api_request(tokens=["tok_aaa1", "tok_bbb2"])
        req._apitoken_index = 1
        req._next_apitoken()
        assert req._apitoken_index == 0
        assert req._session.headers["Authorization"] == "Token tok_aaa1"

    def test_single_token_raises_runtime_error(self):
        req = _make_api_request(tokens=["tok_only1"])
        req._apitoken_index = 0
        with pytest.raises(RuntimeError, match="API rate limit reached"):
            req._next_apitoken()

    def test_rotation_cycle(self):
        tokens = ["tok_aaa1", "tok_bbb2", "tok_ccc3"]
        req = _make_api_request(tokens=tokens)
        req._apitoken_index = 0
        # Rotate through all tokens and back
        req._next_apitoken()
        assert req._apitoken_index == 1
        req._next_apitoken()
        assert req._apitoken_index == 2
        req._next_apitoken()
        assert req._apitoken_index == 0


class TestLogProxy:
    """APIRequest._log_proxy() prints a masked proxy URL."""

    def test_prints_masked_proxy(self, capsys):
        req = _make_api_request()
        req._session.proxies = {
            "https": "http://user:secret_password@proxy.example.com:8080"
        }
        req._log_proxy()
        captured = capsys.readouterr()
        assert "proxy.example.com:8080" in captured.out
        assert "*********" in captured.out
        assert "secret_password" not in captured.out

    def test_no_proxy_does_nothing(self, capsys):
        req = _make_api_request()
        req._session.proxies = {}
        req._log_proxy()
        captured = capsys.readouterr()
        assert captured.out == ""

    def test_proxy_without_password(self, capsys):
        req = _make_api_request()
        req._session.proxies = {"https": "http://proxy.example.com:8080"}
        req._log_proxy()
        captured = capsys.readouterr()
        assert "proxy.example.com:8080" in captured.out


class TestRemoveAuthFromHeaders:
    """APIRequest._remove_auth_from_headers() masks sensitive headers."""

    def test_masks_authorization(self):
        req = _make_api_request()
        resp = Mock()
        resp.request.headers = {"Authorization": "Token secret123"}
        headers = req._remove_auth_from_headers(resp)
        assert headers["Authorization"] == "***hidden***"

    def test_masks_csrf_token(self):
        req = _make_api_request()
        resp = Mock()
        resp.request.headers = {"X-CSRFToken": "csrf_value"}
        headers = req._remove_auth_from_headers(resp)
        assert headers["X-CSRFToken"] == "***hidden***"

    def test_masks_cookie(self):
        req = _make_api_request()
        resp = Mock()
        resp.request.headers = {"Cookie": "session=abc123"}
        headers = req._remove_auth_from_headers(resp)
        assert headers["Cookie"] == "***hidden***"

    def test_masks_all_three(self):
        req = _make_api_request()
        resp = Mock()
        resp.request.headers = {
            "Authorization": "Token x",
            "X-CSRFToken": "y",
            "Cookie": "z",
            "Content-Type": "application/json",
        }
        headers = req._remove_auth_from_headers(resp)
        assert headers["Authorization"] == "***hidden***"
        assert headers["X-CSRFToken"] == "***hidden***"
        assert headers["Cookie"] == "***hidden***"
        # Non-sensitive header left untouched
        assert headers["Content-Type"] == "application/json"

    def test_leaves_non_sensitive_headers(self):
        req = _make_api_request()
        resp = Mock()
        resp.request.headers = {
            "Accept": "application/json",
            "User-Agent": "python-requests/2.32",
        }
        headers = req._remove_auth_from_headers(resp)
        assert headers["Accept"] == "application/json"
        assert headers["User-Agent"] == "python-requests/2.32"


class TestHandleRateLimit:
    """APIRequest._handle_rate_limit() sleeps according to Retry-After
    header or falls back to exponential backoff."""

    @patch("mistapi.__api_request.time.sleep")
    def test_uses_retry_after_header(self, mock_sleep):
        req = _make_api_request()
        resp = Mock()
        resp.headers = {"Retry-After": "10"}
        req._handle_rate_limit(resp, attempt=0)
        mock_sleep.assert_called_once_with(10)

    @patch("mistapi.__api_request.time.sleep")
    def test_exponential_backoff_when_no_header(self, mock_sleep):
        req = _make_api_request()
        resp = Mock()
        resp.headers = {}
        # attempt 0 => 5 * (2**0) = 5
        req._handle_rate_limit(resp, attempt=0)
        mock_sleep.assert_called_once_with(5)

    @patch("mistapi.__api_request.time.sleep")
    def test_exponential_backoff_attempt_1(self, mock_sleep):
        req = _make_api_request()
        resp = Mock()
        resp.headers = {}
        # attempt 1 => 5 * (2**1) = 10
        req._handle_rate_limit(resp, attempt=1)
        mock_sleep.assert_called_once_with(10)

    @patch("mistapi.__api_request.time.sleep")
    def test_exponential_backoff_attempt_2(self, mock_sleep):
        req = _make_api_request()
        resp = Mock()
        resp.headers = {}
        # attempt 2 => 5 * (2**2) = 20
        req._handle_rate_limit(resp, attempt=2)
        mock_sleep.assert_called_once_with(20)

    @patch("mistapi.__api_request.time.sleep")
    def test_invalid_retry_after_falls_back(self, mock_sleep):
        req = _make_api_request()
        resp = Mock()
        resp.headers = {"Retry-After": "not-a-number"}
        # attempt 0 => fallback 5 * (2**0) = 5
        req._handle_rate_limit(resp, attempt=0)
        mock_sleep.assert_called_once_with(5)


class TestRequestWithRetrySuccess:
    """_request_with_retry() on successful responses."""

    def test_returns_api_response_on_200(self):
        req = _make_api_request()
        resp = _mock_response(status_code=200, json_data={"ok": True})
        fn = Mock(return_value=resp)

        result = req._request_with_retry("test", fn, "https://api.mist.com/api/v1/self")

        assert isinstance(result, APIResponse)
        assert result.status_code == 200
        fn.assert_called_once()

    def test_increments_count(self):
        req = _make_api_request()
        assert req._count == 0
        resp = _mock_response(status_code=200)
        fn = Mock(return_value=resp)

        req._request_with_retry("test", fn, "https://example.com")
        assert req._count == 1

        req._request_with_retry("test", fn, "https://example.com")
        assert req._count == 2


class TestRequestWithRetryProxyError:
    """_request_with_retry() on ProxyError."""

    def test_proxy_error_sets_flag(self):
        req = _make_api_request()
        fn = Mock(side_effect=requests.exceptions.ProxyError("proxy down"))

        result = req._request_with_retry("test", fn, "https://example.com")

        assert result.proxy_error is True
        assert result.status_code is None
        assert req._count == 1


class TestRequestWithRetryConnectionError:
    """_request_with_retry() on ConnectionError."""

    def test_connection_error_returns_none_response(self):
        req = _make_api_request()
        fn = Mock(side_effect=requests.exceptions.ConnectionError("no route"))

        result = req._request_with_retry("test", fn, "https://example.com")

        assert result.status_code is None
        assert result.proxy_error is False
        assert req._count == 1


class TestRequestWithRetryHTTPErrorNon429:
    """_request_with_retry() on non-429 HTTPError."""

    def test_non_429_stops_immediately(self):
        req = _make_api_request()
        resp = _mock_response(status_code=403, json_data={"error": "forbidden"})
        http_err = HTTPError(response=resp)
        resp.raise_for_status.side_effect = http_err

        fn = Mock(return_value=resp)
        result = req._request_with_retry("test", fn, "https://example.com")

        # Should only call request_fn once (no retries for non-429)
        fn.assert_called_once()
        assert result.status_code == 403
        assert req._count == 1

    def test_500_error(self):
        req = _make_api_request()
        resp = _mock_response(status_code=500, json_data={"error": "server error"})
        http_err = HTTPError(response=resp)
        resp.raise_for_status.side_effect = http_err

        fn = Mock(return_value=resp)
        result = req._request_with_retry("test", fn, "https://example.com")

        fn.assert_called_once()
        assert result.status_code == 500


class TestRequestWithRetry429:
    """_request_with_retry() on 429 rate-limit responses."""

    @patch("mistapi.__api_request.time.sleep")
    def test_retries_on_429(self, mock_sleep):
        req = _make_api_request(tokens=["tok_aaa1", "tok_bbb2"])

        # First call returns 429, second call succeeds
        resp_429 = _mock_response(status_code=429, headers={"Retry-After": "1"})
        http_err = HTTPError(response=resp_429)
        resp_429.raise_for_status.side_effect = http_err

        resp_ok = _mock_response(status_code=200, json_data={"ok": True})

        fn = Mock(side_effect=[resp_429, resp_ok])
        result = req._request_with_retry("test", fn, "https://example.com")

        assert fn.call_count == 2
        assert result.status_code == 200
        mock_sleep.assert_called_once_with(1)

    @patch("mistapi.__api_request.time.sleep")
    def test_rotates_token_on_429(self, mock_sleep):
        req = _make_api_request(tokens=["tok_aaa1", "tok_bbb2"])

        resp_429 = _mock_response(status_code=429, headers={"Retry-After": "1"})
        http_err = HTTPError(response=resp_429)
        resp_429.raise_for_status.side_effect = http_err

        resp_ok = _mock_response(status_code=200)
        fn = Mock(side_effect=[resp_429, resp_ok])
        req._request_with_retry("test", fn, "https://example.com")

        # Token should have rotated from index 0 to index 1
        assert req._apitoken_index == 1

    @patch("mistapi.__api_request.time.sleep")
    def test_429_exhausted_after_max_retries(self, mock_sleep):
        req = _make_api_request(tokens=["tok_aaa1", "tok_bbb2", "tok_ccc3", "tok_ddd4"])

        resp_429 = _mock_response(status_code=429, headers={"Retry-After": "1"})
        http_err = HTTPError(response=resp_429)
        resp_429.raise_for_status.side_effect = http_err

        # All 4 calls (1 initial + 3 retries) return 429
        fn = Mock(return_value=resp_429)
        result = req._request_with_retry("test", fn, "https://example.com")

        # MAX_429_RETRIES = 3, so total calls = 4 (attempt 0,1,2,3)
        assert fn.call_count == 4
        assert result.status_code == 429
        assert mock_sleep.call_count == 3
        assert req._count == 1

    @patch("mistapi.__api_request.time.sleep")
    def test_429_single_token_still_retries_with_backoff(self, mock_sleep):
        """Even with one token (RuntimeError on rotation), retry with backoff."""
        req = _make_api_request(tokens=["tok_only1"])

        resp_429 = _mock_response(status_code=429, headers={})
        http_err = HTTPError(response=resp_429)
        resp_429.raise_for_status.side_effect = http_err

        resp_ok = _mock_response(status_code=200)
        fn = Mock(side_effect=[resp_429, resp_ok])
        result = req._request_with_retry("test", fn, "https://example.com")

        assert fn.call_count == 2
        assert result.status_code == 200
        # Backoff with attempt=0 => 5 * 1 = 5
        mock_sleep.assert_called_once_with(5)

    @patch("mistapi.__api_request.time.sleep")
    def test_429_calls_handle_rate_limit(self, mock_sleep):
        req = _make_api_request(tokens=["tok_aaa1", "tok_bbb2"])

        resp_429 = _mock_response(status_code=429, headers={"Retry-After": "7"})
        http_err = HTTPError(response=resp_429)
        resp_429.raise_for_status.side_effect = http_err

        resp_ok = _mock_response(status_code=200)
        fn = Mock(side_effect=[resp_429, resp_ok])

        with patch.object(
            req, "_handle_rate_limit", wraps=req._handle_rate_limit
        ) as wrapped:
            req._request_with_retry("test", fn, "https://example.com")
            wrapped.assert_called_once_with(resp_429, 0)

        mock_sleep.assert_called_once_with(7)


class TestRequestWithRetryGenericException:
    """_request_with_retry() on unexpected exceptions."""

    def test_generic_exception_breaks_loop(self):
        req = _make_api_request()
        fn = Mock(side_effect=ValueError("something unexpected"))
        result = req._request_with_retry("test", fn, "https://example.com")

        fn.assert_called_once()
        assert result.status_code is None
        assert req._count == 1


class TestMistGet:
    """mist_get() delegates to _request_with_retry with correct URL+query."""

    def test_get_without_query(self):
        req = _make_api_request()
        resp = _mock_response(status_code=200, json_data={"items": []})
        req._session.get.return_value = resp

        result = req.mist_get("/api/v1/self")

        assert result.status_code == 200
        req._session.get.assert_called_once_with("https://api.mist.com/api/v1/self")

    def test_get_with_query(self):
        req = _make_api_request()
        resp = _mock_response(status_code=200, json_data={})
        req._session.get.return_value = resp

        result = req.mist_get("/api/v1/orgs", query={"page": "2", "limit": "50"})

        assert result.status_code == 200
        expected_url = "https://api.mist.com/api/v1/orgs?page=2&limit=50"
        req._session.get.assert_called_once_with(expected_url)

    def test_get_increments_count(self):
        req = _make_api_request()
        resp = _mock_response(status_code=200)
        req._session.get.return_value = resp

        req.mist_get("/api/v1/self")
        assert req.get_request_count() == 1


class TestMistPost:
    """mist_post() sends JSON body or raw string data."""

    def test_post_dict_body(self):
        req = _make_api_request()
        resp = _mock_response(status_code=200)
        req._session.post.return_value = resp

        body = {"name": "Test Site"}
        result = req.mist_post("/api/v1/sites", body=body)

        assert result.status_code == 200
        req._session.post.assert_called_once_with(
            "https://api.mist.com/api/v1/sites",
            json=body,
            headers={"Content-Type": "application/json"},
        )

    def test_post_string_body(self):
        req = _make_api_request()
        resp = _mock_response(status_code=200)
        req._session.post.return_value = resp

        body = '{"name": "Test Site"}'
        result = req.mist_post("/api/v1/sites", body=body)

        assert result.status_code == 200
        req._session.post.assert_called_once_with(
            "https://api.mist.com/api/v1/sites",
            data=body,
            headers={"Content-Type": "application/json"},
        )

    def test_post_list_body(self):
        req = _make_api_request()
        resp = _mock_response(status_code=200)
        req._session.post.return_value = resp

        body = [{"name": "Site A"}, {"name": "Site B"}]
        result = req.mist_post("/api/v1/sites", body=body)

        assert result.status_code == 200
        req._session.post.assert_called_once_with(
            "https://api.mist.com/api/v1/sites",
            json=body,
            headers={"Content-Type": "application/json"},
        )

    def test_post_none_body(self):
        req = _make_api_request()
        resp = _mock_response(status_code=200)
        req._session.post.return_value = resp

        result = req.mist_post("/api/v1/sites", body=None)

        assert result.status_code == 200
        req._session.post.assert_called_once_with(
            "https://api.mist.com/api/v1/sites",
            json=None,
            headers={"Content-Type": "application/json"},
        )


class TestMistPut:
    """mist_put() sends JSON body or raw string data."""

    def test_put_dict_body(self):
        req = _make_api_request()
        resp = _mock_response(status_code=200)
        req._session.put.return_value = resp

        body = {"name": "Updated Site"}
        result = req.mist_put("/api/v1/sites/123", body=body)

        assert result.status_code == 200
        req._session.put.assert_called_once_with(
            "https://api.mist.com/api/v1/sites/123",
            json=body,
            headers={"Content-Type": "application/json"},
        )

    def test_put_string_body(self):
        req = _make_api_request()
        resp = _mock_response(status_code=200)
        req._session.put.return_value = resp

        body = '{"name": "Updated Site"}'
        result = req.mist_put("/api/v1/sites/123", body=body)

        assert result.status_code == 200
        req._session.put.assert_called_once_with(
            "https://api.mist.com/api/v1/sites/123",
            data=body,
            headers={"Content-Type": "application/json"},
        )

    def test_put_none_body(self):
        req = _make_api_request()
        resp = _mock_response(status_code=200)
        req._session.put.return_value = resp

        result = req.mist_put("/api/v1/sites/123", body=None)

        assert result.status_code == 200
        req._session.put.assert_called_once_with(
            "https://api.mist.com/api/v1/sites/123",
            json=None,
            headers={"Content-Type": "application/json"},
        )


class TestMistDelete:
    """mist_delete() delegates with correct URL+query."""

    def test_delete_without_query(self):
        req = _make_api_request()
        resp = _mock_response(status_code=200)
        req._session.delete.return_value = resp

        result = req.mist_delete("/api/v1/sites/123")

        assert result.status_code == 200
        req._session.delete.assert_called_once_with(
            "https://api.mist.com/api/v1/sites/123"
        )

    def test_delete_with_query(self):
        req = _make_api_request()
        resp = _mock_response(status_code=200)
        req._session.delete.return_value = resp

        result = req.mist_delete("/api/v1/sites/123", query={"force": "true"})

        assert result.status_code == 200
        req._session.delete.assert_called_once_with(
            "https://api.mist.com/api/v1/sites/123?force=true"
        )


class TestMistPostFile:
    """mist_post_file() builds multipart form data and delegates to retry wrapper."""

    def test_post_file_with_file_key(self, tmp_path):
        req = _make_api_request()
        resp = _mock_response(status_code=200)
        req._session.post.return_value = resp

        # Create a real temporary file
        test_file = tmp_path / "upload.bin"
        test_file.write_bytes(b"file content here")

        result = req.mist_post_file(
            "/api/v1/sites/123/maps/import",
            multipart_form_data={"file": str(test_file)},
        )

        assert result.status_code == 200
        req._session.post.assert_called_once()
        call_kwargs = req._session.post.call_args
        files_arg = call_kwargs.kwargs.get("files") or call_kwargs[1].get("files")
        assert "file" in files_arg
        # Tuple structure: (filename, file_obj, content_type)
        assert files_arg["file"][0] == "upload.bin"
        assert files_arg["file"][2] == "application/octet-stream"

    def test_post_file_with_csv_key(self, tmp_path):
        req = _make_api_request()
        resp = _mock_response(status_code=200)
        req._session.post.return_value = resp

        csv_file = tmp_path / "data.csv"
        csv_file.write_text("col1,col2\na,b\n")

        result = req.mist_post_file(
            "/api/v1/orgs/123/inventory",
            multipart_form_data={"csv": str(csv_file)},
        )

        assert result.status_code == 200
        call_kwargs = req._session.post.call_args
        files_arg = call_kwargs.kwargs.get("files") or call_kwargs[1].get("files")
        assert "csv" in files_arg
        assert files_arg["csv"][0] == "data.csv"

    def test_post_file_with_json_field(self):
        req = _make_api_request()
        resp = _mock_response(status_code=200)
        req._session.post.return_value = resp

        result = req.mist_post_file(
            "/api/v1/sites/123/maps",
            multipart_form_data={"json": {"name": "Floor 1"}},
        )

        assert result.status_code == 200
        call_kwargs = req._session.post.call_args
        files_arg = call_kwargs.kwargs.get("files") or call_kwargs[1].get("files")
        assert "json" in files_arg
        # Non-file keys produce (None, json_string) tuples
        assert files_arg["json"][0] is None
        assert json.loads(files_arg["json"][1]) == {"name": "Floor 1"}

    def test_post_file_none_defaults_to_empty(self):
        req = _make_api_request()
        resp = _mock_response(status_code=200)
        req._session.post.return_value = resp

        result = req.mist_post_file("/api/v1/sites/123/maps")

        assert result.status_code == 200
        call_kwargs = req._session.post.call_args
        files_arg = call_kwargs.kwargs.get("files") or call_kwargs[1].get("files")
        assert files_arg == {}

    def test_post_file_skips_falsy_values(self):
        req = _make_api_request()
        resp = _mock_response(status_code=200)
        req._session.post.return_value = resp

        result = req.mist_post_file(
            "/api/v1/sites/123/maps",
            multipart_form_data={"json": None, "file": ""},
        )

        assert result.status_code == 200
        call_kwargs = req._session.post.call_args
        files_arg = call_kwargs.kwargs.get("files") or call_kwargs[1].get("files")
        assert files_arg == {}

    def test_post_file_missing_file_handled_gracefully(self):
        req = _make_api_request()
        resp = _mock_response(status_code=200)
        req._session.post.return_value = resp

        # Point to a file that does not exist
        result = req.mist_post_file(
            "/api/v1/sites/123/maps",
            multipart_form_data={"file": "/nonexistent/path/file.bin"},
        )

        assert result.status_code == 200
        # The OSError is caught silently; file key is not in the generated data
        call_kwargs = req._session.post.call_args
        files_arg = call_kwargs.kwargs.get("files") or call_kwargs[1].get("files")
        assert "file" not in files_arg


class TestGetRequestCount:
    """get_request_count() returns the cumulative request count."""

    def test_initial_count_is_zero(self):
        req = _make_api_request()
        assert req.get_request_count() == 0

    def test_count_after_requests(self):
        req = _make_api_request()
        resp = _mock_response(status_code=200)
        req._session.get.return_value = resp

        req.mist_get("/api/v1/self")
        req.mist_get("/api/v1/self")
        req.mist_get("/api/v1/self")

        assert req.get_request_count() == 3

    def test_count_increments_on_error(self):
        req = _make_api_request()
        fn = Mock(side_effect=requests.exceptions.ConnectionError("fail"))
        req._request_with_retry("test", fn, "https://example.com")
        assert req.get_request_count() == 1
