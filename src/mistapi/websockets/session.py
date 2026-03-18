"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
WebSocket channel for Remote Commands events.
"""

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
    ping_interval : int, default 30
        Interval in seconds to send WebSocket ping frames (keep-alive).
    ping_timeout : int, default 10
        Time in seconds to wait for a ping response before considering the connection dead.
    auto_reconnect : bool, default False
        Automatically reconnect on unexpected disconnections using exponential backoff.
    max_reconnect_attempts : int, default 5
        Maximum number of reconnect attempts before giving up.
    reconnect_backoff : float, default 2.0
        Base backoff delay in seconds. Doubles after each failed attempt.

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
        ping_interval: int = 30,
        ping_timeout: int = 10,
        auto_reconnect: bool = False,
        max_reconnect_attempts: int = 5,
        reconnect_backoff: float = 2.0,
    ) -> None:
        if not url.startswith("wss://"):
            raise ValueError("url must use the wss:// scheme")
        self._url = url
        super().__init__(
            mist_session,
            channels=[],
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            auto_reconnect=auto_reconnect,
            max_reconnect_attempts=max_reconnect_attempts,
            reconnect_backoff=reconnect_backoff,
        )

    def _build_ws_url(self) -> str:
        return self._url
