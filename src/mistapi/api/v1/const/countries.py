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


def listCountryCodes(
    mist_session: _APISession, extend: bool | None = None
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/constants/definitions/list-country-codes

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    QUERY PARAMS
    ------------
    extend : bool

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = "/api/v1/const/countries"
    query_params: dict[str, str] = {}
    if extend:
        query_params["extend"] = str(extend)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
