"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
"""

from mistapi import APISession as _APISession
from mistapi.__logger import logger as LOGGER
from mistapi.api.v1.sites import devices
from mistapi.utils.__ws_wrapper import UtilResponse, WebSocketWrapper


async def show_summary(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    timeout=5,
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
        util_response = await WebSocketWrapper(
            apissession, util_response, timeout=timeout
        ).startCmdEvents(site_id, device_id)
    else:
        LOGGER.error(
            f"Failed to trigger BGP summary command: {trigger.status_code} - {trigger.data}"
        )  # Give the BGP summary command a moment to take effect
    return util_response
