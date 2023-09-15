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

@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.44.2", details="function replaced with listOrgDevices")  
def getOrgDevices(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgDevices
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/devices"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listOrgDevices(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgDevices
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/devices"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countOrgDevices(mist_session:_APISession, org_id:str, distinct:str, hostname:str=None, site_id:str=None, model:str=None, mac:str=None, version:str=None, ip_address:str=None, mxtunnel_status:str=None, mxedge_id:str=None, lldp_system_name:str=None, lldp_system_desc:str=None, lldp_port_id:str=None, lldp_mgmt_addr:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countOrgDevices
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'hostname', 'site_id', 'model', 'mac', 'version', 'ip', 'mxtunnel_status', 'mxedge_id', 'lldp_system_name', 'lldp_system_desc', 'lldp_port_id', 'lldp_mgmt_addr'}, default: model
    hostname : str
      partial / full hostname
    site_id : str
      site id
    model : str
      device model
    mac : str
      AP mac
    version : str
      version
    ip_address : str
    mxtunnel_status : str{'up', 'down'}
      MxTunnel status, up / down
    mxedge_id : str
      Mist Edge id, if AP is connecting to a Mist Edge
    lldp_system_name : str
      LLDP system name
    lldp_system_desc : str
      LLDP system description
    lldp_port_id : str
      LLDP port id
    lldp_mgmt_addr : str
      LLDP management ip address
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
    uri = f"/api/v1/orgs/{org_id}/devices/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if hostname: query_params["hostname"]=hostname
    if site_id: query_params["site_id"]=site_id
    if model: query_params["model"]=model
    if mac: query_params["mac"]=mac
    if version: query_params["version"]=version
    if ip_address: query_params["ip_address"]=ip_address
    if mxtunnel_status: query_params["mxtunnel_status"]=mxtunnel_status
    if mxedge_id: query_params["mxedge_id"]=mxedge_id
    if lldp_system_name: query_params["lldp_system_name"]=lldp_system_name
    if lldp_system_desc: query_params["lldp_system_desc"]=lldp_system_desc
    if lldp_port_id: query_params["lldp_port_id"]=lldp_port_id
    if lldp_mgmt_addr: query_params["lldp_mgmt_addr"]=lldp_mgmt_addr
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countOrgDevicesEvents(mist_session:_APISession, org_id:str, distinct:str, site_id:str=None, ap:str=None, apfw:str=None, model:str=None, text:str=None, timestamp:str=None, type:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countOrgDevicesEvents
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'org_id', 'site_id', 'ap', 'apfw', 'model', 'text', 'timestamp', 'type'}, default: model
    site_id : str
      site id
    ap : str
      AP mac
    apfw : str
      AP Firmware
    model : str
      device model
    text : str
      event message
    timestamp : str
      event time
    type : str
      Events Type
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
    uri = f"/api/v1/orgs/{org_id}/devices/events/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if site_id: query_params["site_id"]=site_id
    if ap: query_params["ap"]=ap
    if apfw: query_params["apfw"]=apfw
    if model: query_params["model"]=model
    if text: query_params["text"]=text
    if timestamp: query_params["timestamp"]=timestamp
    if type: query_params["type"]=type
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchOrgDevicesEvents(mist_session:_APISession, org_id:str, mac:str=None, model:str=None, device_type:str="ap", text:str=None, timestamp:str=None, type:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchOrgDevicesEvents
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    mac : str
      device mac
    model : str
      device model
    device_type : str{'ap', 'switch', 'gateway'}, default: ap
      device type
    text : str
      event message
    timestamp : str
      event time
    type : str
      see [listDeviceEventsDefinitions](/#operation/listDeviceEventsDefinitions)
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/devices/events/search"
    query_params={}
    if mac: query_params["mac"]=mac
    if model: query_params["model"]=model
    if device_type: query_params["device_type"]=device_type
    if text: query_params["text"]=text
    if timestamp: query_params["timestamp"]=timestamp
    if type: query_params["type"]=type
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countOrgDeviceLastConfigs(mist_session:_APISession, org_id:str, device_type:str="ap", distinct:str=None, start:int=None, end:int=None, limit:int=100) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countOrgDeviceLastConfigs
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    device_type : str{'ap', 'switch', 'gateway'}, default: ap
    distinct : str{'mac', 'version', 'name', 'site_id'}
    start : int
    end : int
    limit : int, default: 100        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/devices/last_config/count"
    query_params={}
    if device_type: query_params["device_type"]=device_type
    if distinct: query_params["distinct"]=distinct
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchOrgDeviceLastConfigs(mist_session:_APISession, org_id:str, device_type:str="ap", mac:str=None, name:str=None, version:str=None, start:int=None, end:int=None, limit:int=100, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchOrgDeviceLastConfigs
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    device_type : str{'ap', 'switch', 'gateway'}, default: ap
    mac : str
    name : str
    version : str
    start : int
    end : int
    limit : int, default: 100
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/devices/last_config/search"
    query_params={}
    if device_type: query_params["device_type"]=device_type
    if mac: query_params["mac"]=mac
    if name: query_params["name"]=name
    if version: query_params["version"]=version
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if limit: query_params["limit"]=limit
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.44.2", details="function replaced with listOrgApsMacs")  
def getOrgApsMacs(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgApsMacs
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/devices/radio_macs"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listOrgApsMacs(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgApsMacs
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/devices/radio_macs"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchOrgDevices(mist_session:_APISession, org_id:str, hostname:str=None, site_id:str=None, model:str=None, mac:str=None, version:str=None, power_constrained:bool=None, ip_address:str=None, mxtunnel_status:str=None, mxedge_id:str=None, lldp_system_name:str=None, lldp_system_desc:str=None, lldp_port_id:str=None, lldp_mgmt_addr:str=None, band_24_bandwith:int=None, band_5_bandwith:int=None, band_6_bandwith:int=None, band_24_channel:int=None, band_5_channel:int=None, band_6_channel:int=None, eth0_port_speed:int=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchOrgDevices
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    hostname : str
      partial / full hostname
    site_id : str
      site id
    model : str
      device model
    mac : str
      AP mac
    version : str
      version
    power_constrained : bool
      power_constrained
    ip_address : str
    mxtunnel_status : str{'up', 'down'}
      MxTunnel status, up / down
    mxedge_id : str
      Mist Edge id, if AP is connecting to a Mist Edge
    lldp_system_name : str
      LLDP system name
    lldp_system_desc : str
      LLDP system description
    lldp_port_id : str
      LLDP port id
    lldp_mgmt_addr : str
      LLDP management ip address
    band_24_bandwith : int
      Bandwith of band_24
    band_5_bandwith : int
      Bandwith of band_5
    band_6_bandwith : int
      Bandwith of band_6
    band_24_channel : int
      Channel of band_24
    band_5_channel : int
      Channel of band_5
    band_6_channel : int
      Channel of band_6
    eth0_port_speed : int
      Port speed of eth0
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/devices/search"
    query_params={}
    if hostname: query_params["hostname"]=hostname
    if site_id: query_params["site_id"]=site_id
    if model: query_params["model"]=model
    if mac: query_params["mac"]=mac
    if version: query_params["version"]=version
    if power_constrained: query_params["power_constrained"]=power_constrained
    if ip_address: query_params["ip_address"]=ip_address
    if mxtunnel_status: query_params["mxtunnel_status"]=mxtunnel_status
    if mxedge_id: query_params["mxedge_id"]=mxedge_id
    if lldp_system_name: query_params["lldp_system_name"]=lldp_system_name
    if lldp_system_desc: query_params["lldp_system_desc"]=lldp_system_desc
    if lldp_port_id: query_params["lldp_port_id"]=lldp_port_id
    if lldp_mgmt_addr: query_params["lldp_mgmt_addr"]=lldp_mgmt_addr
    if band_24_bandwith: query_params["band_24_bandwith"]=band_24_bandwith
    if band_5_bandwith: query_params["band_5_bandwith"]=band_5_bandwith
    if band_6_bandwith: query_params["band_6_bandwith"]=band_6_bandwith
    if band_24_channel: query_params["band_24_channel"]=band_24_channel
    if band_5_channel: query_params["band_5_channel"]=band_5_channel
    if band_6_channel: query_params["band_6_channel"]=band_6_channel
    if eth0_port_speed: query_params["eth0_port_speed"]=eth0_port_speed
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.44.2", details="function replaced with listOrgMultiSitesDevicesUpgrades")  
def getOrgMultiSitesDevicesUpgrades(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgMultiSitesDevicesUpgrades
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/devices/upgrade"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listOrgMultiSitesDevicesUpgrades(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgMultiSitesDevicesUpgrades
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/devices/upgrade"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def upgradeOrgMultiSitesDevices(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/upgradeOrgMultiSitesDevices
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/devices/upgrade"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgMultiSitesUpgrade(mist_session:_APISession, org_id:str, upgrade_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgMultiSitesUpgrade
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    upgrade_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/devices/upgrade/{upgrade_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    