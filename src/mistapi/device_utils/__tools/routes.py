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
    """Node Enum for specifying node information in route commands."""

    NODE0 = "node0"
    NODE1 = "node1"


class RouteProtocol(Enum):
    """RouteProtocol Enum for specifying route protocol information in show routes command."""

    ANY = "any"
    BGP = "bgp"
    DIRECT = "direct"
    EVPN = "evpn"
    OSPF = "ospf"
    STATIC = "static"


def show(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    node: Node | None = None,
    prefix: str | None = None,
    protocol: RouteProtocol | None = None,
    route_type: str | None = None,
    vrf: str | None = None,
    timeout=2,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICE: SSR, SRX

    Initiates a show routes command on the gateway and streams the results.

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the gateway is located.
    device_id : str
        UUID of the gateway to perform the show routes command on.
    node : Node, optional
        Node information for the show routes command.
    prefix : str, optional
        Prefix to filter the routes.
    protocol : RouteProtocol, optional
        Protocol to filter the routes.
    route_type : str, optional
        Type of the route to filter.
    vrf : str, optional
        VRF to filter the routes.
    timeout : int, optional
        Timeout for the command in seconds.
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    LOGGER.debug(
        "Initiating show routes command for device %s with node %s, prefix %s, protocol %s, "
        "route_type %s, and VRF %s",
        device_id,
        node,
        prefix,
        protocol,
        route_type,
        vrf,
    )
    body: dict[str, str | list | int] = {}
    if node:
        body["node"] = node.value
    if prefix:
        body["prefix"] = prefix
    if protocol:
        body["protocol"] = protocol.value
    if route_type:
        body["route_type"] = route_type
    if vrf:
        body["vrf"] = vrf
    util_response = UtilResponse()
    return WebSocketWrapper(
        apissession, util_response, timeout=timeout, on_message=on_message
    ).start_with_trigger(
        trigger_fn=lambda: devices.showSiteSsrAndSrxRoutes(
            apissession, site_id=site_id, device_id=device_id, body=body
        ),
        ws_factory_fn=lambda _trigger: DeviceCmdEvents(
            apissession, site_id=site_id, device_ids=[device_id]
        ),
    )
