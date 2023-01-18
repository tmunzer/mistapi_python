from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getSiteMxEdges(mist_session:_APISession, site_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteMxEdges
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/mxedges"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createSiteMxEdge(mist_session:_APISession, site_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createSiteMxEdge
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/mxedges"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteMxEdge(mist_session:_APISession, site_id:str, mxedge_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteMxEdge
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str mxedge_id        
    """
    uri = f"/api/v1/sites/{site_id}/mxedges/{mxedge_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteSiteMxEdge(mist_session:_APISession, site_id:str, mxedge_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteSiteMxEdge
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str mxedge_id        
    """
    uri = f"/api/v1/sites/{site_id}/mxedges/{mxedge_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateSiteMxEdge(mist_session:_APISession, site_id:str, mxedge_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSiteMxEdge
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str mxedge_id        
    """
    uri = f"/api/v1/sites/{site_id}/mxedges/{mxedge_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def uploadSiteMxEdgeSupportFiles(mist_session:_APISession, site_id:str, mxedge_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/uploadSiteMxEdgeSupportFiles
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str mxedge_id        
    """
    uri = f"/api/v1/sites/{site_id}/mxedges/{mxedge_id}/support"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    