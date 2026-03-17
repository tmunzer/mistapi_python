# tests/unit/test_websocket_client.py
"""
Unit tests for _MistWebsocket base class and public WebSocket channel classes.

These tests cover URL building, authentication helpers, SSL options,
callback registration, internal handlers, connect/disconnect lifecycle,
the receive() generator, context-manager support, and the public API
surface of all channel classes (sites, orgs, location, session).
"""

import json
import ssl
import threading
from unittest.mock import Mock, call, patch

import pytest

from mistapi.websockets.__ws_client import _MistWebsocket
from mistapi.websockets.location import (
    BleAssetsEvents,
    ConnectedClientsEvents,
    DiscoveredBleAssetsEvents,
    SdkClientsEvents,
    UnconnectedClientsEvents,
)
from mistapi.websockets.orgs import (
    InsightsEvents,
    MxEdgesEvents,
)
from mistapi.websockets.orgs import MxEdgesStatsEvents as OrgMxEdgesStatsEvents
from mistapi.websockets.session import SessionWithUrl
from mistapi.websockets.sites import (
    ClientsStatsEvents,
    DeviceCmdEvents,
    DeviceEvents,
    DeviceStatsEvents,
    PcapEvents,
)
from mistapi.websockets.sites import (
    MxEdgesStatsEvents as SiteMxEdgesStatsEvents,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def mock_session():
    """
    Lightweight mock of APISession with the internal attributes that
    _MistWebsocket accesses directly.
    """
    session = Mock()
    session._cloud_uri = "api.mist.com"
    session._apitoken = ["test_token"]
    session._apitoken_index = 0

    # requests.Session stand-in
    requests_session = Mock()
    requests_session.cookies = []
    requests_session.verify = True
    requests_session.cert = None
    session._session = requests_session

    return session


@pytest.fixture
def ws_client(mock_session):
    """A _MistWebsocket wired to mock_session with two channels."""
    return _MistWebsocket(
        mist_session=mock_session,
        channels=["/test/channel1", "/test/channel2"],
    )


@pytest.fixture
def single_channel_client(mock_session):
    """A _MistWebsocket with a single channel and custom ping settings."""
    return _MistWebsocket(
        mist_session=mock_session,
        channels=["/events"],
        ping_interval=15,
        ping_timeout=5,
    )


# ---------------------------------------------------------------------------
# URL building
# ---------------------------------------------------------------------------


class TestBuildWsUrl:
    """Tests for _build_ws_url()."""

    def test_replaces_api_with_api_ws(self, ws_client) -> None:
        url = ws_client._build_ws_url()
        assert url == "wss://api-ws.mist.com/api-ws/v1/stream"

    def test_eu_cloud_url(self, mock_session) -> None:
        mock_session._cloud_uri = "api.eu.mist.com"
        client = _MistWebsocket(mock_session, channels=["/ch"])
        assert client._build_ws_url() == "wss://api-ws.eu.mist.com/api-ws/v1/stream"

    def test_gc1_cloud_url(self, mock_session) -> None:
        mock_session._cloud_uri = "api.gc1.mist.com"
        client = _MistWebsocket(mock_session, channels=["/ch"])
        assert client._build_ws_url() == "wss://api-ws.gc1.mist.com/api-ws/v1/stream"


# ---------------------------------------------------------------------------
# Headers (token auth)
# ---------------------------------------------------------------------------


class TestGetHeaders:
    """Tests for _get_headers()."""

    def test_returns_authorization_header_with_token(self, ws_client) -> None:
        headers = ws_client._get_headers()
        assert headers == {"Authorization": "Token test_token"}

    def test_uses_correct_token_index(self, mock_session) -> None:
        mock_session._apitoken = ["token_a", "token_b"]
        mock_session._apitoken_index = 1
        client = _MistWebsocket(mock_session, channels=["/ch"])
        assert client._get_headers() == {"Authorization": "Token token_b"}

    def test_returns_empty_dict_without_token(self, mock_session) -> None:
        mock_session._apitoken = []
        client = _MistWebsocket(mock_session, channels=["/ch"])
        assert client._get_headers() == {}

    def test_returns_empty_dict_when_token_is_none(self, mock_session) -> None:
        mock_session._apitoken = None
        client = _MistWebsocket(mock_session, channels=["/ch"])
        assert client._get_headers() == {}


# ---------------------------------------------------------------------------
# Cookies (session auth)
# ---------------------------------------------------------------------------


class TestGetCookie:
    """Tests for _get_cookie()."""

    def test_formats_cookies_as_semicolon_pairs(self, mock_session) -> None:
        cookie1 = Mock(name="csrftoken", value="abc123")
        cookie1.name = "csrftoken"
        cookie1.value = "abc123"
        cookie2 = Mock(name="sessionid", value="xyz789")
        cookie2.name = "sessionid"
        cookie2.value = "xyz789"
        mock_session._session.cookies = [cookie1, cookie2]

        client = _MistWebsocket(mock_session, channels=["/ch"])
        assert client._get_cookie() == "csrftoken=abc123; sessionid=xyz789"

    def test_returns_none_when_no_cookies(self, mock_session) -> None:
        mock_session._session.cookies = []
        client = _MistWebsocket(mock_session, channels=["/ch"])
        assert client._get_cookie() is None

    def test_filters_cookies_with_cr_in_name(self, mock_session) -> None:
        good = Mock()
        good.name = "ok"
        good.value = "val"
        bad = Mock()
        bad.name = "bad\rname"
        bad.value = "val"
        mock_session._session.cookies = [good, bad]

        client = _MistWebsocket(mock_session, channels=["/ch"])
        assert client._get_cookie() == "ok=val"

    def test_filters_cookies_with_lf_in_name(self, mock_session) -> None:
        bad = Mock()
        bad.name = "bad\nname"
        bad.value = "val"
        mock_session._session.cookies = [bad]

        client = _MistWebsocket(mock_session, channels=["/ch"])
        assert client._get_cookie() is None

    def test_filters_cookies_with_cr_in_value(self, mock_session) -> None:
        bad = Mock()
        bad.name = "name"
        bad.value = "bad\rvalue"
        mock_session._session.cookies = [bad]

        client = _MistWebsocket(mock_session, channels=["/ch"])
        assert client._get_cookie() is None

    def test_filters_cookies_with_lf_in_value(self, mock_session) -> None:
        good = Mock()
        good.name = "safe"
        good.value = "clean"
        bad = Mock()
        bad.name = "name"
        bad.value = "bad\nvalue"
        mock_session._session.cookies = [good, bad]

        client = _MistWebsocket(mock_session, channels=["/ch"])
        assert client._get_cookie() == "safe=clean"

    def test_returns_none_when_all_cookies_filtered(self, mock_session) -> None:
        bad1 = Mock()
        bad1.name = "a\r"
        bad1.value = "v"
        bad2 = Mock()
        bad2.name = "b"
        bad2.value = "v\n"
        mock_session._session.cookies = [bad1, bad2]

        client = _MistWebsocket(mock_session, channels=["/ch"])
        assert client._get_cookie() is None


# ---------------------------------------------------------------------------
# SSL options
# ---------------------------------------------------------------------------


class TestBuildSslopt:
    """Tests for _build_sslopt()."""

    def test_defaults_returns_empty_dict(self, ws_client) -> None:
        # verify=True, cert=None  =>  empty sslopt
        assert ws_client._build_sslopt() == {}

    def test_verify_false(self, mock_session) -> None:
        mock_session._session.verify = False
        mock_session._session.cert = None
        client = _MistWebsocket(mock_session, channels=["/ch"])
        assert client._build_sslopt() == {
            "cert_reqs": ssl.CERT_NONE,
            "check_hostname": False,
        }

    def test_verify_custom_ca_path(self, mock_session) -> None:
        mock_session._session.verify = "/etc/ssl/custom-ca.pem"
        mock_session._session.cert = None
        client = _MistWebsocket(mock_session, channels=["/ch"])
        assert client._build_sslopt() == {"ca_certs": "/etc/ssl/custom-ca.pem"}

    def test_cert_as_string(self, mock_session) -> None:
        mock_session._session.cert = "/path/to/client.pem"
        client = _MistWebsocket(mock_session, channels=["/ch"])
        sslopt = client._build_sslopt()
        assert sslopt["certfile"] == "/path/to/client.pem"
        assert "keyfile" not in sslopt

    def test_cert_as_tuple(self, mock_session) -> None:
        mock_session._session.cert = ("/path/cert.pem", "/path/key.pem")
        client = _MistWebsocket(mock_session, channels=["/ch"])
        sslopt = client._build_sslopt()
        assert sslopt["certfile"] == "/path/cert.pem"
        assert sslopt["keyfile"] == "/path/key.pem"

    def test_cert_tuple_single_element(self, mock_session) -> None:
        mock_session._session.cert = ("/path/cert.pem",)
        client = _MistWebsocket(mock_session, channels=["/ch"])
        sslopt = client._build_sslopt()
        assert sslopt["certfile"] == "/path/cert.pem"
        assert "keyfile" not in sslopt

    def test_verify_false_with_cert_tuple(self, mock_session) -> None:
        mock_session._session.verify = False
        mock_session._session.cert = ("/path/cert.pem", "/path/key.pem")
        client = _MistWebsocket(mock_session, channels=["/ch"])
        sslopt = client._build_sslopt()
        assert sslopt == {
            "cert_reqs": ssl.CERT_NONE,
            "check_hostname": False,
            "certfile": "/path/cert.pem",
            "keyfile": "/path/key.pem",
        }


# ---------------------------------------------------------------------------
# Callback registration
# ---------------------------------------------------------------------------


class TestCallbackRegistration:
    """Tests for on_message / on_error / on_open / on_close setters."""

    def test_on_message_stores_callback(self, ws_client) -> None:
        cb = Mock()
        ws_client.on_message(cb)
        assert ws_client._on_message_cb is cb

    def test_on_error_stores_callback(self, ws_client) -> None:
        cb = Mock()
        ws_client.on_error(cb)
        assert ws_client._on_error_cb is cb

    def test_on_open_stores_callback(self, ws_client) -> None:
        cb = Mock()
        ws_client.on_open(cb)
        assert ws_client._on_open_cb is cb

    def test_on_close_stores_callback(self, ws_client) -> None:
        cb = Mock()
        ws_client.on_close(cb)
        assert ws_client._on_close_cb is cb

    def test_callbacks_initially_none(self, ws_client) -> None:
        assert ws_client._on_message_cb is None
        assert ws_client._on_error_cb is None
        assert ws_client._on_open_cb is None
        assert ws_client._on_close_cb is None


# ---------------------------------------------------------------------------
# Internal handlers
# ---------------------------------------------------------------------------


class TestHandleOpen:
    """Tests for _handle_open()."""

    def test_subscribes_to_each_channel(self, ws_client) -> None:
        mock_ws = Mock()
        ws_client._handle_open(mock_ws)
        expected_calls = [
            call(json.dumps({"subscribe": "/test/channel1"})),
            call(json.dumps({"subscribe": "/test/channel2"})),
        ]
        mock_ws.send.assert_has_calls(expected_calls)
        assert mock_ws.send.call_count == 2

    def test_sets_connected_event(self, ws_client) -> None:
        mock_ws = Mock()
        assert not ws_client._connected.is_set()
        ws_client._handle_open(mock_ws)
        assert ws_client._connected.is_set()

    def test_calls_on_open_callback(self, ws_client) -> None:
        cb = Mock()
        ws_client.on_open(cb)
        ws_client._handle_open(Mock())
        cb.assert_called_once_with()

    def test_no_error_without_on_open_callback(self, ws_client) -> None:
        ws_client._handle_open(Mock())  # Should not raise


class TestHandleMessage:
    """Tests for _handle_message()."""

    def test_parses_valid_json_and_enqueues(self, ws_client) -> None:
        payload = {"event": "device_update", "id": "abc"}
        ws_client._handle_message(Mock(), json.dumps(payload))
        assert ws_client._queue.get_nowait() == payload

    def test_wraps_invalid_json_in_raw_key(self, ws_client) -> None:
        ws_client._handle_message(Mock(), "not valid json {{{")
        item = ws_client._queue.get_nowait()
        assert item == {"raw": "not valid json {{{"}

    def test_calls_on_message_callback_with_parsed_data(self, ws_client) -> None:
        cb = Mock()
        ws_client.on_message(cb)
        payload = {"type": "event"}
        ws_client._handle_message(Mock(), json.dumps(payload))
        cb.assert_called_once_with(payload)

    def test_calls_on_message_callback_with_raw_fallback(self, ws_client) -> None:
        cb = Mock()
        ws_client.on_message(cb)
        ws_client._handle_message(Mock(), "plain text")
        cb.assert_called_once_with({"raw": "plain text"})

    def test_no_error_without_on_message_callback(self, ws_client) -> None:
        ws_client._handle_message(Mock(), '{"ok": true}')  # Should not raise

    def test_decodes_binary_frame_to_str(self, ws_client) -> None:
        ws_client._handle_message(Mock(), b"hello binary")
        item = ws_client._queue.get_nowait()
        assert item == {"raw": "hello binary"}

    def test_strips_null_bytes_from_binary(self, ws_client) -> None:
        ws_client._handle_message(Mock(), b"\x00hello\x00world")
        item = ws_client._queue.get_nowait()
        assert item == {"raw": "helloworld"}

    def test_binary_valid_json_is_parsed(self, ws_client) -> None:
        ws_client._handle_message(Mock(), b'{"event": "data", "key": "value"}')
        item = ws_client._queue.get_nowait()
        assert item == {"event": "data", "key": "value"}

    def test_binary_with_invalid_utf8_uses_replacement(self, ws_client) -> None:
        ws_client._handle_message(Mock(), b"hello\xff\xfeworld")
        item = ws_client._queue.get_nowait()
        assert item["raw"] == "hello\ufffd\ufffdworld"


class TestHandleError:
    """Tests for _handle_error()."""

    def test_calls_on_error_callback(self, ws_client) -> None:
        cb = Mock()
        ws_client.on_error(cb)
        exc = ConnectionError("lost connection")
        ws_client._handle_error(Mock(), exc)
        cb.assert_called_once_with(exc)

    def test_no_error_without_callback(self, ws_client) -> None:
        ws_client._handle_error(Mock(), RuntimeError("boom"))  # Should not raise


class TestHandleClose:
    """Tests for _handle_close().

    Note: _handle_close only clears _connected and stores the close
    code/msg.  The sentinel and on_close callback are fired by
    _run_forever_safe after the reconnect loop exits.
    """

    def test_clears_connected_event(self, ws_client) -> None:
        ws_client._connected.set()
        ws_client._handle_close(Mock(), 1000, "normal closure")
        assert not ws_client._connected.is_set()

    def test_stores_close_code_and_msg(self, ws_client) -> None:
        ws_client._handle_close(Mock(), 1001, "going away")
        assert ws_client._last_close_code == 1001
        assert ws_client._last_close_msg == "going away"

    def test_does_not_put_sentinel_directly(self, ws_client) -> None:
        ws_client._handle_close(Mock(), 1000, "normal closure")
        assert ws_client._queue.empty()

    def test_no_error_without_callback(self, ws_client) -> None:
        ws_client._handle_close(Mock(), 1000, "")  # Should not raise


# ---------------------------------------------------------------------------
# Connect / disconnect lifecycle
# ---------------------------------------------------------------------------


class TestConnect:
    """Tests for connect() and disconnect()."""

    @patch("mistapi.websockets.__ws_client.websocket.WebSocketApp")
    def test_connect_creates_websocket_app(self, mock_ws_cls, ws_client) -> None:
        mock_ws_instance = Mock()
        mock_ws_cls.return_value = mock_ws_instance

        ws_client.connect(run_in_background=False)

        mock_ws_cls.assert_called_once_with(
            "wss://api-ws.mist.com/api-ws/v1/stream",
            header={"Authorization": "Token test_token"},
            cookie=None,
            on_open=ws_client._handle_open,
            on_message=ws_client._handle_message,
            on_error=ws_client._handle_error,
            on_close=ws_client._handle_close,
        )
        mock_ws_instance.run_forever.assert_called_once()

    @patch("mistapi.websockets.__ws_client.websocket.WebSocketApp")
    def test_connect_drains_stale_queue_items(self, mock_ws_cls, ws_client) -> None:
        # Pre-populate queue with stale sentinel and data
        ws_client._queue.put(None)
        ws_client._queue.put({"old": "data"})
        assert not ws_client._queue.empty()

        mock_ws_cls.return_value = Mock()
        ws_client.connect(run_in_background=False)

        # Stale items should have been drained; only the final sentinel
        # from _run_forever_safe remains.
        assert ws_client._queue.get_nowait() is None
        assert ws_client._queue.empty()

    @patch("mistapi.websockets.__ws_client.websocket.WebSocketApp")
    def test_connect_background_starts_thread(self, mock_ws_cls, ws_client) -> None:
        mock_ws_instance = Mock()
        mock_ws_cls.return_value = mock_ws_instance

        with patch(
            "mistapi.websockets.__ws_client.threading.Thread"
        ) as mock_thread_cls:
            mock_thread = Mock()
            mock_thread_cls.return_value = mock_thread

            ws_client.connect(run_in_background=True)

            mock_thread_cls.assert_called_once_with(
                target=ws_client._run_forever_safe, daemon=True
            )
            mock_thread.start.assert_called_once()

    @patch("mistapi.websockets.__ws_client.websocket.WebSocketApp")
    def test_disconnect_calls_close(self, mock_ws_cls, ws_client) -> None:
        mock_ws_instance = Mock()
        mock_ws_cls.return_value = mock_ws_instance

        ws_client.connect(run_in_background=False)
        ws_client.disconnect()

        mock_ws_instance.close.assert_called_once()

    def test_disconnect_without_connect_is_noop(self, ws_client) -> None:
        ws_client.disconnect()  # Should not raise


# ---------------------------------------------------------------------------
# _run_forever_safe
# ---------------------------------------------------------------------------


class TestRunForeverSafe:
    """Tests for _run_forever_safe()."""

    def test_passes_ping_and_ssl_to_run_forever(self, single_channel_client) -> None:
        mock_ws = Mock()
        single_channel_client._ws = mock_ws
        # verify=True, cert=None => empty sslopt dict
        single_channel_client._run_forever_safe()
        mock_ws.run_forever.assert_called_once_with(
            ping_interval=15,
            ping_timeout=5,
            sslopt={},
        )

    def test_passes_sslopt_when_verify_false(self, mock_session) -> None:
        mock_session._session.verify = False
        mock_session._session.cert = None
        client = _MistWebsocket(mock_session, channels=["/ch"])
        mock_ws = Mock()
        client._ws = mock_ws
        client._run_forever_safe()
        mock_ws.run_forever.assert_called_once_with(
            ping_interval=30,
            ping_timeout=10,
            sslopt={"cert_reqs": ssl.CERT_NONE, "check_hostname": False},
        )

    def test_exception_triggers_error_and_close_handlers(self, ws_client) -> None:
        mock_ws = Mock()
        mock_ws.run_forever.side_effect = RuntimeError("connection failed")
        ws_client._ws = mock_ws

        error_cb = Mock()
        close_cb = Mock()
        ws_client.on_error(error_cb)
        ws_client.on_close(close_cb)

        ws_client._run_forever_safe()

        error_cb.assert_called_once()
        assert isinstance(error_cb.call_args[0][0], RuntimeError)
        # _handle_close stores (-1, str(exc)), _run_forever_safe forwards it
        close_cb.assert_called_once_with(-1, "connection failed")

    def test_run_forever_safe_puts_sentinel_on_exit(self, ws_client) -> None:
        mock_ws = Mock()
        ws_client._ws = mock_ws
        ws_client._run_forever_safe()
        assert ws_client._queue.get_nowait() is None


# ---------------------------------------------------------------------------
# receive() generator
# ---------------------------------------------------------------------------


class TestReceive:
    """Tests for the receive() generator."""

    def test_yields_queued_messages(self, ws_client) -> None:
        ws_client._connected.set()
        ws_client._queue.put({"event": "a"})
        ws_client._queue.put({"event": "b"})
        ws_client._queue.put(None)  # sentinel

        results = list(ws_client.receive())
        assert results == [{"event": "a"}, {"event": "b"}]

    def test_returns_immediately_when_not_connected_within_timeout(
        self, ws_client
    ) -> None:
        # _connected is never set, so wait(timeout=10) returns False.
        # Override timeout via monkey-patching for speed.
        original_wait = ws_client._connected.wait
        ws_client._connected.wait = lambda timeout=None: False

        results = list(ws_client.receive())
        assert results == []

        ws_client._connected.wait = original_wait

    def test_stops_on_none_sentinel(self, ws_client) -> None:
        ws_client._connected.set()
        ws_client._queue.put({"first": True})
        ws_client._queue.put(None)
        ws_client._queue.put({"should_not_appear": True})

        results = list(ws_client.receive())
        assert results == [{"first": True}]

    def test_stops_when_disconnected_and_queue_empty(self, ws_client) -> None:
        ws_client._connected.set()
        ws_client._queue.put({"msg": 1})

        gen = ws_client.receive()
        assert next(gen) == {"msg": 1}

        # Simulate disconnect: clear connected, queue is empty
        ws_client._connected.clear()
        results = list(gen)
        assert results == []


# ---------------------------------------------------------------------------
# Context manager
# ---------------------------------------------------------------------------


class TestContextManager:
    """Tests for __enter__ / __exit__."""

    def test_enter_returns_self(self, ws_client) -> None:
        assert ws_client.__enter__() is ws_client

    def test_exit_calls_disconnect(self, ws_client) -> None:
        mock_ws = Mock()
        ws_client._ws = mock_ws
        ws_client.__exit__(None, None, None)
        mock_ws.close.assert_called_once()

    def test_with_statement(self, mock_session) -> None:
        with _MistWebsocket(mock_session, channels=["/ch"]) as client:
            assert isinstance(client, _MistWebsocket)
        # After exiting, disconnect should have been called (no-op here since _ws is None)

    @patch("mistapi.websockets.__ws_client.websocket.WebSocketApp")
    def test_exit_disconnects_active_connection(
        self, mock_ws_cls, mock_session
    ) -> None:
        mock_ws_instance = Mock()
        mock_ws_cls.return_value = mock_ws_instance

        with _MistWebsocket(mock_session, channels=["/ch"]) as client:
            client.connect(run_in_background=False)

        mock_ws_instance.close.assert_called_once()


# ---------------------------------------------------------------------------
# ready()
# ---------------------------------------------------------------------------


class TestReady:
    """Tests for ready()."""

    def test_returns_false_when_ws_is_none(self, ws_client) -> None:
        assert ws_client.ready() is False

    def test_returns_true_when_ws_reports_ready(self, ws_client) -> None:
        mock_ws = Mock()
        mock_ws.ready.return_value = True
        ws_client._ws = mock_ws
        assert ws_client.ready() is True

    def test_returns_false_when_ws_not_ready(self, ws_client) -> None:
        mock_ws = Mock()
        mock_ws.ready.return_value = False
        ws_client._ws = mock_ws
        assert ws_client.ready() is False


# ---------------------------------------------------------------------------
# Initialisation defaults
# ---------------------------------------------------------------------------


class TestInit:
    """Tests for __init__ defaults."""

    def test_default_ping_interval_and_timeout(self, ws_client) -> None:
        assert ws_client._ping_interval == 30
        assert ws_client._ping_timeout == 10

    def test_custom_ping_interval_and_timeout(self, single_channel_client) -> None:
        assert single_channel_client._ping_interval == 15
        assert single_channel_client._ping_timeout == 5

    def test_queue_starts_empty(self, ws_client) -> None:
        assert ws_client._queue.empty()

    def test_connected_event_starts_unset(self, ws_client) -> None:
        assert not ws_client._connected.is_set()

    def test_ws_starts_none(self, ws_client) -> None:
        assert ws_client._ws is None

    def test_thread_starts_none(self, ws_client) -> None:
        assert ws_client._thread is None

    def test_negative_max_reconnect_attempts_raises(self, mock_session) -> None:
        with pytest.raises(ValueError, match="max_reconnect_attempts must be >= 0"):
            _MistWebsocket(mock_session, channels=["/ch"], max_reconnect_attempts=-1)

    def test_zero_reconnect_backoff_raises(self, mock_session) -> None:
        with pytest.raises(ValueError, match="reconnect_backoff must be > 0"):
            _MistWebsocket(mock_session, channels=["/ch"], reconnect_backoff=0)

    def test_negative_reconnect_backoff_raises(self, mock_session) -> None:
        with pytest.raises(ValueError, match="reconnect_backoff must be > 0"):
            _MistWebsocket(mock_session, channels=["/ch"], reconnect_backoff=-1.0)


# ---------------------------------------------------------------------------
# Public WebSocket channel classes
# ---------------------------------------------------------------------------


class TestSiteChannels:
    """Tests for public site-level WebSocket channel classes."""

    def test_clients_stats_events_channels(self, mock_session) -> None:
        ws = ClientsStatsEvents(mock_session, site_ids=["s1", "s2"])
        assert ws._channels == ["/sites/s1/stats/clients", "/sites/s2/stats/clients"]

    def test_device_cmd_events_channels(self, mock_session) -> None:
        ws = DeviceCmdEvents(mock_session, site_id="s1", device_ids=["d1", "d2"])
        assert ws._channels == ["/sites/s1/devices/d1/cmd", "/sites/s1/devices/d2/cmd"]

    def test_device_stats_events_channels(self, mock_session) -> None:
        ws = DeviceStatsEvents(mock_session, site_ids=["s1"])
        assert ws._channels == ["/sites/s1/stats/devices"]

    def test_device_upgrades_events_channels(self, mock_session) -> None:
        ws = DeviceEvents(mock_session, site_ids=["s1"])
        assert ws._channels == ["/sites/s1/devices"]

    def test_site_mxedges_stats_events_channels(self, mock_session) -> None:
        ws = SiteMxEdgesStatsEvents(mock_session, site_ids=["s1"])
        assert ws._channels == ["/sites/s1/stats/mxedges"]

    def test_pcap_events_channels(self, mock_session) -> None:
        ws = PcapEvents(mock_session, site_id="s1")
        assert ws._channels == ["/sites/s1/pcaps"]

    def test_custom_ping_settings(self, mock_session) -> None:
        ws = DeviceStatsEvents(
            mock_session, site_ids=["s1"], ping_interval=60, ping_timeout=20
        )
        assert ws._ping_interval == 60
        assert ws._ping_timeout == 20

    def test_inherits_from_mist_websocket(self, mock_session) -> None:
        ws = DeviceCmdEvents(mock_session, site_id="s1", device_ids=["d1"])
        assert isinstance(ws, _MistWebsocket)


class TestOrgChannels:
    """Tests for public org-level WebSocket channel classes."""

    def test_insights_events_channels(self, mock_session) -> None:
        ws = InsightsEvents(mock_session, org_id="o1")
        assert ws._channels == ["/orgs/o1/insights/summary"]

    def test_org_mxedges_stats_events_channels(self, mock_session) -> None:
        ws = OrgMxEdgesStatsEvents(mock_session, org_id="o1")
        assert ws._channels == ["/orgs/o1/stats/mxedges"]

    def test_mxedges_upgrades_events_channels(self, mock_session) -> None:
        ws = MxEdgesEvents(mock_session, org_id="o1")
        assert ws._channels == ["/orgs/o1/mxedges"]

    def test_inherits_from_mist_websocket(self, mock_session) -> None:
        ws = InsightsEvents(mock_session, org_id="o1")
        assert isinstance(ws, _MistWebsocket)


class TestLocationChannels:
    """Tests for public location-level WebSocket channel classes."""

    def test_ble_assets_events_channels(self, mock_session) -> None:
        ws = BleAssetsEvents(mock_session, site_id="s1", map_ids=["m1", "m2"])
        assert ws._channels == [
            "/sites/s1/stats/maps/m1/assets",
            "/sites/s1/stats/maps/m2/assets",
        ]

    def test_connected_clients_events_channels(self, mock_session) -> None:
        ws = ConnectedClientsEvents(mock_session, site_id="s1", map_ids=["m1"])
        assert ws._channels == ["/sites/s1/stats/maps/m1/clients"]

    def test_sdk_clients_events_channels(self, mock_session) -> None:
        ws = SdkClientsEvents(mock_session, site_id="s1", map_ids=["m1"])
        assert ws._channels == ["/sites/s1/stats/maps/m1/sdkclients"]

    def test_unconnected_clients_events_channels(self, mock_session) -> None:
        ws = UnconnectedClientsEvents(mock_session, site_id="s1", map_ids=["m1"])
        assert ws._channels == ["/sites/s1/stats/maps/m1/unconnected_clients"]

    def test_discovered_ble_assets_events_channels(self, mock_session) -> None:
        ws = DiscoveredBleAssetsEvents(mock_session, site_id="s1", map_ids=["m1"])
        assert ws._channels == ["/sites/s1/stats/maps/m1/discovered_assets"]

    def test_inherits_from_mist_websocket(self, mock_session) -> None:
        ws = BleAssetsEvents(mock_session, site_id="s1", map_ids=["m1"])
        assert isinstance(ws, _MistWebsocket)


class TestSessionChannel:
    """Tests for the SessionWithUrl WebSocket channel class."""

    def test_session_with_url_channels(self, mock_session) -> None:
        ws = SessionWithUrl(mock_session, url="wss://example.com/custom")
        assert ws._channels == []
        assert ws._build_ws_url() == "wss://example.com/custom"

    def test_inherits_from_mist_websocket(self, mock_session) -> None:
        ws = SessionWithUrl(mock_session, url="wss://example.com/custom")
        assert isinstance(ws, _MistWebsocket)


# ---------------------------------------------------------------------------
# Auto-reconnect
# ---------------------------------------------------------------------------


class TestAutoReconnect:
    """Tests for the auto_reconnect feature."""

    def _make_client(self, mock_session, **kwargs):
        defaults = dict(
            mist_session=mock_session,
            channels=["/ch"],
            auto_reconnect=True,
            max_reconnect_attempts=3,
            reconnect_backoff=0.01,  # fast for tests
        )
        defaults.update(kwargs)
        return _MistWebsocket(**defaults)

    def test_retries_on_transient_failure(self, mock_session) -> None:
        client = self._make_client(mock_session, max_reconnect_attempts=2)
        call_count = 0

        def fake_run_forever(**kwargs):
            nonlocal call_count
            call_count += 1
            # Simulate connection drop
            client._handle_close(client._ws, 1006, "abnormal closure")

        mock_ws = Mock()
        mock_ws.run_forever.side_effect = fake_run_forever
        with patch.object(client, "_create_ws_app", return_value=mock_ws):
            client._ws = mock_ws
            client._run_forever_safe()

        # 1 initial + 2 retries = 3 calls
        assert call_count == 3

    def test_gives_up_after_max_attempts(self, mock_session) -> None:
        client = self._make_client(mock_session, max_reconnect_attempts=2)
        close_cb = Mock()
        client.on_close(close_cb)

        mock_ws = Mock()
        mock_ws.run_forever.side_effect = lambda **kw: client._handle_close(
            mock_ws, 1006, "drop"
        )
        with patch.object(client, "_create_ws_app", return_value=mock_ws):
            client._ws = mock_ws
            client._run_forever_safe()

        # Callback fires exactly once (on final close)
        close_cb.assert_called_once_with(1006, "drop")
        # Sentinel put exactly once
        assert client._queue.get_nowait() is None
        assert client._queue.empty()

    def test_disconnect_during_backoff_exits_immediately(self, mock_session) -> None:
        client = self._make_client(
            mock_session, max_reconnect_attempts=5, reconnect_backoff=10.0
        )
        call_count = 0
        entered_backoff = threading.Event()

        original_wait = client._user_disconnect.wait

        def wait_and_signal(timeout=None):
            """Signal that the backoff wait has started, then delegate."""
            entered_backoff.set()
            return original_wait(timeout=timeout)

        def fake_run_forever(**kwargs):
            nonlocal call_count
            call_count += 1
            client._handle_close(client._ws, 1006, "drop")

        mock_ws = Mock()
        mock_ws.run_forever.side_effect = fake_run_forever

        def disconnect_when_ready():
            entered_backoff.wait()  # deterministic: wait until backoff starts
            client.disconnect()

        with (
            patch.object(client, "_create_ws_app", return_value=mock_ws),
            patch.object(client._user_disconnect, "wait", side_effect=wait_and_signal),
        ):
            client._ws = mock_ws
            t = threading.Thread(target=disconnect_when_ready)
            t.start()
            client._run_forever_safe()
            t.join(timeout=2)

        # Should have run once, then been interrupted during first backoff
        assert call_count == 1
        assert client._queue.get_nowait() is None

    def test_handle_open_resets_reconnect_attempts(self, mock_session) -> None:
        client = self._make_client(mock_session, max_reconnect_attempts=3)
        client._reconnect_attempts = 5
        client._handle_open(Mock())
        assert client._reconnect_attempts == 0

    def test_successful_reconnect_resets_counter(self, mock_session) -> None:
        client = self._make_client(mock_session, max_reconnect_attempts=2)
        call_count = 0

        def fake_run_forever(**kwargs):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                # First connection drops
                client._handle_close(client._ws, 1006, "drop")
            elif call_count == 2:
                # Reconnect succeeds, then simulate open + later drop
                client._handle_open(client._ws)
                client._handle_close(client._ws, 1006, "drop again")
            elif call_count == 3:
                # Another reconnect succeeds, then clean exit
                client._handle_open(client._ws)
                client._handle_close(client._ws, 1006, "drop again")
            elif call_count == 4:
                # Final reconnect succeeds then user disconnects
                client._user_disconnect.set()

        mock_ws = Mock()
        mock_ws.run_forever.side_effect = fake_run_forever
        with patch.object(client, "_create_ws_app", return_value=mock_ws):
            client._ws = mock_ws
            client._run_forever_safe()

        # Counter was reset by _handle_open, so we got more than max_attempts+1 total calls
        assert call_count == 4

    def test_no_reconnect_when_disabled(self, mock_session) -> None:
        client = _MistWebsocket(
            mist_session=mock_session,
            channels=["/ch"],
            auto_reconnect=False,
        )
        mock_ws = Mock()
        client._ws = mock_ws
        client._run_forever_safe()

        # run_forever called exactly once, no retry
        mock_ws.run_forever.assert_called_once()
