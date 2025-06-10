'''
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
'''

from typing import Union, Awaitable
from mistapi import APISession as _APISession
from mistapi.__decorator import sync_async_compatible
from mistapi.__api_response import APIResponse as _APIResponse
import deprecation

@sync_async_compatible
def countSiteWirelessClients(mist_session:_APISession, site_id:str, distinct:str="device", ssid:str=None, ap:str=None, ip_address:str=None, vlan:str=None, hostname:str=None, os:str=None, model:str=None, device:str=None, start:int=None, end:int=None, duration:str="1d", limit:int=100) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/clients/wireless/count-site-wireless-clients
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'ap', 'device', 'hostname', 'ip', 'model', 'os', 'ssid', 'vlan'}, default: device
    ssid : str
    ap : str
    ip_address : str
    vlan : str
    hostname : str
    os : str
    model : str
    device : str
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100        
    
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
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def disconnectSiteMultipleClients(mist_session:_APISession, site_id:str, body:object) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/wi-fi/disconnect-site-multiple-clients
    
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
    
@sync_async_compatible
def countSiteWirelessClientEvents(mist_session:_APISession, site_id:str, distinct:str=None, type:str=None, reason_code:int=None, ssid:str=None, ap:str=None, proto:str=None, band:str=None, wlan_id:str=None, start:int=None, end:int=None, duration:str="1d", limit:int=100) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/clients/wireless/count-site-wireless-client-events
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'band', 'channel', 'proto', 'ssid', 'type', 'wlan_id'}
    type : str
    reason_code : int
    ssid : str
    ap : str
    proto : str{'a', 'ac', 'ax', 'b', 'g', 'n'}
      a / b / g / n / ac / ax
    band : str{'24', '5', '6'}
      802.11 Band
    wlan_id : str
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100        
    
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
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def searchSiteWirelessClientEvents(mist_session:_APISession, site_id:str, type:str=None, reason_code:int=None, ssid:str=None, ap:str=None, proto:str=None, band:str=None, wlan_id:str=None, nacrule_id:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/clients/wireless/search-site-wireless-client-events
    
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
    
@sync_async_compatible
def searchSiteWirelessClients(mist_session:_APISession, site_id:str, mac:str=None, ip_address:str=None, hostname:str=None, device:str=None, os:str=None, model:str=None, ap:str=None, ssid:str=None, text:str=None, nacrule_id:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/clients/wireless/search-site-wireless-clients
    
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
    ip_address : str
    hostname : str
    device : str
    os : str
    model : str
    ap : str
    ssid : str
    text : str
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
    
@sync_async_compatible
def countSiteWirelessClientSessions(mist_session:_APISession, site_id:str, distinct:str="mac", ap:str=None, band:str=None, client_family:str=None, client_manufacture:str=None, client_model:str=None, client_os:str=None, ssid:str=None, wlan_id:str=None, start:int=None, end:int=None, duration:str="1d", limit:int=100) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/clients/wireless/count-site-wireless-client-sessions
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'ap', 'client_family', 'client_manufacture', 'client_model', 'client_os', 'mac', 'ssid', 'wlan_id'}, default: mac
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
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def searchSiteWirelessClientSessions(mist_session:_APISession, site_id:str, ap:str=None, band:str=None, client_family:str=None, client_manufacture:str=None, client_model:str=None, client_username:str=None, client_os:str=None, ssid:str=None, wlan_id:str=None, psk_id:str=None, psk_name:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/clients/wireless/search-site-wireless-client-sessions
    
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
    
@sync_async_compatible
def unauthorizeSiteMultipleClients(mist_session:_APISession, site_id:str, body:object) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/wi-fi/unauthorize-site-multiple-clients
    
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
    
@sync_async_compatible
def reauthSiteDot1xWirelessClient(mist_session:_APISession, site_id:str, client_mac:str) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/wi-fi/reauth-site-dot1x-wireless-client
    
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
    
@sync_async_compatible
def disconnectSiteWirelessClient(mist_session:_APISession, site_id:str, client_mac:str) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/wi-fi/disconnect-site-wireless-client
    
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
    
@sync_async_compatible
def getSiteEventsForClient(mist_session:_APISession, site_id:str, client_mac:str, type:str=None, proto:str=None, band:str=None, channel:str=None, wlan_id:str=None, ssid:str=None, start:int=None, end:int=None, duration:str="1d", limit:int=100, page:int=1) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/clients/wireless/get-site-events-for-client
    
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
    type : str
    proto : str{'a', 'ac', 'ax', 'b', 'g', 'n'}
      a / b / g / n / ac / ax
    band : str{'24', '5', '6'}
      802.11 Band
    channel : str
    wlan_id : str
    ssid : str
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
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def unauthorizeSiteWirelessClient(mist_session:_APISession, site_id:str, client_mac:str) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/wi-fi/unauthorize-site-wireless-client
    
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
    