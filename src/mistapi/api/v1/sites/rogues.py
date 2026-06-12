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


def countSiteRogueEvents(
    mist_session: _APISession,
    site_id: str,
    distinct: str | None = None,
    type: str | None = None,
    ssid: str | None = None,
    bssid: str | None = None,
    ap_mac: str | None = None,
    channel: str | None = None,
    seen_on_lan: bool | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/rogues/count-site-rogue-events

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    distinct : str{'ap', 'bssid', 'ssid', 'type'}, default: bssid
      Field used to group this count response. enum: `ap`, `bssid`, `ssid`, `type`
    type : str{'honeypot', 'lan', 'others', 'spoof'}
      Rogue classification used to filter the results. enum: `honeypot`, `lan`, `others`, `spoof`
    ssid : str
      Filter results by SSID
    bssid : str
      Filter results by BSSID
    ap_mac : str
      MAC of the device that had strongest signal strength for ssid/bssid pair
    channel : str
      Filter results by channel
    seen_on_lan : bool
      Whether the reporting AP see a wireless client (on LAN) connecting to it
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    duration : str, default: 1d
      Time range duration for the query, using relative units such as `10m`, `7d`, or `2w`
    limit : int, default: 100
      Maximum number of results to return per page

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/rogues/events/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if type:
        query_params["type"] = str(type)
    if ssid:
        query_params["ssid"] = str(ssid)
    if bssid:
        query_params["bssid"] = str(bssid)
    if ap_mac:
        query_params["ap_mac"] = str(ap_mac)
    if channel:
        query_params["channel"] = str(channel)
    if seen_on_lan:
        query_params["seen_on_lan"] = str(seen_on_lan)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if duration:
        query_params["duration"] = str(duration)
    if limit:
        query_params["limit"] = str(limit)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def searchSiteRogueEvents(
    mist_session: _APISession,
    site_id: str,
    type: str | None = None,
    ssid: str | None = None,
    bssid: str | None = None,
    ap_mac: str | None = None,
    channel: int | None = None,
    seen_on_lan: bool | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/rogues/search-site-rogue-events

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    type : str{'honeypot', 'lan', 'others', 'spoof'}
      Rogue classification used to filter the results. enum: `honeypot`, `lan`, `others`, `spoof`
    ssid : str
      Filter results by SSID
    bssid : str
      Filter results by BSSID
    ap_mac : str
      MAC of the device that had strongest signal strength for ssid/bssid pair
    channel : int
      Filter results by channel
    seen_on_lan : bool
      Whether the reporting AP see a wireless client (on LAN) connecting to it
    limit : int, default: 100
      Maximum number of results to return per page
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    duration : str, default: 1d
      Time range duration for the query, using relative units such as `10m`, `7d`, or `2w`
    sort : str, default: timestamp
      On which field the list should be sorted, -prefix represents DESC order
    search_after : str
      Pagination cursor for retrieving subsequent pages of results. This value is automatically populated by Mist in the `next` URL from the previous response and should not be manually constructed.

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/rogues/events/search"
    query_params: dict[str, str] = {}
    if type:
        query_params["type"] = str(type)
    if ssid:
        query_params["ssid"] = str(ssid)
    if bssid:
        query_params["bssid"] = str(bssid)
    if ap_mac:
        query_params["ap_mac"] = str(ap_mac)
    if channel:
        query_params["channel"] = str(channel)
    if seen_on_lan:
        query_params["seen_on_lan"] = str(seen_on_lan)
    if limit:
        query_params["limit"] = str(limit)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if duration:
        query_params["duration"] = str(duration)
    if sort:
        query_params["sort"] = str(sort)
    if search_after:
        query_params["search_after"] = str(search_after)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def getSiteRogueAP(
    mist_session: _APISession, site_id: str, rogue_bssid: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/rogues/get-site-rogue-a-p

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    rogue_bssid : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/rogues/{rogue_bssid}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def deauthSiteWirelessClientsConnectedToARogue(
    mist_session: _APISession, site_id: str, rogue_bssid: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/wi-fi/deauth-site-wireless-clients-connected-to-a-rogue

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    rogue_bssid : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/rogues/{rogue_bssid}/deauth_clients"
    resp = mist_session.mist_post(uri=uri)
    return resp
