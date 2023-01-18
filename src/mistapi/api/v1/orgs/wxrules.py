from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOrgWxRules(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgWxRules
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/wxrules"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgWxRule(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgWxRule
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/wxrules"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgWxRulesDerived(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgWxRulesDerived
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/wxrules/derived"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getOrgWxRule(mist_session:_APISession, org_id:str, wxrules_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgWxRule
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str wxrules_id        
    """
    uri = f"/api/v1/orgs/{org_id}/wxrules/{wxrules_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgWxRule(mist_session:_APISession, org_id:str, wxrules_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgWxRule
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str wxrules_id        
    """
    uri = f"/api/v1/orgs/{org_id}/wxrules/{wxrules_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgWxRule(mist_session:_APISession, org_id:str, wxrules_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgWxRule
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str wxrules_id        
    """
    uri = f"/api/v1/orgs/{org_id}/wxrules/{wxrules_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    