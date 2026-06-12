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
      Filter results by MAC address
    peer_mac : str
      Filter results by peer MAC address
    port_id : str
      Port ID for the device
    peer_port_id : str
      Peer Port ID for the device
    policy : str
      Filter results by WAN path policy
    tenant : str
      Filter results by tenant network
    path_type : str
      Filter results by port path type
    distinct : str{'mac', 'path_type', 'peer_mac', 'peer_port_id', 'policy', 'port_id', 'tenant'}, default: policy
      Field used to group this count response. enum: `mac`, `path_type`, `peer_mac`, `peer_port_id`, `policy`, `port_id`, `tenant`
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
      Filter results by MAC address
    peer_mac : str
      Filter results by peer MAC address
    port_id : str
      Port ID for the device
    peer_port_id : str
      Peer Port ID for the device
    policy : str
      Filter results by WAN path policy
    tenant : str
      Filter results by tenant network
    path_type : str
      Filter results by port path type
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
