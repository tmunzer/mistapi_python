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
    """Node Enum for specifying node information in OSPF commands."""

    NODE0 = "node0"
    NODE1 = "node1"


def showDatabase(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    node: Node | None = None,
    self_originate: bool | None = None,
    vrf: str | None = None,
    timeout=5,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICES: SRX, SSR

    Shows OSPF database on a device (SRX / SSR) and streams the results.


    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to show OSPF database on.
    node : Node, optional
        Node information for the show OSPF database command.
    self_originate : bool, optional
        Filter for self-originated routes in the OSPF database.
    vrf : str, optional
        VRF to filter the OSPF database.
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    body: dict[str, str | list | int] = {}
    if node:
        body["node"] = node.value
    if self_originate is not None:
        body["self_originate"] = self_originate
    if vrf:
        body["vrf"] = vrf
    trigger = devices.showSiteGatewayOspfDatabase(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(f"OSPF database command triggered for device {device_id}")
        ws = DeviceCmdEvents(apissession, site_id=site_id, device_ids=[device_id])
        util_response = WebSocketWrapper(
            apissession, util_response, timeout=timeout, on_message=on_message
        ).start(ws)
    else:
        LOGGER.error(
            f"Failed to trigger OSPF database command: {trigger.status_code} - {trigger.data}"
        )  # Give the OSPF database command a moment to take effect
    return util_response


def showInterfaces(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    node: Node | None = None,
    port_id: str | None = None,
    vrf: str | None = None,
    timeout=5,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICES: SRX, SSR

    Shows OSPF interfaces on a device (SRX / SSR) and streams the results.


    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to show OSPF interfaces on.
    node : Node, optional
        Node information for the show OSPF interfaces command.
    port_id : str, optional
        Port ID to filter the OSPF interfaces.
    vrf : str, optional
        VRF to filter the OSPF interfaces.
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    body: dict[str, str | list | int] = {}
    if node:
        body["node"] = node.value
    if port_id:
        body["port_id"] = port_id
    if vrf:
        body["vrf"] = vrf
    trigger = devices.showSiteGatewayOspfInterfaces(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(f"OSPF interfaces command triggered for device {device_id}")
        ws = DeviceCmdEvents(apissession, site_id=site_id, device_ids=[device_id])
        util_response = WebSocketWrapper(
            apissession, util_response, timeout=timeout, on_message=on_message
        ).start(ws)
    else:
        LOGGER.error(
            f"Failed to trigger OSPF interfaces command: {trigger.status_code} - {trigger.data}"
        )  # Give the OSPF interfaces command a moment to take effect
    return util_response


def showNeighbors(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    neighbor: str | None = None,
    node: Node | None = None,
    port_id: str | None = None,
    vrf: str | None = None,
    timeout=5,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICES: SRX, SSR

    Shows OSPF neighbors on a device (SRX / SSR) and streams the results.


    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to show OSPF neighbors on.
    neighbor : str, optional
        Neighbor IP address to filter the OSPF neighbors.
    node : Node, optional
        Node information for the show OSPF neighbors command.
    port_id : str, optional
        Port ID to filter the OSPF neighbors.
    vrf : str, optional
        VRF to filter the OSPF neighbors.
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    body: dict[str, str | list | int] = {}
    if node:
        body["node"] = node.value
    if port_id:
        body["port_id"] = port_id
    if vrf:
        body["vrf"] = vrf
    if neighbor:
        body["neighbor"] = neighbor
    trigger = devices.showSiteGatewayOspfNeighbors(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(f"OSPF neighbors command triggered for device {device_id}")
        ws = DeviceCmdEvents(apissession, site_id=site_id, device_ids=[device_id])
        util_response = WebSocketWrapper(
            apissession, util_response, timeout=timeout, on_message=on_message
        ).start(ws)
    else:
        LOGGER.error(
            f"Failed to trigger OSPF neighbors command: {trigger.status_code} - {trigger.data}"
        )  # Give the OSPF neighbors command a moment to take effect
    return util_response


def showSummary(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    node: Node | None = None,
    vrf: str | None = None,
    timeout=5,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICES: SRX, SSR

    Shows OSPF summary on a device (SRX / SSR) and streams the results.


    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to show OSPF summary on.
    node : Node, optional
        Node information for the show OSPF summary command.
    vrf : str, optional
        VRF to filter the OSPF summary.
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    body: dict[str, str | list | int] = {}
    if node:
        body["node"] = node.value
    if vrf:
        body["vrf"] = vrf
    trigger = devices.showSiteGatewayOspfSummary(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(f"OSPF summary command triggered for device {device_id}")
        ws = DeviceCmdEvents(apissession, site_id=site_id, device_ids=[device_id])
        util_response = WebSocketWrapper(
            apissession, util_response, timeout=timeout, on_message=on_message
        ).start(ws)
    else:
        LOGGER.error(
            f"Failed to trigger OSPF summary command: {trigger.status_code} - {trigger.data}"
        )  # Give the OSPF summary command a moment to take effect
    return util_response
