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
from mistapi.device_utils.__tools.__ws_wrapper import UtilResponse, WebSocketWrapper
from mistapi.websockets.sites import DeviceCmdEvents


def clear_mac_table(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    mac_address: str | None = None,
    port_id: str | None = None,
    vlan_id: str | None = None,
) -> UtilResponse:
    """
    DEVICES: EX

    Clears the MAC table on a switch (EX).

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
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    LOGGER.debug(
        "Initiating clear MAC table command for device %s with MAC address filter %s, "
        "port filter %s, and VLAN filter %s",
        device_id,
        mac_address,
        port_id,
        vlan_id,
    )
    body: dict[str, str | list | int] = {}
    if mac_address:
        body["mac_address"] = mac_address
    if port_id:
        body["port_id"] = port_id
    if vlan_id:
        body["vlan_id"] = vlan_id
    util_response = UtilResponse()
    return WebSocketWrapper(apissession, util_response).start_with_trigger(
        trigger_fn=lambda: devices.clearSiteDeviceMacTable(
            apissession, site_id=site_id, device_id=device_id, body=body
        ),
    )


def retrieve_mac_table(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    mac_address: str | None = None,
    port_id: str | None = None,
    vlan_id: str | None = None,
    timeout=5,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICES: EX

    Retrieves the MAC Table table from a switch (EX) and streams the results.

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to retrieve the ARP table from.
    mac_address : str, optional
        MAC address to filter the ARP table retrieval.
    port_id : str, optional
        Port ID to filter the ARP table retrieval.
    vlan_id : str, optional
        VLAN ID to filter the ARP table retrieval.
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
        "Initiating MAC table retrieval for device %s with MAC address filter %s, port filter %s, "
        "VLAN filter %s, and timeout %s",
        device_id,
        mac_address,
        port_id,
        vlan_id,
        timeout,
    )
    body: dict[str, str | list | int] = {}
    if mac_address:
        body["mac_address"] = mac_address
    if port_id:
        body["port_id"] = port_id
    if vlan_id:
        body["vlan_id"] = vlan_id
    util_response = UtilResponse()
    return WebSocketWrapper(
        apissession, util_response, timeout=timeout, on_message=on_message
    ).start_with_trigger(
        trigger_fn=lambda: devices.showSiteDeviceMacTable(
            apissession, site_id=site_id, device_id=device_id, body=body
        ),
        ws_factory_fn=lambda _trigger: DeviceCmdEvents(
            apissession, site_id=site_id, device_ids=[device_id]
        ),
    )


def clear_learned_mac(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    port_ids: list[str],
) -> UtilResponse:
    """
    DEVICES: EX

    Clears learned MAC addresses on the specified ports of a switch (EX).

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
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    LOGGER.debug(
        "Initiating clear learned MACs command for device %s on ports %s",
        device_id,
        port_ids,
    )
    body: dict[str, str | list | int] = {"ports": port_ids}
    util_response = UtilResponse()
    return WebSocketWrapper(apissession, util_response).start_with_trigger(
        trigger_fn=lambda: devices.clearAllLearnedMacsFromPortOnSwitch(
            apissession, site_id=site_id, device_id=device_id, body=body
        ),
    )
