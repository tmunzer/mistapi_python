"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
"""

from collections.abc import Callable
from enum import Enum

from mistapi import APISession as _APISession
from mistapi.__logger import logger as LOGGER
from mistapi.api.v1.sites import devices
from mistapi.device_utils.__tools.__ws_wrapper import UtilResponse, WebSocketWrapper
from mistapi.websockets.sites import DeviceCmdEvents


class Node(Enum):
    """Node Enum for specifying node information in service path commands."""

    NODE0 = "node0"
    NODE1 = "node1"


def show_service_path(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    node: Node | None = None,
    service_name: str | None = None,
    timeout: int = 5,
    on_message: Callable[[dict], None] | None = None,
) -> UtilResponse:
    """
    DEVICES: SSR

    Initiates a show service path command on the gateway and streams the results.

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
    on_message : Callable, optional
        Callback invoked with each extracted raw message as it arrives.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
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
        ws = DeviceCmdEvents(apissession, site_id=site_id, device_ids=[device_id])
        util_response = WebSocketWrapper(
            apissession, util_response, timeout=timeout, on_message=on_message
        ).start(ws)
    else:
        LOGGER.error(
            f"Failed to trigger SSR service path command: {trigger.status_code} - {trigger.data}"
        )  # Give the SSR service path command a moment to take effect
    return util_response
