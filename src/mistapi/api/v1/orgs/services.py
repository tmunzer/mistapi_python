from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOrgServices(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgServices
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/services"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgService(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgService
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/services"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgService(mist_session:_APISession, org_id:str, service_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgService
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str service_id        
    """
    uri = f"/api/v1/orgs/{org_id}/services/{service_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgService(mist_session:_APISession, org_id:str, service_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgService
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str service_id        
    """
    uri = f"/api/v1/orgs/{org_id}/services/{service_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgService(mist_session:_APISession, org_id:str, service_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgService
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str service_id        
    """
    uri = f"/api/v1/orgs/{org_id}/services/{service_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    