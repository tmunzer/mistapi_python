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

def countSiteRogueEvents(mist_session:_APISession, site_id:str, distinct:str="bssid", type:str=None, ssid:str=None, bssid:str=None, ap_mac:str=None, channel:str=None, seen_on_lan:bool=None, start:int=None, end:int=None, duration:str="1d", limit:int=100) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/rogues/count-site-rogue-events
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'ap', 'bssid', 'ssid', 'type'}, default: bssid
    type : str{'honeypot', 'lan', 'others', 'spoof'}
    ssid : str
    bssid : str
    ap_mac : str
    channel : str
    seen_on_lan : bool
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/rogues/events/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if type: query_params["type"]=type
    if ssid: query_params["ssid"]=ssid
    if bssid: query_params["bssid"]=bssid
    if ap_mac: query_params["ap_mac"]=ap_mac
    if channel: query_params["channel"]=channel
    if seen_on_lan: query_params["seen_on_lan"]=seen_on_lan
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteRogueEvents(mist_session:_APISession, site_id:str, type:str=None, ssid:str=None, bssid:str=None, ap_mac:str=None, channel:int=None, seen_on_lan:bool=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/rogues/search-site-rogue-events
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    type : str{'honeypot', 'lan', 'others', 'spoof'}
    ssid : str
    bssid : str
    ap_mac : str
    channel : int
    seen_on_lan : bool
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/rogues/events/search"
    query_params={}
    if type: query_params["type"]=type
    if ssid: query_params["ssid"]=ssid
    if bssid: query_params["bssid"]=bssid
    if ap_mac: query_params["ap_mac"]=ap_mac
    if channel: query_params["channel"]=channel
    if seen_on_lan: query_params["seen_on_lan"]=seen_on_lan
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteRogueAP(mist_session:_APISession, site_id:str, rogue_bssid:str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/rogues/get-site-rogue-a-p
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    rogue_bssid : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/rogues/{rogue_bssid}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deauthSiteWirelessClientsConnectedToARogue(mist_session:_APISession, site_id:str, rogue_bssid:str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/wi-fi/deauth-site-wireless-clients-connected-to-a-rogue
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    rogue_bssid : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/rogues/{rogue_bssid}/deauth_clients"
    resp = mist_session.mist_post(uri=uri)
    return resp
    