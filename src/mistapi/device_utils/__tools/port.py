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


def bounce(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    port_ids: list[str],
    timeout=5,
    on_message: Callable[[dict], None] | None = None,
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
    timeout : int, default 5
        Timeout for the bounce command in seconds.
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    LOGGER.debug(
        "Initiating bounce command for device %s on ports %s with timeout %s",
        device_id,
        port_ids,
        timeout,
    )
    body: dict[str, str | list | int] = {}
    if port_ids:
        body["ports"] = port_ids
    util_response = UtilResponse()
    return WebSocketWrapper(
        apissession, util_response, timeout, on_message=on_message
    ).start_with_trigger(
        trigger_fn=lambda: devices.bounceDevicePort(
            apissession, site_id=site_id, device_id=device_id, body=body
        ),
        ws_factory_fn=lambda _trigger: DeviceCmdEvents(
            apissession, site_id=site_id, device_ids=[device_id]
        ),
    )


def cable_test(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    port_id: str,
    timeout=10,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICES: EX

    Initiates a cable test on a switch port and streams the results.

    PARAMS
    -----------
    apisession: mistapi.APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the switch is located.
    device_id : str
        UUID of the switch to perform the cable test on.
    port_id : str
        Port ID to perform the cable test on.
    timeout : int, default 10
        Timeout for the cable test command in seconds.
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    LOGGER.debug(
        "Initiating cable test for device %s on port %s with timeout %s",
        device_id,
        port_id,
        timeout,
    )
    body: dict[str, str | list | int] = {"port": port_id}
    util_response = UtilResponse()
    return WebSocketWrapper(
        apissession, util_response, timeout=timeout, on_message=on_message
    ).start_with_trigger(
        trigger_fn=lambda: devices.cableTestFromSwitch(
            apissession, site_id=site_id, device_id=device_id, body=body
        ),
        ws_factory_fn=lambda _trigger: DeviceCmdEvents(
            apissession, site_id=site_id, device_ids=[device_id]
        ),
    )
