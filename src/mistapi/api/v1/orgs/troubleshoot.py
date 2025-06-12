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


def troubleshootOrg(
    mist_session: _APISession,
    org_id: str,
    mac: str | None = None,
    site_id: str | None = None,
    start: int | None = None,
    end: int | None = None,
    type: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/marvis/troubleshoot-org

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    mac : str
    site_id : str
    start : int
    end : int
    type : str{'wan', 'wired', 'wireless'}
      When troubleshooting site, type of network to troubleshoot

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/troubleshoot"
    query_params: dict[str, str] = {}
    if mac:
        query_params["mac"] = str(mac)
    if site_id:
        query_params["site_id"] = str(site_id)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if type:
        query_params["type"] = str(type)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
