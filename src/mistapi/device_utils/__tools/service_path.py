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


def show_service_path(
    apisession: _APISession,
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
    apisession: mistapi.APISession
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
    LOGGER.debug(
        "Initiating show service path command for device %s with node %s, service name %s, "
        "and timeout %s",
        device_id,
        node,
        service_name,
        timeout,
    )
    body: dict[str, str | list | int] = {}
    if node:
        body["node"] = node.value
    if service_name:
        body["service_name"] = service_name
    util_response = UtilResponse()
    return WebSocketWrapper(
        apisession, util_response, timeout=timeout, on_message=on_message
    ).start_with_trigger(
        trigger_fn=lambda: devices.showSiteSsrServicePath(
            apisession, site_id=site_id, device_id=device_id, body=body
        ),
        ws_factory_fn=lambda _trigger: DeviceCmdEvents(
            apisession, site_id=site_id, device_ids=[device_id]
        ),
    )
