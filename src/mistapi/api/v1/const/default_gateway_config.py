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


def getGatewayDefaultConfig(
    mist_session: _APISession, model: str, ha: str | None = None
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/constants/models/get-gateway-default-config

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    QUERY PARAMS
    ------------
    model : str
    ha : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = "/api/v1/const/default_gateway_config"
    query_params: dict[str, str] = {}
    if model:
        query_params["model"] = str(model)
    if ha:
        query_params["ha"] = str(ha)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
