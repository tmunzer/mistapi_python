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
from mistapi.device_utils.__tools.__ws_wrapper import UtilResponse, WebSocketWrapper


def clear_hit_count(
    apisession: _APISession,
    site_id: str,
    device_id: str,
    policy_name: str,
) -> UtilResponse:
    """
    DEVICE: EX

    Clears the policy hit count on a device.

    PARAMS
    -----------
    apisession : _APISession
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
    LOGGER.debug(
        "Initiating clear policy hit count command for device %s and policy %s",
        device_id,
        policy_name,
    )
    util_response = UtilResponse()
    return WebSocketWrapper(apisession, util_response).start_with_trigger(
        trigger_fn=lambda: devices.clearSiteDevicePolicyHitCount(
            apisession,
            site_id=site_id,
            device_id=device_id,
            body={"policy_name": policy_name},
        ),
    )
