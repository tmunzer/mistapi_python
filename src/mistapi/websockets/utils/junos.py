from mistapi import APISession as _APISession
from mistapi.__logger import logger as LOGGER
from mistapi.api.v1.sites import devices
from mistapi.websockets.utils.__ws_wrapper import UtilResponse, WebSocketWrapper


# TODO
async def monitor_traffic(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    port_id: str | None = None,
    timeout=30,
) -> UtilResponse:
    """
    For EX and SRX Only. Initiates a monitor traffic command on the device and streams the results.

    * if `port_id` is provided, JUNOS uses cmd "monitor interface" to monitor traffic on particular
    * if `port_id` is not provided, JUNOS uses cmd "monitor interface traffic" to monitor traffic on all ports

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to monitor traffic on.
    port_id : str, optional
        Port ID to filter the traffic.
    timeout : int, optional
        Timeout for the monitor traffic command in seconds.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received from the WebSocket stream.
    """
    body: dict[str, str | int] = {"duration": 60}
    if port_id:
        body["port"] = port_id
    trigger = devices.monitorSiteDeviceTraffic(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"Monitor traffic command triggered for device {device_id}")
        util_response = await WebSocketWrapper(
            apissession, util_response, timeout=timeout
        ).startSessionUrl(trigger.data.get("url", ""))
    else:
        LOGGER.error(
            f"Failed to trigger monitor traffic command: {trigger.status_code} - {trigger.data}"
        )  # Give the monitor traffic command a moment to take effect
    return util_response


async def clear_policy_hit_count(
    apissession: _APISession,
    site_id: str,
    device_id: str,
    policy_name: str,
    timeout=30,
) -> UtilResponse:
    """
    For EX and SRX Only. Clears the policy hit count on the device.

    PARAMS
    -----------
    apissession : _APISession
        The API session to use for the request.
    site_id : str
        UUID of the site where the device is located.
    device_id : str
        UUID of the device to clear the policy hit count on.
    policy_name : str
        Name of the policy to clear the hit count for.
    timeout : int, optional
        Timeout for the clear policy hit count command in seconds.

    RETURNS
    -----------
    UtilResponse
        A UtilResponse object containing the API response and a list of raw messages received from the WebSocket stream.
    """
    body: dict[str, str] = {}
    if policy_name:
        body["policy_name"] = policy_name
    trigger = devices.clearSiteDevicePolicyHitCount(
        apissession,
        site_id=site_id,
        device_id=device_id,
        body=body,
    )
    util_response = UtilResponse(trigger)
    if trigger.status_code == 200:
        LOGGER.info(trigger.data)
        print(f"Clear policy hit count command triggered for device {device_id}")
        util_response = await WebSocketWrapper(
            apissession, util_response, timeout=timeout
        ).startCmdEvents(site_id, device_id)
    else:
        LOGGER.error(
            f"Failed to trigger clear policy hit count command: {trigger.status_code} - {trigger.data}"
        )  # Give the clear policy hit count command a moment to take effect
    return util_response
