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

def listOrgUserMacs(mist_session:_APISession, org_id:str, blacklisted:bool=None, for_guest_wifi:bool=None, cross_site:bool=None, site_id:str=None, page:int=1, limit:int=100) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgUserMacs
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    blacklisted : bool
    for_guest_wifi : bool
    cross_site : bool
    site_id : str
    page : int, default: 1
    limit : int, default: 100        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/usermacs"
    query_params={}
    if blacklisted: query_params["blacklisted"]=blacklisted
    if for_guest_wifi: query_params["for_guest_wifi"]=for_guest_wifi
    if cross_site: query_params["cross_site"]=cross_site
    if site_id: query_params["site_id"]=site_id
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgUserMacs(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgUserMacs
    
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
    uri = f"/api/v1/orgs/{org_id}/usermacs"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def importOrgUserMacsFile(mist_session:_APISession, org_id:str, file:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/importOrgUserMacs
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    BODY PARAMS
    -----------
    file : str
        path to the file to upload. file to updload
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    multipart_form_data = {
        "file":file,
    }
    uri = f"/api/v1/orgs/{org_id}/usermacs/import"
    resp = mist_session.mist_post_file(uri=uri, multipart_form_data=multipart_form_data)
    return resp

def importOrgUserMacs(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/importOrgUserMacs
    
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
    uri = f"/api/v1/orgs/{org_id}/usermacs/import"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def searchOrgUserMacs(mist_session:_APISession, org_id:str, mac:str=None, labels:list=None, page:int=1, limit:int=100) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchOrgUserMacs
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    mac : str
    labels : list
      optional, array of strings of labels
    page : int, default: 1
    limit : int, default: 100        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/usermacs/search"
    query_params={}
    if mac: query_params["mac"]=mac
    if labels: query_params["labels"]=labels
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getOrgUserMac(mist_session:_APISession, org_id:str, usermac_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgUserMac
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    usermac_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/usermacs/search/{usermac_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgUserMac(mist_session:_APISession, org_id:str, usermac_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgUserMac
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    usermac_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/usermacs/search/{usermac_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    