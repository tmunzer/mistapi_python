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
    ping_interval : int, default 30
        Interval in seconds to send WebSocket ping frames (keep-alive).
    ping_timeout : int, default 10
        Time in seconds to wait for a ping response before considering the connection dead.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = sessionWithUrl(session, url="wss://example.com/channel")
        ws.on_message(lambda data: print(data))
        ws.connect()  # non-blocking, runs in background thread
        input("Press Enter to stop")
        ws.disconnect()

    Generator style::

        ws = sessionWithUrl(session, url="wss://example.com/channel")
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with sessionWithUrl(session, url="wss://example.com/channel") as ws:
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
    ) -> None:
        super().__init__(
            mist_session,
            channels=[url],
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
        )
