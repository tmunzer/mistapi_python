
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

def getSiteWxRules(mist_session:_APISession, site_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteWxRules
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/wxrules"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createSiteWxRule(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createSiteWxRule
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/wxrules"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteWxRulesDerived(mist_session:_APISession, site_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteWxRulesDerived
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/wxrules/derived"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteWxRule(mist_session:_APISession, site_id:str, wxrules_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteWxRule
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str wxrules_id        
    """
    uri = f"/api/v1/sites/{site_id}/wxrules/{wxrules_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteSiteWxRule(mist_session:_APISession, site_id:str, wxrules_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteSiteWxRule
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str wxrules_id        
    """
    uri = f"/api/v1/sites/{site_id}/wxrules/{wxrules_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateSiteWxRule(mist_session:_APISession, site_id:str, wxrules_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSiteWxRule
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str wxrules_id        
    """
    uri = f"/api/v1/sites/{site_id}/wxrules/{wxrules_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    