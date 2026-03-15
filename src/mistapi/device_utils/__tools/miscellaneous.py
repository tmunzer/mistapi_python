from collections.abc import Callable
from enum import Enum

from mistapi import APISession as _APISession
from mistapi.__logger import logger as LOGGER
from mistapi.api.v1.sites import devices
from mistapi.device_utils.__tools.__common import Node
from mistapi.device_utils.__tools.__ws_wrapper import UtilResponse, WebSocketWrapper
from mistapi.websockets.session import SessionWithUrl
from mistapi.websockets.sites import DeviceCmdEvents


class TracerouteProtocol(Enum):
    """Enum for specifying protocol in traceroute command."""

    ICMP = "icmp"
    UDP = "udp"


def ping(
    apisession: _APISession,
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
    apisession: mistapi.APISession
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
    LOGGER.debug(
        "Initiating ping command for device %s to host %s with count %s, node %s, size %s, "
        "VRF %s, and timeout %s",
        device_id,
        host,
        count,
        node,
        size,
        vrf,
        timeout,
    )
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
    util_response = UtilResponse()
    return WebSocketWrapper(
        apisession, util_response, timeout, on_message=on_message
    ).start_with_trigger(
        trigger_fn=lambda: devices.pingFromDevice(
            apisession, site_id=site_id, device_id=device_id, body=body
        ),
        ws_factory_fn=lambda _trigger: DeviceCmdEvents(
            apisession, site_id=site_id, device_ids=[device_id]
        ),
    )


## NO DATA
# def service_ping(
#     apisession: _APISession,
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
#     apisession: mistapi.APISession
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
#         apisession,
#         site_id=site_id,
#         device_id=device_id,
#         body=body,
#     )
#     util_response = UtilResponse(trigger)
#     if trigger.status_code == 200:
#         LOGGER.info(f"Service Ping command triggered for device {device_id}")
#         ws = DeviceCmdEvents(apisession, site_id=site_id, device_ids=[device_id])
#         util_response = WebSocketWrapper(
#             apisession, util_response, timeout, on_message=on_message
#         ).start(ws)
#     else:
#         LOGGER.error(
#             f"Failed to trigger Service Ping command: {trigger.status_code} - {trigger.data}"
#         )  # Give the ping command a moment to take effect
#     return util_response


def traceroute(
    apisession: _APISession,
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
    apisession: mistapi.APISession
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
    LOGGER.debug(
        "Initiating traceroute command for device %s to host %s with protocol %s, port %s, "
        "and timeout %s",
        device_id,
        host,
        protocol,
        port,
        timeout,
    )
    body: dict[str, str | list | int] = {"host": host}
    if protocol:
        body["protocol"] = protocol.value
    if port:
        body["port"] = port
    util_response = UtilResponse()
    return WebSocketWrapper(
        apisession, util_response, timeout, on_message=on_message
    ).start_with_trigger(
        trigger_fn=lambda: devices.tracerouteFromDevice(
            apisession, site_id=site_id, device_id=device_id, body=body
        ),
        ws_factory_fn=lambda _trigger: DeviceCmdEvents(
            apisession, site_id=site_id, device_ids=[device_id]
        ),
    )


def monitor_traffic(
    apisession: _APISession,
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
    apisession: mistapi.APISession
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
    LOGGER.debug(
        "Initiating monitor traffic command for device %s on port %s with timeout %s",
        device_id,
        port_id,
        timeout,
    )
    body: dict[str, str | int] = {"duration": 60}
    if port_id:
        body["port"] = port_id

    def _ws_factory(trigger):
        if isinstance(trigger.data, dict) and "url" in trigger.data:
            return SessionWithUrl(apisession, url=trigger.data.get("url", ""))
        LOGGER.error(
            "Monitor traffic command did not return a valid URL: %s", trigger.data
        )
        return None

    util_response = UtilResponse()
    return WebSocketWrapper(
        apisession, util_response, timeout=timeout, on_message=on_message
    ).start_with_trigger(
        trigger_fn=lambda: devices.monitorSiteDeviceTraffic(
            apisession, site_id=site_id, device_id=device_id, body=body
        ),
        ws_factory_fn=_ws_factory,
    )


# NO DATA
def top_command(
    apisession: _APISession,
    site_id: str,
    device_id: str,
    timeout=10,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICE: EX, SRX

    Initiates a top command on the device and streams the results.

    PARAMS
    -----------
    apisession: mistapi.APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to run the top command on.
    timeout : int, optional
        Timeout for the top command in seconds.
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """

    def _ws_factory(trigger):
        if isinstance(trigger.data, dict) and "url" in trigger.data:
            return SessionWithUrl(apisession, url=trigger.data.get("url", ""))
        LOGGER.error("Top command did not return a valid URL: %s", trigger.data)
        return None

    util_response = UtilResponse()
    return WebSocketWrapper(
        apisession, util_response, timeout=timeout, on_message=on_message
    ).start_with_trigger(
        trigger_fn=lambda: devices.runSiteSrxTopCommand(
            apisession, site_id=site_id, device_id=device_id
        ),
        ws_factory_fn=_ws_factory,
    )
