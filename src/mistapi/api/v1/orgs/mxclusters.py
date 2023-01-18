from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOrgMxEdgeClusters(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgMxEdgeClusters
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxclusters"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgMxEdgeCluster(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgMxEdgeCluster
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxclusters"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgMxEdgeCluster(mist_session:_APISession, org_id:str, mxcluster_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgMxEdgeCluster
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str mxcluster_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxclusters/{mxcluster_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgMxEdgeCluster(mist_session:_APISession, org_id:str, mxcluster_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgMxEdgeCluster
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str mxcluster_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxclusters/{mxcluster_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgMxEdgeCluster(mist_session:_APISession, org_id:str, mxcluster_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgMxEdgeCluster
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str mxcluster_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxclusters/{mxcluster_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    