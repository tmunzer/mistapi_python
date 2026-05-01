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


def searchSiteIotEndpoints(
    mist_session: _APISession,
    site_id: str,
    ap_mac: str | None = None,
    mac: str | None = None,
    type: str | None = None,
    mfg: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/iot-endpoints/search-site-iot-endpoints

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    ap_mac : str
    mac : str
    type : str
    mfg : str
    limit : int, default: 100
    start : str
    end : str
    duration : str, default: 1d

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/iotendpoints/search"
    query_params: dict[str, str] = {}
    if ap_mac:
        query_params["ap_mac"] = str(ap_mac)
    if mac:
        query_params["mac"] = str(mac)
    if type:
        query_params["type"] = str(type)
    if mfg:
        query_params["mfg"] = str(mfg)
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
