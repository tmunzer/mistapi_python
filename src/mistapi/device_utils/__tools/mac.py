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
    # timeout=30,
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
    # AP is returning RAW data
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
        #     apissession, util_response, timeout=timeout, on_message=on_message
        # ).start(ws)
    else:
        LOGGER.error(
            f"Failed to trigger clear MAC Table command: {trigger.status_code} - {trigger.data}"
        )  # Give the clear MAC Table command a moment to take effect
    return util_response


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
    # AP is returning RAW data
    # SWITCH is returning ???
    # GATEWAY is returning JSON
    body: dict[str, str | list | int] = {}
    if mac_address:
        body["mac_address"] = mac_address
    if port_id:
        body["port_id"] = port_id
    if vlan_id:
        body["vlan_id"] = vlan_id
    trigger = devices.showSiteDeviceMacTable(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"Show MAC Table command triggered for device {device_id}")
        ws = DeviceCmdEvents(apissession, site_id=site_id, device_ids=[device_id])
        util_response = WebSocketWrapper(
            apissession, util_response, timeout=timeout, on_message=on_message
        ).start(ws)
    else:
        LOGGER.error(
            f"Failed to trigger show MAC Table command: {trigger.status_code} - {trigger.data}"
        )  # Give the show ARP command a moment to take effect
    return util_response


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
