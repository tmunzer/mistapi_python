from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse

def getSiteWxTunnels(mist_session:_APISession, site_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteWxTunnels
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/wxtunnels"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createSiteWxTunnel(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createSiteWxTunnel
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/wxtunnels"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteWxTunnel(mist_session:_APISession, site_id:str, wxtunnel_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteWxTunnel
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str wxtunnel_id        
    """
    uri = f"/api/v1/sites/{site_id}/wxtunnels/{wxtunnel_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteSiteWxTunnel(mist_session:_APISession, site_id:str, wxtunnel_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteSiteWxTunnel
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str wxtunnel_id        
    """
    uri = f"/api/v1/sites/{site_id}/wxtunnels/{wxtunnel_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateSiteWxTunnel(mist_session:_APISession, site_id:str, wxtunnel_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSiteWxTunnel
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str wxtunnel_id        
    """
    uri = f"/api/v1/sites/{site_id}/wxtunnels/{wxtunnel_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    