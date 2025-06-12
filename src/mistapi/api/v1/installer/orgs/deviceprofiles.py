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


def listInstallerDeviceProfiles(
    mist_session: _APISession, org_id: str, type: str = "ap"
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/installer/list-installer-device-profiles

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    type : str{'ap', 'gateway', 'switch'}, default: ap

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/installer/orgs/{org_id}/deviceprofiles"
    query_params: dict[str, str] = {}
    if type:
        query_params["type"] = str(type)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
