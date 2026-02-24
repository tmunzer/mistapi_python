"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
This module provides the _MistWebsocket base class for WebSocket connections
to the Mist API streaming endpoint (wss://{host}/api-ws/v1/stream).
"""

import json
import queue
import threading
from collections.abc import Callable, Generator
from typing import TYPE_CHECKING

import websocket

if TYPE_CHECKING:
    from mistapi import APISession


class _MistWebsocket:
    """
    Base class for Mist API WebSocket channels.

    Connects to wss://{host}/api-ws/v1/stream and subscribes to a channel
    by sending {"subscribe": "<channel>"} on open.

    Auth is handled automatically:
    - API token sessions use an Authorization header.
    - Login/password sessions pass the requests Session cookies.
    """

    def __init__(
        self,
        mist_session: "APISession",
        channel: str,
        ping_interval: int = 30,
        ping_timeout: int = 10,
    ) -> None:
        self._mist_session = mist_session
        self._channel = channel
        self._ping_interval = ping_interval
        self._ping_timeout = ping_timeout
        self._ws: websocket.WebSocketApp | None = None
        self._thread: threading.Thread | None = None
        self._queue: queue.Queue[dict | None] = queue.Queue()
        self._on_message_cb: Callable[[dict], None] | None = None
        self._on_error_cb: Callable[[Exception], None] | None = None
        self._on_open_cb: Callable[[], None] | None = None
        self._on_close_cb: Callable[[int, str], None] | None = None

    # ------------------------------------------------------------------
    # Auth / URL helpers

    def _build_ws_url(self) -> str:
        return f"wss://{self._mist_session._cloud_uri.replace('api.', 'api-ws.')}/api-ws/v1/stream"

    def _get_headers(self) -> dict:
        if self._mist_session._apitoken:
            token = self._mist_session._apitoken[self._mist_session._apitoken_index]
            return {"Authorization": f"Token {token}"}
        return {}

    def _get_cookie(self) -> str | None:
        cookies = self._mist_session._session.cookies
        if cookies:
            pairs = "; ".join(f"{c.name}={c.value}" for c in cookies)
            return pairs if pairs else None
        return None

    # ------------------------------------------------------------------
    # Callback registration

    def on_message(self, callback: Callable[[dict], None]) -> None:
        """Register a callback invoked for every incoming message."""
        self._on_message_cb = callback

    def on_error(self, callback: Callable[[Exception], None]) -> None:
        """Register a callback invoked on WebSocket errors."""
        self._on_error_cb = callback

    def on_open(self, callback: Callable[[], None]) -> None:
        """Register a callback invoked when the connection is established."""
        self._on_open_cb = callback

    def on_close(self, callback: Callable[[int, str], None]) -> None:
        """Register a callback invoked when the connection closes."""
        self._on_close_cb = callback

    # ------------------------------------------------------------------
    # Internal WebSocketApp handlers

    def _handle_open(self, ws: websocket.WebSocketApp) -> None:
        ws.send(json.dumps({"subscribe": self._channel}))
        if self._on_open_cb:
            self._on_open_cb()

    def _handle_message(self, ws: websocket.WebSocketApp, message: str) -> None:
        try:
            data = json.loads(message)
        except json.JSONDecodeError:
            data = {"raw": message}
        self._queue.put(data)
        if self._on_message_cb:
            self._on_message_cb(data)

    def _handle_error(self, ws: websocket.WebSocketApp, error: Exception) -> None:
        if self._on_error_cb:
            self._on_error_cb(error)

    def _handle_close(
        self,
        ws: websocket.WebSocketApp,
        close_status_code: int,
        close_msg: str,
    ) -> None:
        self._queue.put(None)  # Signals receive() generator to stop
        if self._on_close_cb:
            self._on_close_cb(close_status_code, close_msg)

    # ------------------------------------------------------------------
    # Lifecycle

    def connect(self, run_in_background: bool = True) -> None:
        """
        Open the WebSocket connection and subscribe to the channel.

        PARAMS
        -----------
        run_in_background : bool, default True
            If True, runs the WebSocket loop in a daemon thread (non-blocking).
            If False, blocks the calling thread until disconnected.
        """
        self._ws = websocket.WebSocketApp(
            self._build_ws_url(),
            header=self._get_headers(),
            cookie=self._get_cookie(),
            on_open=self._handle_open,
            on_message=self._handle_message,
            on_error=self._handle_error,
            on_close=self._handle_close,
        )
        if run_in_background:
            self._thread = threading.Thread(target=self._run_forever_safe, daemon=True)
            self._thread.start()
        else:
            self._run_forever_safe()

    def _run_forever_safe(self) -> None:
        if self._ws:
            try:
                self._ws.run_forever(
                    ping_interval=self._ping_interval, ping_timeout=self._ping_timeout
                )
            except Exception as exc:
                self._handle_error(self._ws, exc)
                self._handle_close(self._ws, -1, str(exc))

    def disconnect(self) -> None:
        """Close the WebSocket connection."""
        if self._ws:
            self._ws.close()

    def receive(self) -> Generator[dict, None, None]:
        """
        Blocking generator that yields each incoming message as a dict.

        Exits cleanly when the connection closes (disconnect() is called or
        the server closes the connection).

        Intended for use after connect(run_in_background=True).
        """
        while True:
            item = self._queue.get()
            if item is None:
                break
            yield item

    # ------------------------------------------------------------------
    # Context manager

    def __enter__(self) -> "_MistWebsocket":
        return self

    def __exit__(self, *args) -> None:
        self.disconnect()

    def ready(self) -> bool | None:
        """Returns True if the WebSocket connection is open and ready."""
        return self._ws is not None and self._ws.ready()
