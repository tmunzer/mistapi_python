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


def clear_sessions(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    port_ids: list[str],
) -> UtilResponse:
    """
    DEVICES: EX

    Clears dot1x sessions on the specified ports of a switch (EX).

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the switch is located.
    device_id : str
        UUID of the switch to clear dot1x sessions on.
    port_ids : list[str]
        List of port IDs to clear dot1x sessions on.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    LOGGER.debug(
        "Initiating clear dot1x sessions command for device %s on ports %s",
        device_id,
        port_ids,
    )
    body: dict[str, str | list | int] = {"ports": port_ids}
    util_response = UtilResponse()
    return WebSocketWrapper(apissession, util_response).start_with_trigger(
        trigger_fn=lambda: devices.clearSiteDeviceDot1xSession(
            apissession, site_id=site_id, device_id=device_id, body=body
        ),
    )
