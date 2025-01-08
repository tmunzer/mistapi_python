'''
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
'''

from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse
import deprecation

def listSiteAllGuestAuthorizations(mist_session:_APISession, site_id:str, wlan_id:str=None) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/guests/list-site-all-guest-authorizations
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    wlan_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/guests"
    query_params={}
    if wlan_id: query_params["wlan_id"]=wlan_id
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countSiteGuestAuthorizations(mist_session:_APISession, site_id:str, distinct:str="auth_method", start:int=None, end:int=None, duration:str="1d", limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/guests/count-site-guest-authorizations
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'auth_method', 'company', 'ssid'}, default: auth_method
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100
    page : int, default: 1        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/guests/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listSiteAllGuestAuthorizationsDerived(mist_session:_APISession, site_id:str, wlan_id:str=None, cross_site:bool=None) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/guests/list-site-all-guest-authorizations-derived
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    wlan_id : str
    cross_site : bool        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/guests/derived"
    query_params={}
    if wlan_id: query_params["wlan_id"]=wlan_id
    if cross_site: query_params["cross_site"]=cross_site
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteGuestAuthorization(mist_session:_APISession, site_id:str, wlan_id:str=None, auth_method:str=None, ssid:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/guests/search-site-guest-authorization
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    wlan_id : str
    auth_method : str
    ssid : str
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/guests/search"
    query_params={}
    if wlan_id: query_params["wlan_id"]=wlan_id
    if auth_method: query_params["auth_method"]=auth_method
    if ssid: query_params["ssid"]=ssid
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteGuestAuthorization(mist_session:_APISession, site_id:str, guest_mac:str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/guests/get-site-guest-authorization
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    guest_mac : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/guests/{guest_mac}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteSiteGuestAuthorization(mist_session:_APISession, site_id:str, guest_mac:str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/guests/delete-site-guest-authorization
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    guest_mac : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/guests/{guest_mac}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateSiteGuestAuthorization(mist_session:_APISession, site_id:str, guest_mac:str, body:object) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/guests/update-site-guest-authorization
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    guest_mac : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/guests/{guest_mac}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    