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


def listMspOrgs(mist_session: _APISession, msp_id: str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/msps/orgs/list-msp-orgs

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    msp_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/msps/{msp_id}/orgs"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def createMspOrg(
    mist_session: _APISession, msp_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/msps/orgs/create-msp-org

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    msp_id : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/msps/{msp_id}/orgs"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def manageMspOrgs(mist_session: _APISession, msp_id: str, body: dict) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/msps/orgs/manage-msp-orgs

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    msp_id : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/msps/{msp_id}/orgs"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp


def searchMspOrgs(
    mist_session: _APISession,
    msp_id: str,
    name: str | None = None,
    org_id: str | None = None,
    sub_insufficient: bool | None = None,
    trial_enabled: bool | None = None,
    usage_types: list | None = None,
    limit: int = 100,
    sort: str = "timestamp",
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/msps/orgs/search-msp-orgs

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    msp_id : str

    QUERY PARAMS
    ------------
    name : str
    org_id : str
    sub_insufficient : bool
    trial_enabled : bool
    usage_types : list
      List of types that enabled by usage
    limit : int, default: 100
    sort : str, default: timestamp

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/msps/{msp_id}/orgs/search"
    query_params: dict[str, str] = {}
    if name:
        query_params["name"] = str(name)
    if org_id:
        query_params["org_id"] = str(org_id)
    if sub_insufficient:
        query_params["sub_insufficient"] = str(sub_insufficient)
    if trial_enabled:
        query_params["trial_enabled"] = str(trial_enabled)
    if usage_types:
        query_params["usage_types"] = str(usage_types)
    if limit:
        query_params["limit"] = str(limit)
    if sort:
        query_params["sort"] = str(sort)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def getMspOrg(mist_session: _APISession, msp_id: str, org_id: str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/msps/orgs/get-msp-org

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    msp_id : str
    org_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/msps/{msp_id}/orgs/{org_id}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def deleteMspOrg(mist_session: _APISession, msp_id: str, org_id: str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/msps/orgs/delete-msp-org

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    msp_id : str
    org_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/msps/{msp_id}/orgs/{org_id}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp


def updateMspOrg(
    mist_session: _APISession, msp_id: str, org_id: str, body: dict
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/msps/orgs/update-msp-org

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    msp_id : str
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

    uri = f"/api/v1/msps/{msp_id}/orgs/{org_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
