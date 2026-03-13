from collections.abc import Callable
from enum import Enum

from mistapi import APISession as _APISession
from mistapi.__logger import logger as LOGGER
from mistapi.api.v1.sites import devices
from mistapi.device_utils.__tools.__ws_wrapper import UtilResponse, WebSocketWrapper
from mistapi.websockets.session import SessionWithUrl
from mistapi.websockets.sites import DeviceCmdEvents


class Node(Enum):
    """Node Enum for specifying node information in commands."""

    NODE0 = "node0"
    NODE1 = "node1"


class TracerouteProtocol(Enum):
    """Enum for specifying protocol in traceroute command."""

    ICMP = "icmp"
    UDP = "udp"


def ping(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    host: str,
    count: int | None = None,
    node: Node | None = None,
    size: int | None = None,
    vrf: str | None = None,
    timeout: int = 3,
    on_message: Callable[[dict], None] | None = None,
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
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

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
        ws = DeviceCmdEvents(apissession, site_id=site_id, device_ids=[device_id])
        util_response = WebSocketWrapper(
            apissession, util_response, timeout, on_message=on_message
        ).start(ws)
    else:
        LOGGER.error(
            f"Failed to trigger ping command: {trigger.status_code} - {trigger.data}"
        )  # Give the ping command a moment to take effect
    return util_response


## NO DATA
# def service_ping(
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
#     on_message: Callable[[dict], None] | None = None,
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
#     on_message : Callable, optional
#         Callback invoked with each extracted raw message as it arrives.

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
#         ws = DeviceCmdEvents(apissession, site_id=site_id, device_ids=[device_id])
#         util_response = WebSocketWrapper(
#             apissession, util_response, timeout, on_message=on_message
#         ).start(ws)
#     else:
#         LOGGER.error(
#             f"Failed to trigger Service Ping command: {trigger.status_code} - {trigger.data}"
#         )  # Give the ping command a moment to take effect
#     return util_response


def traceroute(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    host: str,
    protocol: TracerouteProtocol = TracerouteProtocol.ICMP,
    port: int | None = None,
    timeout: int = 10,
    on_message: Callable[[dict], None] | None = None,
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
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

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
        ws = DeviceCmdEvents(apissession, site_id=site_id, device_ids=[device_id])
        util_response = WebSocketWrapper(
            apissession, util_response, timeout, on_message=on_message
        ).start(ws)
    else:
        LOGGER.error(
            f"Failed to trigger traceroute command: {trigger.status_code} - {trigger.data}"
        )  # Give the traceroute command a moment to take effect
    return util_response


def monitor_traffic(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    port_id: str | None = None,
    timeout=30,
    on_message: Callable[[dict], None] | None = None,
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
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

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
        ws = SessionWithUrl(apissession, url=trigger.data.get("url", ""))
        util_response = WebSocketWrapper(
            apissession, util_response, timeout=timeout, on_message=on_message
        ).start(ws)
    else:
        LOGGER.error(
            f"Failed to trigger monitor traffic command: {trigger.status_code} - {trigger.data}"
        )  # Give the monitor traffic command a moment to take effect
    return util_response


## NO DATA
# def srx_top_command(
#     apissession: _APISession,
#     site_id: str,
#     device_id: str,
#     timeout=10,
#     on_message: Callable[[dict], None] | None = None,
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
#     on_message : Callable, optional
#         Callback invoked with each extracted raw message as it arrives.

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
#         ws = SessionWithUrl(apissession, url=trigger.data.get("url", ""))
#         util_response = WebSocketWrapper(
#             apissession, util_response, timeout=timeout, on_message=on_message
#         ).start(ws)
#     else:
#         LOGGER.error(
#             f"Failed to trigger top command: {trigger.status_code} - {trigger.data}"
#         )  # Give the top command a moment to take effect
#     return util_response
