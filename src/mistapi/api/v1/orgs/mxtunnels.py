from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOrgMxTunnels(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgMxTunnels
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxtunnels"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgMxTunnel(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgMxTunnel
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxtunnels"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgMxTunnel(mist_session:_APISession, org_id:str, mxtunnel_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgMxTunnel
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str mxtunnel_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxtunnels/{mxtunnel_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgMxTunnel(mist_session:_APISession, org_id:str, mxtunnel_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgMxTunnel
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str mxtunnel_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxtunnels/{mxtunnel_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgMxTunnel(mist_session:_APISession, org_id:str, mxtunnel_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgMxTunnel
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str mxtunnel_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxtunnels/{mxtunnel_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    