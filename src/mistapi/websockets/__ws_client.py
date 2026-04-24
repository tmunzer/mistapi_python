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
import logging
import queue
import re
import ssl
import threading
from collections.abc import Callable, Generator
from typing import TYPE_CHECKING, Any

import websocket

from mistapi.__logger import logger


class _HeaderRedactFilter(logging.Filter):
    """Redact Authorization and Cookie values from websocket-client log output."""

    _REDACT = re.compile(r"((?:Authorization|Cookie):\s*).+", re.IGNORECASE)

    def filter(self, record: logging.LogRecord) -> bool:
        rendered = record.getMessage()
        redacted = self._REDACT.sub(r"\1****", rendered)
        if redacted != rendered:
            record.msg = redacted
            record.args = ()
        return True


_ws_logger = logging.getLogger("websocket")
if not any(isinstance(f, _HeaderRedactFilter) for f in _ws_logger.filters):
    _ws_logger.addFilter(_HeaderRedactFilter())

if TYPE_CHECKING:
    from mistapi import APISession


MAX_CHANNELS_PER_CONNECTION = 2000
HIGH_CHANNEL_COUNT_WARNING = 1500


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
        ping_interval: int = 60,
        ping_timeout: int = 45,
        auto_reconnect: bool = False,
        max_reconnect_attempts: int = 5,
        reconnect_backoff: float = 2.0,
        max_reconnect_backoff: float | None = None,
        queue_maxsize: int = 0,
        subscription_watchdog_timeout: float = 10.0,
        rate_limit_backoff: float = 30.0,
        throughput_log_interval: int = 100,
    ) -> None:
        if ping_interval < 0:
            raise ValueError("ping_interval must be >= 0")
        if ping_timeout <= 0:
            raise ValueError("ping_timeout must be > 0")
        if ping_interval and ping_interval <= ping_timeout:
            raise ValueError(
                "ping_interval must be greater than ping_timeout when enabled"
            )
        if max_reconnect_attempts < 0:
            raise ValueError("max_reconnect_attempts must be >= 0 (0 = unlimited)")
        if reconnect_backoff <= 0:
            raise ValueError("reconnect_backoff must be > 0")
        if max_reconnect_backoff is not None and max_reconnect_backoff <= 0:
            raise ValueError("max_reconnect_backoff must be > 0")
        if queue_maxsize < 0:
            raise ValueError("queue_maxsize must be >= 0")
        if subscription_watchdog_timeout <= 0:
            raise ValueError("subscription_watchdog_timeout must be > 0")
        if rate_limit_backoff <= 0:
            raise ValueError("rate_limit_backoff must be > 0")
        if throughput_log_interval < 0:
            raise ValueError("throughput_log_interval must be >= 0")

        deduped_channels = list(dict.fromkeys(channels))
        if len(deduped_channels) != len(channels):
            logger.warning(
                "Duplicate channels detected; using %d unique channels instead of %d",
                len(deduped_channels),
                len(channels),
            )
        if len(deduped_channels) > MAX_CHANNELS_PER_CONNECTION:
            raise ValueError(
                f"Too many channels ({len(deduped_channels)}). "
                f"Mist supports up to {MAX_CHANNELS_PER_CONNECTION} channels per connection"
            )
        if len(deduped_channels) >= HIGH_CHANNEL_COUNT_WARNING:
            logger.warning(
                "High channel count (%d). Consider spreading subscriptions over multiple "
                "WebSocket connections to reduce message backlog risk.",
                len(deduped_channels),
            )

        self._mist_session = mist_session
        self._channels = deduped_channels
        self._expected_channels = set(deduped_channels)
        self._ping_interval = ping_interval
        self._ping_timeout = ping_timeout
        self._auto_reconnect = auto_reconnect
        self._max_reconnect_attempts = max_reconnect_attempts
        self._reconnect_backoff = reconnect_backoff
        self._max_reconnect_backoff = max_reconnect_backoff
        self._subscription_watchdog_timeout = subscription_watchdog_timeout
        self._rate_limit_backoff = rate_limit_backoff
        self._throughput_log_interval = throughput_log_interval
        self._lock = threading.Lock()
        self._subscription_lock = threading.Lock()
        self._metrics_lock = threading.Lock()
        self._ws: websocket.WebSocketApp | None = None
        self._thread: threading.Thread | None = None
        self._callback_thread: threading.Thread | None = None
        self._subscription_watchdog: threading.Timer | None = None
        self._queue: queue.Queue[dict | None] = queue.Queue(maxsize=queue_maxsize)
        self._callback_queue: queue.Queue[dict | None] = queue.Queue(
            maxsize=queue_maxsize
        )
        self._connected = (
            threading.Event()
        )  # tracks whether the WebSocket connection is currently open
        self._user_disconnect = threading.Event()
        self._callback_stop = threading.Event()
        self._finished = threading.Event()
        self._finished.set()  # not running initially
        self._reconnect_attempts = 0
        self._last_close_code: int | None = None
        self._last_close_msg: str | None = None
        self._last_http_status: int | None = None
        self._subscribed_channels: set[str] = set()
        self._messages_received = 0
        self._messages_dropped = 0
        self._messages_processed = 0
        self._on_message_cb: Callable[[dict], None] | None = None
        self._on_error_cb: Callable[[Exception], None] | None = None
        self._on_open_cb: Callable[[], None] | None = None
        self._on_close_cb: Callable[[int | None, str | None], None] | None = None
        self._on_ping_cb: Callable[[str | bytes | None], None] | None = None
        self._on_pong_cb: Callable[[str | bytes | None], None] | None = None

    # ------------------------------------------------------------------
    # Auth / URL helpers

    def _build_ws_url(self) -> str:
        cloud_uri = self._mist_session._cloud_uri
        if not cloud_uri.startswith("api."):
            logger.warning(
                "cloud_uri %r does not start with 'api.'; "
                "WebSocket URL may be incorrect",
                cloud_uri,
            )
        ws_host = cloud_uri.replace("api.", "api-ws.", 1)
        return f"wss://{ws_host}/api-ws/v1/stream"

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
                safe.append(f"{c.name}={c.value or ''}")
            return "; ".join(safe) if safe else None
        return None

    def _build_sslopt(self) -> dict:
        """Build SSL options from the APISession's requests.Session."""
        sslopt: dict = {}
        session = self._mist_session._session
        if session.verify is False:
            sslopt["cert_reqs"] = ssl.CERT_NONE
            sslopt["check_hostname"] = False
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

    def on_close(self, callback: Callable[[int | None, str | None], None]) -> None:
        """Register a callback invoked when the connection closes."""
        self._on_close_cb = callback

    def on_ping(self, callback: Callable[[str | bytes | None], None]) -> None:
        """Register a callback invoked when a ping frame is received."""
        self._on_ping_cb = callback

    def on_pong(self, callback: Callable[[str | bytes | None], None]) -> None:
        """Register a callback invoked when a pong frame is received."""
        self._on_pong_cb = callback

    # ------------------------------------------------------------------
    # Internal helpers

    @staticmethod
    def _extract_status_code(error: Exception) -> int | None:
        status_code = getattr(error, "status_code", None)
        if isinstance(status_code, int):
            return status_code
        response = getattr(error, "response", None)
        if response is not None:
            response_code = getattr(response, "status_code", None)
            if isinstance(response_code, int):
                return response_code
        return None

    def _drain_queue(self, target_queue: queue.Queue[Any]) -> None:
        while not target_queue.empty():
            try:
                target_queue.get_nowait()
            except queue.Empty:
                break

    def _start_callback_worker(self) -> None:
        if self._callback_thread is not None and self._callback_thread.is_alive():
            return
        self._callback_stop.clear()
        self._callback_thread = threading.Thread(
            target=self._run_callback_worker, daemon=True
        )
        self._callback_thread.start()

    def _run_callback_worker(self) -> None:
        while True:
            if self._callback_stop.is_set():
                break
            try:
                item = self._callback_queue.get(timeout=1)
            except queue.Empty:
                if self._finished.is_set() and self._callback_queue.empty():
                    break
                continue
            if item is None:
                if self._callback_stop.is_set() or self._finished.is_set():
                    break
                continue
            callback = self._on_message_cb
            if callback is None:
                continue
            try:
                callback(item)
            except Exception:
                logger.exception("on_message callback raised")
            with self._metrics_lock:
                self._messages_processed += 1
                messages_processed = self._messages_processed
                messages_dropped = self._messages_dropped
            if (
                self._throughput_log_interval
                and messages_processed % self._throughput_log_interval == 0
            ):
                logger.info(
                    "WebSocket callback worker processed %d messages. "
                    "Callback queue size=%d dropped=%d",
                    messages_processed,
                    self._callback_queue.qsize(),
                    messages_dropped,
                )

    def _cancel_subscription_watchdog(self) -> None:
        with self._lock:
            timer = self._subscription_watchdog
            self._subscription_watchdog = None
        if timer is not None:
            timer.cancel()

    def _arm_subscription_watchdog(self, ws: websocket.WebSocketApp) -> None:
        if not self._expected_channels:
            return

        def _watchdog_expired() -> None:
            if self._user_disconnect.is_set():
                return
            with self._lock:
                current_ws = self._ws
            if ws is not current_ws:
                return
            with self._subscription_lock:
                missing = sorted(self._expected_channels - self._subscribed_channels)
            if not missing:
                return
            preview = ", ".join(missing[:5])
            if len(missing) > 5:
                preview = f"{preview}, ..."
            self._last_close_code = 1008
            self._last_close_msg = (
                f"subscription watchdog timeout: missing {len(missing)} channels"
            )
            logger.error(
                "Subscription watchdog timeout after %.1fs: received %d/%d subscriptions. "
                "Missing: %s",
                self._subscription_watchdog_timeout,
                len(self._expected_channels) - len(missing),
                len(self._expected_channels),
                preview,
            )
            ws.close()

        timer = threading.Timer(self._subscription_watchdog_timeout, _watchdog_expired)
        timer.daemon = True
        self._cancel_subscription_watchdog()
        with self._lock:
            self._subscription_watchdog = timer
        timer.start()

    def _process_subscription_event(
        self, ws: websocket.WebSocketApp, data: dict
    ) -> None:
        event = data.get("event")
        channel = data.get("channel")
        if not isinstance(channel, str):
            channel = None

        if event == "channel_subscribed" and channel:
            with self._subscription_lock:
                self._subscribed_channels.add(channel)
                subscribed_count = len(self._subscribed_channels)
                expected_count = len(self._expected_channels)
            logger.debug(
                "Channel subscribed (%d/%d): %s",
                subscribed_count,
                expected_count,
                channel,
            )
            if expected_count and (
                subscribed_count == 1
                or subscribed_count % 100 == 0
                or subscribed_count >= expected_count
            ):
                logger.info(
                    "Subscription progress: received %d/%d channel acknowledgements",
                    subscribed_count,
                    expected_count,
                )
            if channel not in self._expected_channels:
                logger.warning(
                    "Received channel_subscribed for unexpected channel: %s", channel
                )
            if subscribed_count >= expected_count:
                self._cancel_subscription_watchdog()
                logger.info("All requested channels subscribed (%d)", expected_count)
            return

        if event == "subscribe_failed":
            detail = data.get("detail")
            logger.error(
                "Subscription failed for channel %s: %s. Closing to trigger reconnect.",
                channel,
                detail,
            )
            self._last_close_code = 1008
            self._last_close_msg = f"subscribe_failed channel={channel} detail={detail}"
            self._cancel_subscription_watchdog()
            ws.close()

    def _enqueue_message(self, message: dict, to_callback_queue: bool) -> None:
        target_queue = self._callback_queue if to_callback_queue else self._queue
        queue_name = "callback" if to_callback_queue else "receive"
        with self._metrics_lock:
            self._messages_received += 1
            messages_received = self._messages_received
        try:
            target_queue.put_nowait(message)
        except queue.Full:
            with self._metrics_lock:
                self._messages_dropped += 1
            logger.warning("%s queue full; dropping message", queue_name.capitalize())
            return
        if (
            self._throughput_log_interval
            and messages_received % self._throughput_log_interval == 0
        ):
            with self._metrics_lock:
                messages_dropped = self._messages_dropped
            logger.info(
                "WebSocket received %d messages. %s queue size=%d dropped=%d",
                messages_received,
                queue_name.capitalize(),
                target_queue.qsize(),
                messages_dropped,
            )

    # ------------------------------------------------------------------
    # Internal WebSocketApp handlers

    def _handle_open(self, ws: websocket.WebSocketApp) -> None:
        logger.info(
            "WebSocket opened. Requesting %d channel subscription(s)",
            len(self._channels),
        )
        self._last_http_status = None
        with self._subscription_lock:
            self._subscribed_channels.clear()
        try:
            for channel in self._channels:
                ws.send(json.dumps({"subscribe": channel}))
        except Exception as exc:
            logger.error("Subscription send failed: %s", exc)
            ws.close()
            return
        if self._expected_channels:
            self._arm_subscription_watchdog(ws)
        self._reconnect_attempts = 0
        self._last_close_code = None
        self._last_close_msg = None
        self._connected.set()
        if self._on_open_cb:
            try:
                self._on_open_cb()
            except Exception:
                logger.exception("on_open callback raised")

    def _handle_message(self, ws: websocket.WebSocketApp, message: str | bytes) -> None:
        if isinstance(message, bytes):
            message = message.replace(b"\x00", b"").decode("utf-8", errors="replace")
        try:
            data = json.loads(message)
        except (json.JSONDecodeError, TypeError):
            data = {"raw": message}
        if not isinstance(data, dict):
            data = {"data": data}

        if isinstance(data, dict):
            self._process_subscription_event(ws, data)

        if self._on_message_cb:
            self._start_callback_worker()
            self._enqueue_message(data, to_callback_queue=True)
            return

        self._enqueue_message(data, to_callback_queue=False)

    def _handle_error(self, _ws: websocket.WebSocketApp, error: Exception) -> None:
        status_code = self._extract_status_code(error)
        self._last_http_status = status_code
        if status_code == 429:
            logger.warning(
                "WebSocket received HTTP 429 (rate limit). "
                "Reconnect backoff will be raised to at least %.1fs",
                self._rate_limit_backoff,
            )
        else:
            logger.error("WebSocket error: %s", error)
        if self._on_error_cb:
            try:
                self._on_error_cb(error)
            except Exception:
                logger.exception("on_error callback raised")

    def _handle_ping(
        self, _ws: websocket.WebSocketApp, message: str | bytes | None
    ) -> None:
        logger.debug("WebSocket ping received")
        if self._on_ping_cb:
            try:
                self._on_ping_cb(message)
            except Exception:
                logger.exception("on_ping callback raised")

    def _handle_pong(
        self, _ws: websocket.WebSocketApp, message: str | bytes | None
    ) -> None:
        logger.debug("WebSocket pong received")
        if self._on_pong_cb:
            try:
                self._on_pong_cb(message)
            except Exception:
                logger.exception("on_pong callback raised")

    def _handle_close(
        self,
        _ws: websocket.WebSocketApp,
        close_status_code: int | None,
        close_msg: str | None,
    ) -> None:
        self._connected.clear()
        self._cancel_subscription_watchdog()
        if close_status_code is not None:
            self._last_close_code = close_status_code
        if close_msg not in (None, ""):
            self._last_close_msg = close_msg
        logger.info(
            "WebSocket closed. code=%s message=%s",
            self._last_close_code,
            self._last_close_msg,
        )

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
            on_ping=self._handle_ping,
            on_pong=self._handle_pong,
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
        with self._lock:
            if self._connected.is_set() or not self._finished.is_set():
                raise RuntimeError("Already connected; call disconnect() first")
            self._finished.clear()
            self._user_disconnect.clear()
            self._callback_stop.clear()
            self._reconnect_attempts = 0
            self._messages_received = 0
            self._messages_dropped = 0
            self._messages_processed = 0
            # Drain stale sentinel from previous connection
            self._drain_queue(self._queue)
            self._drain_queue(self._callback_queue)

            self._ws = self._create_ws_app()
            if self._on_message_cb:
                self._start_callback_worker()
            if run_in_background:
                self._thread = threading.Thread(
                    target=self._run_forever_safe, daemon=True
                )
                self._thread.start()
            else:
                self._thread = None
        if not run_in_background:
            self._run_forever_safe()

    def _run_forever_safe(self) -> None:
        try:
            while True:
                with self._lock:
                    ws = self._ws
                if ws is None:
                    break
                try:
                    sslopt = self._build_sslopt()
                    ws.run_forever(
                        ping_interval=self._ping_interval,
                        ping_timeout=self._ping_timeout,
                        sslopt=sslopt,
                    )
                except Exception as exc:
                    self._handle_error(ws, exc)
                    self._handle_close(ws, -1, str(exc))

                if self._user_disconnect.is_set() or not self._auto_reconnect:
                    break

                self._reconnect_attempts += 1
                if (
                    self._max_reconnect_attempts > 0
                    and self._reconnect_attempts > self._max_reconnect_attempts
                ):
                    logger.warning(
                        "Max reconnect attempts (%d) reached, giving up",
                        self._max_reconnect_attempts,
                    )
                    break

                delay = self._reconnect_backoff * (2 ** (self._reconnect_attempts - 1))
                if self._max_reconnect_backoff is not None:
                    delay = min(delay, self._max_reconnect_backoff)
                if self._last_http_status == 429:
                    delay = max(delay, self._rate_limit_backoff)
                if self._max_reconnect_attempts > 0:
                    logger.info(
                        "Reconnecting in %.1fs (attempt %d/%d)",
                        delay,
                        self._reconnect_attempts,
                        self._max_reconnect_attempts,
                    )
                else:
                    logger.info(
                        "Reconnecting in %.1fs (attempt %d, unlimited)",
                        delay,
                        self._reconnect_attempts,
                    )
                if self._user_disconnect.wait(timeout=delay):
                    break  # disconnect() called during backoff

                # Guard against a disconnect that happens immediately after the
                # backoff wait returns but before creating a new WebSocketApp.
                if self._user_disconnect.is_set():
                    break

                with self._lock:
                    old_ws = self._ws
                    self._ws = self._create_ws_app()
                if old_ws:
                    try:
                        old_ws.close()
                    except Exception:
                        pass

        finally:
            self._cancel_subscription_watchdog()
            self._callback_stop.set()
            try:
                self._queue.put_nowait(None)  # sentinel — unblocks receive()
            except queue.Full:
                pass  # _finished.set() below will unblock receive() independently
            try:
                self._callback_queue.put_nowait(None)  # sentinel — unblocks worker
            except queue.Full:
                pass
            self._finished.set()  # mark as not running — unblocks connect()
            if self._on_close_cb:
                try:
                    self._on_close_cb(self._last_close_code, self._last_close_msg)
                except Exception:
                    logger.exception("on_close callback raised")

    def disconnect(self, wait: bool = False, timeout: float | None = None) -> None:
        """Close the WebSocket connection.

        PARAMS
        -----------
        wait : bool, default False
            If True, block until the background thread has finished.
        timeout : float or None, default None
            Maximum seconds to wait for the thread to finish (only used
            when *wait* is True). ``None`` means wait indefinitely.
        """
        self._user_disconnect.set()
        self._callback_stop.set()
        self._cancel_subscription_watchdog()
        with self._lock:
            ws = self._ws
        if ws:
            ws.close()
        try:
            self._callback_queue.put_nowait(None)
        except queue.Full:
            pass
        if wait and self._thread is not None:
            if self._thread is not threading.current_thread():
                self._thread.join(timeout=timeout)
        if wait and self._callback_thread is not None:
            if self._callback_thread is not threading.current_thread():
                self._callback_thread.join(timeout=timeout)

    def receive(self) -> Generator[dict, None, None]:
        """
        Blocking generator that yields each incoming message as a dict.

        Exits cleanly when the connection closes (disconnect() is called or
        the server closes the connection).

        Intended for use after connect(run_in_background=True).
        Cannot be used when an on_message callback is registered.
        """
        if self._on_message_cb is not None:
            raise RuntimeError(
                "receive() cannot be used when an on_message callback is "
                "registered; use one or the other"
            )
        if self._auto_reconnect:
            while (
                not self._connected.is_set()
                and not self._user_disconnect.is_set()
                and not self._finished.is_set()
            ):
                self._connected.wait(timeout=1)
            if not self._connected.is_set():
                return
        elif not self._connected.wait(timeout=10):
            if not self._finished.is_set():
                return
            # Thread already finished — fall through to drain queued messages
        while True:
            try:
                item = self._queue.get(timeout=1)
            except queue.Empty:
                if self._finished.is_set() and self._queue.empty():
                    break
                if not self._connected.is_set() and self._queue.empty():
                    if (
                        self._auto_reconnect
                        and not self._user_disconnect.is_set()
                        and not self._finished.is_set()
                    ):
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

    def ready(self) -> bool:
        """Returns True if the WebSocket connection is open and ready."""
        return bool(self._ws is not None and self._ws.ready())
