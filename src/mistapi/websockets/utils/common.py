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


async def retrieve_arp_table(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    node: Node | None = None,
    timeout=5,
) -> UtilResponse:
    """
    Retrieves the ARP table from a device and streams the results.

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

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received from the WebSocket stream.
    """
    # AP is returnning RAW data
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
        util_response = await WebSocketWrapper(
            apissession, util_response, timeout=timeout
        ).startCmdEvents(site_id, device_id)
    else:
        LOGGER.error(
            f"Failed to trigger show ARP command: {trigger.status_code} - {trigger.data}"
        )  # Give the show ARP command a moment to take effect
    return util_response


async def bounce_ports(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    port_ids: list[str],
    timeout=5,
) -> UtilResponse:
    """
    Initiates a bounce command on the specified ports of a device and streams the results.

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
        A UtilResponse object containing the API response and a list of raw messages received from the WebSocket stream.
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


async def clear_mac_table(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    mac_address: str | None = None,
    port_id: str | None = None,
    vlan_id: str | None = None,
    # timeout=30,
) -> UtilResponse:
    """
    Clears the MAC table on a device and streams the results.

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to clear the MAC table from.
    mac_address : str, optional
        MAC address to clear from the MAC table.
    port_id : str, optional
        Port ID to clear from the MAC table.
    vlan_id : str, optional
        VLAN ID to clear from the MAC table.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received from the WebSocket stream.
    """
    # AP is returnning RAW data
    # SWITCH is returning ???
    # GATEWAY is returning JSON
    body: dict[str, str | list | int] = {}
    if mac_address:
        body["mac_address"] = mac_address
    if port_id:
        body["port_id"] = port_id
    if vlan_id:
        body["vlan_id"] = vlan_id
    trigger = devices.clearSiteDeviceMacTable(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"Clear MAC Table command triggered for device {device_id}")
        # util_response = await WebSocketWrapper(
        #     apissession, util_response, timeout=timeout
        # ).startCmdEvents(site_id, device_id)
    else:
        LOGGER.error(
            f"Failed to trigger clear MAC Table command: {trigger.status_code} - {trigger.data}"
        )  # Give the clear MAC Table command a moment to take effect
    return util_response


async def release_dhcp_leases(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    macs: list[str] | None = None,
    network: str | None = None,
    node: Node | None = None,
    port_id: str | None = None,
    timeout=5,
) -> UtilResponse:
    """
    Releases DHCP leases on a device and streams the results.
    valid combinations are:
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

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received from the WebSocket stream.
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
        util_response = await WebSocketWrapper(
            apissession, util_response, timeout=timeout
        ).startCmdEvents(site_id, device_id)
    else:
        LOGGER.error(
            f"Failed to trigger release DHCP leases command: {trigger.status_code} - {trigger.data}"
        )  # Give the release DHCP leases command a moment to take effect
    return util_response


# TODO
async def retrieve_dhcp_leases(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    network: str,
    node: Node | None = None,
    timeout=15,
) -> UtilResponse:
    """
    Retrieves DHCP leases on a device and streams the results.

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
        util_response = await WebSocketWrapper(
            apissession, util_response, timeout=timeout
        ).startCmdEvents(site_id, device_id)
    else:
        LOGGER.error(
            f"Failed to trigger retrieve DHCP leases command: {trigger.status_code} - {trigger.data}"
        )  # Give the release DHCP leases command a moment to take effect
    return util_response


#######################################################
## Switch
#######################################################


async def switch_clear_bpdu_error(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    port_ids: list[str],
) -> UtilResponse:
    """
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
        A UtilResponse object containing the API response and a list of raw messages received from the WebSocket stream.
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


async def switch_clear_learned_mac(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    port_ids: list[str],
) -> UtilResponse:
    """
    Clears learned MAC addresses on the specified ports of a device.

    PARAMS
    -----------
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to clear learned MAC addresses on.
    port_ids : list[str]
        List of port IDs to clear learned MAC addresses on.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received from the WebSocket stream.
    """
    body: dict[str, str | list | int] = {"ports": port_ids}
    trigger = devices.clearSiteDeviceDot1xSession(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"Clear learned MACs command triggered for device {device_id}")
    else:
        LOGGER.error(
            f"Failed to trigger clear learned MACs command: {trigger.status_code} - {trigger.data}"
        )  # Give the clear learned MACs command a moment to take effect
    return util_response


async def switch_clear_dot1x_sessions(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    port_ids: list[str],
) -> UtilResponse:
    """
    Clears dot1x sessions on the specified ports of a switch.

    PARAMS
    -----------
    site_id : str
        UUID of the site where the switch is located.
    device_id : str
        UUID of the switch to clear dot1x sessions on.
    port_ids : list[str]
        List of port IDs to clear dot1x sessions on.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received from the WebSocket stream.
    """
    body: dict[str, str | list | int] = {"ports": port_ids}
    trigger = devices.clearAllLearnedMacsFromPortOnSwitch(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"Clear learned MACs command triggered for device {device_id}")
    else:
        LOGGER.error(
            f"Failed to trigger clear learned MACs command: {trigger.status_code} - {trigger.data}"
        )  # Give the clear learned MACs command a moment to take effect
    return util_response


#######################################################
## Websocket
#######################################################


async def ping(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    host: str,
    count: int | None = None,
    node: None | None = None,
    size: int | None = None,
    vrf: str | None = None,
    timeout: int = 5,
) -> UtilResponse:
    """
    Initiates a ping command from a device to a specified host and streams the results.

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to initiate the ping from.
    host : str
        The host to ping.
    count : int, optional
        Number of ping requests to send.
    node : None, optional
        Node information for the ping command.
    size : int, optional
        Size of the ping packet.
    vrf : str, optional
        VRF to use for the ping command.
    timeout : int, optional
        Timeout for the ping command in seconds.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received from the WebSocket stream.
    """
    body: dict[str, str | list | int] = {}
    if count:
        body["count"] = count
    if host:
        body["host"] = host
    if node:
        body["node"] = node.value
    if size:
        body["size"] = size
    if vrf:
        body["vrf"] = vrf
    trigger = devices.pingFromDevice(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(f"Ping command triggered for device {device_id}")
        util_response = await WebSocketWrapper(
            apissession, util_response, timeout
        ).startCmdEvents(site_id, device_id)
    else:
        LOGGER.error(
            f"Failed to trigger ping command: {trigger.status_code} - {trigger.data}"
        )  # Give the ping command a moment to take effect
    return util_response


# async def gateway_dns_resolution(
#     self,
#     site_id: str,
#     device_id: str,
#     timeout=10,
# ) -> list[str]:
#   """For SSR Only. Initiates a DNS resolution command on the gateway and streams the results."""
#     self.timeout = timeout
#     trigger = testSiteSsrDnsResolution(
#         apissession,
#         site_id=site_id,
#         device_id=device_id,
#     )
#     if trigger.status_code == 200:
#         print(trigger.data)
#         print(f"SSR DNS resolution command triggered for device {device_id}")
#         self.startCmdEvents(site_id, device_id)
#     else:
#         print(
#             f"Failed to trigger SSR DNS resolution command: {trigger.status_code} - {trigger.data}"
#         )  # Give the SSR DNS resolution command a moment to take effect
#     return util_response

#######################################################
## Websocket Session
#######################################################
