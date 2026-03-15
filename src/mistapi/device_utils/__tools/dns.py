"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
"""

from enum import Enum


class Node(Enum):
    """Node Enum for specifying node information in DNS commands."""

    NODE0 = "node0"
    NODE1 = "node1"


## NO DATA
# def test_resolution(
#     apissession: _APISession,
#     site_id: str,
#     device_id: str,
#     node: Node | None = None,
#     hostname: str | None = None,
#     timeout=5,
#     on_message: Callable[[dict], None] | None = None,
# ) -> UtilResponse:
#     """
#     DEVICES: SSR

#     Initiates a DNS resolution command on the gateway and streams the results.

#     PARAMS
#     -----------
#     apissession : _APISession
#         The API session to use for the request.
#     site_id : str
#         UUID of the site where the gateway is located.
#     device_id : str
#         UUID of the gateway to perform the DNS resolution command on.
#     node : Node, optional
#         Node information for the DNS resolution command.
#     hostname : str, optional
#         Hostname to resolve.
#     timeout : int, optional
#         Timeout for the command in seconds.
#     on_message : Callable, optional
#         Callback invoked with each extracted raw message as it arrives.

#     RETURNS
#     -----------
#     UtilResponse
#         A UtilResponse object containing the API response and a list of raw messages received
#         from the WebSocket stream.
#     """
#     body: dict[str, str | list | int] = {}
#     if node:
#         body["node"] = node.value
#     if hostname:
#         body["hostname"] = hostname
#     trigger = devices.testSiteSsrDnsResolution(
#         apissession,
#         site_id=site_id,
#         device_id=device_id,
#         body=body,
#     )
#     util_response = UtilResponse(trigger)
#     if trigger.status_code == 200:
#         LOGGER.info(trigger.data)
#         print(f"SSR DNS resolution command triggered for device {device_id}")
#         ws = DeviceCmdEvents(apissession, site_id=site_id, device_ids=[device_id])
#         util_response = await WebSocketWrapper(
#             apissession, util_response, timeout=timeout, on_message=on_message
#         ).start(ws)
#     else:
#         LOGGER.error(
#             f"Failed to trigger SSR DNS resolution command: {trigger.status_code} - {trigger.data}"
#         )  # Give the SSR DNS resolution command a moment to take effect
#     return util_response
