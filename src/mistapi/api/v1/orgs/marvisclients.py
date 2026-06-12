"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
"""

from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse


def countOrgMarvisClientEvents(
    mist_session: _APISession,
    org_id: str,
    distinct: str | None = None,
    type: str | None = None,
    device_id: str | None = None,
    wifi_mac: str | None = None,
    wifi_ip: str | None = None,
    hostname: str | None = None,
    ssid: str | None = None,
    bssid: str | None = None,
    channel: str | None = None,
    pre_bssid: str | None = None,
    pre_channel: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/marvis/count-org-marvis-client-events

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str, default: type
      Field to count by. enum: `type`, `device_id`, `wifi_mac`, `wifi_ip`, `hostname`, `ssid`, `bssid`, `channel`, `pre_bssid`, `pre_channel`
    type : str
      Filter by event type
    device_id : str
      Filter by Marvis Client installation device UUID
    wifi_mac : str
      Filter by device Wi-Fi MAC address
    wifi_ip : str
      Filter by device Wi-Fi IP address
    hostname : str
      Filter by device hostname
    ssid : str
      Filter by SSID involved in roam events
    bssid : str
      Filter by BSSID the client roamed to
    channel : str
      Filter by channel the client roamed to
    pre_bssid : str
      Filter by BSSID the client roamed from
    pre_channel : str
      Filter by channel the client roamed from
    limit : int, default: 100
      Maximum number of results to return per page
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    duration : str, default: 1d
      Time range duration for the query, using relative units such as `10m`, `7d`, or `2w`

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/marvisclients/events/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if type:
        query_params["type"] = str(type)
    if device_id:
        query_params["device_id"] = str(device_id)
    if wifi_mac:
        query_params["wifi_mac"] = str(wifi_mac)
    if wifi_ip:
        query_params["wifi_ip"] = str(wifi_ip)
    if hostname:
        query_params["hostname"] = str(hostname)
    if ssid:
        query_params["ssid"] = str(ssid)
    if bssid:
        query_params["bssid"] = str(bssid)
    if channel:
        query_params["channel"] = str(channel)
    if pre_bssid:
        query_params["pre_bssid"] = str(pre_bssid)
    if pre_channel:
        query_params["pre_channel"] = str(pre_channel)
    if limit:
        query_params["limit"] = str(limit)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if duration:
        query_params["duration"] = str(duration)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def searchOrgMarvisClientEvents(
    mist_session: _APISession,
    org_id: str,
    type: str | None = None,
    device_id: str | None = None,
    wifi_mac: str | None = None,
    wifi_ip: str | None = None,
    hostname: str | None = None,
    ssid: str | None = None,
    bssid: str | None = None,
    channel: str | None = None,
    pre_bssid: str | None = None,
    pre_channel: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/marvis/search-org-marvis-client-events

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    type : str
      Filter by event type
    device_id : str
      Filter by Marvis Client installation device UUID
    wifi_mac : str
      Filter by device Wi-Fi MAC address
    wifi_ip : str
      Filter by device Wi-Fi IP address
    hostname : str
      Filter by device hostname
    ssid : str
      Filter by SSID involved in roam events
    bssid : str
      Filter by BSSID the client roamed to
    channel : str
      Filter by channel the client roamed to
    pre_bssid : str
      Filter by BSSID the client roamed from
    pre_channel : str
      Filter by channel the client roamed from
    limit : int, default: 100
      Maximum number of results to return per page
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    duration : str, default: 1d
      Time range duration for the query, using relative units such as `10m`, `7d`, or `2w`

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/marvisclients/events/search"
    query_params: dict[str, str] = {}
    if type:
        query_params["type"] = str(type)
    if device_id:
        query_params["device_id"] = str(device_id)
    if wifi_mac:
        query_params["wifi_mac"] = str(wifi_mac)
    if wifi_ip:
        query_params["wifi_ip"] = str(wifi_ip)
    if hostname:
        query_params["hostname"] = str(hostname)
    if ssid:
        query_params["ssid"] = str(ssid)
    if bssid:
        query_params["bssid"] = str(bssid)
    if channel:
        query_params["channel"] = str(channel)
    if pre_bssid:
        query_params["pre_bssid"] = str(pre_bssid)
    if pre_channel:
        query_params["pre_channel"] = str(pre_channel)
    if limit:
        query_params["limit"] = str(limit)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if duration:
        query_params["duration"] = str(duration)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
