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


def listApplications(
    mist_session: _APISession, device_type: str | None = None
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/constants/definitions/list-applications

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    QUERY PARAMS
    ------------
    device_type : str{'ap', 'gateway'}
      Optional. Filter to applications identifiable by a device family. When omitted, the full recognized list is returned. enum: `ap`, `gateway`

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = "/api/v1/const/applications"
    query_params: dict[str, str] = {}
    if device_type:
        query_params["device_type"] = str(device_type)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
