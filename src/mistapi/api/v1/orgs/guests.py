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


def listOrgGuestAuthorizations(mist_session: _APISession, org_id: str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/guests/list-org-guest-authorizations

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/guests"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def countOrgGuestAuthorizations(
    mist_session: _APISession,
    org_id: str,
    distinct: str = "auth_method",
    start: str | None = None,
    end: str | None = None,
    duration: str = "1d",
    limit: int = 100,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/guests/count-org-guest-authorizations

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str{'auth_method', 'company', 'ssid'}, default: auth_method
    start : str
    end : str
    duration : str, default: 1d
    limit : int, default: 100

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/guests/count"
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


def searchOrgGuestAuthorization(
    mist_session: _APISession,
    org_id: str,
    wlan_id: str | None = None,
    auth_method: str | None = None,
    ssid: str | None = None,
    limit: int = 100,
    start: str | None = None,
    end: str | None = None,
    duration: str = "1d",
    sort: str = "timestamp",
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/guests/search-org-guest-authorization

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    wlan_id : str
    auth_method : str
    ssid : str
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

    uri = f"/api/v1/orgs/{org_id}/guests/search"
    query_params: dict[str, str] = {}
    if wlan_id:
        query_params["wlan_id"] = str(wlan_id)
    if auth_method:
        query_params["auth_method"] = str(auth_method)
    if ssid:
        query_params["ssid"] = str(ssid)
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


def getOrgGuestAuthorization(
    mist_session: _APISession, org_id: str, guest_mac: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/guests/get-org-guest-authorization

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    guest_mac : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/guests/{guest_mac}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def deleteOrgGuestAuthorization(
    mist_session: _APISession, org_id: str, guest_mac: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/guests/delete-org-guest-authorization

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    guest_mac : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/guests/{guest_mac}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp


def updateOrgGuestAuthorization(
    mist_session: _APISession, org_id: str, guest_mac: str, body: dict
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/guests/update-org-guest-authorization

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    guest_mac : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/guests/{guest_mac}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
