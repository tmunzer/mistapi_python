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

def countSiteWirelessClients(mist_session:_APISession, site_id:str, distinct:str, ssid:str=None, ap:str=None, ip_address:str=None, vlan:str=None, hostname:str=None, os:str=None, model:str=None, device:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteWirelessClients
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'ssid', 'ap', 'ip', 'vlan', 'hostname', 'os', 'model', 'device'}, default: device
    ssid : str
    ap : str
    ip_address : str
    vlan : str
    hostname : str
    os : str
    model : str
    device : str
    page : int, default: 1
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
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
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/clients/disconnect"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def countSiteWirelessClientEvents(mist_session:_APISession, site_id:str, distinct:str=None, type:str=None, reason_code:int=None, ssid:str=None, ap:str=None, proto:str=None, band:str=None, wlan_id:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteWirelessClientEvents
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'type', 'proto', 'band', 'channel', 'wlan_id', 'ssid'}
      type / proto / band / channel / wlan_id / ssid
    type : str
      event type, e.g. MARVIS_EVENT_CLIENT_FBT_FAILURE
    reason_code : int
      for assoc/disassoc events
    ssid : str
      SSID Name
    ap : str
      AP MAC
    proto : str{'b', 'g', 'n', 'ac', 'ax', 'a'}
      802.11 standard
    band : str{'24', '5'}
      24 / 5
    wlan_id : str
      wlan_id
    page : int, default: 1
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
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
    
def searchSiteWirelessClientEvents(mist_session:_APISession, site_id:str, type:str=None, reason_code:int=None, ssid:str=None, ap:str=None, proto:str=None, band:str=None, wlan_id:str=None, nacrule_id:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteWirelessClientEvents
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    type : str
      event type, e.g. MARVIS_EVENT_CLIENT_FBT_FAILURE
    reason_code : int
      for assoc/disassoc events
    ssid : str
      SSID Name
    ap : str
      AP MAC
    proto : str{'b', 'g', 'n', 'ac', 'ax', 'a'}
      802.11 standard
    band : str{'24', '5'}
      24 / 5
    wlan_id : str
      wlan_id
    nacrule_id : str
      nacrule_id
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
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
    if nacrule_id: query_params["nacrule_id"]=nacrule_id
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteWirelessClients(mist_session:_APISession, site_id:str, mac:str=None, ip_address:str=None, hostname:str=None, device:str=None, os:str=None, model:str=None, ap:str=None, ssid:str=None, text:str=None, nacrule_id:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteWirelessClients
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    mac : str
      partial / full MAC address
    ip_address : str
    hostname : str
      partial / full hostname
    device : str
      device type, e.g. Mac, Nvidia, iPhone
    os : str
      os, e.g. Sierra, Yosemite, Windows 10
    model : str
      model, e.g. “MBP 15 late 2013”, 6, 6s, “8+ GSM”
    ap : str
      AP mac where the client has connected to
    ssid : str
    text : str
      partial / full MAC address, hostname, username, psk_name or ip
    nacrule_id : str
      nacrule_id
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
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
    if nacrule_id: query_params["nacrule_id"]=nacrule_id
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countSiteWirelessClientSessions(mist_session:_APISession, site_id:str, distinct:str="mac", ap:str=None, band:str=None, client_family:str=None, client_manufacture:str=None, client_model:str=None, client_os:str=None, ssid:str=None, wlan_id:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteWirelessClientSessions
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'ssid', 'wlan_id', 'ap', 'mac', 'client_family', 'client_manufacture', 'client_model', 'client_os'}, default: mac
    ap : str
      AP MAC
    band : str
      24 /5
    client_family : str
      E.g. “Mac”, “iPhone”, “Apple watch”
    client_manufacture : str
      E.g. “Apple”
    client_model : str
      E.g. “8+”, “XS”
    client_os : str
      E.g. “Mojave”, “Windows 10”, “Linux”
    ssid : str
      SSID
    wlan_id : str
      wlan_id
    page : int, default: 1
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
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
    
def searchSiteWirelessClientSessions(mist_session:_APISession, site_id:str, ap:str=None, band:str=None, client_family:str=None, client_manufacture:str=None, client_model:str=None, client_username:str=None, client_os:str=None, ssid:str=None, wlan_id:str=None, psk_id:str=None, psk_name:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteWirelessClientSessions
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    ap : str
      AP MAC
    band : str{'24', '5'}
      5 / 24
    client_family : str
      E.g. “Mac”, “iPhone”, “Apple watch”
    client_manufacture : str
      E.g. “Apple”
    client_model : str
      E.g. “8+”, “XS”
    client_username : str
      Username
    client_os : str
      E.g. “Mojave”, “Windows 10”, “Linux”
    ssid : str
      SSID
    wlan_id : str
      wlan_id
    psk_id : str
    psk_name : str
      PSK Name
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
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
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/clients/unauthorize"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def reauthSiteDot1xWirelessClient(mist_session:_APISession, site_id:str, client_mac:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/reauthSiteDot1xWirelessClient
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    client_mac : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/clients/{client_mac}/coa"
    resp = mist_session.mist_post(uri=uri)
    return resp
    
def disconnectSiteWirelessClient(mist_session:_APISession, site_id:str, client_mac:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/disconnectSiteWirelessClient
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    client_mac : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/clients/{client_mac}/disconnect"
    resp = mist_session.mist_post(uri=uri)
    return resp
    
def getSiteEventsForClient(mist_session:_APISession, site_id:str, client_mac:str, type:str=None, proto:str=None, band:str=None, channel:str=None, wlan_id:str=None, ssid:str=None, start:int=None, end:int=None, page:int=1, limit:int=100, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteEventsForClient
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    client_mac : str        
    
    QUERY PARAMS
    ------------
    type : str{'b', 'g', 'n'}
      e.g. MARVIS_EVENT_CLIENT_DHCP_STUCK
    proto : str{'a', 'b', 'g', 'n', 'ac', 'ax'}
      a / b / g / n / ac / ax
    band : str
      24 / 5
    channel : str
    wlan_id : str
    ssid : str
    start : int
    end : int
    page : int, default: 1
    limit : int, default: 100
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
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
    
def unauthorizeSiteWirelessClient(mist_session:_APISession, site_id:str, client_mac:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/unauthorizeSiteWirelessClient
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    client_mac : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/clients/{client_mac}/unauthorize"
    resp = mist_session.mist_post(uri=uri)
    return resp
    