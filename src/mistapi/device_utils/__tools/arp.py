"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
"""

from collections.abc import Callable
from enum import Enum

from mistapi import APISession as _APISession
from mistapi.__logger import logger as LOGGER
from mistapi.api.v1.sites import devices
from mistapi.device_utils.__tools.__ws_wrapper import UtilResponse, WebSocketWrapper
from mistapi.websockets.sites import DeviceCmdEvents


class Node(Enum):
    """Node Enum for specifying node information in ARP commands."""

    NODE0 = "node0"
    NODE1 = "node1"


async def retrieve_ap_arp_table(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    node: Node | None = None,
    timeout=1,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICES: AP

    Retrieves the ARP table from a Mist Access Point and streams the results.

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to retrieve the ARP table from.
    node : Node, optional
        Node information for the ARP table retrieval command.
    timeout : int, optional
        Timeout for the ARP table retrieval command in seconds.
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    # AP is returning RAW data
    # SWITCH is returning ???
    # GATEWAY is returning JSON
    body: dict[str, str | list | int] = {}
    if node:
        body["node"] = node.value
    trigger = devices.arpFromDevice(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"Show ARP command triggered for device {device_id}")
        ws = DeviceCmdEvents(apissession, site_id=site_id, device_ids=[device_id])
        util_response = WebSocketWrapper(
            apissession, util_response, timeout=timeout, on_message=on_message
        ).start(ws)
    else:
        LOGGER.error(
            f"Failed to trigger show ARP command: {trigger.status_code} - {trigger.data}"
        )  # Give the show ARP command a moment to take effect
    return util_response


async def retrieve_ssr_arp_table(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    node: Node | None = None,
    timeout=1,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICES: SSR

    Retrieves the ARP table from a SSR Gateway and streams the results.

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to retrieve the ARP table from.
    node : Node, optional
        Node information for the ARP table retrieval command.
    timeout : int, optional
        Timeout for the ARP table retrieval command in seconds.
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received from
        the WebSocket stream.
    """
    # AP is returning RAW data
    # SWITCH is returning ???
    # GATEWAY is returning JSON
    body: dict[str, str | list | int] = {}
    if node:
        body["node"] = node.value
    trigger = devices.arpFromDevice(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"Show ARP command triggered for device {device_id}")
        ws = DeviceCmdEvents(apissession, site_id=site_id, device_ids=[device_id])
        util_response = WebSocketWrapper(
            apissession, util_response, timeout=timeout, on_message=on_message
        ).start(ws)
    else:
        LOGGER.error(
            f"Failed to trigger show ARP command: {trigger.status_code} - {trigger.data}"
        )  # Give the show ARP command a moment to take effect
    return util_response


async def retrieve_junos_arp_table(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    ip: str | None = None,
    port_id: str | None = None,
    vrf: str | None = None,
    timeout=1,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICES: EX, SRX

    Retrieve the ARP table from a Junos device (EX / SRX) with optional filters for IP, port,
    and VRF.

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to retrieve the ARP table from.
    ip : str, optional
        IP address to filter the ARP table.
    port_id : str, optional
        Port ID to filter the ARP table.
    vrf : str, optional
        VRF to filter the ARP table.
    timeout : int, optional
        Timeout for the ARP table retrieval command in seconds.
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    body: dict[str, str | list | int] = {"duration": 1, "interval": 1}
    if ip:
        body["ip"] = ip
    if vrf:
        body["vrf"] = vrf
    if port_id:
        body["port_id"] = port_id
    trigger = devices.showSiteDeviceArpTable(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"Show ARP command triggered for device {device_id}")
        ws = DeviceCmdEvents(apissession, site_id=site_id, device_ids=[device_id])
        util_response = WebSocketWrapper(
            apissession, util_response, timeout=timeout, on_message=on_message
        ).start(ws)
    else:
        LOGGER.error(
            f"Failed to trigger show ARP command: {trigger.status_code} - {trigger.data}"
        )  # Give the show ARP command a moment to take effect
    return util_response
