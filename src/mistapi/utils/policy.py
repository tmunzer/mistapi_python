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
from mistapi.utils.__ws_wrapper import UtilResponse


async def clear_hit_count(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    policy_name: str,
) -> UtilResponse:
    """
    DEVICE: EX

    Clears the policy hit count on a device.

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to clear the policy hit count on.
    policy_name : str
        Name of the policy to clear the hit count for.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received from the WebSocket stream.
    """
    trigger = devices.clearSiteDevicePolicyHitCount(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body={"policy_name": policy_name},
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(f"Clear policy hit count command triggered for device {device_id}")
        # util_response = await WebSocketWrapper(
        #     apissession, util_response, timeout=timeout
        # ).startCmdEvents(site_id, device_id)
    else:
        LOGGER.error(
            f"Failed to trigger clear policy hit count command: {trigger.status_code} - {trigger.data}"
        )  # Give the clear policy hit count command a moment to take effect
    return util_response
