from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOrgGuestAuthorizations(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgGuestAuthorizations
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/guests"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countOrgGuestAuthorizations(mist_session:_APISession, org_id:str, distinct:str="auth_method", page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/countOrgGuestAuthorizations
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(auth_method, ssid, company)
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/orgs/{org_id}/guests/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchOrgGuestAuthorization(mist_session:_APISession, org_id:str, wlan_id:str=None, auth_method:str=None, ssid:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchOrgGuestAuthorization
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str wlan_id
    :param str auth_method
    :param str ssid
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/orgs/{org_id}/guests/search"
    query_params={}
    if wlan_id: query_params["wlan_id"]=wlan_id
    if auth_method: query_params["auth_method"]=auth_method
    if ssid: query_params["ssid"]=ssid
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getOrgGuestAuthorization(mist_session:_APISession, org_id:str, guest_mac:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgGuestAuthorization
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str guest_mac        
    """
    uri = f"/api/v1/orgs/{org_id}/guests/{guest_mac}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgGuestAuthorization(mist_session:_APISession, org_id:str, guest_mac:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgGuestAuthorization
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str guest_mac        
    """
    uri = f"/api/v1/orgs/{org_id}/guests/{guest_mac}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgGuestAuthorization(mist_session:_APISession, org_id:str, guest_mac:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgGuestAuthorization
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str guest_mac        
    """
    uri = f"/api/v1/orgs/{org_id}/guests/{guest_mac}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    