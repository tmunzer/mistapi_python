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
    """Node Enum for specifying node information in DHCP commands."""

    NODE0 = "node0"
    NODE1 = "node1"


def releaseDhcpLeases(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    macs: list[str] | None = None,
    network: str | None = None,
    node: Node | None = None,
    port_id: str | None = None,
    timeout=5,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICES: EX, SRX, SSR

    Releases DHCP leases on a device (EX/ SRX / SSR) and streams the results.

    valid combinations for EX are:
    - network + macs
    - network + port_id
    - port_id

    valid combinations for SRX / SSR are:
    - network
    - network + macs
    - network + port_id
    - port_id
    - port_id + macs

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to release DHCP leases on.
    macs : list[str], optional
        List of MAC addresses to release DHCP leases for.
    network : str, optional
        Network to release DHCP leases for.
    node : Node, optional
        Node information for the DHCP lease release command.
    port_id : str, optional
        Port ID to release DHCP leases for.
    timeout : int, optional
        Timeout for the release DHCP leases command in seconds.
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    body: dict[str, str | list | int] = {}
    if macs:
        body["macs"] = macs
    if network:
        body["network"] = network
    if node:
        body["node"] = node.value
    if port_id:
        body["port_id"] = port_id
    trigger = devices.releaseSiteDeviceDhcpLease(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(f"Release DHCP leases command triggered for device {device_id}")
        ws = DeviceCmdEvents(apissession, site_id=site_id, device_ids=[device_id])
        util_response = WebSocketWrapper(
            apissession, util_response, timeout=timeout, on_message=on_message
        ).start(ws)
    else:
        LOGGER.error(
            f"Failed to trigger release DHCP leases command: {trigger.status_code} - {trigger.data}"
        )  # Give the release DHCP leases command a moment to take effect
    return util_response


def retrieveDhcpLeases(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    network: str,
    node: Node | None = None,
    timeout=15,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICES: SRX, SSR

    Retrieves DHCP leases on a gateway (SRX / SSR) and streams the results.

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to retrieve DHCP leases from.
    network : str
        Network to release DHCP leases for.
    node : Node, optional
        Node information for the DHCP lease release command.
    port_id : str, optional
        Port ID to release DHCP leases for.
    timeout : int, optional
        Timeout for the release DHCP leases command in seconds.
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received from the WebSocket stream.
    """
    body: dict[str, str | list | int] = {"network": network}
    if node:
        body["node"] = node.value
    trigger = devices.showSiteDeviceDhcpLeases(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(f"Retrieve DHCP leases command triggered for device {device_id}")
        ws = DeviceCmdEvents(apissession, site_id=site_id, device_ids=[device_id])
        util_response = WebSocketWrapper(
            apissession, util_response, timeout=timeout, on_message=on_message
        ).start(ws)
    else:
        LOGGER.error(
            f"Failed to trigger retrieve DHCP leases command: {trigger.status_code} - {trigger.data}"
        )  # Give the release DHCP leases command a moment to take effect
    return util_response
