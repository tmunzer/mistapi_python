"""
Unit tests for mistapi.__api_response.APIResponse

Tests cover:
- Construction with None response (default field values)
- Construction with a valid JSON response (data, status_code, headers)
- _check_next() when "next" key is present in response data
- _check_next() pagination via X-Page-Total / X-Page-Limit / X-Page-Page headers
- _check_next() on the last page (next stays None)
- _check_next() when the URL already contains a page= parameter
- Error responses (4xx status codes)
- proxy_error flag propagation
- Non-JSON responses (exception path in __init__)
"""

import json
from unittest.mock import Mock

import pytest

from mistapi.__api_response import APIResponse


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_mock_response(status_code=200, data=None, headers=None, json_raises=False):
    """Build a mock requests.Response with the given attributes."""
    mock = Mock()
    mock.status_code = status_code
    mock.headers = headers or {}
    if json_raises:
        mock.content = b"not-json"
        mock.json.side_effect = ValueError("No JSON")
    else:
        payload = data if data is not None else {}
        mock.content = json.dumps(payload).encode()
        mock.text = json.dumps(payload)
        mock.json.return_value = payload
    return mock


# ---------------------------------------------------------------------------
# Tests: construction / default fields
# ---------------------------------------------------------------------------


class TestAPIResponseConstruction:
    """Tests for APIResponse.__init__ with different response inputs."""

    def test_none_response_defaults(self):
        """When response is None every field should keep its default value."""
        resp = APIResponse(response=None, url="https://api.mist.com/api/v1/test")

        assert resp.raw_data == ""
        assert resp.data == {}
        assert resp.url == "https://api.mist.com/api/v1/test"
        assert resp.next is None
        assert resp.headers is None
        assert resp.status_code is None
        assert resp.proxy_error is False

    def test_200_response_with_json(self, api_response_factory):
        """A 200 response with JSON body should populate data, status_code, headers."""
        data = {"id": "abc-123", "name": "widget"}
        headers = {"Content-Type": "application/json"}

        resp = api_response_factory(status_code=200, data=data, headers=headers)

        assert resp.status_code == 200
        assert resp.data == data
        assert resp.headers == headers
        assert resp.url == "https://api.mist.com/api/v1/test"

    def test_raw_data_is_string_of_content(self):
        """raw_data should be response.text."""
        data = {"key": "value"}
        mock = _make_mock_response(data=data)
        resp = APIResponse(response=mock, url="https://host/api/v1/x")

        assert resp.raw_data == json.dumps(data)

    def test_proxy_error_true(self):
        """proxy_error=True should be stored on the instance."""
        resp = APIResponse(response=None, url="https://host/api/v1/x", proxy_error=True)

        assert resp.proxy_error is True

    def test_proxy_error_false_by_default(self):
        """proxy_error defaults to False."""
        resp = APIResponse(response=None, url="https://host/api/v1/x")

        assert resp.proxy_error is False

    def test_proxy_error_with_response(self):
        """proxy_error flag should propagate even when a valid response is present."""
        mock = _make_mock_response(status_code=502, data={"error": "bad gateway"})
        resp = APIResponse(response=mock, url="https://host/api/v1/x", proxy_error=True)

        assert resp.proxy_error is True
        assert resp.status_code == 502


# ---------------------------------------------------------------------------
# Tests: error responses
# ---------------------------------------------------------------------------


class TestAPIResponseErrors:
    """Tests for error HTTP status codes and error payloads."""

    @pytest.mark.parametrize("status_code", [400, 401, 403, 404, 500, 502, 503])
    def test_error_status_codes_stored(self, api_response_factory, status_code):
        """Error status codes should be stored without raising."""
        data = {"error": "something went wrong"}
        resp = api_response_factory(status_code=status_code, data=data)

        assert resp.status_code == status_code
        assert resp.data == data

    def test_error_key_in_200_response(self, api_response_factory):
        """A 200 with an 'error' key in the body should still store data."""
        data = {"error": "unexpected error in body"}
        resp = api_response_factory(status_code=200, data=data)

        assert resp.status_code == 200
        assert resp.data == data

    def test_non_json_response_handled_gracefully(self):
        """When response.json() raises, the exception path should not propagate."""
        mock = _make_mock_response(json_raises=True)
        # Should not raise
        resp = APIResponse(response=mock, url="https://host/api/v1/x")

        # data stays at default because json() failed
        assert resp.data == {}
        assert resp.status_code == 200
        assert resp.next is None


# ---------------------------------------------------------------------------
# Tests: _check_next with "next" in data
# ---------------------------------------------------------------------------


class TestCheckNextFromData:
    """Tests for _check_next() when the response body contains a 'next' key."""

    def test_next_in_data(self, api_response_factory):
        """When data contains 'next', self.next should be set from data."""
        data = {"results": [], "next": "/api/v1/test?page=2"}
        resp = api_response_factory(data=data)

        assert resp.next == "/api/v1/test?page=2"

    def test_next_in_data_takes_precedence_over_headers(self):
        """'next' in data should take precedence over pagination headers."""
        headers = {
            "X-Page-Total": "100",
            "X-Page-Limit": "10",
            "X-Page-Page": "1",
        }
        data = {"next": "/api/v1/custom-next"}
        mock = _make_mock_response(data=data, headers=headers)
        resp = APIResponse(response=mock, url="https://host/api/v1/items")

        assert resp.next == "/api/v1/custom-next"

    def test_next_value_none_in_data(self, api_response_factory):
        """When data['next'] is None, self.next should be set to None."""
        data = {"results": [], "next": None}
        resp = api_response_factory(data=data)

        assert resp.next is None


# ---------------------------------------------------------------------------
# Tests: _check_next with pagination headers
# ---------------------------------------------------------------------------


class TestCheckNextFromHeaders:
    """Tests for _check_next() computing the next URL from pagination headers."""

    def _make_paginated_response(self, total, limit, page, url=None):
        """Helper: build an APIResponse with pagination headers."""
        url = url or "https://api.mist.com/api/v1/sites"
        headers = {
            "X-Page-Total": str(total),
            "X-Page-Limit": str(limit),
            "X-Page-Page": str(page),
        }
        mock = _make_mock_response(data={"results": []}, headers=headers)
        return APIResponse(response=mock, url=url)

    def test_next_page_computed_from_headers(self):
        """When there are more pages, next should be computed from headers."""
        resp = self._make_paginated_response(total=50, limit=10, page=1)

        assert resp.next == "/api/v1/sites?page=2"

    def test_next_page_with_existing_query_string(self):
        """When URL already has a query string, page should use '&'."""
        resp = self._make_paginated_response(
            total=50, limit=10, page=1, url="https://api.mist.com/api/v1/sites?limit=10"
        )

        assert resp.next == "/api/v1/sites?limit=10&page=2"

    def test_last_page_next_is_none(self):
        """On the last page (limit*page >= total), next should remain None."""
        resp = self._make_paginated_response(total=30, limit=10, page=3)

        assert resp.next is None

    def test_beyond_last_page_next_is_none(self):
        """When limit*page > total, next should remain None."""
        resp = self._make_paginated_response(total=25, limit=10, page=3)

        assert resp.next is None

    def test_single_page_result(self):
        """When all results fit in one page, next stays None."""
        resp = self._make_paginated_response(total=5, limit=10, page=1)

        assert resp.next is None

    def test_existing_page_param_replaced(self):
        """When URL already contains page=N, it should be replaced."""
        resp = self._make_paginated_response(
            total=100,
            limit=10,
            page=2,
            url="https://api.mist.com/api/v1/sites?limit=10&page=2",
        )

        assert resp.next == "/api/v1/sites?limit=10&page=3"

    def test_existing_page_param_first_page(self):
        """Replacing page=1 with page=2 when page param already in URL."""
        resp = self._make_paginated_response(
            total=100,
            limit=10,
            page=1,
            url="https://api.mist.com/api/v1/sites?page=1&limit=10",
        )

        assert resp.next == "/api/v1/sites?page=2&limit=10"

    def test_missing_total_header(self):
        """When X-Page-Total is missing, next should remain None."""
        headers = {
            "X-Page-Limit": "10",
            "X-Page-Page": "1",
        }
        mock = _make_mock_response(data={"results": []}, headers=headers)
        resp = APIResponse(response=mock, url="https://host/api/v1/items")

        assert resp.next is None

    def test_missing_limit_header(self):
        """When X-Page-Limit is missing, next should remain None."""
        headers = {
            "X-Page-Total": "50",
            "X-Page-Page": "1",
        }
        mock = _make_mock_response(data={"results": []}, headers=headers)
        resp = APIResponse(response=mock, url="https://host/api/v1/items")

        assert resp.next is None

    def test_missing_page_header(self):
        """When X-Page-Page is missing, next should remain None."""
        headers = {
            "X-Page-Total": "50",
            "X-Page-Limit": "10",
        }
        mock = _make_mock_response(data={"results": []}, headers=headers)
        resp = APIResponse(response=mock, url="https://host/api/v1/items")

        assert resp.next is None

    def test_non_numeric_headers_handled(self):
        """Non-numeric pagination header values should not raise."""
        headers = {
            "X-Page-Total": "abc",
            "X-Page-Limit": "10",
            "X-Page-Page": "1",
        }
        mock = _make_mock_response(data={"results": []}, headers=headers)
        resp = APIResponse(response=mock, url="https://host/api/v1/items")

        assert resp.next is None

    def test_no_headers_at_all(self, api_response_factory):
        """When there are no pagination headers and no 'next' in data, next is None."""
        resp = api_response_factory(data={"results": []})

        assert resp.next is None

    def test_pagination_strips_host_prefix(self):
        """The computed next URL should be a relative /api/... path, not absolute."""
        resp = self._make_paginated_response(
            total=100,
            limit=10,
            page=1,
            url="https://api.eu.mist.com/api/v1/orgs/abc/devices",
        )

        assert resp.next.startswith("/api/v1/")
        assert "api.eu.mist.com" not in resp.next
        assert resp.next == "/api/v1/orgs/abc/devices?page=2"


# ---------------------------------------------------------------------------
# Tests: data types preserved
# ---------------------------------------------------------------------------


class TestDataTypes:
    """Verify that different JSON response shapes are handled correctly."""

    def test_list_response(self):
        """An API that returns a JSON list should store it in data."""
        data = [{"id": "a"}, {"id": "b"}]
        mock = _make_mock_response(data=data)
        resp = APIResponse(response=mock, url="https://host/api/v1/x")

        assert resp.data == data
        # When data is a list, there is no 'next' key lookup issue
        assert resp.next is None

    def test_empty_dict_response(self, api_response_factory):
        """An empty dict body should result in data=={} and next==None."""
        resp = api_response_factory(data={})

        assert resp.data == {}
        assert resp.next is None
