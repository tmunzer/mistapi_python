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

def listOrgWxRules(mist_session:_APISession, org_id:str, limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgWxRules
    
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
    uri = f"/api/v1/orgs/{org_id}/wxrules"
    query_params={}
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgWxRule(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgWxRule
    
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
    uri = f"/api/v1/orgs/{org_id}/wxrules"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgWxRule(mist_session:_APISession, org_id:str, wxrule_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgWxRule
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    wxrule_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/wxrules/{wxrule_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgWxRule(mist_session:_APISession, org_id:str, wxrule_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgWxRule
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    wxrule_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/wxrules/{wxrule_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgWxRule(mist_session:_APISession, org_id:str, wxrule_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgWxRule
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    wxrule_id : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/wxrules/{wxrule_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    