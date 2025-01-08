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

def countOrgWirelessClients(mist_session:_APISession, org_id:str, distinct:str="device", mac:str=None, hostname:str=None, device:str=None, os:str=None, model:str=None, ap:str=None, vlan:str=None, ssid:str=None, ip_address:str=None, start:int=None, end:int=None, duration:str="1d", limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/wireless/count-org-wireless-clients
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'ap', 'device', 'hostname', 'ip', 'mac', 'model', 'os', 'ssid', 'vlan'}, default: device
    mac : str
    hostname : str
    device : str
    os : str
    model : str
    ap : str
    vlan : str
    ssid : str
    ip_address : str
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
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchOrgWirelessClientEvents(mist_session:_APISession, org_id:str, type:str=None, reason_code:int=None, ssid:str=None, ap:str=None, proto:str=None, band:str=None, wlan_id:str=None, nacrule_id:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/wireless/search-org-wireless-client-events
    
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
    reason_code : int
    ssid : str
    ap : str
    proto : str{'a', 'ac', 'ax', 'b', 'g', 'n'}
      a / b / g / n / ac / ax
    band : str{'24', '5', '6'}
      802.11 Band
    wlan_id : str
    nacrule_id : str
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
    if nacrule_id: query_params["nacrule_id"]=nacrule_id
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchOrgWirelessClients(mist_session:_APISession, org_id:str, site_id:str=None, mac:str=None, ip_address:str=None, hostname:str=None, band:str=None, device:str=None, os:str=None, model:str=None, ap:str=None, psk_id:str=None, psk_name:str=None, username:str=None, vlan:str=None, ssid:str=None, text:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/wireless/search-org-wireless-clients
    
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
    mac : str
    ip_address : str
    hostname : str
    band : str
    device : str
    os : str
    model : str
    ap : str
    psk_id : str
    psk_name : str
    username : str
    vlan : str
    ssid : str
    text : str
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
    if band: query_params["band"]=band
    if device: query_params["device"]=device
    if os: query_params["os"]=os
    if model: query_params["model"]=model
    if ap: query_params["ap"]=ap
    if psk_id: query_params["psk_id"]=psk_id
    if psk_name: query_params["psk_name"]=psk_name
    if username: query_params["username"]=username
    if vlan: query_params["vlan"]=vlan
    if ssid: query_params["ssid"]=ssid
    if text: query_params["text"]=text
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countOrgWirelessClientsSessions(mist_session:_APISession, org_id:str, distinct:str="device", ap:str=None, band:str=None, client_family:str=None, client_manufacture:str=None, client_model:str=None, client_os:str=None, ssid:str=None, wlan_id:str=None, start:int=None, end:int=None, duration:str="1d", limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/wireless/count-org-wireless-clients-sessions
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'ap', 'device', 'hostname', 'ip', 'model', 'os', 'ssid', 'vlan'}, default: device
    ap : str
    band : str{'24', '5', '6'}
      802.11 Band
    client_family : str
    client_manufacture : str
    client_model : str
    client_os : str
    ssid : str
    wlan_id : str
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
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchOrgWirelessClientSessions(mist_session:_APISession, org_id:str, ap:str=None, band:str=None, client_family:str=None, client_manufacture:str=None, client_model:str=None, client_username:str=None, client_os:str=None, ssid:str=None, wlan_id:str=None, psk_id:str=None, psk_name:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/wireless/search-org-wireless-client-sessions
    
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
    band : str{'24', '5', '6'}
      802.11 Band
    client_family : str
    client_manufacture : str
    client_model : str
    client_username : str
    client_os : str
    ssid : str
    wlan_id : str
    psk_id : str
    psk_name : str
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
    
def reauthOrgDot1xWirelessClient(mist_session:_APISession, org_id:str, client_mac:str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/wi-fi/reauth-org-dot1x-wireless-client
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    client_mac : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/clients/{client_mac}/coa"
    resp = mist_session.mist_post(uri=uri)
    return resp
    