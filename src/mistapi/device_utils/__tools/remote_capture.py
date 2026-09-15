"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
"""

from collections.abc import Callable

from mistapi import APISession as _APISession
from mistapi.__logger import logger as LOGGER
from mistapi.api.v1.orgs import pcaps as org_pcaps
from mistapi.api.v1.sites import pcaps as site_pcaps
from mistapi.device_utils.__tools.__ws_wrapper import UtilResponse, WebSocketWrapper
from mistapi.websockets.orgs import PcapEvents as OrgPcapEvents
from mistapi.websockets.sites import PcapEvents as SitePcapEvents


def _build_pcap_body(
    device_interfaces: dict[str, dict[str, str | None]],
    device_key: str,
    device_type: str,
    tcpdump_expression: str | None,
    duration: int,
    max_pkt_len: int,
    num_packets: int,
    raw: bool | None = None,
) -> dict:
    """Build the request body for remote pcap commands (SRX, SSR, EX)."""
    devices = {}
    for device_id, interfaces in device_interfaces.items():
        ports = {}
        for interface_id, interface_expression in interfaces.items():
            ports[interface_id] = (
                {"tcpdump_expression": interface_expression}
                if interface_expression is not None
                else {}
            )
        devices[device_id.split("-")[-1]] = {"ports": ports}

    body: dict = {
        "duration": duration,
        "max_pkt_len": max_pkt_len,
        "num_packets": num_packets,
        device_key: devices,
        "type": device_type,
        "format": "stream",
    }
    if raw is not None:
        body["raw"] = raw
    if tcpdump_expression is not None:
        body["tcpdump_expression"] = tcpdump_expression
    return body


def _build_mxedge_pcap_body(
    device_interfaces: dict[str, dict[str, str | None]],
    tcpdump_expression: str | None,
    duration: int,
    max_pkt_len: int,
    num_packets: int,
) -> dict:
    """Build a Mist Edge packet capture request body."""
    mxedges = {}
    for mxedge_id, interfaces in device_interfaces.items():
        mxedges[mxedge_id] = {
            "interfaces": {
                interface_id: (
                    {"tcpdump_expression": interface_expression}
                    if interface_expression is not None
                    else {}
                )
                for interface_id, interface_expression in interfaces.items()
            }
        }

    body: dict = {
        "duration": duration,
        "format": "stream",
        "max_pkt_len": max_pkt_len,
        "mxedges": mxedges,
        "num_packets": num_packets,
        "type": "mxedge",
    }
    if tcpdump_expression is not None:
        body["tcpdump_expression"] = tcpdump_expression
    return body


def ap_remote_pcap_wireless(
    apisession: _APISession,
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
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICE: AP

    Initiates a remote pcap command on the device and streams the results.

    PARAMS
    -----------
    apisession: mistapi.APISession
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
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    LOGGER.debug(
        "Initiating remote pcap for device %s on band %s with timeout %s",
        device_id,
        band,
        timeout,
    )
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
    body["ap_mac"] = ap_mac or device_id.split("-")[-1]
    if tcpdump_expression:
        body["tcpdump_expression"] = tcpdump_expression
    util_response = UtilResponse()
    return WebSocketWrapper(
        apisession, util_response, timeout=timeout, on_message=on_message
    ).start_with_trigger(
        trigger_fn=lambda: site_pcaps.startSitePacketCapture(
            apisession, site_id=site_id, body=body
        ),
        ws_factory_fn=lambda _trigger: SitePcapEvents(apisession, site_id=site_id),
    )


def ap_remote_pcap_wired(
    apisession: _APISession,
    site_id: str,
    device_id: str,
    tcpdump_expression: str | None = None,
    duration: int = 600,
    max_pkt_len: int = 512,
    num_packets: int = 1024,
    timeout=10,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICE: AP

    Initiates a remote pcap command on the device and streams the results.

    PARAMS
    -----------
    apisession: mistapi.APISession
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
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    LOGGER.debug(
        "Initiating remote pcap for device %s with timeout %s",
        device_id,
        timeout,
    )
    body: dict[str, str | int] = {
        "duration": duration,
        "max_pkt_len": max_pkt_len,
        "num_packets": num_packets,
        "type": "wired",
        "format": "stream",
    }
    if tcpdump_expression:
        body["tcpdump_expression"] = tcpdump_expression
    util_response = UtilResponse()
    return WebSocketWrapper(
        apisession, util_response, timeout=timeout, on_message=on_message
    ).start_with_trigger(
        trigger_fn=lambda: site_pcaps.startSitePacketCapture(
            apisession, site_id=site_id, body=body
        ),
        ws_factory_fn=lambda _trigger: SitePcapEvents(apisession, site_id=site_id),
    )


def srx_remote_pcap(
    apisession: _APISession,
    site_id: str,
    device_interfaces: dict[str, dict[str, str | None]],
    tcpdump_expression: str | None = None,
    duration: int = 600,
    max_pkt_len: int = 512,
    num_packets: int = 1024,
    timeout=10,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICE: SRX

    Initiates a remote pcap command on the device and streams the results.

    PARAMS
    -----------
    apisession: mistapi.APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_interfaces : dict[str, dict[str, str | None]]
        Device IDs mapped to port IDs and their optional tcpdump expressions.
        ex: {"ge-0/0/0": {"tcpdump_expression": "udp port 67 or udp port 68 -vvv -tttt -en"}}
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
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    LOGGER.debug(
        "Initiating remote pcap for device interfaces %s with timeout %s",
        device_interfaces,
        timeout,
    )
    body = _build_pcap_body(
        device_interfaces,
        "gateways",
        "gateway",
        tcpdump_expression,
        duration,
        max_pkt_len,
        num_packets,
    )
    util_response = UtilResponse()
    return WebSocketWrapper(
        apisession, util_response, timeout=timeout, on_message=on_message
    ).start_with_trigger(
        trigger_fn=lambda: site_pcaps.startSitePacketCapture(
            apisession, site_id=site_id, body=body
        ),
        ws_factory_fn=lambda _trigger: SitePcapEvents(apisession, site_id=site_id),
    )


def ssr_remote_pcap(
    apisession: _APISession,
    site_id: str,
    device_interfaces: dict[str, dict[str, str | None]],
    tcpdump_expression: str | None = None,
    duration: int = 600,
    max_pkt_len: int = 512,
    num_packets: int = 1024,
    timeout=10,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICE: SSR

    Initiates a remote pcap command on the device and streams the results.

    PARAMS
    -----------
    apisession: mistapi.APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_interfaces : dict[str, dict[str, str | None]]
        Device IDs mapped to port IDs and their optional tcpdump expressions.
        ex: {"ge-0/0/0": {"tcpdump_expression": "udp port 67 or udp port 68 -vvv -tttt -en"}}
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
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    LOGGER.debug(
        "Initiating remote pcap for device interfaces %s with timeout %s",
        device_interfaces,
        timeout,
    )
    body = _build_pcap_body(
        device_interfaces,
        "gateways",
        "gateway",
        tcpdump_expression,
        duration,
        max_pkt_len,
        num_packets,
        raw=False,
    )
    util_response = UtilResponse()
    return WebSocketWrapper(
        apisession, util_response, timeout=timeout, on_message=on_message
    ).start_with_trigger(
        trigger_fn=lambda: site_pcaps.startSitePacketCapture(
            apisession, site_id=site_id, body=body
        ),
        ws_factory_fn=lambda _trigger: SitePcapEvents(apisession, site_id=site_id),
    )


def ex_remote_pcap(
    apisession: _APISession,
    site_id: str,
    device_interfaces: dict[str, dict[str, str | None]],
    tcpdump_expression: str | None = None,
    duration: int = 600,
    max_pkt_len: int = 512,
    num_packets: int = 1024,
    timeout=10,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICE: EX

    Initiates a remote pcap command on the device and streams the results.

    PARAMS
    -----------
    apisession: mistapi.APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_interfaces : dict[str, dict[str, str | None]]
        Device IDs mapped to port IDs and their optional tcpdump expressions.
        ex: {"ge-0/0/0": {"tcpdump_expression": "udp port 67 or udp port 68 -vvv -tttt -en"}}
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
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    LOGGER.debug(
        "Initiating remote pcap for device interfaces %s with timeout %s",
        device_interfaces,
        timeout,
    )
    body = _build_pcap_body(
        device_interfaces,
        "switches",
        "switch",
        tcpdump_expression,
        duration,
        max_pkt_len,
        num_packets,
    )
    util_response = UtilResponse()
    return WebSocketWrapper(
        apisession, util_response, timeout=timeout, on_message=on_message
    ).start_with_trigger(
        trigger_fn=lambda: site_pcaps.startSitePacketCapture(
            apisession, site_id=site_id, body=body
        ),
        ws_factory_fn=lambda _trigger: SitePcapEvents(apisession, site_id=site_id),
    )


def site_mxedge_remote_pcap(
    apisession: _APISession,
    site_id: str,
    device_interfaces: dict[str, dict[str, str | None]],
    tcpdump_expression: str | None = None,
    duration: int = 600,
    max_pkt_len: int = 512,
    num_packets: int = 1024,
    timeout=10,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICE: Mist Edge

    Initiates a remote pcap command on the device and streams the results.

    PARAMS
    -----------
    apisession: mistapi.APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_interfaces : dict[str, dict[str, str | None]]
        Device IDs mapped to port IDs and their optional tcpdump expressions.
        ex: {"port0": {"tcpdump_expression": "udp port 67 or udp port 68 -vvv -tttt -en"}, "oobm": {}}
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
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    LOGGER.debug(
        "Initiating site remote pcap for Mist Edge interfaces %s",
        device_interfaces,
    )
    body = _build_mxedge_pcap_body(
        device_interfaces,
        tcpdump_expression,
        duration,
        max_pkt_len,
        num_packets,
    )
    util_response = UtilResponse()
    return WebSocketWrapper(
        apisession, util_response, timeout=timeout, on_message=on_message
    ).start_with_trigger(
        trigger_fn=lambda: site_pcaps.startSitePacketCapture(
            apisession, site_id=site_id, body=body
        ),
        ws_factory_fn=lambda _trigger: SitePcapEvents(apisession, site_id=site_id),
    )


def org_mxedge_remote_pcap(
    apisession: _APISession,
    org_id: str,
    device_interfaces: dict[str, dict[str, str | None]],
    tcpdump_expression: str | None = None,
    duration: int = 600,
    max_pkt_len: int = 512,
    num_packets: int = 1024,
    timeout=10,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICE: Mist Edge

    Initiates a remote pcap command on the device and streams the results.

    PARAMS
    -----------
    apisession: mistapi.APISession
        The API session to use for the request.
    org_id : str
        UUID of the organization where the device is located.
    device_interfaces : dict[str, dict[str, str | None]]
        Device IDs mapped to port IDs and their optional tcpdump expressions.
        ex: {"port0": {"tcpdump_expression": "udp port 67 or udp port 68 -vvv -tttt -en"}, "oobm": {}}
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
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    LOGGER.debug(
        "Initiating org remote pcap for Mist Edge interfaces %s",
        device_interfaces,
    )
    body = _build_mxedge_pcap_body(
        device_interfaces,
        tcpdump_expression,
        duration,
        max_pkt_len,
        num_packets,
    )
    util_response = UtilResponse()
    return WebSocketWrapper(
        apisession, util_response, timeout=timeout, on_message=on_message
    ).start_with_trigger(
        trigger_fn=lambda: org_pcaps.startOrgPacketCapture(
            apisession, org_id=org_id, body=body
        ),
        ws_factory_fn=lambda _trigger: OrgPcapEvents(apisession, org_id=org_id),
    )
