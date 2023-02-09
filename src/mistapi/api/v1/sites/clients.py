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

def countSiteByDistinctAttributesOfClients(mist_session:_APISession, site_id:str, distinct:str, ssid:str=None, ap:str=None, ip_address:str=None, vlan:str=None, hostname:str=None, os:str=None, model:str=None, device:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteByDistinctAttributesOfClients
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(ssid, ap, ip, vlan, hostname, os, model, device)
    :param str ssid
    :param str ap
    :param str ip_address
    :param str vlan
    :param str hostname
    :param str os
    :param str model
    :param str device
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/clients/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if ssid: query_params["ssid"]=ssid
    if ap: query_params["ap"]=ap
    if ip_address: query_params["ip_address"]=ip_address
    if vlan: query_params["vlan"]=vlan
    if hostname: query_params["hostname"]=hostname
    if os: query_params["os"]=os
    if model: query_params["model"]=model
    if device: query_params["device"]=device
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def disconnectSiteMultipleClients(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/disconnectSiteMultipleClients
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/clients/disconnect"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def countSiteByDistinctAttributesOfClientsEvents(mist_session:_APISession, site_id:str, distinct:str=None, type:str=None, reason_code:int=None, ssid:str=None, ap:str=None, proto:str=None, band:str=None, wlan_id:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteByDistinctAttributesOfClientsEvents
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(type, proto, band, channel, wlan_id, ssid) - type / proto / band / channel / wlan_id / ssid
    :param str type - event type, e.g. MARVIS_EVENT_CLIENT_FBT_FAILURE
    :param int reason_code - for assoc/disassoc events
    :param str ssid - SSID Name
    :param str ap - AP MAC
    :param str proto(b, g, n, ac, ax, a) - 802.11 standard
    :param str band(24, 5) - 24 / 5
    :param str wlan_id - wlan_id
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/clients/events/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if type: query_params["type"]=type
    if reason_code: query_params["reason_code"]=reason_code
    if ssid: query_params["ssid"]=ssid
    if ap: query_params["ap"]=ap
    if proto: query_params["proto"]=proto
    if band: query_params["band"]=band
    if wlan_id: query_params["wlan_id"]=wlan_id
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteClientsEvents(mist_session:_APISession, site_id:str, type:str=None, reason_code:int=None, ssid:str=None, ap:str=None, proto:str=None, band:str=None, wlan_id:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteClientsEvents
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str type - event type, e.g. MARVIS_EVENT_CLIENT_FBT_FAILURE
    :param int reason_code - for assoc/disassoc events
    :param str ssid - SSID Name
    :param str ap - AP MAC
    :param str proto(b, g, n, ac, ax, a) - 802.11 standard
    :param str band(24, 5) - 24 / 5
    :param str wlan_id - wlan_id
    :param int limit
    :param int start
    :param int end
    :param str duration        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/clients/events/search"
    query_params={}
    if type: query_params["type"]=type
    if reason_code: query_params["reason_code"]=reason_code
    if ssid: query_params["ssid"]=ssid
    if ap: query_params["ap"]=ap
    if proto: query_params["proto"]=proto
    if band: query_params["band"]=band
    if wlan_id: query_params["wlan_id"]=wlan_id
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteClientsWireless(mist_session:_APISession, site_id:str, mac:str=None, ip_address:str=None, hostname:str=None, device:str=None, os:str=None, model:str=None, ap:str=None, ssid:str=None, text:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteClientsWireless
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str mac - partial / full MAC address
    :param str ip_address
    :param str hostname - partial / full hostname
    :param str device - device type, e.g. Mac, Nvidia, iPhone
    :param str os - os, e.g. Sierra, Yosemite, Windows 10
    :param str model - model, e.g. “MBP 15 late 2013”, 6, 6s, “8+ GSM”
    :param str ap - AP mac where the client has connected to
    :param str ssid
    :param str text - partial / full MAC address, hostname, username or ip
    :param int limit
    :param int start
    :param int end
    :param str duration        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/clients/search"
    query_params={}
    if mac: query_params["mac"]=mac
    if ip_address: query_params["ip_address"]=ip_address
    if hostname: query_params["hostname"]=hostname
    if device: query_params["device"]=device
    if os: query_params["os"]=os
    if model: query_params["model"]=model
    if ap: query_params["ap"]=ap
    if ssid: query_params["ssid"]=ssid
    if text: query_params["text"]=text
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countSiteByDistinctAttributesOfClientSessions(mist_session:_APISession, site_id:str, distinct:str="mac", ap:str=None, band:str=None, client_family:str=None, client_manufacture:str=None, client_model:str=None, client_os:str=None, ssid:str=None, wlan_id:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteByDistinctAttributesOfClientSessions
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(ssid, wlan_id, ap, mac, client_family, client_manufacture, client_model, client_os)
    :param str ap - AP MAC
    :param str band - 24 /5
    :param str client_family - E.g. “Mac”, “iPhone”, “Apple watch”
    :param str client_manufacture - E.g. “Apple”
    :param str client_model - E.g. “8+”, “XS”
    :param str client_os - E.g. “Mojave”, “Windows 10”, “Linux”
    :param str ssid - SSID
    :param str wlan_id - wlan_id
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/clients/sessions/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if ap: query_params["ap"]=ap
    if band: query_params["band"]=band
    if client_family: query_params["client_family"]=client_family
    if client_manufacture: query_params["client_manufacture"]=client_manufacture
    if client_model: query_params["client_model"]=client_model
    if client_os: query_params["client_os"]=client_os
    if ssid: query_params["ssid"]=ssid
    if wlan_id: query_params["wlan_id"]=wlan_id
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteClientWirelessSessions(mist_session:_APISession, site_id:str, ap:str=None, band:str=None, client_family:str=None, client_manufacture:str=None, client_model:str=None, client_username:str=None, client_os:str=None, ssid:str=None, wlan_id:str=None, psk_id:str=None, psk_name:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteClientWirelessSessions
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str ap - AP MAC
    :param str band(24, 5) - 5 / 24
    :param str client_family - E.g. “Mac”, “iPhone”, “Apple watch”
    :param str client_manufacture - E.g. “Apple”
    :param str client_model - E.g. “8+”, “XS”
    :param str client_username - Username
    :param str client_os - E.g. “Mojave”, “Windows 10”, “Linux”
    :param str ssid - SSID
    :param str wlan_id - wlan_id
    :param str psk_id
    :param str psk_name - PSK Name
    :param int limit
    :param int start
    :param int end
    :param str duration        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/clients/sessions/search"
    query_params={}
    if ap: query_params["ap"]=ap
    if band: query_params["band"]=band
    if client_family: query_params["client_family"]=client_family
    if client_manufacture: query_params["client_manufacture"]=client_manufacture
    if client_model: query_params["client_model"]=client_model
    if client_username: query_params["client_username"]=client_username
    if client_os: query_params["client_os"]=client_os
    if ssid: query_params["ssid"]=ssid
    if wlan_id: query_params["wlan_id"]=wlan_id
    if psk_id: query_params["psk_id"]=psk_id
    if psk_name: query_params["psk_name"]=psk_name
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def unauthorizeSiteMultipleClients(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/unauthorizeSiteMultipleClients
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/clients/unauthorize"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def disconnectSiteClient(mist_session:_APISession, site_id:str, client_mac:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/disconnectSiteClient
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str client_mac        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/clients/{client_mac}/disconnect"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteEventsForClient(mist_session:_APISession, site_id:str, client_mac:str, type:str=None, proto:str=None, band:str=None, channel:str=None, wlan_id:str=None, ssid:str=None, start:int=None, end:int=None, page:int=1, limit:int=100, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteEventsForClient
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str client_mac        
    
    QUERY PARAMS
    ------------
    :param str type(b, g, n) - e.g. MARVIS_EVENT_CLIENT_DHCP_STUCK
    :param str proto(a, b, g, n, ac, ax) - a / b / g / n / ac / ax
    :param str band - 24 / 5
    :param str channel
    :param str wlan_id
    :param str ssid
    :param int start
    :param int end
    :param int page
    :param int limit
    :param str duration        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/clients/{client_mac}/events"
    query_params={}
    if type: query_params["type"]=type
    if proto: query_params["proto"]=proto
    if band: query_params["band"]=band
    if channel: query_params["channel"]=channel
    if wlan_id: query_params["wlan_id"]=wlan_id
    if ssid: query_params["ssid"]=ssid
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def unauthorizeSiteClient(mist_session:_APISession, site_id:str, client_mac:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/unauthorizeSiteClient
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str client_mac        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/clients/{client_mac}/unauthorize"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    