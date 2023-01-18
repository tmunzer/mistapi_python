from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOrgTemplates(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgTemplates
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/templates"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgTemplate(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgTemplate
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/templates"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgTemplate(mist_session:_APISession, org_id:str, template_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgTemplate
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str template_id        
    """
    uri = f"/api/v1/orgs/{org_id}/templates/{template_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgTemplate(mist_session:_APISession, org_id:str, template_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgTemplate
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str template_id        
    """
    uri = f"/api/v1/orgs/{org_id}/templates/{template_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgTemplate(mist_session:_APISession, org_id:str, template_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgTemplate
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str template_id        
    """
    uri = f"/api/v1/orgs/{org_id}/templates/{template_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def cloneOrgTemplate(mist_session:_APISession, org_id:str, template_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/cloneOrgTemplate
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str template_id        
    """
    uri = f"/api/v1/orgs/{org_id}/templates/{template_id}/clone"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    