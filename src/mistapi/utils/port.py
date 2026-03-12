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


async def bounce(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    port_ids: list[str],
    timeout=60,
) -> UtilResponse:
    """
    DEVICE: EX, SRX, SSR

    Initiates a bounce command on the specified ports of a device (EX / SRX / SSR) and streams
    the results.

    PARAMS
    -----------
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to perform the bounce command on.
    port_ids : list[str]
        List of port IDs to bounce.
    timeout : int, async default 5
        Timeout for the bounce command in seconds.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    body: dict[str, str | list | int] = {}
    if port_ids:
        body["ports"] = port_ids
    trigger = devices.bounceDevicePort(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(
            f"Bounce command triggered for ports {port_ids} on device {device_id}"
        )
        util_response = await WebSocketWrapper(
            apissession, util_response, timeout
        ).startCmdEvents(site_id=site_id, device_id=device_id)
    else:
        LOGGER.error(
            f"Failed to trigger bounce command: {trigger.status_code} - {trigger.data}"
        )  # Give the bounce command a moment to take effect
    return util_response


async def cable_test(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    port_id: str,
    timeout=10,
) -> UtilResponse:
    """
    DEVICES: EX

    Initiates a cable test on a switch port and streams the results.

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the switch is located.
    device_id : str
        UUID of the switch to perform the cable test on.
    port_id : str
        Port ID to perform the cable test on.
    timeout : int, optional
        Timeout for the cable test command in seconds.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    body: dict[str, str | list | int] = {"port": port_id}
    trigger = devices.cableTestFromSwitch(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"Cable test command triggered for device {device_id}")
        util_response = await WebSocketWrapper(
            apissession, util_response, timeout=timeout
        ).startCmdEvents(site_id, device_id)
    else:
        LOGGER.error(
            f"Failed to trigger cable test command: {trigger.status_code} - {trigger.data}"
        )  # Give the cable test command a moment to take effect
    return util_response
