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


def getOauthAuthorization(
    mist_session: _APISession,
    client_id: str,
    redirect_uri: str,
    response_type: str,
    state: str,
    code_challenge: str | None = None,
    code_challenge_method: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/oauth2/get-oauth-authorization

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    QUERY PARAMS
    ------------
    client_id : str
      Composite `<org_id>.<token_id>` of the API token (`oauth_client_id`)
    redirect_uri : str
      Must exactly match one of the registered `oauth_redirect_uris` of the API token, or be the loopback URL `http://127.0.0.1[:port]`
    response_type : str{'code'}
      Must be `code`. enum: `code`
    state : str
      Opaque value returned unchanged to the client
    code_challenge : str
      Required for a loopback redirect or when the client has `oauth_pkce_required` set. BASE64URL(SHA256(code_verifier))
    code_challenge_method : str{'S256'}
      Required with `code_challenge`. Must be `S256`. enum: `S256`

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = "/api/v1/orgs/oauth/authorize"
    query_params: dict[str, str] = {}
    if client_id:
        query_params["client_id"] = str(client_id)
    if redirect_uri:
        query_params["redirect_uri"] = str(redirect_uri)
    if response_type:
        query_params["response_type"] = str(response_type)
    if state:
        query_params["state"] = str(state)
    if code_challenge:
        query_params["code_challenge"] = str(code_challenge)
    if code_challenge_method:
        query_params["code_challenge_method"] = str(code_challenge_method)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def grantOauthAuthorization(
    mist_session: _APISession, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/oauth2/grant-oauth-authorization

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = "/api/v1/orgs/oauth/authorize"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def exchangeOauthToken(mist_session: _APISession, body: dict | list) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/oauth2/exchange-oauth-token

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = "/api/v1/orgs/oauth/token"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
