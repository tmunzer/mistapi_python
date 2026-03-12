"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
"""

from enum import Enum

from mistapi import APISession as _APISession
from mistapi.__logger import logger as LOGGER
from mistapi.api.v1.sites import devices
from mistapi.utils.__ws_wrapper import UtilResponse, WebSocketWrapper


class Node(Enum):
    """Node Enum for specifying node information in DNS commands."""

    NODE0 = "node0"
    NODE1 = "node1"


async def test_resolution(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    node: Node | None = None,
    hostname: str | None = None,
    timeout=5,
) -> UtilResponse:
    """
    DEVICES: SSR

    Initiates a DNS resolution command on the gateway and streams the results.

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the gateway is located.
    device_id : str
        UUID of the gateway to perform the DNS resolution command on.
    node : Node, optional
        Node information for the DNS resolution command.
    hostname : str, optional
        Hostname to resolve.
    timeout : int, optional
        Timeout for the command in seconds.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received
        from the WebSocket stream.
    """
    body: dict[str, str | list | int] = {}
    if node:
        body["node"] = node.value
    if hostname:
        body["hostname"] = hostname
    trigger = devices.testSiteSsrDnsResolution(
        apissession,
        site_id=site_id,
        device_id=device_id,
        # body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"SSR DNS resolution command triggered for device {device_id}")
        util_response = await WebSocketWrapper(
            apissession, util_response, timeout=timeout
        ).startCmdEvents(site_id, device_id)
    else:
        LOGGER.error(
            f"Failed to trigger SSR DNS resolution command: {trigger.status_code} - {trigger.data}"
        )  # Give the SSR DNS resolution command a moment to take effect
    return util_response
