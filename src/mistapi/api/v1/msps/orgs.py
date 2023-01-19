from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse

def getMspOrgs(mist_session:_APISession, msp_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getMspOrgs
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    """
    uri = f"/api/v1/msps/{msp_id}/orgs"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createMspOrg(mist_session:_APISession, msp_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createMspOrg
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    """
    uri = f"/api/v1/msps/{msp_id}/orgs"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def manageMspOrgs(mist_session:_APISession, msp_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/manageMspOrgs
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    """
    uri = f"/api/v1/msps/{msp_id}/orgs"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def searchMspOrgs(mist_session:_APISession, msp_id:str, name:str=None, org_id:str=None, sub_insufficient:bool=None, trial_enabled:bool=None, usage_types:list=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchMspOrgs
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    
    QUERY PARAMS
    ------------
    :param str name
    :param str org_id - org id
    :param bool sub_insufficient - if this org has sufficient subscription
    :param bool trial_enabled - if this org is under trial period
    :param list usage_types - a list of types that enabled by usage        
    """
    uri = f"/api/v1/msps/{msp_id}/orgs/search"
    query_params={}
    if name: query_params["name"]=name
    if org_id: query_params["org_id"]=org_id
    if sub_insufficient: query_params["sub_insufficient"]=sub_insufficient
    if trial_enabled: query_params["trial_enabled"]=trial_enabled
    if usage_types: query_params["usage_types"]=usage_types
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getMspOrg(mist_session:_APISession, msp_id:str, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getMspOrg
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id
    :param str org_id        
    """
    uri = f"/api/v1/msps/{msp_id}/orgs/{org_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    