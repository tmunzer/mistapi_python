from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getSiteWlans(mist_session:_APISession, site_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteWlans
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/wlans"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createSiteWlan(mist_session:_APISession, site_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createSiteWlan
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/wlans"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteWlanDerived(mist_session:_APISession, site_id:str, resolve:bool=None) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteWlanDerived
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param bool resolve - whether to resolve SITE_VARS        
    """
    uri = f"/api/v1/sites/{site_id}/wlans/derived"
    query_params={}
    if resolve: query_params["resolve"]=resolve
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteWlan(mist_session:_APISession, site_id:str, wlan_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteWlan
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str wlan_id        
    """
    uri = f"/api/v1/sites/{site_id}/wlans/{wlan_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteSiteWlan(mist_session:_APISession, site_id:str, wlan_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteSiteWlan
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str wlan_id        
    """
    uri = f"/api/v1/sites/{site_id}/wlans/{wlan_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateSiteWlan(mist_session:_APISession, site_id:str, wlan_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSiteWlan
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str wlan_id        
    """
    uri = f"/api/v1/sites/{site_id}/wlans/{wlan_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def uploadSiteWlanPortalImage(mist_session:_APISession, site_id:str, wlan_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/uploadSiteWlanPortalImage
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str wlan_id        
    """
    uri = f"/api/v1/sites/{site_id}/wlans/{wlan_id}/portal_image"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def updateSiteWlanPortalTemplate(mist_session:_APISession, site_id:str, wlan_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSiteWlanPortalTemplate
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str wlan_id        
    """
    uri = f"/api/v1/sites/{site_id}/wlans/{wlan_id}/portal_template"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    