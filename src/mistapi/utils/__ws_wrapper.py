import json
import threading
import time
from enum import Enum

from mistapi import APISession
from mistapi.__api_response import APIResponse as _APIResponse
from mistapi.__logger import logger as LOGGER
from mistapi.websockets.session import SessionWithUrl
from mistapi.websockets.sites import DeviceCmdEvents, PcapEvents


class TimerAction(Enum):
    START = "start"
    STOP = "stop"
    RESET = "reset"


class Timer(Enum):
    TIMEOUT = "timeout"
    FIRST_MESSAGE_TIMEOUT = "first_message_timeout"
    MAX_DURATION = "max_duration"


class UtilResponse:
    """
    A simple class to encapsulate the response from utility WebSocket functions.
    This class can be extended in the future to include additional metadata or helper methods.
    """

    def __init__(
        self,
        api_response: _APIResponse,
    ) -> None:
        self.trigger_api_response = api_response
        self.ws_required: bool = False  # This can be set to True if the WebSocket connection was successfully initiated
        self.ws_data: list[str] = []
        self.ws_raw_events: list[str] = []


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
        # self._reset_timer()  # Start the timer when the connection opens

    ####################################################################################################################
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

    ####################################################################################################################
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
            self._timeout_handler(Timer.TIMEOUT, TimerAction.RESET)

    ####################################################################################################################
    ## Message processing and WebSocket connection management
    def _extract_session_id(self, message) -> bool:
        """
        Extracts the session_id from the message and compares it to the expected session_id.
        This method is designed to handle messages that may have the session_id nested at different levels.
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
        This method is designed to handle messages that may have the raw message nested at different levels.
        Handles both command events (with "raw" field) and pcap events (with "pcap_dict" field).
        """
        self.raw_events.append(message)
        event = message
        if isinstance(event, str):
            try:
                event = json.loads(message)
                if isinstance(event, dict):
                    # Check for raw field (command events)
                    if "raw" in event:
                        LOGGER.debug("Extracted raw message: %s", event["raw"])
                        return event["raw"]
                    # Check for pcap_dict field (pcap events)
                    if "pcap_dict" in event:
                        LOGGER.debug("Extracted pcap_dict: %s", event["pcap_dict"])
                        return event["pcap_dict"]
            except json.JSONDecodeError:
                LOGGER.warning("Failed to decode message as JSON: %s", message)
                return None
        if event.get("event") == "data" and event.get("data"):
            return self._extract_raw(event["data"])
        if event.get("raw"):
            self.received_messages += 1
            LOGGER.debug("Received raw message: %s", event.get("raw"))
            return event["raw"]
        if event.get("pcap_dict"):
            self.received_messages += 1
            LOGGER.debug("Received pcap data: %s", event["pcap_dict"])
            return event["pcap_dict"]
        return None

    ####################################################################################################################
    ## WebSocket connection management
    async def startCmdEvents(self, site_id: str, device_id: str) -> UtilResponse:
        """
        Start a WebSocket stream for site device command events.

        PARAMS
        -----------
        site_id : str
            UUID of the site to stream events from.
        device_id : str
            UUID of the device to stream events from.
        """
        self.ws = DeviceCmdEvents(
            self.apissession, site_id=site_id, device_ids=[device_id]
        )
        self.ws.on_message(self._handle_message)
        self.ws.on_error(lambda error: LOGGER.error(f"Error: {error}"))
        self.ws.on_close(
            lambda code, msg: LOGGER.info(f"WebSocket closed: {code} - {msg}")
        )
        self.ws.on_open(self._on_open)
        self.ws.connect()  # non-blocking
        LOGGER.info(
            "WebSocket connection initiated: site_id=%s, device_id=%s",
            site_id,
            device_id,
        )
        time.sleep(1)
        while self.ws and self.ws.ready():
            time.sleep(1)
        LOGGER.info("WebSocket connection closed, exiting")
        self.util_response.ws_required = True
        self.util_response.ws_data = self.data
        self.util_response.ws_raw_events = self.raw_events
        return self.util_response

    async def startSessionUrl(self, url: str) -> UtilResponse:
        """
        Start a WebSocket stream using a custom URL.
        This should be used when Mist is returning a WebSocket URL from an API call.

        PARAMS
        -----------
        url : str
            Full WebSocket URL to connect to (e.g., wss://api-ws.mist.com/ssh?jwt=eyJhbGciOiJI...).
        """
        self.ws = SessionWithUrl(self.apissession, url=url)
        self.ws.on_message(self._handle_message)
        self.ws.on_error(lambda error: LOGGER.error(f"Error: {error}"))
        self.ws.on_close(
            lambda code, msg: LOGGER.info(f"WebSocket closed: {code} - {msg}")
        )
        self.ws.on_open(self._on_open)
        self.ws.connect()  # non-blocking
        LOGGER.info("WebSocket connection initiated: url=%s", url)
        time.sleep(1)
        while self.ws and self.ws.ready():
            time.sleep(1)
        LOGGER.info("WebSocket connection closed, exiting")
        self.util_response.ws_required = True
        self.util_response.ws_data = self.data
        self.util_response.ws_raw_events = self.raw_events
        return self.util_response

    async def startRemotePcap(self, site_id: str) -> UtilResponse:
        """
        Start a WebSocket stream for remote PCAP events.
        This should be used when Mist is returning a WebSocket URL from an API call.

        PARAMS
        -----------
        site_id : str
            UUID of the site to stream PCAP events from.
        """
        self.ws = PcapEvents(self.apissession, site_id=site_id)
        self.ws.on_message(self._handle_message)
        self.ws.on_error(lambda error: LOGGER.error(f"Error: {error}"))
        self.ws.on_close(
            lambda code, msg: LOGGER.info(f"WebSocket closed: {code} - {msg}")
        )
        self.ws.on_open(self._on_open)
        self.ws.connect()  # non-blocking
        LOGGER.info("WebSocket connection initiated: /sites/%s/pcaps", site_id)
        time.sleep(1)
        while self.ws and self.ws.ready():
            time.sleep(1)
        LOGGER.info("WebSocket connection closed, exiting")
        self.util_response.ws_required = True
        self.util_response.ws_data = self.data
        self.util_response.ws_raw_events = self.raw_events
        return self.util_response
