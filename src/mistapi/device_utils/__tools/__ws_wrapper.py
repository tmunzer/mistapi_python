import json
import queue
import re
import threading
from collections.abc import Callable, Generator
from enum import Enum

from mistapi import APISession
from mistapi.__api_response import APIResponse as _APIResponse
from mistapi.__logger import logger as LOGGER

# Matches ANSI CSI sequences, OSC sequences, and character set designations
_ANSI_ESCAPE_RE = re.compile(
    r"\x1b\[[0-9;]*[a-zA-Z]|\x1b\][^\x07]*\x07|\x1b[()][A-B0-2]"
)

# Detects VT100 cursor positioning / clear-screen (triggers screen-buffer mode)
_SCREEN_MODE_RE = re.compile(r"\x1b\[[\d;]*H|\x1b\[2J")


class _VT100Screen:
    """Minimal VT100 terminal emulator for rendering screen-based output.

    Handles the subset of VT100 sequences used by Junos ``top`` and
    ``monitor interface`` commands: cursor positioning, screen/line
    clearing, and cursor movement.  SGR (colors), scroll regions, and
    mode changes are silently ignored.
    """

    def __init__(self, rows: int = 80, cols: int = 200) -> None:
        self.rows = rows
        self.cols = cols
        self.cursor_row = 0
        self.cursor_col = 0
        self.grid: list[list[str]] = [[" "] * cols for _ in range(rows)]

    def feed(self, text: str) -> None:
        """Process *text* (may contain VT100 sequences) into the screen buffer."""
        i = 0
        n = len(text)
        while i < n:
            ch = text[i]

            if ch == "\x1b" and i + 1 < n:
                nxt = text[i + 1]
                if nxt == "[":
                    # CSI sequence: \x1b[ <params> <cmd>
                    j = i + 2
                    params = ""
                    while j < n and text[j] in "0123456789;":
                        params += text[j]
                        j += 1
                    if j < n:
                        self._handle_csi(params, text[j])
                        i = j + 1
                    else:
                        i = j
                    continue
                if nxt in "()":
                    # Character-set designation – skip 3 bytes
                    i += 3 if i + 2 < n else n
                    continue
                if nxt == "]":
                    # OSC sequence – skip until BEL
                    j = i + 2
                    while j < n and text[j] != "\x07":
                        j += 1
                    i = j + 1
                    continue
                # Unknown escape – skip \x1b and the next char
                i += 2
                continue

            if ch == "\r":
                self.cursor_col = 0
                i += 1
                continue

            if ch == "\n":
                self.cursor_row += 1
                self.cursor_col = 0
                if self.cursor_row >= self.rows:
                    self.grid.pop(0)
                    self.grid.append([" "] * self.cols)
                    self.cursor_row = self.rows - 1
                i += 1
                continue

            if ch == "\x00":
                i += 1
                continue

            # Printable character
            if 0 <= self.cursor_row < self.rows and 0 <= self.cursor_col < self.cols:
                self.grid[self.cursor_row][self.cursor_col] = ch
            self.cursor_col += 1
            i += 1

    # ------------------------------------------------------------------
    def _handle_csi(self, params: str, cmd: str) -> None:
        nums = []
        for p in params.split(";") if params else []:
            try:
                nums.append(int(p))
            except ValueError:
                nums.append(0)

        if cmd in ("H", "f"):  # Cursor position
            row = (nums[0] - 1) if nums else 0
            col = (nums[1] - 1) if len(nums) > 1 else 0
            self.cursor_row = max(0, min(row, self.rows - 1))
            self.cursor_col = max(0, min(col, self.cols - 1))
        elif cmd == "A":  # Cursor up
            self.cursor_row = max(0, self.cursor_row - (nums[0] if nums else 1))
        elif cmd == "B":  # Cursor down
            self.cursor_row = min(
                self.rows - 1, self.cursor_row + (nums[0] if nums else 1)
            )
        elif cmd == "C":  # Cursor forward
            self.cursor_col = min(
                self.cols - 1, self.cursor_col + (nums[0] if nums else 1)
            )
        elif cmd == "D":  # Cursor back
            self.cursor_col = max(0, self.cursor_col - (nums[0] if nums else 1))
        elif cmd == "J":  # Erase in display
            n = nums[0] if nums else 0
            if n == 2:
                self.grid = [[" "] * self.cols for _ in range(self.rows)]
                self.cursor_row = 0
                self.cursor_col = 0
            elif n == 0:
                for c in range(self.cursor_col, self.cols):
                    self.grid[self.cursor_row][c] = " "
                for r in range(self.cursor_row + 1, self.rows):
                    self.grid[r] = [" "] * self.cols
        elif cmd == "K":  # Erase in line
            n = nums[0] if nums else 0
            if n == 0:
                for c in range(self.cursor_col, self.cols):
                    self.grid[self.cursor_row][c] = " "
            elif n == 1:
                for c in range(self.cursor_col + 1):
                    self.grid[self.cursor_row][c] = " "
            elif n == 2:
                self.grid[self.cursor_row] = [" "] * self.cols
        # SGR (m), scroll region (r), mode set/reset (l, h) – ignore

    # ------------------------------------------------------------------
    def render(self) -> str:
        """Return screen content as text with trailing whitespace trimmed."""
        lines = ["".join(row).rstrip() for row in self.grid]
        while lines and not lines[-1]:
            lines.pop()
        return "\n".join(lines)


class TimerAction(Enum):
    """
    TimerAction Enum for managing timer actions in WebSocketWrapper.
    """

    START = "start"
    STOP = "stop"
    RESET = "reset"


class Timer(Enum):
    """
    Timer Enum for specifying different timer types in WebSocketWrapper.
    """

    TIMEOUT = "timeout"
    FIRST_MESSAGE_TIMEOUT = "first_message_timeout"
    MAX_DURATION = "max_duration"


class UtilResponse:
    """
    Encapsulates the response from device utility functions.

    Returned immediately by tool functions. When a WebSocket stream is
    involved, data is collected in the background. Use ``receive()``,
    ``wait()``, or the ``on_message`` callback to consume results.

    USAGE PATTERNS
    -----------
    Callback style (on_message passed at call time)::

        response = ex.ping(session, site_id, device_id, host="8.8.8.8",
                           on_message=lambda msg: print(msg))
        do_other_work()
        response.wait()
        print(response.ws_data)

    Generator style::

        response = ex.ping(session, site_id, device_id, host="8.8.8.8")
        for msg in response.receive():
            print(msg)

    Context manager::

        with ex.ping(session, site_id, device_id, host="8.8.8.8") as response:
            for msg in response.receive():
                print(msg)

    Async await::

        response = ex.ping(session, site_id, device_id, host="8.8.8.8")
        await response
        print(response.ws_data)
    """

    def __init__(
        self,
        api_response: _APIResponse | None = None,
    ) -> None:
        self.trigger_api_response = api_response
        self.ws_required: bool = False
        self.ws_data: list[str] = []
        self.ws_raw_events: list[str] = []
        self._queue: queue.Queue[str | None] = queue.Queue()
        self._closed = threading.Event()
        self._await_timeout: float | None = None
        if api_response is not None:
            # api_response provided → done immediately, no WS needed
            self._closed.set()
        # api_response is None → _closed stays unset (in-progress, waiting for WS)
        self._disconnect_fn: Callable[[], None] | None = None

    @property
    def done(self) -> bool:
        """True if data collection is complete (or no WS was needed)."""
        return self._closed.is_set()

    def wait(self, timeout: float | None = None) -> "UtilResponse":
        """Block until data collection is complete. Returns self."""
        self._closed.wait(timeout=timeout)
        return self

    def receive(self) -> Generator[str, None, None]:
        """
        Blocking generator that yields each processed message as it arrives.

        Mirrors ``_MistWebsocket.receive()``. Exits cleanly when the
        WebSocket connection closes or ``disconnect()`` is called.
        """
        while True:
            try:
                item = self._queue.get(timeout=0.1)
            except queue.Empty:
                if self._closed.is_set() and self._queue.empty():
                    break
                continue
            if item is None:
                break
            yield item

    def disconnect(self) -> None:
        """Stop the WebSocket connection early."""
        fn = self._disconnect_fn
        if fn is not None:
            fn()

    def __enter__(self) -> "UtilResponse":
        return self

    def __exit__(self, *args) -> None:
        self.disconnect()

    def __await__(self):
        """Allow ``result = await response`` in async contexts."""
        import asyncio

        async def _await_impl():
            timed_out = not await asyncio.to_thread(
                self._closed.wait, self._await_timeout
            )
            if timed_out:
                LOGGER.warning("await timed out after %s seconds", self._await_timeout)
            return self

        return _await_impl().__await__()


class WebSocketWrapper:
    """
    A wrapper class for managing WebSocket connections and events.
    This class provides a simplified interface for connecting to WebSocket channels,
    handling messages, and managing connection timeouts.
    """

    def __init__(
        self,
        apisession: APISession,
        util_response: UtilResponse,
        timeout: int = 10,
        max_duration: int = 60,
        on_message: Callable[[dict], None] | None = None,
    ) -> None:
        self.apisession = apisession
        self.util_response = util_response
        self.timers = {
            Timer.TIMEOUT.value: {
                "thread": None,
                "duration": timeout,
            },
            Timer.FIRST_MESSAGE_TIMEOUT.value: {
                "thread": None,
                "duration": 30,
            },
            Timer.MAX_DURATION.value: {
                "thread": None,
                "duration": max_duration,
            },
        }
        self.received_messages = 0
        self.data = []
        self.raw_events = []
        self.ws = None
        self.session_id: str | None = None
        self.capture_id: str | None = None
        self._on_message_cb = on_message
        self._screen: _VT100Screen | None = None
        self._screen_mode: bool = False
        self._extract_trigger_ids()

    def _extract_trigger_ids(self):
        """Extract session_id and capture_id from the trigger API response."""
        if not self.util_response.trigger_api_response:
            return
        LOGGER.debug(
            "trigger response: %s", self.util_response.trigger_api_response.data
        )
        if self.util_response.trigger_api_response.data and isinstance(
            self.util_response.trigger_api_response.data, dict
        ):
            self.session_id = self.util_response.trigger_api_response.data.get(
                "session", None
            )
            self.capture_id = self.util_response.trigger_api_response.data.get(
                "id", None
            )
            LOGGER.debug("Extracted session_id: %s", self.session_id)
            LOGGER.debug("Extracted capture_id: %s", self.capture_id)

    def _on_open(self):
        LOGGER.info("WebSocket connection opened")
        # Start the max duration timer
        self._timeout_handler(Timer.MAX_DURATION, TimerAction.START)

    def _on_close(self, code, msg):
        LOGGER.info("WebSocket closed: %s - %s", code, msg)
        self._stop_all_timers()
        self.util_response._queue.put(None)  # sentinel for receive()
        self.util_response._closed.set()  # signal completion

    ##########################################################################
    ## Helper methods for managing timers
    def _timeout_handler(self, timer_type: Timer, action: TimerAction):
        duration = self.timers[timer_type.value]["duration"]
        if action == TimerAction.STOP or action == TimerAction.RESET:
            if self.timers[timer_type.value]["thread"]:
                LOGGER.debug("Stopping %s timer", timer_type.value)
                self.timers[timer_type.value]["thread"].cancel()
                self.timers[timer_type.value]["thread"] = None
            elif action == TimerAction.STOP:
                # Only warn when explicitly stopping (not resetting) a non-active timer
                LOGGER.warning("%s timer is not active to stop", timer_type.value)
        if action == TimerAction.START or action == TimerAction.RESET:
            if self.ws:
                LOGGER.debug(
                    "Starting %s timer with duration: %s seconds",
                    timer_type.value,
                    duration,
                )
                self.timers[timer_type.value]["thread"] = threading.Timer(
                    duration, self.ws.disconnect
                )
                self.timers[timer_type.value]["thread"].start()
            else:
                LOGGER.warning(
                    "WebSocket is not available to start %s timer", timer_type.value
                )

    def _stop_all_timers(self):
        for timer_info in self.timers.values():
            if timer_info["thread"]:
                timer_info["thread"].cancel()
                timer_info["thread"] = None

    ##########################################################################
    ## WebSocket event handlers

    def _handle_message(self, msg):
        if isinstance(msg, dict) and msg.get("event") == "channel_subscribed":
            LOGGER.debug("channel_subscribed: %s", msg)
            # Start the first message timeout timer when the channel is successfully subscribed
            self._timeout_handler(Timer.FIRST_MESSAGE_TIMEOUT, TimerAction.START)
        elif self._extract_session_id(msg):
            # Stop the first message timeout timer on receiving the first message
            if self.timers[Timer.FIRST_MESSAGE_TIMEOUT.value]["thread"]:
                self._timeout_handler(Timer.FIRST_MESSAGE_TIMEOUT, TimerAction.STOP)
            LOGGER.debug("data: %s", msg)
            raw = self._extract_raw(msg)
            if raw:
                self.data.append(raw)
                self.util_response._queue.put(raw)  # feed receive() generator
                if self._on_message_cb:
                    self._on_message_cb(raw)
            self._timeout_handler(Timer.TIMEOUT, TimerAction.RESET)

    ##########################################################################
    ## Message processing and WebSocket connection management
    def _extract_session_id(self, message) -> bool:
        """
        Extracts the session_id from the message and compares it to the expected session_id.
        This method is designed to handle messages that may have the session_id nested at
        different levels.
        If the expected session_id is None, it will accept all messages.
        """
        if not self.session_id and not self.capture_id:
            LOGGER.debug("No session_id or capture_id provided, accepting all messages")
            return True
        if isinstance(message, str):
            LOGGER.debug("Trying to decode message: %s", message)
            try:
                message = json.loads(message)
            except json.JSONDecodeError:
                LOGGER.warning("Failed to decode message as JSON: %s", message)
                return False
        if isinstance(message, dict):
            if message.get("event") == "data" and message.get("data"):
                LOGGER.debug(
                    "Checking nested data for session_id or capture_id: %s",
                    message["data"],
                )
                return self._extract_session_id(message["data"])
            if message.get("session") == self.session_id:
                LOGGER.info(
                    "Message session_id matches expected session_id: %s",
                    self.session_id,
                )
                return True
            if message.get("capture_id") == self.capture_id:
                LOGGER.info(
                    "Message capture_id matches expected capture_id: %s",
                    self.capture_id,
                )
                return True
        return False

    def _extract_raw(self, message, root: bool = True):
        """
        Extracts the raw message from the given message.
        This method is designed to handle messages that may have the raw message nested at
        different levels.
        Handles both command events (with "raw" field) and pcap events (with "pcap_dict" field).
        """
        if root:
            self.raw_events.append(message)
        event = message
        if isinstance(event, str):
            try:
                event = json.loads(event)
            except json.JSONDecodeError:
                LOGGER.warning("Failed to decode message as JSON: %s", message)
                return None
        if isinstance(event, dict):
            if event.get("event") == "data" and event.get("data"):
                return self._extract_raw(event["data"], root=False)
            if "raw" in event:
                self.received_messages += 1
                raw_value = event["raw"]
                if isinstance(raw_value, str):
                    # Detect screen-mode (cursor positioning / clear-screen)
                    if not self._screen_mode and _SCREEN_MODE_RE.search(raw_value):
                        self._screen_mode = True
                        self._screen = _VT100Screen()
                    if self._screen_mode and self._screen is not None:
                        self._screen.feed(raw_value)
                        raw_value = self._screen.render()
                    else:
                        raw_value = _ANSI_ESCAPE_RE.sub("", raw_value)
                LOGGER.debug("Extracted raw message: %s", raw_value)
                return raw_value
            if "pcap_dict" in event:
                self.received_messages += 1
                LOGGER.debug("Extracted pcap data: %s", event["pcap_dict"])
                return event["pcap_dict"]
        return None

    ##########################################################################
    ## WebSocket connection management
    def start(self, ws) -> UtilResponse:
        """
        Start the WS connection in the background and return immediately.

        The returned ``UtilResponse`` collects data as it streams in. Use
        ``response.receive()``, ``response.wait()``, or the ``on_message``
        callback to consume results.

        PARAMS
        -----------
        ws : _MistWebsocket
            An already-constructed WebSocket channel object.
        """
        self.ws = ws
        ws.on_message(self._handle_message)
        ws.on_error(lambda error: LOGGER.error("Error: %s", error))
        ws.on_close(self._on_close)
        ws.on_open(self._on_open)

        # Wire up UtilResponse before starting WS
        # _closed is already unset (in-progress) from UtilResponse.__init__
        self.util_response.ws_required = True
        self.util_response.ws_data = self.data  # live list reference
        self.util_response.ws_raw_events = self.raw_events
        self.util_response._await_timeout = (
            self.timers[Timer.MAX_DURATION.value]["duration"] + 10
        )
        self.util_response._disconnect_fn = ws.disconnect

        ws.connect(run_in_background=True)  # non-blocking
        return self.util_response

    def start_with_trigger(
        self,
        trigger_fn: Callable,
        ws_factory_fn: Callable | None = None,
    ) -> UtilResponse:
        """
        Run the trigger API call and optionally start a WebSocket stream.

        If ``ws_factory_fn`` is provided, the trigger and WebSocket setup
        run in a background thread (non-blocking). If ``ws_factory_fn`` is
        ``None``, the trigger runs synchronously so that
        ``trigger_api_response`` is immediately available on the returned
        ``UtilResponse``.

        PARAMS
        -----------
        trigger_fn : Callable
            A zero-argument callable that performs the REST API trigger and
            returns an ``APIResponse``.
        ws_factory_fn : Callable, optional
            A one-argument callable that receives the trigger ``APIResponse``
            and returns a WebSocket channel object (e.g. ``DeviceCmdEvents``).
            If ``None``, no WebSocket is started and the ``UtilResponse``
            completes as soon as the trigger finishes.
        """
        if ws_factory_fn is None:
            return self._trigger_only(trigger_fn)

        def _run():
            try:
                trigger = trigger_fn()
                self.util_response.trigger_api_response = trigger
                if trigger.status_code == 200:
                    LOGGER.info("Trigger succeeded: %s", trigger.data)
                    self._extract_trigger_ids()
                    ws = ws_factory_fn(trigger)
                    if ws:
                        self.start(ws)
                        return  # start() / _on_close manages _closed
                    LOGGER.error("WS factory returned None")
                else:
                    LOGGER.error(
                        "Failed to trigger command: %s - %s",
                        trigger.status_code,
                        trigger.data,
                    )
            except Exception as e:
                LOGGER.error("Error during trigger: %s", e)
            # Mark done (failure or WS factory returned None)
            self.util_response._queue.put(None)
            self.util_response._closed.set()

        threading.Thread(target=_run, daemon=True).start()
        return self.util_response

    def _trigger_only(self, trigger_fn: Callable) -> UtilResponse:
        """Run a trigger-only command synchronously (no WebSocket needed)."""
        try:
            trigger = trigger_fn()
            self.util_response.trigger_api_response = trigger
            if trigger.status_code == 200:
                LOGGER.info("Trigger succeeded: %s", trigger.data)
            else:
                LOGGER.error(
                    "Failed to trigger command: %s - %s",
                    trigger.status_code,
                    trigger.data,
                )
        except Exception as e:
            LOGGER.error("Error during trigger: %s", e)
        self.util_response._queue.put(None)
        self.util_response._closed.set()
        return self.util_response
