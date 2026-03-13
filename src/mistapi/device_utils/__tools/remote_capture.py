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
from mistapi.api.v1.sites import pcaps
from mistapi.device_utils.__tools.__ws_wrapper import UtilResponse, WebSocketWrapper
from mistapi.websockets.sites import PcapEvents


def _build_pcap_body(
    device_id: str,
    port_ids: list[str],
    device_key: str,
    device_type: str,
    tcpdump_expression: str | None,
    duration: int,
    max_pkt_len: int,
    num_packets: int,
    raw: bool | None = None,
) -> dict:
    """Build the request body for remote pcap commands (SRX, SSR, EX)."""
    mac = device_id.split("-")[-1]
    body: dict = {
        "duration": duration,
        "max_pkt_len": max_pkt_len,
        "num_packets": num_packets,
        device_key: {mac: {"ports": {}}},
        "type": device_type,
        "format": "stream",
    }
    if raw is not None:
        body["raw"] = raw
    for port_id in port_ids:
        port_entry: dict = {}
        if tcpdump_expression is not None:
            port_entry["tcpdump_expression"] = tcpdump_expression
        body[device_key][mac]["ports"][port_id] = port_entry
    if tcpdump_expression:
        body["tcpdump_expression"] = tcpdump_expression
    return body


def ap_remote_pcap_wireless(
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
    on_message: Callable[[dict], None] | None = None,
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
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

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
        ws = PcapEvents(apissession, site_id=site_id)
        util_response = WebSocketWrapper(
            apissession, util_response, timeout=timeout, on_message=on_message
        ).start(ws)
    else:
        LOGGER.error(
            f"Failed to trigger remote pcap command: {trigger.status_code} - {trigger.data}"
        )  # Give the remote pcap command a moment to take effect
    return util_response


def ap_remote_pcap_wired(
    apissession: _APISession,
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
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

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
        ws = PcapEvents(apissession, site_id=site_id)
        util_response = WebSocketWrapper(
            apissession, util_response, timeout=timeout, on_message=on_message
        ).start(ws)
    else:
        LOGGER.error(
            f"Failed to trigger remote pcap command: {trigger.status_code} - {trigger.data}"
        )  # Give the remote pcap command a moment to take effect
    return util_response


def srx_remote_pcap(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    port_ids: list[str],
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
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    body = _build_pcap_body(
        device_id,
        port_ids,
        "gateways",
        "gateway",
        tcpdump_expression,
        duration,
        max_pkt_len,
        num_packets,
    )
    trigger = pcaps.startSitePacketCapture(
        apissession,
        site_id=site_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"Remote pcap command triggered for device {device_id}")
        ws = PcapEvents(apissession, site_id=site_id)
        util_response = WebSocketWrapper(
            apissession, util_response, timeout=timeout, on_message=on_message
        ).start(ws)
    else:
        LOGGER.error(
            f"Failed to trigger remote pcap command: {trigger.status_code} - {trigger.data}"
        )  # Give the remote pcap command a moment to take effect
    return util_response


def ssr_remote_pcap(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    port_ids: list[str],
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
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    body = _build_pcap_body(
        device_id,
        port_ids,
        "gateways",
        "gateway",
        tcpdump_expression,
        duration,
        max_pkt_len,
        num_packets,
        raw=False,
    )
    trigger = pcaps.startSitePacketCapture(
        apissession,
        site_id=site_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"Remote pcap command triggered for device {device_id}")
        ws = PcapEvents(apissession, site_id=site_id)
        util_response = WebSocketWrapper(
            apissession, util_response, timeout=timeout, on_message=on_message
        ).start(ws)
    else:
        LOGGER.error(
            f"Failed to trigger remote pcap command: {trigger.status_code} - {trigger.data}"
        )  # Give the remote pcap command a moment to take effect
    return util_response


def ex_remote_pcap(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    port_ids: list[str],
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
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    body = _build_pcap_body(
        device_id,
        port_ids,
        "switches",
        "switch",
        tcpdump_expression,
        duration,
        max_pkt_len,
        num_packets,
    )
    trigger = pcaps.startSitePacketCapture(
        apissession,
        site_id=site_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"Remote pcap command triggered for device {device_id}")
        ws = PcapEvents(apissession, site_id=site_id)
        util_response = WebSocketWrapper(
            apissession, util_response, timeout=timeout, on_message=on_message
        ).start(ws)
    else:
        LOGGER.error(
            f"Failed to trigger remote pcap command: {trigger.status_code} - {trigger.data}"
        )  # Give the remote pcap command a moment to take effect
    return util_response
