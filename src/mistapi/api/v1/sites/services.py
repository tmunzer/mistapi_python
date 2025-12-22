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
    distinct: str = "type",
    type: str | None = None,
    text: str | None = None,
    vpn_name: str | None = None,
    vpn_path: str | None = None,
    policy: str | None = None,
    port_id: str | None = None,
    model: str | None = None,
    version: str | None = None,
    timestamp: float | None = None,
    mac: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str = "1d",
    limit: int = 100,
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
    type : str
    text : str
    vpn_name : str
    vpn_path : str
    policy : str
    port_id : str
    model : str
    version : str
    timestamp : float
    mac : str
    start : str
    end : str
    duration : str, default: 1d
    limit : int, default: 100

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
    if timestamp:
        query_params["timestamp"] = str(timestamp)
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
    timestamp: float | None = None,
    mac: str | None = None,
    limit: int = 100,
    start: str | None = None,
    end: str | None = None,
    duration: str = "1d",
    sort: str = "timestamp",
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
    text : str
    peer_port_id : str
    peer_mac : str
    vpn_name : str
    vpn_path : str
    policy : str
    port_id : str
    model : str
    version : str
    timestamp : float
    mac : str
    limit : int, default: 100
    start : str
    end : str
    duration : str, default: 1d
    sort : str, default: timestamp
    search_after : str

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
    if timestamp:
        query_params["timestamp"] = str(timestamp)
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
