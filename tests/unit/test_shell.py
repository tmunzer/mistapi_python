# tests/unit/test_shell.py
"""
Unit tests for ShellSession and create_shell_session.
"""

import json
from unittest.mock import Mock, patch

import pytest
import websocket

from mistapi.api.v1.sites import devices as devices_module
from mistapi.device_utils.__tools import shell as shell_module
from mistapi.device_utils.__tools.shell import ShellSession, create_shell_session


# ------------------------------------------------------------------
# Fixtures
# ------------------------------------------------------------------


@pytest.fixture
def mock_apisession():
    session = Mock()
    session._apitoken = ["test-token-abc123"]
    session._apitoken_index = 0
    session._session = Mock()
    session._session.verify = True
    session._session.cert = None
    session._session.cookies = []
    return session


@pytest.fixture
def shell_session(mock_apisession):
    return ShellSession(mock_apisession, "wss://example.com/shell")


@pytest.fixture
def mock_ws():
    ws = Mock()
    ws.connected = True
    ws.gettimeout.return_value = 0.1
    return ws


# ------------------------------------------------------------------
# Auth helpers
# ------------------------------------------------------------------


class TestAuthHelpers:
    """Tests for auth/SSL helper methods."""

    def test_get_headers_with_api_token(self, shell_session) -> None:
        headers = shell_session._get_headers()
        assert headers == ["Authorization: Token test-token-abc123"]

    def test_get_headers_without_api_token(self, mock_apisession) -> None:
        mock_apisession._apitoken = []
        session = ShellSession(mock_apisession, "wss://example.com/shell")
        assert session._get_headers() == []

    def test_get_cookie_with_cookies(self, mock_apisession) -> None:
        cookie1 = Mock()
        cookie1.name = "session_id"
        cookie1.value = "abc123"
        cookie2 = Mock()
        cookie2.name = "csrf"
        cookie2.value = "xyz789"
        mock_apisession._session.cookies = [cookie1, cookie2]
        session = ShellSession(mock_apisession, "wss://example.com/shell")
        assert session._get_cookie() == "session_id=abc123; csrf=xyz789"

    def test_get_cookie_without_cookies(self, shell_session) -> None:
        assert shell_session._get_cookie() is None

    def test_get_cookie_skips_crlf(self, mock_apisession) -> None:
        bad_cookie = Mock()
        bad_cookie.name = "bad\rcookie"
        bad_cookie.value = "val"
        mock_apisession._session.cookies = [bad_cookie]
        session = ShellSession(mock_apisession, "wss://example.com/shell")
        assert session._get_cookie() is None

    def test_build_sslopt_verify_false(self, mock_apisession) -> None:
        import ssl

        mock_apisession._session.verify = False
        session = ShellSession(mock_apisession, "wss://example.com/shell")
        assert session._build_sslopt()["cert_reqs"] == ssl.CERT_NONE

    def test_build_sslopt_custom_ca(self, mock_apisession) -> None:
        mock_apisession._session.verify = "/path/to/ca.pem"
        session = ShellSession(mock_apisession, "wss://example.com/shell")
        assert session._build_sslopt()["ca_certs"] == "/path/to/ca.pem"

    def test_build_sslopt_client_cert_tuple(self, mock_apisession) -> None:
        mock_apisession._session.cert = ("/path/cert.pem", "/path/key.pem")
        session = ShellSession(mock_apisession, "wss://example.com/shell")
        sslopt = session._build_sslopt()
        assert sslopt["certfile"] == "/path/cert.pem"
        assert sslopt["keyfile"] == "/path/key.pem"


# ------------------------------------------------------------------
# Lifecycle
# ------------------------------------------------------------------


class TestLifecycle:
    """Tests for connect/disconnect/connected."""

    def test_connect_calls_create_connection(
        self, shell_session, mock_ws
    ) -> None:
        with patch.object(
            shell_module.websocket,
            "create_connection",
            return_value=mock_ws,
        ) as mock_create:
            shell_session.connect()

            mock_create.assert_called_once_with(
                "wss://example.com/shell",
                header=["Authorization: Token test-token-abc123"],
                cookie=None,
                sslopt={},
            )

    def test_connect_sends_resize(self, shell_session, mock_ws) -> None:
        with patch.object(
            shell_module.websocket,
            "create_connection",
            return_value=mock_ws,
        ):
            shell_session.connect()

            mock_ws.send.assert_called_once_with(
                json.dumps({"resize": {"width": 80, "height": 24}})
            )

    def test_disconnect_closes_ws(self, shell_session, mock_ws) -> None:
        with patch.object(
            shell_module.websocket,
            "create_connection",
            return_value=mock_ws,
        ):
            shell_session.connect()
            shell_session.disconnect()

            mock_ws.close.assert_called_once()
            assert shell_session._ws is None

    def test_disconnect_without_connect_is_safe(self, shell_session) -> None:
        shell_session.disconnect()  # Should not raise

    def test_connected_false_before_connect(self, shell_session) -> None:
        assert shell_session.connected is False

    def test_connected_true_after_connect(self, shell_session, mock_ws) -> None:
        with patch.object(
            shell_module.websocket,
            "create_connection",
            return_value=mock_ws,
        ):
            shell_session.connect()
            assert shell_session.connected is True


# ------------------------------------------------------------------
# I/O
# ------------------------------------------------------------------


class TestIO:
    """Tests for send/recv/resize."""

    def test_send_binary(self, shell_session, mock_ws) -> None:
        with patch.object(
            shell_module.websocket,
            "create_connection",
            return_value=mock_ws,
        ):
            shell_session.connect()
            shell_session.send(b"\x00hello")
            mock_ws.send_binary.assert_called_once_with(b"\x00hello")

    def test_send_text_prefixes_null(self, shell_session, mock_ws) -> None:
        with patch.object(
            shell_module.websocket,
            "create_connection",
            return_value=mock_ws,
        ):
            shell_session.connect()
            shell_session.send_text("ls\r\n")
            called_data = mock_ws.send_binary.call_args[0][0]
            assert called_data == b"\x00ls\r\n"

    def test_recv_returns_bytes(self, shell_session, mock_ws) -> None:
        mock_ws.recv.return_value = b"output data"
        with patch.object(
            shell_module.websocket,
            "create_connection",
            return_value=mock_ws,
        ):
            shell_session.connect()
            result = shell_session.recv()
            assert result == b"output data"

    def test_recv_converts_str_to_bytes(self, shell_session, mock_ws) -> None:
        mock_ws.recv.return_value = "text output"
        with patch.object(
            shell_module.websocket,
            "create_connection",
            return_value=mock_ws,
        ):
            shell_session.connect()
            result = shell_session.recv()
            assert result == b"text output"

    def test_recv_returns_none_on_timeout(self, shell_session, mock_ws) -> None:
        mock_ws.recv.side_effect = websocket.WebSocketTimeoutException()
        with patch.object(
            shell_module.websocket,
            "create_connection",
            return_value=mock_ws,
        ):
            shell_session.connect()
            result = shell_session.recv()
            assert result is None

    def test_recv_returns_none_on_closed(self, shell_session, mock_ws) -> None:
        mock_ws.recv.side_effect = websocket.WebSocketConnectionClosedException()
        with patch.object(
            shell_module.websocket,
            "create_connection",
            return_value=mock_ws,
        ):
            shell_session.connect()
            result = shell_session.recv()
            assert result is None

    def test_recv_returns_none_when_not_connected(self, shell_session) -> None:
        assert shell_session.recv() is None

    def test_resize_sends_json(self, shell_session, mock_ws) -> None:
        with patch.object(
            shell_module.websocket,
            "create_connection",
            return_value=mock_ws,
        ):
            shell_session.connect()
            mock_ws.send.reset_mock()  # clear initial resize from connect()

            shell_session.resize(40, 120)
            mock_ws.send.assert_called_once_with(
                json.dumps({"resize": {"width": 120, "height": 40}})
            )


# ------------------------------------------------------------------
# Context manager
# ------------------------------------------------------------------


class TestContextManager:
    """Tests for context manager support."""

    def test_exit_calls_disconnect(self, mock_apisession, mock_ws) -> None:
        with patch.object(
            shell_module.websocket,
            "create_connection",
            return_value=mock_ws,
        ):
            session = ShellSession(mock_apisession, "wss://example.com/shell")
            session.connect()

            with session:
                pass

            mock_ws.close.assert_called_once()


# ------------------------------------------------------------------
# create_shell_session
# ------------------------------------------------------------------


class TestCreateShellSession:
    """Tests for the create_shell_session factory."""

    def test_happy_path(self, mock_apisession, mock_ws) -> None:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.data = {"url": "wss://example.com/shell/abc"}

        with patch.object(
            shell_module.websocket,
            "create_connection",
            return_value=mock_ws,
        ), patch.object(
            devices_module,
            "createSiteDeviceShellSession",
            return_value=mock_response,
        ) as mock_shell_api:
            session = create_shell_session(mock_apisession, "site-1", "device-1")

            assert isinstance(session, ShellSession)
            mock_shell_api.assert_called_once_with(
                mock_apisession, site_id="site-1", device_id="device-1", body={}
            )

    def test_api_failure_raises(self, mock_apisession) -> None:
        mock_response = Mock()
        mock_response.status_code = 403
        mock_response.data = {"error": "forbidden"}

        with patch.object(
            devices_module,
            "createSiteDeviceShellSession",
            return_value=mock_response,
        ):
            with pytest.raises(RuntimeError, match="Shell API call failed"):
                create_shell_session(mock_apisession, "site-1", "device-1")

    def test_missing_url_raises(self, mock_apisession) -> None:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.data = {"session": "abc"}  # no "url" key

        with patch.object(
            devices_module,
            "createSiteDeviceShellSession",
            return_value=mock_response,
        ):
            with pytest.raises(RuntimeError, match="did not contain a WebSocket URL"):
                create_shell_session(mock_apisession, "site-1", "device-1")
