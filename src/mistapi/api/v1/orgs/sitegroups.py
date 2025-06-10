'''
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
'''

from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse
import deprecation

def listOrgSiteGroups(mist_session:_APISession, org_id:str, limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/sitegroups/list-org-site-groups

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    limit : int, default: 100
    page : int, default: 1

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/sitegroups"
    query_params:dict[str, str]={}
    if limit:
        query_params["limit"]=str(limit)
    if page:
        query_params["page"]=str(page)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp

def createOrgSiteGroup(mist_session:_APISession, org_id:str, body:dict) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/sitegroups/create-org-site-group

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
    uri = f"/api/v1/orgs/{org_id}/sitegroups"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp

def getOrgSiteGroup(mist_session:_APISession, org_id:str, sitegroup_id:str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/sitegroups/get-org-site-group

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    sitegroup_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/sitegroups/{sitegroup_id}"
    query_params:dict[str, str]={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp

def deleteOrgSiteGroup(mist_session:_APISession, org_id:str, sitegroup_id:str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/sitegroups/delete-org-site-group

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    sitegroup_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/sitegroups/{sitegroup_id}"
    query_params:dict[str, str]={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp

def updateOrgSiteGroup(mist_session:_APISession, org_id:str, sitegroup_id:str, body:dict) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/sitegroups/update-org-site-group

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    sitegroup_id : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/sitegroups/{sitegroup_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
