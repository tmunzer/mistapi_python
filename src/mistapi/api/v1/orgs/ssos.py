'''
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
'''

from typing import Union, Awaitable
from mistapi import APISession as _APISession
from mistapi.__decorator import sync_async_compatible
from mistapi.__api_response import APIResponse as _APIResponse
import deprecation

@sync_async_compatible
def listOrgSsos(mist_session:_APISession, org_id:str, limit:int=100, page:int=1) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/sso/list-org-ssos
    
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
    uri = f"/api/v1/orgs/{org_id}/ssos"
    query_params={}
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def createOrgSso(mist_session:_APISession, org_id:str, body:object) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/sso/create-org-sso
    
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
    uri = f"/api/v1/orgs/{org_id}/ssos"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
@sync_async_compatible
def getOrgSso(mist_session:_APISession, org_id:str, sso_id:str) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/sso/get-org-sso
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    sso_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/ssos/{sso_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def deleteOrgSso(mist_session:_APISession, org_id:str, sso_id:str) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/sso/delete-org-sso
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    sso_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/ssos/{sso_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def updateOrgSso(mist_session:_APISession, org_id:str, sso_id:str, body:object) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/sso/update-org-sso
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    sso_id : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/ssos/{sso_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
@sync_async_compatible
def listOrgSsoLatestFailures(mist_session:_APISession, org_id:str, sso_id:str, start:int=None, end:int=None, duration:str="1d", limit:int=100, page:int=1) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/sso/list-org-sso-latest-failures
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    sso_id : str        
    
    QUERY PARAMS
    ------------
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100
    page : int, default: 1        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/ssos/{sso_id}/failures"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def getOrgSamlMetadata(mist_session:_APISession, org_id:str, sso_id:str) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/sso/get-org-saml-metadata
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    sso_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/ssos/{sso_id}/metadata"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def downloadOrgSamlMetadata(mist_session:_APISession, org_id:str, sso_id:str) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/sso/download-org-saml-metadata
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    sso_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/ssos/{sso_id}/metadata.xml"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    