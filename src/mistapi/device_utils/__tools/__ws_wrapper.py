import json
import queue
import threading
from collections.abc import Callable, Generator
from enum import Enum

from mistapi import APISession
from mistapi.__api_response import APIResponse as _APIResponse
from mistapi.__logger import logger as LOGGER


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
        if api_response is not None:
            self._closed.set()  # done immediately (no WS to wait for)
        # When api_response is None, _closed stays unset (in-progress)
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
                item = self._queue.get(timeout=1)
            except queue.Empty:
                if self._closed.is_set() and self._queue.empty():
                    break
                continue
            if item is None:
                break
            yield item

    def disconnect(self) -> None:
        """Stop the WebSocket connection early."""
        if self._disconnect_fn:
            self._disconnect_fn()

    def __enter__(self) -> "UtilResponse":
        return self

    def __exit__(self, *args) -> None:
        self.disconnect()

    def __await__(self):
        """Allow ``result = await response`` in async contexts."""
        import asyncio

        async def _await_impl():
            await asyncio.to_thread(self._closed.wait)
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
        apissession: APISession,
        util_response: UtilResponse,
        timeout: int = 10,
        max_duration: int = 60,
        on_message: Callable[[dict], None] | None = None,
    ) -> None:
        self.apissession = apissession
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

    def _extract_raw(self, message):
        """
        Extracts the raw message from the given message.
        This method is designed to handle messages that may have the raw message nested at
        different levels.
        Handles both command events (with "raw" field) and pcap events (with "pcap_dict" field).
        """
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
                return self._extract_raw(event["data"])
            if "raw" in event:
                self.received_messages += 1
                LOGGER.debug("Extracted raw message: %s", event["raw"])
                return event["raw"]
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
        self.util_response.ws_required = True
        self.util_response.ws_data = self.data  # live list reference
        self.util_response.ws_raw_events = self.raw_events
        self.util_response._closed.clear()  # mark as "in progress"
        self.util_response._disconnect_fn = ws.disconnect

        ws.connect(run_in_background=True)  # non-blocking
        return self.util_response

    def start_with_trigger(
        self,
        trigger_fn: Callable,
        ws_factory_fn: Callable | None = None,
    ) -> UtilResponse:
        """
        Run the trigger API call (and optional WS setup) in a background thread.

        Returns the ``UtilResponse`` immediately. The trigger HTTP request and
        the subsequent WebSocket connection both run in background threads, so
        the calling code is never blocked.

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

        def _run():
            try:
                trigger = trigger_fn()
                self.util_response.trigger_api_response = trigger
                if trigger.status_code == 200:
                    LOGGER.info("Trigger succeeded: %s", trigger.data)
                    self._extract_trigger_ids()
                    if ws_factory_fn:
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
            # Mark done (success without WS, or failure)
            self.util_response._queue.put(None)
            self.util_response._closed.set()

        threading.Thread(target=_run, daemon=True).start()
        return self.util_response
