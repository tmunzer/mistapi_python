from enum import Enum

from mistapi import APISession as _APISession
from mistapi.__logger import logger as LOGGER
from mistapi.api.v1.sites import devices, pcaps
from mistapi.utils.__ws_wrapper import UtilResponse, WebSocketWrapper


class Node(Enum):
    """Node Enum for specifying node information in commands."""

    NODE0 = "node0"
    NODE1 = "node1"


class TracerouteProtocol(Enum):
    """Enum for specifying protocol in traceroute command."""

    ICMP = "icmp"
    UDP = "udp"


async def ping(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    host: str,
    count: int | None = None,
    node: None | None = None,
    size: int | None = None,
    vrf: str | None = None,
    timeout: int = 3,
) -> UtilResponse:
    """
    DEVICES: AP, EX, SRX, SSR

    Initiates a ping command from a device (AP / EX/ SRX / SSR) to a specified host and
    streams the results.

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
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
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


## NO DATA
# async def service_ping(
#     apissession: _APISession,
#     site_id: str,
#     device_id: str,
#     host: str,
#     service: str,
#     tenant: str,
#     count: int | None = None,
#     node: None | None = None,
#     size: int | None = None,
#     timeout: int = 3,
# ) -> UtilResponse:
#     """
#     DEVICES: SSR

#     Initiates a service ping command from a SSR to a specified host and streams the results.

#     PARAMS
#     -----------
#     apissession : _APISession
#         The API session to use for the request.
#     site_id : str
#         UUID of the site where the device is located.
#     device_id : str
#         UUID of the device to initiate the ping from.
#     host : str
#         The host to ping.
#     service : str
#         The service to ping.
#     tenant : str
#         Tenant to use for the ping command.
#     count : int, optional
#         Number of ping requests to send.
#     node : None, optional
#         Node information for the ping command.
#     size : int, optional
#         Size of the ping packet.
#     timeout : int, optional
#         Timeout for the ping command in seconds.

#     RETURNS
#     -----------
#     UtilResponse
#         A UtilResponse object containing the API response and a list of raw messages received
#         from the WebSocket stream.
#     """
#     body: dict[str, str | list | int] = {}
#     if count:
#         body["count"] = count
#     if host:
#         body["host"] = host
#     if node:
#         body["node"] = node.value
#     if size:
#         body["size"] = size
#     if tenant:
#         body["tenant"] = tenant
#     if service:
#         body["service"] = service
#     trigger = devices.servicePingFromSsr(
#         apissession,
#         site_id=site_id,
#         device_id=device_id,
#         body=body,
#     )
#     util_response = UtilResponse(trigger)
#     if trigger.status_code == 200:
#         LOGGER.info(f"Service Ping command triggered for device {device_id}")
#         util_response = await WebSocketWrapper(
#             apissession, util_response, timeout
#         ).startCmdEvents(site_id, device_id)
#     else:
#         LOGGER.error(
#             f"Failed to trigger Service Ping command: {trigger.status_code} - {trigger.data}"
#         )  # Give the ping command a moment to take effect
#     return util_response


async def traceroute(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    host: str,
    protocol: TracerouteProtocol = TracerouteProtocol.ICMP,
    port: int | None = None,
    timeout: int = 10,
) -> UtilResponse:
    """
    DEVICES: AP, EX, SRX, SSR

    Initiates a traceroute command from a device (AP / EX/ SRX / SSR) to a specified host and
    streams the results.

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to initiate the traceroute from.
    host : str
        The host to traceroute.
    protocol : TracerouteProtocol, optional
        Protocol to use for the traceroute command (icmp or udp).
    port : int, optional
        Port to use for UDP traceroute.
    timeout : int, optional
        Timeout for the traceroute command in seconds.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    body: dict[str, str | list | int] = {"host": host}
    if protocol:
        body["protocol"] = protocol.value
    if port:
        body["port"] = port
    trigger = devices.tracerouteFromDevice(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(f"Traceroute command triggered for device {device_id}")
        util_response = await WebSocketWrapper(
            apissession, util_response, timeout
        ).startCmdEvents(site_id, device_id)
    else:
        LOGGER.error(
            f"Failed to trigger traceroute command: {trigger.status_code} - {trigger.data}"
        )  # Give the traceroute command a moment to take effect
    return util_response


async def monitor_traffic(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    port_id: str | None = None,
    timeout=30,
) -> UtilResponse:
    """
    DEVICE: EX, SRX

    Initiates a monitor traffic command on the device and streams the results.

    * if `port_id` is provided, JUNOS uses cmd "monitor interface" to monitor traffic on particular
    * if `port_id` is not provided, JUNOS uses cmd "monitor interface traffic" to monitor traffic
      on all ports

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to monitor traffic on.
    port_id : str, optional
        Port ID to filter the traffic.
    timeout : int, optional
        Timeout for the monitor traffic command in seconds.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    body: dict[str, str | int] = {"duration": 60}
    if port_id:
        body["port"] = port_id
    trigger = devices.monitorSiteDeviceTraffic(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"Monitor traffic command triggered for device {device_id}")
        util_response = await WebSocketWrapper(
            apissession, util_response, timeout=timeout
        ).startSessionUrl(trigger.data.get("url", ""))
    else:
        LOGGER.error(
            f"Failed to trigger monitor traffic command: {trigger.status_code} - {trigger.data}"
        )  # Give the monitor traffic command a moment to take effect
    return util_response


async def ap_remote_pcap_wireless(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    band: str,
    tcpdump_expression: str | None = None,
    ssid: str | None = None,
    ap_mac: str | None = None,
    duration: int = 600,
    max_pkt_len: int = 512,
    num_packets: int = 1024,
    timeout=10,
) -> UtilResponse:
    """
    DEVICE: AP

    Initiates a remote pcap command on the device and streams the results.

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to run remote pcap on.
    band : str
        Comma-separated list of radio bands (24, 5, or 6).
    tcpdump_expression : str, optional
        Tcpdump expression to filter the captured traffic.
        e.g. "type mgt or type ctl -vvv -tttt -en"
    ssid : str, optional
        SSID to filter the wireless traffic.
    ap_mac : str, optional
        AP MAC address to filter the wireless traffic.
    duration : int, optional
        Duration of the remote pcap in seconds (default: 600).
    max_pkt_len : int, optional
        Maximum packet length to capture (default: 512).
    num_packets : int, optional
        Maximum number of packets to capture (default: 1024).
    timeout : int, optional
        Timeout for the remote pcap command in seconds.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    body: dict[str, str | int] = {
        "band": band,
        "duration": duration,
        "max_pkt_len": max_pkt_len,
        "num_packets": num_packets,
        "type": "radiotap",
        "format": "stream",
    }
    if ssid:
        body["ssid"] = ssid
    if ap_mac:
        body["ap_mac"] = ap_mac
    if tcpdump_expression:
        body["tcpdump_expression"] = tcpdump_expression
    trigger = pcaps.startSitePacketCapture(
        apissession,
        site_id=site_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"Remote pcap command triggered for device {device_id}")
        util_response = await WebSocketWrapper(
            apissession, util_response, timeout=timeout
        ).startRemotePcap(site_id)
    else:
        LOGGER.error(
            f"Failed to trigger remote pcap command: {trigger.status_code} - {trigger.data}"
        )  # Give the remote pcap command a moment to take effect
    return util_response


async def ap_remote_pcap_wired(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    tcpdump_expression: str | None = None,
    duration: int = 600,
    max_pkt_len: int = 512,
    num_packets: int = 1024,
    timeout=10,
) -> UtilResponse:
    """
    DEVICE: AP

    Initiates a remote pcap command on the device and streams the results.

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to run remote pcap on.
    tcpdump_expression : str, optional
        Tcpdump expression to filter the captured traffic.
        e.g. "udp port 67 or udp port 68 -vvv -tttt -en"
    duration : int, optional
        Duration of the remote pcap in seconds (default: 600).
    max_pkt_len : int, optional
        Maximum packet length to capture (default: 512).
    num_packets : int, optional
        Maximum number of packets to capture (default: 1024).
    timeout : int, optional
        Timeout for the remote pcap command in seconds.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    body: dict[str, str | int] = {
        "duration": duration,
        "max_pkt_len": max_pkt_len,
        "num_packets": num_packets,
        "type": "wired",
        "format": "stream",
    }
    if tcpdump_expression:
        body["tcpdump_expression"] = tcpdump_expression
    trigger = pcaps.startSitePacketCapture(
        apissession,
        site_id=site_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"Remote pcap command triggered for device {device_id}")
        util_response = await WebSocketWrapper(
            apissession, util_response, timeout=timeout
        ).startRemotePcap(site_id)
    else:
        LOGGER.error(
            f"Failed to trigger remote pcap command: {trigger.status_code} - {trigger.data}"
        )  # Give the remote pcap command a moment to take effect
    return util_response


async def srx_remote_pcap(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    port_ids: list[str],
    tcpdump_expression: str | None = None,
    duration: int = 600,
    max_pkt_len: int = 512,
    num_packets: int = 1024,
    timeout=10,
) -> UtilResponse:
    """
    DEVICE: SRX

    Initiates a remote pcap command on the device and streams the results.

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to run remote pcap on.
    port_ids : list[str]
        List of port IDs to monitor.
    tcpdump_expression : str, optional
        Tcpdump expression to filter the captured traffic.
        e.g. "udp port 67 or udp port 68 -vvv -tttt -en"
    duration : int, optional
        Duration of the remote pcap in seconds (default: 600).
    max_pkt_len : int, optional
        Maximum packet length to capture (default: 512).
    num_packets : int, optional
        Maximum number of packets to capture (default: 1024).
    timeout : int, optional
        Timeout for the remote pcap command in seconds.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    gateway_mac = device_id.split("-")[-1]
    body: dict[str, str | int | dict] = {
        "duration": duration,
        "max_pkt_len": max_pkt_len,
        "num_packets": num_packets,
        "gateways": {gateway_mac: {"ports": {}}},
        "type": "gateway",
        "format": "stream",
    }
    for port_id in port_ids:
        gateway_dict = body["gateways"]
        assert isinstance(gateway_dict, dict)
        mac_dict = gateway_dict[gateway_mac]
        assert isinstance(mac_dict, dict)
        ports_dict = mac_dict["ports"]
        assert isinstance(ports_dict, dict)
        ports_dict[port_id] = {"tcpdump_expression": tcpdump_expression}
    if tcpdump_expression:
        body["tcpdump_expression"] = tcpdump_expression
    trigger = pcaps.startSitePacketCapture(
        apissession,
        site_id=site_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"Remote pcap command triggered for device {device_id}")
        util_response = await WebSocketWrapper(
            apissession, util_response, timeout=timeout
        ).startRemotePcap(site_id)
    else:
        LOGGER.error(
            f"Failed to trigger remote pcap command: {trigger.status_code} - {trigger.data}"
        )  # Give the remote pcap command a moment to take effect
    return util_response


async def ssr_remote_pcap(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    port_ids: list[str],
    tcpdump_expression: str | None = None,
    duration: int = 600,
    max_pkt_len: int = 512,
    num_packets: int = 1024,
    timeout=10,
) -> UtilResponse:
    """
    DEVICE: SSR

    Initiates a remote pcap command on the device and streams the results.

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to run remote pcap on.
    port_ids : list[str]
        List of port IDs to monitor.
    tcpdump_expression : str, optional
        Tcpdump expression to filter the captured traffic.
        e.g. "udp port 67 or udp port 68 -vvv -tttt -en"
    duration : int, optional
        Duration of the remote pcap in seconds (default: 600).
    max_pkt_len : int, optional
        Maximum packet length to capture (default: 512).
    num_packets : int, optional
        Maximum number of packets to capture (default: 1024).
    timeout : int, optional
        Timeout for the remote pcap command in seconds.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    gateway_mac = device_id.split("-")[-1]
    body: dict[str, str | int | dict] = {
        "duration": duration,
        "max_pkt_len": max_pkt_len,
        "num_packets": num_packets,
        "raw": False,
        "gateways": {gateway_mac: {"ports": {}}},
        "type": "gateway",
        "format": "stream",
    }
    for port_id in port_ids:
        gateway_dict = body["gateways"]
        assert isinstance(gateway_dict, dict)
        mac_dict = gateway_dict[gateway_mac]
        assert isinstance(mac_dict, dict)
        ports_dict = mac_dict["ports"]
        assert isinstance(ports_dict, dict)
        ports_dict[port_id] = {"tcpdump_expression": tcpdump_expression}
    if tcpdump_expression:
        body["tcpdump_expression"] = tcpdump_expression
    trigger = pcaps.startSitePacketCapture(
        apissession,
        site_id=site_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"Remote pcap command triggered for device {device_id}")
        util_response = await WebSocketWrapper(
            apissession, util_response, timeout=timeout
        ).startRemotePcap(site_id)
    else:
        LOGGER.error(
            f"Failed to trigger remote pcap command: {trigger.status_code} - {trigger.data}"
        )  # Give the remote pcap command a moment to take effect
    return util_response


async def ex_remote_pcap(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    port_ids: list[str],
    tcpdump_expression: str | None = None,
    duration: int = 600,
    max_pkt_len: int = 512,
    num_packets: int = 1024,
    timeout=10,
) -> UtilResponse:
    """
    DEVICE: EX

    Initiates a remote pcap command on the device and streams the results.

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to run remote pcap on.
    port_ids : list[str]
        List of port IDs to monitor.
    tcpdump_expression : str, optional
        Tcpdump expression to filter the captured traffic.
        e.g. "udp port 67 or udp port 68 -vvv -tttt -en"
    duration : int, optional
        Duration of the remote pcap in seconds (default: 600).
    max_pkt_len : int, optional
        Maximum packet length to capture (default: 512).
    num_packets : int, optional
        Maximum number of packets to capture (default: 1024).
    timeout : int, optional
        Timeout for the remote pcap command in seconds.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    switch_mac = device_id.split("-")[-1]
    body: dict[str, str | int | dict] = {
        "duration": duration,
        "max_pkt_len": max_pkt_len,
        "num_packets": num_packets,
        "switches": {switch_mac: {"ports": {}}},
        "type": "switch",
        "format": "stream",
    }
    for port_id in port_ids:
        switch_dict = body["switches"]
        assert isinstance(switch_dict, dict)
        mac_dict = switch_dict[switch_mac]
        assert isinstance(mac_dict, dict)
        ports_dict = mac_dict["ports"]
        assert isinstance(ports_dict, dict)
        ports_dict[port_id] = {"tcpdump_expression": tcpdump_expression}
    if tcpdump_expression:
        body["tcpdump_expression"] = tcpdump_expression
    trigger = pcaps.startSitePacketCapture(
        apissession,
        site_id=site_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"Remote pcap command triggered for device {device_id}")
        util_response = await WebSocketWrapper(
            apissession, util_response, timeout=timeout
        ).startRemotePcap(site_id)
    else:
        LOGGER.error(
            f"Failed to trigger remote pcap command: {trigger.status_code} - {trigger.data}"
        )  # Give the remote pcap command a moment to take effect
    return util_response


## NO DATA
# async def srx_top_command(
#     apissession: _APISession,
#     site_id: str,
#     device_id: str,
#     timeout=10,
# ) -> UtilResponse:
#     """
#     DEVICE: SRX

#     For SRX Only. Initiates a top command on the device and streams the results.

#     PARAMS
#     -----------
#     apissession : _APISession
#         The API session to use for the request.
#     site_id : str
#         UUID of the site where the device is located.
#     device_id : str
#         UUID of the device to run the top command on.
#     timeout : int, optional
#         Timeout for the top command in seconds.

#     RETURNS
#     -----------
#     UtilResponse
#         A UtilResponse object containing the API response and a list of raw messages received
#         from the WebSocket stream.
#     """
#     trigger = devices.runSiteSrxTopCommand(
#         apissession,
#         site_id=site_id,
#         device_id=device_id,
#     )
#     util_response = UtilResponse(trigger)
#     if trigger.status_code == 200:
#         LOGGER.info(trigger.data)
#         print(f"Top command triggered for device {device_id}")
#         util_response = await WebSocketWrapper(
#             apissession, util_response, timeout=timeout
#         ).startSessionUrl(site_id)
#     else:
#         LOGGER.error(
#             f"Failed to trigger top command: {trigger.status_code} - {trigger.data}"
#         )  # Give the top command a moment to take effect
#     return util_response
