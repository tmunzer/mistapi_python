import json
import threading
import time

from mistapi import APISession
from mistapi.__api_response import APIResponse as _APIResponse
from mistapi.__logger import logger as LOGGER
from mistapi.websockets.session import SessionWithUrl
from mistapi.websockets.sites import DeviceCmdEvents


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
        self.timeout_timer = None
        self.timeout = timeout
        self.max_duration_timer = None
        self.max_duration = max_duration
        self.received_messages = 0
        self.data = []
        self.raw_events = []
        self.ws = None

    def _on_open(self):
        LOGGER.info("WebSocket connection opened")
        if self.max_duration_timer and self.ws:
            self.max_duration_timer = threading.Timer(
                self.max_duration, self.ws.disconnect
            )
            self.max_duration_timer.start()
        self._reset_timer()  # Start the timer when the connection opens

    def _reset_timer(self):
        if self.timeout_timer:
            self.timeout_timer.cancel()
        if self.ws:
            self.timeout_timer = threading.Timer(self.timeout, self.ws.disconnect)
            self.timeout_timer.start()

    def _extract_raw(self, message):
        self.raw_events.append(message)
        event = message
        if isinstance(event, str):
            try:
                event = json.loads(message)
                if isinstance(event, dict) and "raw" in event:
                    return event["raw"]
            except json.JSONDecodeError:
                return
        if event.get("event") == "data" and event.get("data"):
            return self._extract_raw(event["data"])
        elif event.get("raw"):
            self.received_messages += 1
            LOGGER.debug(f"Received raw message: {event['raw']}")
            return event["raw"]
        return None

    def _handle_message(self, msg):
        if isinstance(msg, dict) and msg.get("event") == "channel_subscribed":
            LOGGER.debug(msg)
        else:
            LOGGER.debug(msg)
            raw = self._extract_raw(msg)
            if raw:
                self.data.append(raw)
        self._reset_timer()  # Reset timeout on each message

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
        LOGGER.info("WebSocket connection initiated")
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
            Full WebSocket URL to connect to (e.g., wss://api.mist.com/ws/v1/orgs/{org_id}/sites/{site_id}/devices/{device_id}/cmds).

        """
        self.ws = SessionWithUrl(self.apissession, url=url)
        self.ws.on_message(self._handle_message)
        self.ws.on_error(lambda error: LOGGER.error(f"Error: {error}"))
        self.ws.on_close(
            lambda code, msg: LOGGER.info(f"WebSocket closed: {code} - {msg}")
        )
        self.ws.on_open(self._on_open)
        self.ws.connect()  # non-blocking
        LOGGER.info("WebSocket connection initiated")
        time.sleep(1)
        while self.ws and self.ws.ready():
            time.sleep(1)
        LOGGER.info("WebSocket connection closed, exiting")
        self.util_response.ws_required = True
        self.util_response.ws_data = self.data
        self.util_response.ws_raw_events = self.raw_events
        return self.util_response
