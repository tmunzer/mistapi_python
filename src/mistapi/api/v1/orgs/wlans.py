from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOrgWlans(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgWlans
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/wlans"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgWlan(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgWlan
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/wlans"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgWlanDerived(mist_session:_APISession, org_id:str, resolve:bool=None) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgWlanDerived
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param bool resolve - whether to resolve SITE_VARS        
    """
    uri = f"/api/v1/orgs/{org_id}/wlans/derived"
    query_params={}
    if resolve: query_params["resolve"]=resolve
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getOrgWLAN(mist_session:_APISession, org_id:str, wlan_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgWLAN
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str wlan_id        
    """
    uri = f"/api/v1/orgs/{org_id}/wlans/{wlan_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgWlan(mist_session:_APISession, org_id:str, wlan_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgWlan
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str wlan_id        
    """
    uri = f"/api/v1/orgs/{org_id}/wlans/{wlan_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgWlan(mist_session:_APISession, org_id:str, wlan_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgWlan
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str wlan_id        
    """
    uri = f"/api/v1/orgs/{org_id}/wlans/{wlan_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def deleteOrgWlanPortalImage(mist_session:_APISession, org_id:str, wlan_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgWlanPortalImage
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str wlan_id        
    """
    uri = f"/api/v1/orgs/{org_id}/wlans/{wlan_id}/portal_image"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def uploadOrgWlanPortalImage(mist_session:_APISession, org_id:str, wlan_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/uploadOrgWlanPortalImage
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str wlan_id        
    """
    uri = f"/api/v1/orgs/{org_id}/wlans/{wlan_id}/portal_image"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def updateOrgWlanPortalTemplate(mist_session:_APISession, org_id:str, wlan_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgWlanPortalTemplate
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str wlan_id        
    """
    uri = f"/api/v1/orgs/{org_id}/wlans/{wlan_id}/portal_template"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    