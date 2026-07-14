"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
WebSocket channel for Remote Commands events.
"""

from urllib.parse import urlparse

from mistapi import APISession
from mistapi.websockets.__ws_client import _MistWebsocket


class SessionWithUrl(_MistWebsocket):
    """WebSocket stream for remote commands events.

    Open a WebSocket connection to a custom channel URL for remote command events.
    This is a base class that can be used to implement specific remote command event streams by providing the
    appropriate channel URL.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    url : str
        URL of the WebSocket channel to connect to.

        .. warning::

            The session's authentication credentials (API token or cookies)
            are sent to whatever host is specified in this URL. Only use
            trusted URLs — never pass user-supplied or untrusted input.
    ping_interval : int, default 60
        Interval in seconds to send WebSocket ping frames (keep-alive).
    ping_timeout : int | None, default None
        Time in seconds to wait for a ping response before considering the
        connection dead. Defaults to ``min(45, ping_interval - 1)`` when
        pings are enabled, or ``45`` when ``ping_interval`` is 0 (unused
        since pings are disabled). Must be lower than ping_interval when
        pings are enabled.
    auto_reconnect : bool, default False
        Automatically reconnect on unexpected disconnections using exponential backoff.
    max_reconnect_attempts : int, default 5
        Maximum number of reconnect attempts before giving up.
    reconnect_backoff : float, default 2.0
        Base backoff delay in seconds. Doubles after each failed attempt.
    max_reconnect_backoff : float | None, default None
        Maximum backoff delay in seconds. If None, backoff grows indefinitely.
    queue_maxsize : int, default 0
        Maximum number of messages buffered in each of the internal queues
        used for the ``receive()`` generator and callback delivery. ``0``
        means unbounded. When set, incoming messages are dropped with a
        warning when the target queue is full, preventing memory growth on
        high-frequency streams.
    subscription_watchdog_timeout : float, default 10.0
        Maximum time in seconds to wait for all channel subscription
        acknowledgements after connect. On timeout, the error is reported to
        ``on_error`` and the connection is closed (auto_reconnect, when
        enabled, then reconnects).
    rate_limit_backoff : float, default 30.0
        Minimum reconnect delay in seconds after an HTTP 429 rate-limit
        response.
    throughput_log_interval : int, default 100
        Log queue depth and processed counts every N messages. ``0`` disables
        periodic throughput logs.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = SessionWithUrl(session, url="wss://example.com/channel")
        ws.on_message(lambda data: print(data))
        ws.connect()  # non-blocking, runs in background thread
        input("Press Enter to stop")
        ws.disconnect()

    Generator style::

        ws = SessionWithUrl(session, url="wss://example.com/channel")
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with SessionWithUrl(session, url="wss://example.com/channel") as ws:
            ws.on_message(my_handler)
            ws.connect()  # non-blocking, runs in background thread
            time.sleep(60)
    """

    def __init__(
        self,
        mist_session: APISession,
        url: str,
        ping_interval: int = 60,
        ping_timeout: int | None = None,
        auto_reconnect: bool = False,
        max_reconnect_attempts: int = 5,
        reconnect_backoff: float = 2.0,
        max_reconnect_backoff: float | None = None,
        queue_maxsize: int = 0,
        subscription_watchdog_timeout: float = 10.0,
        rate_limit_backoff: float = 30.0,
        throughput_log_interval: int = 100,
    ) -> None:
        parsed = urlparse(url)
        if parsed.scheme.lower() != "wss" or not parsed.netloc:
            raise ValueError("url must be a valid wss:// URL with a host")
        self._url = url
        super().__init__(
            mist_session,
            channels=[],
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            auto_reconnect=auto_reconnect,
            max_reconnect_attempts=max_reconnect_attempts,
            reconnect_backoff=reconnect_backoff,
            max_reconnect_backoff=max_reconnect_backoff,
            queue_maxsize=queue_maxsize,
            subscription_watchdog_timeout=subscription_watchdog_timeout,
            rate_limit_backoff=rate_limit_backoff,
            throughput_log_interval=throughput_log_interval,
        )

    def _build_ws_url(self) -> str:
        return self._url
