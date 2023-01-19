from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse

def countSiteRogueEvents(mist_session:_APISession, site_id:str, distinct:str="bssid", type:str=None, ssid:str=None, bssid:str=None, ap_mac:str=None, channel:str=None, seen_on_lan:bool=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteRogueEvents
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(bssid, ssid, ap, type)
    :param str type(honeypot, lan, others, spoof)
    :param str ssid - ssid of the network detected as threat
    :param str bssid - bssid of the network detected as threat
    :param str ap_mac - mac of the device that had strongest signal strength for ssid/bssid pair
    :param str channel - channel over which ap_mac heard ssid/bssid pair
    :param bool seen_on_lan - whether the reporting AP see a wireless client (on LAN) connecting to it  
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
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
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteRogueEvents(mist_session:_APISession, site_id:str, type:str=None, ssid:str=None, bssid:str=None, ap_mac:str=None, channel:str=None, seen_on_lan:bool=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteRogueEvents
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str type(honeypot, lan, others, spoof)
    :param str ssid - ssid of the network detected as threat
    :param str bssid - bssid of the network detected as threat
    :param str ap_mac - mac of the device that had strongest signal strength for ssid/bssid pair
    :param str channel - channel over which ap_mac heard ssid/bssid pair
    :param bool seen_on_lan - whether the reporting AP see a wireless client (on LAN) connecting to it  
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/sites/{site_id}/rogues/events/search"
    query_params={}
    if type: query_params["type"]=type
    if ssid: query_params["ssid"]=ssid
    if bssid: query_params["bssid"]=bssid
    if ap_mac: query_params["ap_mac"]=ap_mac
    if channel: query_params["channel"]=channel
    if seen_on_lan: query_params["seen_on_lan"]=seen_on_lan
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteRogueAP(mist_session:_APISession, site_id:str, rogue_bssid:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteRogueAP
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str rogue_bssid        
    """
    uri = f"/api/v1/sites/{site_id}/rogues/{rogue_bssid}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deauthSiteClientsConnectedToARogue(mist_session:_APISession, site_id:str, rogue_bssid:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deauthSiteClientsConnectedToARogue
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str rogue_bssid        
    """
    uri = f"/api/v1/sites/{site_id}/rogues/{rogue_bssid}/deauth_clients"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    