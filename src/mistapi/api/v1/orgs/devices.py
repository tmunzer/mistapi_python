
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

def getOrgDevices(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgDevices
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/devices"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countOrgDevices(mist_session:_APISession, org_id:str, distinct:str, hostname:str=None, site_id:str=None, model:str=None, mac:str=None, version:str=None, ip_address:str=None, mxtunnel_status:str=None, mxedge_id:str=None, lldp_system_name:str=None, lldp_system_desc:str=None, lldp_port_id:str=None, lldp_mgmt_addr:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countOrgDevices
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(hostname, site_id, model, mac, version, ip, mxtunnel_status, mxedge_id, lldp_system_name, lldp_system_desc, lldp_port_id, lldp_mgmt_addr)
    :param str hostname - partial / full hostname
    :param str site_id - site id
    :param str model - device model
    :param str mac - AP mac
    :param str version - version
    :param str ip_address
    :param str mxtunnel_status(up, down) - MxTunnel status, up / down
    :param str mxedge_id - Mist Edge id, if AP is connecting to a Mist Edge
    :param str lldp_system_name - LLDP system name
    :param str lldp_system_desc - LLDP system description
    :param str lldp_port_id - LLDP port id
    :param str lldp_mgmt_addr - LLDP management ip address
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
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
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(org_id, site_id, ap, apfw, model, text, timestamp, type)
    :param str site_id - site id
    :param str ap - AP mac
    :param str apfw - AP Firmware
    :param str model - device model
    :param str text - event message
    :param str timestamp - event time
    :param str type(AP_CONFIG_CHANGED_BY_RRM, AP_CONFIG_CHANGED_BY_USER, AP_CONFIGURED, AP_RECONFIGURED, AP_RESTARTED, AP_RESTART_BY_USER, AP_RRM_ACTION, CLIENT_DNS_OK, MARVIS_DNS_FAILURE) - Events Type
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
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
    
def searchOrgDevicesEvents(mist_session:_APISession, org_id:str, site_id:str=None, ap:str=None, apfw:str=None, model:str=None, text:str=None, timestamp:str=None, type:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchOrgDevicesEvents
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str site_id - site id
    :param str ap - AP mac
    :param str apfw - AP Firmware
    :param str model - device model
    :param str text - event message
    :param str timestamp - event time
    :param str type(AP_CONFIG_CHANGED_BY_RRM, AP_CONFIG_CHANGED_BY_USER, AP_CONFIGURED, AP_RECONFIGURED, AP_RESTARTED, AP_RESTART_BY_USER, AP_RRM_ACTION, CLIENT_DNS_OK, MARVIS_DNS_FAILURE) - Events Type
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/orgs/{org_id}/devices/events/search"
    query_params={}
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
    
def countOrgDeviceLastConfigs(mist_session:_APISession, org_id:str, device_type:str="ap", distinct:str=None, start:int=None, end:int=None, limit:int=100) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countOrgDeviceLastConfigs
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str device_type(ap, switch, gateway)
    :param str distinct(mac, version, name, site_id)
    :param int start
    :param int end
    :param int limit        
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
    
def searchOrgDeviceLastConfig(mist_session:_APISession, org_id:str, device_type:str="ap", mac:str=None, start:int=None, end:int=None, limit:int=100) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchOrgDeviceLastConfig
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str device_type(ap, switch, gateway)
    :param str mac
    :param int start
    :param int end
    :param int limit        
    """
    uri = f"/api/v1/orgs/{org_id}/devices/last_config/search"
    query_params={}
    if device_type: query_params["device_type"]=device_type
    if mac: query_params["mac"]=mac
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getOrgApsMacs(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgApsMacs
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/devices/radio_macs"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchOrgDevices(mist_session:_APISession, org_id:str, hostname:str=None, site_id:str=None, model:str=None, mac:str=None, version:str=None, power_constrained:bool=None, ip_address:str=None, mxtunnel_status:str=None, mxedge_id:str=None, lldp_system_name:str=None, lldp_system_desc:str=None, lldp_port_id:str=None, lldp_mgmt_addr:str=None, band_24_bandwith:int=None, band_5_bandwith:int=None, band_6_bandwith:int=None, band_24_channel:int=None, band_5_channel:int=None, band_6_channel:int=None, eth0_port_speed:int=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchOrgDevices
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str hostname - partial / full hostname
    :param str site_id - site id
    :param str model - device model
    :param str mac - AP mac
    :param str version - version
    :param bool power_constrained - power_constrained
    :param str ip_address
    :param str mxtunnel_status(up, down) - MxTunnel status, up / down
    :param str mxedge_id - Mist Edge id, if AP is connecting to a Mist Edge
    :param str lldp_system_name - LLDP system name
    :param str lldp_system_desc - LLDP system description
    :param str lldp_port_id - LLDP port id
    :param str lldp_mgmt_addr - LLDP management ip address
    :param int band_24_bandwith - Bandwith of band_24
    :param int band_5_bandwith - Bandwith of band_5
    :param int band_6_bandwith - Bandwith of band_6
    :param int band_24_channel - Channel of band_24
    :param int band_5_channel - Channel of band_5
    :param int band_6_channel - Channel of band_6
    :param int eth0_port_speed - Port speed of eth0
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
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
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getOrgMultiSitesDevicesUpgrades(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgMultiSitesDevicesUpgrades
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/devices/upgrade"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def upgradeOrgMultiSitesDevices(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/upgradeOrgMultiSitesDevices
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/devices/upgrade"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgMultiSitesUpgrade(mist_session:_APISession, org_id:str, upgrade_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgMultiSitesUpgrade
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str upgrade_id        
    """
    uri = f"/api/v1/orgs/{org_id}/devices/upgrade/{upgrade_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    