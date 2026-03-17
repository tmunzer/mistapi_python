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
import ssl
import threading
from collections.abc import Callable, Generator
from typing import TYPE_CHECKING

import websocket

from mistapi.__logger import logger

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
        channels: list[str],
        ping_interval: int = 30,
        ping_timeout: int = 10,
        auto_reconnect: bool = False,
        max_reconnect_attempts: int = 5,
        reconnect_backoff: float = 2.0,
    ) -> None:
        self._mist_session = mist_session
        self._channels = channels
        self._ping_interval = ping_interval
        self._ping_timeout = ping_timeout
        self._auto_reconnect = auto_reconnect
        self._max_reconnect_attempts = max_reconnect_attempts
        self._reconnect_backoff = reconnect_backoff
        self._ws: websocket.WebSocketApp | None = None
        self._thread: threading.Thread | None = None
        self._queue: queue.Queue[dict | None] = queue.Queue()
        self._connected = (
            threading.Event()
        )  # tracks whether the WebSocket connection is currently open
        self._user_disconnect = threading.Event()
        self._reconnect_attempts = 0
        self._last_close_code: int | None = None
        self._last_close_msg: str | None = None
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
            safe = []
            for c in cookies:
                has_crlf = (
                    "\r" in c.name
                    or "\n" in c.name
                    or (c.value and ("\r" in c.value or "\n" in c.value))
                )
                if has_crlf:
                    logger.warning(
                        "Skipping cookie %r: contains CRLF characters (possible header injection)",
                        c.name,
                    )
                    continue
                safe.append(f"{c.name}={c.value}")
            return "; ".join(safe) if safe else None
        return None

    def _build_sslopt(self) -> dict:
        """Build SSL options from the APISession's requests.Session."""
        sslopt: dict = {}
        session = self._mist_session._session
        if session.verify is False:
            sslopt["cert_reqs"] = ssl.CERT_NONE
        elif isinstance(session.verify, str):
            sslopt["ca_certs"] = session.verify
        if session.cert:
            if isinstance(session.cert, str):
                sslopt["certfile"] = session.cert
            elif isinstance(session.cert, tuple):
                sslopt["certfile"] = session.cert[0]
                if len(session.cert) > 1:
                    sslopt["keyfile"] = session.cert[1]
        return sslopt

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
        for channel in self._channels:
            ws.send(json.dumps({"subscribe": channel}))
        self._reconnect_attempts = 0
        self._connected.set()
        if self._on_open_cb:
            self._on_open_cb()

    def _handle_message(self, ws: websocket.WebSocketApp, message: str | bytes) -> None:
        if isinstance(message, bytes):
            message = message.replace(b"\x00", b"").decode("utf-8", errors="replace")
        try:
            data = json.loads(message)
        except (json.JSONDecodeError, TypeError):
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
        self._connected.clear()
        self._last_close_code = close_status_code
        self._last_close_msg = close_msg

    # ------------------------------------------------------------------
    # Lifecycle

    def _create_ws_app(self) -> websocket.WebSocketApp:
        """Create a new WebSocketApp instance with current auth/URL."""
        return websocket.WebSocketApp(
            self._build_ws_url(),
            header=self._get_headers(),
            cookie=self._get_cookie(),
            on_open=self._handle_open,
            on_message=self._handle_message,
            on_error=self._handle_error,
            on_close=self._handle_close,
        )

    def connect(self, run_in_background: bool = True) -> None:
        """
        Open the WebSocket connection and subscribe to the channel.

        PARAMS
        -----------
        run_in_background : bool, default True
            If True, runs the WebSocket loop in a daemon thread (non-blocking).
            If False, blocks the calling thread until disconnected.
        """
        self._user_disconnect.clear()
        self._reconnect_attempts = 0
        # Drain stale sentinel from previous connection
        while not self._queue.empty():
            try:
                self._queue.get_nowait()
            except queue.Empty:
                break

        self._ws = self._create_ws_app()
        if run_in_background:
            self._thread = threading.Thread(target=self._run_forever_safe, daemon=True)
            self._thread.start()
        else:
            self._run_forever_safe()

    def _run_forever_safe(self) -> None:
        while True:
            try:
                sslopt = self._build_sslopt()
                self._ws.run_forever(
                    ping_interval=self._ping_interval,
                    ping_timeout=self._ping_timeout,
                    sslopt=sslopt,
                )
            except Exception as exc:
                self._handle_error(self._ws, exc)
                self._handle_close(self._ws, -1, str(exc))

            if self._user_disconnect.is_set() or not self._auto_reconnect:
                break

            self._reconnect_attempts += 1
            if self._reconnect_attempts > self._max_reconnect_attempts:
                logger.warning(
                    "Max reconnect attempts (%d) reached, giving up",
                    self._max_reconnect_attempts,
                )
                break

            delay = self._reconnect_backoff * (2 ** (self._reconnect_attempts - 1))
            logger.info(
                "Reconnecting in %.1fs (attempt %d/%d)",
                delay,
                self._reconnect_attempts,
                self._max_reconnect_attempts,
            )
            if self._user_disconnect.wait(timeout=delay):
                break  # disconnect() called during backoff

            self._ws = self._create_ws_app()

        # Final close: put sentinel and call callback
        self._queue.put(None)
        if self._on_close_cb:
            self._on_close_cb(self._last_close_code, self._last_close_msg)

    def disconnect(self) -> None:
        """Close the WebSocket connection."""
        self._user_disconnect.set()
        ws = self._ws
        if ws:
            ws.close()

    def receive(self) -> Generator[dict, None, None]:
        """
        Blocking generator that yields each incoming message as a dict.

        Exits cleanly when the connection closes (disconnect() is called or
        the server closes the connection).

        Intended for use after connect(run_in_background=True).
        """
        if not self._connected.wait(timeout=10):
            return
        while True:
            try:
                item = self._queue.get(timeout=1)
            except queue.Empty:
                if not self._connected.is_set() and self._queue.empty():
                    if self._auto_reconnect and not self._user_disconnect.is_set():
                        continue  # reconnect in progress, keep waiting
                    break
                continue
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
