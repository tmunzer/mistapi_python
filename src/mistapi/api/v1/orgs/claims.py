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


def listOrgAsyncClaims(
    mist_session: _APISession, org_id: str, detail: bool | None = None
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/licenses/list-org-async-claims

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    detail : bool
      Whether to include per-device detail in each claim record

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/claims"
    query_params: dict[str, str] = {}
    if detail:
        query_params["detail"] = str(detail)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def createOrgAsyncClaim(
    mist_session: _APISession, org_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/licenses/create-org-async-claim

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/claims"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def getOrgAsyncClaimStatus(
    mist_session: _APISession, org_id: str, claim_id: str, detail: bool | None = None
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/licenses/get-org-async-claim-status

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    claim_id : str
      Unique identifier of the async claim job

    QUERY PARAMS
    ------------
    detail : bool
      Whether to include per-device detail in the claim status response

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/claims/{claim_id}"
    query_params: dict[str, str] = {}
    if detail:
        query_params["detail"] = str(detail)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
