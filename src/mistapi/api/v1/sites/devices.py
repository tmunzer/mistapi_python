
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

def getSiteDevices(mist_session:_APISession, site_id:str, type:str="ap", name:str=None, page:int=1, limit:int=100) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteDevices
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str type(ap, switch, gateway, all) - device type
    :param str name
    :param int page
    :param int limit        
    """
    uri = f"/api/v1/sites/{site_id}/devices"
    query_params={}
    if type: query_params["type"]=type
    if name: query_params["name"]=name
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createSiteDevice(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createSiteDevice
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteDeviceRadioChannels(mist_session:_APISession, site_id:str, country_code:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteDeviceRadioChannels
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str country_code - country code for the site (for AP config generation), in [two-character](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)        
    """
    uri = f"/api/v1/sites/{site_id}/devices/ap_channels"
    query_params={}
    if country_code: query_params["country_code"]=country_code
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countSiteDeviceConfigHistory(mist_session:_APISession, site_id:str, distinct:str=None, mac:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteDeviceConfigHistory
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str distinct
    :param str mac
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/sites/{site_id}/devices/config_history/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if mac: query_params["mac"]=mac
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteDeviceConfigHistory(mist_session:_APISession, site_id:str, device_type:str="ap", mac:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteDeviceConfigHistory
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str device_type(ap, switch, gateway)
    :param str mac - Device MAC Address
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/sites/{site_id}/devices/config_history/search"
    query_params={}
    if device_type: query_params["device_type"]=device_type
    if mac: query_params["mac"]=mac
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countSiteDevices(mist_session:_APISession, site_id:str, distinct:str="model", hostname:str=None, model:str=None, mac:str=None, version:str=None, mxtunnel_status:str=None, mxedge_id:str=None, lldp_system_name:str=None, lldp_system_desc:str=None, lldp_port_id:str=None, lldp_mgmt_addr:str=None, map_id:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteDevices
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(model, version, map_id, hostname, mxtunnel_status, mxedge_id, lldp_system_name, lldp_system_desc, lldp_port_id, lldp_mgmt_addr)
    :param str hostname
    :param str model
    :param str mac
    :param str version
    :param str mxtunnel_status
    :param str mxedge_id
    :param str lldp_system_name
    :param str lldp_system_desc
    :param str lldp_port_id
    :param str lldp_mgmt_addr
    :param str map_id
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/sites/{site_id}/devices/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if hostname: query_params["hostname"]=hostname
    if model: query_params["model"]=model
    if mac: query_params["mac"]=mac
    if version: query_params["version"]=version
    if mxtunnel_status: query_params["mxtunnel_status"]=mxtunnel_status
    if mxedge_id: query_params["mxedge_id"]=mxedge_id
    if lldp_system_name: query_params["lldp_system_name"]=lldp_system_name
    if lldp_system_desc: query_params["lldp_system_desc"]=lldp_system_desc
    if lldp_port_id: query_params["lldp_port_id"]=lldp_port_id
    if lldp_mgmt_addr: query_params["lldp_mgmt_addr"]=lldp_mgmt_addr
    if map_id: query_params["map_id"]=map_id
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countSiteDeviceEvents(mist_session:_APISession, site_id:str, distinct:str="model", model:str=None, type:str=None, type_code:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteDeviceEvents
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(model, type, type_code, mac)
    :param str model
    :param str type
    :param str type_code
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/sites/{site_id}/devices/events/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if model: query_params["model"]=model
    if type: query_params["type"]=type
    if type_code: query_params["type_code"]=type_code
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteDeviceEvents(mist_session:_APISession, site_id:str, model:str=None, type:str=None, type_code:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteDeviceEvents
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str model
    :param str type
    :param str type_code
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/sites/{site_id}/devices/events/search"
    query_params={}
    if model: query_params["model"]=model
    if type: query_params["type"]=type
    if type_code: query_params["type_code"]=type_code
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def exportSiteDevices(mist_session:_APISession, site_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/exportSiteDevices
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/export"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def importSiteDevices(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/importSiteDevices
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/import"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def countSiteDeviceLastConfig(mist_session:_APISession, site_id:str, distinct:str="mac", page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteDeviceLastConfig
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(version, name, site_id, mac)
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/sites/{site_id}/devices/last_config/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteDeviceLastConfigs(mist_session:_APISession, site_id:str, device_type:str="ap", mac:str=None, version:str=None, name:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteDeviceLastConfigs
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str device_type(ap, switch, gateway)
    :param str mac
    :param str version
    :param str name
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/sites/{site_id}/devices/last_config/search"
    query_params={}
    if device_type: query_params["device_type"]=device_type
    if mac: query_params["mac"]=mac
    if version: query_params["version"]=version
    if name: query_params["name"]=name
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def reprovisionSiteAllAps(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/reprovisionSiteAllAps
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/reprovision"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def resetSiteAllApsToUseRrm(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/resetSiteAllApsToUseRrm
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/reset_radio_config"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def multiRestartSiteDevices(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/multiRestartSiteDevices
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/restart"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def searchSiteDevices(mist_session:_APISession, site_id:str, hostname:str=None, type:str="ap", model:str=None, mac:str=None, version:str=None, power_constrained:bool=None, ip_address:str=None, mxtunnel_status:str=None, mxedge_id:str=None, lldp_system_name:str=None, lldp_system_desc:str=None, lldp_port_id:str=None, lldp_mgmt_addr:str=None, band_24_channel:int=None, band_5_channel:int=None, band_6_channel:int=None, eth0_port_speed:int=None, sort:str="timestamp", desc_sort:str=None, stats:bool=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteDevices
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str hostname - partial / full hostname
    :param str type(ap, switch, gateway) - device type
    :param str model - device model
    :param str mac - device MAC
    :param str version - version
    :param bool power_constrained - power_constrained
    :param str ip_address
    :param str mxtunnel_status(up, down) - MxTunnel status, up / down
    :param str mxedge_id - Mist Edge id, if AP is connecting to a Mist Edge
    :param str lldp_system_name - LLDP system name
    :param str lldp_system_desc - LLDP system description
    :param str lldp_port_id - LLDP port id
    :param str lldp_mgmt_addr - LLDP management ip address
    :param int band_24_channel - Channel of band_24
    :param int band_5_channel - Channel of band_5
    :param int band_6_channel - Channel of band_6
    :param int eth0_port_speed - Port speed of eth0
    :param str sort(timestamp, mac, model, sku) - sort options
    :param str desc_sort(timestamp, mac, model, sku) - sort options in reverse order
    :param bool stats - whether to return device stats
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/sites/{site_id}/devices/search"
    query_params={}
    if hostname: query_params["hostname"]=hostname
    if type: query_params["type"]=type
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
    if band_24_channel: query_params["band_24_channel"]=band_24_channel
    if band_5_channel: query_params["band_5_channel"]=band_5_channel
    if band_6_channel: query_params["band_6_channel"]=band_6_channel
    if eth0_port_speed: query_params["eth0_port_speed"]=eth0_port_speed
    if sort: query_params["sort"]=sort
    if desc_sort: query_params["desc_sort"]=desc_sort
    if stats: query_params["stats"]=stats
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteDevicesUpgrade(mist_session:_APISession, site_id:str, status:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteDevicesUpgrade
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str status(downloading, completed, created, downloaded, upgrading, cancelled, failed)        
    """
    uri = f"/api/v1/sites/{site_id}/devices/upgrade"
    query_params={}
    if status: query_params["status"]=status
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def multiUpgradeSiteDevices(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/multiUpgradeSiteDevices
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/upgrade"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteUpgrade(mist_session:_APISession, site_id:str, upgrade_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteUpgrade
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str upgrade_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/upgrade/{upgrade_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def cancelSiteDeviceUpgrade(mist_session:_APISession, site_id:str, upgrade_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/cancelSiteDeviceUpgrade
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str upgrade_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/upgrade/{upgrade_id}/cancel"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteAvailableDeviceVersions(mist_session:_APISession, site_id:str, type:str="ap") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteAvailableDeviceVersions
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str type(ap, switch, gateway)        
    """
    uri = f"/api/v1/sites/{site_id}/devices/versions"
    query_params={}
    if type: query_params["type"]=type
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def zeroizeSiteFipsAllAps(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/zeroizeSiteFipsAllAps
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/zerioze"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteDevice(mist_session:_APISession, site_id:str, device_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteDevice
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteSiteDevice(mist_session:_APISession, site_id:str, device_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteSiteDevice
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateSiteDevice(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSiteDevice
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def arpFromDevice(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/arpFromDevice
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/arp"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def portsBounceFromSwitch(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/portsBounceFromSwitch
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/bounce_port"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def cableTestFromSwitch(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/cableTestFromSwitch
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/cable_test"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def startSiteSwitchRadiusSyntheticTest(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/startSiteSwitchRadiusSyntheticTest
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/check_radius_server"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def clearSiteSsrArpCache(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/clearSiteSsrArpCache
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/clear_arp"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def clearSiteSsrBgpRoutes(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/clearSiteSsrBgpRoutes
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/clear_bgp"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def clearBpduErrosFromPortsOnSwitch(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/clearBpduErrosFromPortsOnSwitch
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/clear_bpdu_error"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def clearAllLearnedMacsFromPortOnSwitch(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/clearAllLearnedMacsFromPortOnSwitch
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/clear_macs"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteDeviceConfigCmd(mist_session:_APISession, site_id:str, device_id:str, sort:str="false") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteDeviceConfigCmd
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    
    QUERY PARAMS
    ------------
    :param str sort(true, false) - Make output cmds sorted (for better readability) or not.        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/config_cmd"
    query_params={}
    if sort: query_params["sort"]=sort
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteSiteDeviceHaCluster(mist_session:_APISession, site_id:str, device_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteSiteDeviceHaCluster
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/ha"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def createSiteDeviceHaCluster(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createSiteDeviceHaCluster
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/ha"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def swapSiteDeviceHaClusterNode(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/swapSiteDeviceHaClusterNode
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/ha"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def getSiteDeviceIotPort(mist_session:_APISession, site_id:str, device_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteDeviceIotPort
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/iot"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def setSiteDeviceIotPort(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/setSiteDeviceIotPort
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/iot"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def deleteSiteLocalSwitchPortConfig(mist_session:_APISession, site_id:str, device_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteSiteLocalSwitchPortConfig
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/local_port_config"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateSiteLocalSwitchPortConfig(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSiteLocalSwitchPortConfig
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/local_port_config"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def startSiteLocateDevice(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/startSiteLocateDevice
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/locate"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def pingFromDevice(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/pingFromDevice
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/ping"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def pollSiteSwitchStats(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/pollSiteSwitchStats
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/poll_stats"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def releaseSiteSsrDhcpLease(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/releaseSiteSsrDhcpLease
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/release_dhcp"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteDeviceZtpPassword(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteDeviceZtpPassword
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/request_ztp_password"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def testSiteSsrDnsResolution(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/testSiteSsrDnsResolution
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/resolve_dns"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def restartSiteDevice(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/restartSiteDevice
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/restart"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def servicePingFromSsr(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/servicePingFromSsr
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/service_ping"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteSsrAndSrxRoutes(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteSsrAndSrxRoutes
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/show_route"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteSsrAndSrxSessions(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteSsrAndSrxSessions
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/show_session"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def createSiteDeviceSnapshot(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createSiteDeviceSnapshot
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/snapshot"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def uploadSiteDeviceSupportFile(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/uploadSiteDeviceSupportFile
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/support"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def StartSiteDeviceSyntheticTest(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/StartSiteDeviceSyntheticTest
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/synthetic_test"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def tracerouteFromDevice(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/tracerouteFromDevice
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/traceroute"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def stopSiteLocateDevice(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/stopSiteLocateDevice
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/unlocate"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def upgradeSiteDevice(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/upgradeSiteDevice
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/upgrade"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteVirtualChassis(mist_session:_APISession, site_id:str, device_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteVirtualChassis
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/vc"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteSiteVirtualChassis(mist_session:_APISession, site_id:str, device_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteSiteVirtualChassis
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/vc"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def createSiteVirtualChassis(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createSiteVirtualChassis
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/vc"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def removeSiteVirtualChassisMember(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/removeSiteVirtualChassisMember
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/vc"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def setSiteVcPort(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/setSiteVcPort
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/vc/vc_port"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def deleteSiteDeviceImage(mist_session:_APISession, site_id:str, device_id:str, image_name:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteSiteDeviceImage
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id
    :param str image_name        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/{image_name}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def addSiteDeviceImage(mist_session:_APISession, site_id:str, device_id:str, image_name:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/addSiteDeviceImage
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id
    :param str image_name        
    """
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/{image_name}"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    