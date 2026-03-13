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
from mistapi.device_utils.__tools.__ws_wrapper import UtilResponse


async def clearError(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    port_ids: list[str],
) -> UtilResponse:
    """
    DEVICES: EX

    Clears BPDU error state on the specified ports of a switch.

    PARAMS
    -----------
    site_id : str
        UUID of the site where the switch is located.
    device_id : str
        UUID of the switch to clear BPDU errors on.
    port_ids : list[str]
        List of port IDs to clear BPDU errors on.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """

    body: dict[str, str | list | int] = {"ports": port_ids}
    trigger = devices.clearBpduErrorsFromPortsOnSwitch(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"Clear BPDU error command triggered for device {device_id}")
    else:
        LOGGER.error(
            f"Failed to trigger clear BPDU error command: {trigger.status_code} - {trigger.data}"
        )  # Give the clear BPDU error command a moment to take effect
    return util_response
