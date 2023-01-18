from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOrgNacRules(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgNacRules
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/nacrules"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgNacRule(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgNacRule
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/nacrules"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgNacRule(mist_session:_APISession, org_id:str, nacrule_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgNacRule
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str nacrule_id        
    """
    uri = f"/api/v1/orgs/{org_id}/nacrules/{nacrule_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgNacRule(mist_session:_APISession, org_id:str, nacrule_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgNacRule
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str nacrule_id        
    """
    uri = f"/api/v1/orgs/{org_id}/nacrules/{nacrule_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgNacRule(mist_session:_APISession, org_id:str, nacrule_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgNacRule
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str nacrule_id        
    """
    uri = f"/api/v1/orgs/{org_id}/nacrules/{nacrule_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    