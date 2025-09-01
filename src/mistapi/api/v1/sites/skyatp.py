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


def countSiteSkyatpEvents(
    mist_session: _APISession,
    site_id: str,
    distinct: str = "type",
    type: str | None = None,
    mac: str | None = None,
    device_mac: str | None = None,
    threat_level: int | None = None,
    ip_address: str | None = None,
    start: int | None = None,
    end: int | None = None,
    duration: str = "1d",
    limit: int = 100,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/skyatp/count-site-skyatp-events

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    distinct : str{'device_mac', 'mac', 'threat_level', 'type'}, default: type
    type : str
    mac : str
    device_mac : str
    threat_level : int
    ip_address : str
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/skyatp/events/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if type:
        query_params["type"] = str(type)
    if mac:
        query_params["mac"] = str(mac)
    if device_mac:
        query_params["device_mac"] = str(device_mac)
    if threat_level:
        query_params["threat_level"] = str(threat_level)
    if ip_address:
        query_params["ip_address"] = str(ip_address)
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


def searchSiteSkyatpEvents(
    mist_session: _APISession,
    site_id: str,
    type: str | None = None,
    mac: str | None = None,
    device_mac: str | None = None,
    threat_level: int | None = None,
    ip_address: str | None = None,
    limit: int = 100,
    start: int | None = None,
    end: int | None = None,
    duration: str = "1d",
    sort: str = "timestamp",
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/skyatp/search-site-skyatp-events

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
    device_mac : str
    threat_level : int
    ip_address : str
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

    uri = f"/api/v1/sites/{site_id}/skyatp/events/search"
    query_params: dict[str, str] = {}
    if type:
        query_params["type"] = str(type)
    if mac:
        query_params["mac"] = str(mac)
    if device_mac:
        query_params["device_mac"] = str(device_mac)
    if threat_level:
        query_params["threat_level"] = str(threat_level)
    if ip_address:
        query_params["ip_address"] = str(ip_address)
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
