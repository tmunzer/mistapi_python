from enum import Enum

from mistapi import APISession as _APISession
from mistapi.__logger import logger as LOGGER
from mistapi.api.v1.sites import devices
from mistapi.websockets.utils.__ws_wrapper import UtilResponse, WebSocketWrapper


class Node(Enum):
    NODE0 = "node0"
    NODE1 = "node1"


class RouteProtocol(Enum):
    ANY = "any"
    BGP = "bgp"
    DIRECT = "direct"
    EVPN = "evpn"
    OSPF = "ospf"
    STATIC = "static"


async def show_routes(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    node: Node | None = None,
    prefix: str | None = None,
    protocol: RouteProtocol | None = None,
    route_type: str | None = None,
    vrf: str | None = None,
    timeout=5,
) -> UtilResponse:
    """
    For SSR and SRX. Initiates a show service path command on the gateway and streams the results.

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

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received from the WebSocket stream.
    """

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
    trigger = devices.showSiteSsrAndSrxRoutes(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"SSR service path command triggered for device {device_id}")
        util_response = await WebSocketWrapper(
            apissession, util_response, timeout=timeout
        ).startCmdEvents(site_id, device_id)
    else:
        LOGGER.error(
            f"Failed to trigger SSR service path command: {trigger.status_code} - {trigger.data}"
        )  # Give the SSR service path command a moment to take effect
    return util_response


async def test_dns_resolution(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    node: Node | None = None,
    hostname: str | None = None,
    timeout=5,
) -> UtilResponse:
    """
    For SSR Only. Initiates a DNS resolution command on the gateway and streams the results.

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the gateway is located.
    device_id : str
        UUID of the gateway to perform the DNS resolution command on.
    node : Node, optional
        Node information for the DNS resolution command.
    hostname : str, optional
        Hostname to resolve.
    timeout : int, optional
        Timeout for the command in seconds.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received from the WebSocket stream.
    """
    body: dict[str, str | list | int] = {}
    if node:
        body["node"] = node.value
    if hostname:
        body["hostname"] = hostname
    trigger = devices.testSiteSsrDnsResolution(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"SSR DNS resolution command triggered for device {device_id}")
        util_response = await WebSocketWrapper(
            apissession, util_response, timeout=timeout
        ).startCmdEvents(site_id, device_id)
    else:
        LOGGER.error(
            f"Failed to trigger SSR DNS resolution command: {trigger.status_code} - {trigger.data}"
        )  # Give the SSR DNS resolution command a moment to take effect
    return util_response


async def show_service_path(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    node: Node | None = None,
    service_name: str | None = None,
    timeout=5,
) -> UtilResponse:
    """
    For SSR Only. Initiates a show service path command on the gateway and streams the results.

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the gateway is located.
    device_id : str
        UUID of the gateway to perform the show service path command on.
    node : Node, optional
        Node information for the show service path command.
    service_name : str, optional
        Name of the service to show the path for.
    timeout : int, optional
        Timeout for the command in seconds.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received from the WebSocket stream.
    """
    body: dict[str, str | list | int] = {}
    if node:
        body["node"] = node.value
    if service_name:
        body["service_name"] = service_name
    trigger = devices.showSiteSsrServicePath(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"SSR service path command triggered for device {device_id}")
        util_response = await WebSocketWrapper(
            apissession, util_response, timeout=timeout
        ).startCmdEvents(site_id, device_id)
    else:
        LOGGER.error(
            f"Failed to trigger SSR service path command: {trigger.status_code} - {trigger.data}"
        )  # Give the SSR service path command a moment to take effect
    return util_response


async def clear_policy_hit_count(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    policy_name: str,
    # timeout: int = 10,
) -> UtilResponse:
    """
    Clears the policy hit count on a device.

    PARAMS
    -----------
    apissession : _APISession
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
    trigger = devices.clearSiteDevicePolicyHitCount(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body={"policy_name": policy_name},
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(f"Clear policy hit count command triggered for device {device_id}")
        # util_response = await WebSocketWrapper(
        #     apissession, util_response, timeout=timeout
        # ).startCmdEvents(site_id, device_id)
    else:
        LOGGER.error(
            f"Failed to trigger clear policy hit count command: {trigger.status_code} - {trigger.data}"
        )  # Give the clear policy hit count command a moment to take effect
    return util_response
