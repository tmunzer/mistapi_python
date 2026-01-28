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


def countSiteWanUsage(
    mist_session: _APISession,
    site_id: str,
    mac: str | None = None,
    peer_mac: str | None = None,
    port_id: str | None = None,
    peer_port_id: str | None = None,
    policy: str | None = None,
    tenant: str | None = None,
    path_type: str | None = None,
    distinct: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/wan-usages/count-site-wan-usage

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    mac : str
    peer_mac : str
    port_id : str
    peer_port_id : str
    policy : str
    tenant : str
    path_type : str
    distinct : str{'mac', 'path_type', 'peer_mac', 'peer_port_id', 'policy', 'port_id', 'tenant'}, default: policy
    start : str
    end : str
    duration : str, default: 1d
    limit : int, default: 100

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/wan_usages/count"
    query_params: dict[str, str] = {}
    if mac:
        query_params["mac"] = str(mac)
    if peer_mac:
        query_params["peer_mac"] = str(peer_mac)
    if port_id:
        query_params["port_id"] = str(port_id)
    if peer_port_id:
        query_params["peer_port_id"] = str(peer_port_id)
    if policy:
        query_params["policy"] = str(policy)
    if tenant:
        query_params["tenant"] = str(tenant)
    if path_type:
        query_params["path_type"] = str(path_type)
    if distinct:
        query_params["distinct"] = str(distinct)
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


def searchSiteWanUsage(
    mist_session: _APISession,
    site_id: str,
    mac: str | None = None,
    peer_mac: str | None = None,
    port_id: str | None = None,
    peer_port_id: str | None = None,
    policy: str | None = None,
    tenant: str | None = None,
    path_type: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/wan-usages/search-site-wan-usage

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    mac : str
    peer_mac : str
    port_id : str
    peer_port_id : str
    policy : str
    tenant : str
    path_type : str
    limit : int, default: 100
    start : str
    end : str
    duration : str, default: 1d
    sort : str, default: timestamp

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/wan_usages/search"
    query_params: dict[str, str] = {}
    if mac:
        query_params["mac"] = str(mac)
    if peer_mac:
        query_params["peer_mac"] = str(peer_mac)
    if port_id:
        query_params["port_id"] = str(port_id)
    if peer_port_id:
        query_params["peer_port_id"] = str(peer_port_id)
    if policy:
        query_params["policy"] = str(policy)
    if tenant:
        query_params["tenant"] = str(tenant)
    if path_type:
        query_params["path_type"] = str(path_type)
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
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
