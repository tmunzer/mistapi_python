
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

def countOrgClientsWireless(mist_session:_APISession, org_id:str, distinct:str="device", mac:str=None, hostname:str=None, device:str=None, os:str=None, model:str=None, ap:str=None, vlan:str=None, ssid:str=None, ip_address:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countOrgClientsWireless
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(mac, hostname, device, os, model, ap, vlan, ssid, ip)
    :param str mac - partial / full MAC address
    :param str hostname - partial / full hostname
    :param str device - device type, e.g. Mac, Nvidia, iPhone
    :param str os - os, e.g. Sierra, Yosemite, Windows 10
    :param str model - model, e.g. “MBP 15 late 2013”, 6, 6s, “8+ GSM”
    :param str ap - AP mac where the client has connected to
    :param str vlan - vlan
    :param str ssid - SSID
    :param str ip_address
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/orgs/{org_id}/clients/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if mac: query_params["mac"]=mac
    if hostname: query_params["hostname"]=hostname
    if device: query_params["device"]=device
    if os: query_params["os"]=os
    if model: query_params["model"]=model
    if ap: query_params["ap"]=ap
    if vlan: query_params["vlan"]=vlan
    if ssid: query_params["ssid"]=ssid
    if ip_address: query_params["ip_address"]=ip_address
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchOrgClientEvents(mist_session:_APISession, org_id:str, type:str=None, reason_code:int=None, ssid:str=None, ap:str=None, proto:str=None, band:str=None, wlan_id:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchOrgClientEvents
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
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
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/orgs/{org_id}/clients/events/search"
    query_params={}
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
    
def searchOrgClientsWireless(mist_session:_APISession, org_id:str, mac:str=None, ip_address:str=None, hostname:str=None, device:str=None, os:str=None, model:str=None, ap:str=None, psk_id:str=None, psk_name:str=None, vlan:str=None, ssid:str=None, text:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchOrgClientsWireless
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str mac - partial / full MAC address
    :param str ip_address
    :param str hostname - partial / full hostname
    :param str device - device type, e.g. Mac, Nvidia, iPhone
    :param str os - os, e.g. Sierra, Yosemite, Windows 10
    :param str model - model, e.g. “MBP 15 late 2013”, 6, 6s, “8+ GSM”
    :param str ap - AP mac where the client has connected to
    :param str psk_id
    :param str psk_name - PSK Name
    :param str vlan - vlan
    :param str ssid - SSID
    :param str text - partial / full MAC address, hostname
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/orgs/{org_id}/clients/search"
    query_params={}
    if mac: query_params["mac"]=mac
    if ip_address: query_params["ip_address"]=ip_address
    if hostname: query_params["hostname"]=hostname
    if device: query_params["device"]=device
    if os: query_params["os"]=os
    if model: query_params["model"]=model
    if ap: query_params["ap"]=ap
    if psk_id: query_params["psk_id"]=psk_id
    if psk_name: query_params["psk_name"]=psk_name
    if vlan: query_params["vlan"]=vlan
    if ssid: query_params["ssid"]=ssid
    if text: query_params["text"]=text
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countOrgWirelessClientsSessions(mist_session:_APISession, org_id:str, distinct:str, ap:str=None, band:str=None, client_family:str=None, client_manufacture:str=None, client_model:str=None, client_os:str=None, ssid:str=None, wlan_id:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countOrgWirelessClientsSessions
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(ssid, ap, ip, vlan, hostname, os, model, device)
    :param str ap - AP MAC
    :param str band(24, 5) - 5 / 24
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
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/orgs/{org_id}/clients/sessions/count"
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
    
def searchOrgClientWirelessSessions(mist_session:_APISession, org_id:str, ap:str=None, band:str=None, client_family:str=None, client_manufacture:str=None, client_model:str=None, client_os:str=None, ssid:str=None, wlan_id:str=None, psk_id:str=None, psk_name:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchOrgClientWirelessSessions
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str ap - AP MAC
    :param str band(24, 5) - 5 / 24
    :param str client_family - E.g. “Mac”, “iPhone”, “Apple watch”
    :param str client_manufacture - E.g. “Apple”
    :param str client_model - E.g. “8+”, “XS”
    :param str client_os - E.g. “Mojave”, “Windows 10”, “Linux”
    :param str ssid - SSID
    :param str wlan_id - wlan_id
    :param str psk_id
    :param str psk_name - PSK Name
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/orgs/{org_id}/clients/sessions/search"
    query_params={}
    if ap: query_params["ap"]=ap
    if band: query_params["band"]=band
    if client_family: query_params["client_family"]=client_family
    if client_manufacture: query_params["client_manufacture"]=client_manufacture
    if client_model: query_params["client_model"]=client_model
    if client_os: query_params["client_os"]=client_os
    if ssid: query_params["ssid"]=ssid
    if wlan_id: query_params["wlan_id"]=wlan_id
    if psk_id: query_params["psk_id"]=psk_id
    if psk_name: query_params["psk_name"]=psk_name
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    