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
def listOrgWlans(mist_session:_APISession, org_id:str, limit:int=100, page:int=1) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/wlans/list-org-wlans
    
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
    uri = f"/api/v1/orgs/{org_id}/wlans"
    query_params={}
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def createOrgWlan(mist_session:_APISession, org_id:str, body:object) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/wlans/create-org-wlan
    
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
    uri = f"/api/v1/orgs/{org_id}/wlans"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
@sync_async_compatible
def getOrgWLAN(mist_session:_APISession, org_id:str, wlan_id:str) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/wlans/get-org-w-l-a-n
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    wlan_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/wlans/{wlan_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def deleteOrgWlan(mist_session:_APISession, org_id:str, wlan_id:str) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/wlans/delete-org-wlan
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    wlan_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/wlans/{wlan_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def updateOrgWlan(mist_session:_APISession, org_id:str, wlan_id:str, body:object) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/wlans/update-org-wlan
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    wlan_id : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/wlans/{wlan_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
@sync_async_compatible
def deleteOrgWlanPortalImage(mist_session:_APISession, org_id:str, wlan_id:str) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/wlans/delete-org-wlan-portal-image
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    wlan_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/wlans/{wlan_id}/portal_image"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def uploadOrgWlanPortalImageFile(mist_session:_APISession, org_id:str, wlan_id:str, file:str=None, json:str=None) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/wlans/upload-org-wlan-portal-image
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    wlan_id : str        
    
    BODY PARAMS
    -----------
    file : str
        path to the file to upload. Binary file
    json : str
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    multipart_form_data = {
        "file":file,
        "json":json,
    }
    uri = f"/api/v1/orgs/{org_id}/wlans/{wlan_id}/portal_image"
    resp = mist_session.mist_post_file(uri=uri, multipart_form_data=multipart_form_data)
    return resp

@sync_async_compatible
def updateOrgWlanPortalTemplate(mist_session:_APISession, org_id:str, wlan_id:str, body:object) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/wlans/update-org-wlan-portal-template
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    wlan_id : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/wlans/{wlan_id}/portal_template"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    