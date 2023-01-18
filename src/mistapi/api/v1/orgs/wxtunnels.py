from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOrgWxTunnels(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgWxTunnels
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/wxtunnels"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgWxTunnel(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgWxTunnel
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/wxtunnels"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgWxTunnel(mist_session:_APISession, org_id:str, wxtunnel_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgWxTunnel
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str wxtunnel_id        
    """
    uri = f"/api/v1/orgs/{org_id}/wxtunnels/{wxtunnel_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgWxTunnel(mist_session:_APISession, org_id:str, wxtunnel_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgWxTunnel
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str wxtunnel_id        
    """
    uri = f"/api/v1/orgs/{org_id}/wxtunnels/{wxtunnel_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgWxTunnel(mist_session:_APISession, org_id:str, wxtunnel_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgWxTunnel
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str wxtunnel_id        
    """
    uri = f"/api/v1/orgs/{org_id}/wxtunnels/{wxtunnel_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    