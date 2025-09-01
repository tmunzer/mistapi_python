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


def countSiteWanClients(
    mist_session: _APISession,
    site_id: str,
    distinct: str = "mac",
    start: int | None = None,
    end: int | None = None,
    duration: str = "1d",
    limit: int = 100,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/clients/wan/count-site-wan-clients

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    distinct : str{'hostname', 'ip', 'mac', 'mfg'}, default: mac
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/wan_clients/count"
    query_params: dict[str, str] = {}
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


def searchSiteWanClientEvents(
    mist_session: _APISession,
    site_id: str,
    type: str | None = None,
    mac: str | None = None,
    hostname: str | None = None,
    ip: str | None = None,
    mfg: str | None = None,
    nacrule_id: str | None = None,
    limit: int = 100,
    start: int | None = None,
    end: int | None = None,
    duration: str = "1d",
    sort: str = "timestamp",
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/clients/wan/search-site-wan-client-events

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
    mac : str
    hostname : str
    ip : str
    mfg : str
    nacrule_id : str
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d
    sort : str, default: timestamp

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/wan_clients/events/search"
    query_params: dict[str, str] = {}
    if type:
        query_params["type"] = str(type)
    if mac:
        query_params["mac"] = str(mac)
    if hostname:
        query_params["hostname"] = str(hostname)
    if ip:
        query_params["ip"] = str(ip)
    if mfg:
        query_params["mfg"] = str(mfg)
    if nacrule_id:
        query_params["nacrule_id"] = str(nacrule_id)
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


def searchSiteWanClients(
    mist_session: _APISession,
    site_id: str,
    mac: str | None = None,
    hostname: str | None = None,
    ip: str | None = None,
    mfg: str | None = None,
    limit: int = 100,
    page: int = 1,
    start: int | None = None,
    end: int | None = None,
    duration: str = "1d",
    sort: str = "timestamp",
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/clients/wan/search-site-wan-clients

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
    hostname : str
    ip : str
    mfg : str
    limit : int, default: 100
    page : int, default: 1
    start : int
    end : int
    duration : str, default: 1d
    sort : str, default: timestamp

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/wan_clients/search"
    query_params: dict[str, str] = {}
    if mac:
        query_params["mac"] = str(mac)
    if hostname:
        query_params["hostname"] = str(hostname)
    if ip:
        query_params["ip"] = str(ip)
    if mfg:
        query_params["mfg"] = str(mfg)
    if limit:
        query_params["limit"] = str(limit)
    if page:
        query_params["page"] = str(page)
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
