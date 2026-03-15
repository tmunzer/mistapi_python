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
from mistapi.api.v1.sites import devices
from mistapi.device_utils.__tools.__common import Node
from mistapi.device_utils.__tools.__ws_wrapper import UtilResponse, WebSocketWrapper
from mistapi.websockets.sites import DeviceCmdEvents


def retrieve_ap_arp_table(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    node: Node | None = None,
    timeout=1,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICES: AP

    Retrieves the ARP table from a Mist Access Point and streams the results.

    PARAMS
    -----------
    apisession: mistapi.APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to retrieve the ARP table from.
    node : Node, optional
        Node information for the ARP table retrieval command.
    timeout : int, optional
        Timeout for the ARP table retrieval command in seconds.
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    LOGGER.debug(
        "Initiating ARP table retrieval for device %s with node %s and timeout %s",
        device_id,
        node,
        timeout,
    )
    body: dict[str, str | list | int] = {}
    if node:
        body["node"] = node.value
    util_response = UtilResponse()
    return WebSocketWrapper(
        apissession, util_response, timeout=timeout, on_message=on_message
    ).start_with_trigger(
        trigger_fn=lambda: devices.arpFromDevice(
            apissession, site_id=site_id, device_id=device_id, body=body
        ),
        ws_factory_fn=lambda _trigger: DeviceCmdEvents(
            apissession, site_id=site_id, device_ids=[device_id]
        ),
    )


def retrieve_ssr_arp_table(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    node: Node | None = None,
    timeout=1,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICES: SSR

    Retrieves the ARP table from a SSR Gateway and streams the results.

    PARAMS
    -----------
    apisession: mistapi.APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to retrieve the ARP table from.
    node : Node, optional
        Node information for the ARP table retrieval command.
    timeout : int, optional
        Timeout for the ARP table retrieval command in seconds.
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received from
        the WebSocket stream.
    """
    LOGGER.debug(
        "Initiating SSR ARP table retrieval for device %s with node %s and timeout %s",
        device_id,
        node,
        timeout,
    )
    body: dict[str, str | list | int] = {}
    if node:
        body["node"] = node.value
    util_response = UtilResponse()
    return WebSocketWrapper(
        apissession, util_response, timeout=timeout, on_message=on_message
    ).start_with_trigger(
        trigger_fn=lambda: devices.arpFromDevice(
            apissession, site_id=site_id, device_id=device_id, body=body
        ),
        ws_factory_fn=lambda _trigger: DeviceCmdEvents(
            apissession, site_id=site_id, device_ids=[device_id]
        ),
    )


def retrieve_junos_arp_table(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    ip: str | None = None,
    port_id: str | None = None,
    vrf: str | None = None,
    timeout=1,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICES: EX, SRX

    Retrieve the ARP table from a Junos device (EX / SRX) with optional filters for IP, port,
    and VRF.

    PARAMS
    -----------
    apisession: mistapi.APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to retrieve the ARP table from.
    ip : str, optional
        IP address to filter the ARP table.
    port_id : str, optional
        Port ID to filter the ARP table.
    vrf : str, optional
        VRF to filter the ARP table.
    timeout : int, optional
        Timeout for the ARP table retrieval command in seconds.
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    LOGGER.debug(
        "Initiating Junos ARP table retrieval for device %s with IP filter %s, port filter %s, "
        "VRF filter %s, and timeout %s",
        device_id,
        ip,
        port_id,
        vrf,
        timeout,
    )
    body: dict[str, str | list | int] = {"duration": 1, "interval": 1}
    if ip:
        body["ip"] = ip
    if vrf:
        body["vrf"] = vrf
    if port_id:
        body["port_id"] = port_id
    util_response = UtilResponse()
    return WebSocketWrapper(
        apissession, util_response, timeout=timeout, on_message=on_message
    ).start_with_trigger(
        trigger_fn=lambda: devices.showSiteDeviceArpTable(
            apissession, site_id=site_id, device_id=device_id, body=body
        ),
        ws_factory_fn=lambda _trigger: DeviceCmdEvents(
            apissession, site_id=site_id, device_ids=[device_id]
        ),
    )
