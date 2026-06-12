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


def listSiteServicesDerived(
    mist_session: _APISession, site_id: str, resolve: bool | None = None
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/services/list-site-services-derived

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    resolve : bool
      Whether resolve the site variables

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/services/derived"
    query_params: dict[str, str] = {}
    if resolve:
        query_params["resolve"] = str(resolve)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def countSiteServicePathEvents(
    mist_session: _APISession,
    site_id: str,
    distinct: str | None = None,
    type: str | None = None,
    text: str | None = None,
    vpn_name: str | None = None,
    vpn_path: str | None = None,
    policy: str | None = None,
    port_id: str | None = None,
    model: str | None = None,
    version: str | None = None,
    mac: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/services/count-site-service-path-events

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    distinct : str{'mac', 'model', 'policy', 'port_id', 'site_id', 'type', 'vpn_name', 'vpn_path'}, default: type
      Field used to group this count response. enum: `mac`, `model`, `policy`, `port_id`, `site_id`, `type`, `vpn_name`, `vpn_path`
    type : str
      Event type, e.g. GW_SERVICE_PATH_DOWN
    text : str
      Description of the event including the reason it is triggered
    vpn_name : str
      Filter results by vpn name
    vpn_path : str
      Filter results by vpn path
    policy : str
      Service policy associated with that specific path
    port_id : str
      Filter results by port identifier
    model : str
      Filter results by device model
    version : str
      Filter results by software version
    mac : str
      Filter results by MAC address
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

    uri = f"/api/v1/sites/{site_id}/services/events/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if type:
        query_params["type"] = str(type)
    if text:
        query_params["text"] = str(text)
    if vpn_name:
        query_params["vpn_name"] = str(vpn_name)
    if vpn_path:
        query_params["vpn_path"] = str(vpn_path)
    if policy:
        query_params["policy"] = str(policy)
    if port_id:
        query_params["port_id"] = str(port_id)
    if model:
        query_params["model"] = str(model)
    if version:
        query_params["version"] = str(version)
    if mac:
        query_params["mac"] = str(mac)
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


def searchSiteServicePathEvents(
    mist_session: _APISession,
    site_id: str,
    type: str | None = None,
    text: str | None = None,
    peer_port_id: str | None = None,
    peer_mac: str | None = None,
    vpn_name: str | None = None,
    vpn_path: str | None = None,
    policy: str | None = None,
    port_id: str | None = None,
    model: str | None = None,
    version: str | None = None,
    mac: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/services/search-site-service-path-events

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    type : str
      Event type, e.g. GW_SERVICE_PATH_DOWN
    text : str
      Description of the event including the reason it is triggered
    peer_port_id : str
      Port ID of the peer gateway
    peer_mac : str
      MAC address of the peer gateway
    vpn_name : str
      Filter results by vpn name
    vpn_path : str
      Filter results by vpn path
    policy : str
      Service policy associated with that specific path
    port_id : str
      Filter results by port identifier
    model : str
      Filter results by device model
    version : str
      Filter results by software version
    mac : str
      Filter results by MAC address
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

    uri = f"/api/v1/sites/{site_id}/services/events/search"
    query_params: dict[str, str] = {}
    if type:
        query_params["type"] = str(type)
    if text:
        query_params["text"] = str(text)
    if peer_port_id:
        query_params["peer_port_id"] = str(peer_port_id)
    if peer_mac:
        query_params["peer_mac"] = str(peer_mac)
    if vpn_name:
        query_params["vpn_name"] = str(vpn_name)
    if vpn_path:
        query_params["vpn_path"] = str(vpn_path)
    if policy:
        query_params["policy"] = str(policy)
    if port_id:
        query_params["port_id"] = str(port_id)
    if model:
        query_params["model"] = str(model)
    if version:
        query_params["version"] = str(version)
    if mac:
        query_params["mac"] = str(mac)
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
