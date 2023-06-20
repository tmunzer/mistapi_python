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

def countOrgWirelessClients(mist_session:_APISession, org_id:str, distinct:str="device", mac:str=None, hostname:str=None, device:str=None, os:str=None, model:str=None, ap:str=None, vlan:str=None, ssid:str=None, ip_address:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countOrgWirelessClients
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'mac', 'hostname', 'device', 'os', 'model', 'ap', 'vlan', 'ssid', 'ip'}, default: device
    mac : str
      partial / full MAC address
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
    vlan : str
      vlan
    ssid : str
      SSID
    ip_address : str
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
    
def searchOrgWirelessClientsEvents(mist_session:_APISession, org_id:str, type:str=None, reason_code:int=None, ssid:str=None, ap:str=None, proto:str=None, band:str=None, wlan_id:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchOrgWirelessClientsEvents
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
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
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
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
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchOrgWirelessClients(mist_session:_APISession, org_id:str, site_id:str=None, mac:str=None, ip_address:str=None, hostname:str=None, device:str=None, os:str=None, model:str=None, ap:str=None, psk_id:str=None, psk_name:str=None, vlan:str=None, ssid:str=None, text:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchOrgWirelessClients
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    site_id : str
      Site ID
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
    psk_id : str
    psk_name : str
      PSK Name
    vlan : str
      vlan
    ssid : str
      SSID
    text : str
      partial / full MAC address, hostname
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/clients/search"
    query_params={}
    if site_id: query_params["site_id"]=site_id
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
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countOrgWirelessClientsSessions(mist_session:_APISession, org_id:str, distinct:str, ap:str=None, band:str=None, client_family:str=None, client_manufacture:str=None, client_model:str=None, client_os:str=None, ssid:str=None, wlan_id:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countOrgWirelessClientsSessions
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'ssid', 'ap', 'ip', 'vlan', 'hostname', 'os', 'model', 'device'}, default: device
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
    
def searchOrgWirelessClientSessions(mist_session:_APISession, org_id:str, ap:str=None, band:str=None, client_family:str=None, client_manufacture:str=None, client_model:str=None, client_username:str=None, client_os:str=None, ssid:str=None, wlan_id:str=None, psk_id:str=None, psk_name:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchOrgWirelessClientSessions
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
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
    uri = f"/api/v1/orgs/{org_id}/clients/sessions/search"
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
    