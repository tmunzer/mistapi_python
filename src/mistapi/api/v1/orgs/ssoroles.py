from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOrgSsoRoles(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgSsoRoles
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/ssoroles"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgSsoRole(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgSsoRole
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/ssoroles"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgSsoRole(mist_session:_APISession, org_id:str, ssorole_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgSsoRole
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str ssorole_id        
    """
    uri = f"/api/v1/orgs/{org_id}/ssoroles/{ssorole_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgSsoRoles(mist_session:_APISession, org_id:str, ssorole_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgSsoRoles
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str ssorole_id        
    """
    uri = f"/api/v1/orgs/{org_id}/ssoroles/{ssorole_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgSsoRole(mist_session:_APISession, org_id:str, ssorole_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgSsoRole
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str ssorole_id        
    """
    uri = f"/api/v1/orgs/{org_id}/ssoroles/{ssorole_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    