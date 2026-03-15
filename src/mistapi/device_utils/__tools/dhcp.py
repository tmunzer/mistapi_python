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


def release_dhcp_leases(
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
    LOGGER.debug(
        "Initiating DHCP lease release for device %s with MACs %s, network %s, node %s, port ID %s, "
        "and timeout %s",
        device_id,
        macs,
        network,
        node,
        port_id,
        timeout,
    )
    body: dict[str, str | list | int] = {}
    if macs:
        body["macs"] = macs
    if network:
        body["network"] = network
    if node:
        body["node"] = node.value
    if port_id:
        body["port_id"] = port_id
    util_response = UtilResponse()
    return WebSocketWrapper(
        apissession, util_response, timeout=timeout, on_message=on_message
    ).start_with_trigger(
        trigger_fn=lambda: devices.releaseSiteDeviceDhcpLease(
            apissession, site_id=site_id, device_id=device_id, body=body
        ),
        ws_factory_fn=lambda _trigger: DeviceCmdEvents(
            apissession, site_id=site_id, device_ids=[device_id]
        ),
    )


def retrieve_dhcp_leases(
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
        Network to retrieve DHCP leases for.
    node : Node, optional
        Node information for the DHCP lease retrieval command.
    timeout : int, optional
        Timeout for the retrieve DHCP leases command in seconds.
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received from the WebSocket stream.
    """
    LOGGER.debug(
        "Initiating DHCP lease retrieval for device %s with network %s, node %s, and timeout %s",
        device_id,
        network,
        node,
        timeout,
    )
    body: dict[str, str | list | int] = {"network": network}
    if node:
        body["node"] = node.value
    util_response = UtilResponse()
    return WebSocketWrapper(
        apissession, util_response, timeout=timeout, on_message=on_message
    ).start_with_trigger(
        trigger_fn=lambda: devices.showSiteDeviceDhcpLeases(
            apissession, site_id=site_id, device_id=device_id, body=body
        ),
        ws_factory_fn=lambda _trigger: DeviceCmdEvents(
            apissession, site_id=site_id, device_ids=[device_id]
        ),
    )
