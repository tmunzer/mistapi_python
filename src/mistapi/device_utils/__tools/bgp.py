"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
"""

from collections.abc import Callable

from mistapi import APISession as _APISession
from mistapi.__logger import logger as LOGGER
from mistapi.api.v1.sites import devices
from mistapi.device_utils.__tools.__ws_wrapper import UtilResponse, WebSocketWrapper
from mistapi.websockets.sites import DeviceCmdEvents


def summary(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    timeout=5,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICES: EX, SRX, SSR

    Shows BGP summary on a device (EX/ SRX / SSR) and streams the results.


    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to show BGP summary on.
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    body: dict[str, str | list | int] = {"protocol": "bgp"}
    trigger = devices.showSiteDeviceBgpSummary(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(f"BGP summary command triggered for device {device_id}")
        ws = DeviceCmdEvents(apissession, site_id=site_id, device_ids=[device_id])
        util_response = WebSocketWrapper(
            apissession, util_response, timeout=timeout, on_message=on_message
        ).start(ws)
    else:
        LOGGER.error(
            f"Failed to trigger BGP summary command: {trigger.status_code} - {trigger.data}"
        )  # Give the BGP summary command a moment to take effect
    return util_response
