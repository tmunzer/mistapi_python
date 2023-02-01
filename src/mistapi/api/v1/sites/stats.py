
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

def getSiteStats(mist_session:_APISession, site_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteStats
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/stats"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countSiteApps(mist_session:_APISession, site_id:str, distinct:str=None, device_mac:str=None, app:str=None, wired:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteApps
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(ap, wcid, ssid, wlan_id app, device_mac, src_ip, port_id, app, category, service) - Default for wireless devices is `ap`. Default for wired devices is `device_mac`
    :param str device_mac - MAC of the device
    :param str app - Application name
    :param str wired - If a device is wired or wireless. Default is False.        
    """
    uri = f"/api/v1/sites/{site_id}/stats/apps/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if device_mac: query_params["device_mac"]=device_mac
    if app: query_params["app"]=app
    if wired: query_params["wired"]=wired
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteAssetsStats(mist_session:_APISession, site_id:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteAssetsStats
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration        
    """
    uri = f"/api/v1/sites/{site_id}/stats/assets"
    query_params={}
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteAssetStats(mist_session:_APISession, site_id:str, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteAssetStats
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param int start
    :param int end
    :param str duration        
    """
    uri = f"/api/v1/sites/{site_id}/stats/assets/asset_id"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countSiteAssets(mist_session:_APISession, site_id:str, distinct:str="map_id") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteAssets
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(mac, map_id, ibeacon_uuid, ibeacon_major, ibeacon_minor, eddystone_uid_namespace, eddystone_uid_instance, eddystone_url, by, name, device_name)        
    """
    uri = f"/api/v1/sites/{site_id}/stats/assets/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteAssets(mist_session:_APISession, site_id:str, mac:str=None, map_id:str=None, ibeacon_uuid:str=None, ibeacon_major:int=None, ibeacon_minor:int=None, eddystone_uid_namespace:str=None, eddystone_uid_instance:str=None, eddystone_url:str=None, device_name:str=None, by:str=None, name:str=None, ap_mac:str=None, beam:str=None, rssi:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteAssets
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str mac
    :param str map_id
    :param str ibeacon_uuid
    :param int ibeacon_major
    :param int ibeacon_minor
    :param str eddystone_uid_namespace
    :param str eddystone_uid_instance
    :param str eddystone_url
    :param str device_name
    :param str by
    :param str name
    :param str ap_mac
    :param str beam
    :param str rssi
    :param int limit
    :param int start
    :param int end
    :param str duration        
    """
    uri = f"/api/v1/sites/{site_id}/stats/assets/search"
    query_params={}
    if mac: query_params["mac"]=mac
    if map_id: query_params["map_id"]=map_id
    if ibeacon_uuid: query_params["ibeacon_uuid"]=ibeacon_uuid
    if ibeacon_major: query_params["ibeacon_major"]=ibeacon_major
    if ibeacon_minor: query_params["ibeacon_minor"]=ibeacon_minor
    if eddystone_uid_namespace: query_params["eddystone_uid_namespace"]=eddystone_uid_namespace
    if eddystone_uid_instance: query_params["eddystone_uid_instance"]=eddystone_uid_instance
    if eddystone_url: query_params["eddystone_url"]=eddystone_url
    if device_name: query_params["device_name"]=device_name
    if by: query_params["by"]=by
    if name: query_params["name"]=name
    if ap_mac: query_params["ap_mac"]=ap_mac
    if beam: query_params["beam"]=beam
    if rssi: query_params["rssi"]=rssi
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteBeaconsStats(mist_session:_APISession, site_id:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteBeaconsStats
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration        
    """
    uri = f"/api/v1/sites/{site_id}/stats/beacons"
    query_params={}
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countSiteBgpStats(mist_session:_APISession, site_id:str, state:str=None, distinct:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteBgpStats
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str state
    :param str distinct        
    """
    uri = f"/api/v1/sites/{site_id}/stats/bgp_peers/count"
    query_params={}
    if state: query_params["state"]=state
    if distinct: query_params["distinct"]=distinct
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteBgpStats(mist_session:_APISession, site_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteBgpStats
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/stats/bgp_peers/search"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countSiteCalls(mist_session:_APISession, site_id:str, distrinct:str="mac", app:str=None, start:str=None, end:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteCalls
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str distrinct(mac)
    :param str app
    :param str start
    :param str end        
    """
    uri = f"/api/v1/sites/{site_id}/stats/calls/count"
    query_params={}
    if distrinct: query_params["distrinct"]=distrinct
    if app: query_params["app"]=app
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteCalls(mist_session:_APISession, site_id:str, mac:str=None, app:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteCalls
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str mac - device identifier
    :param str app - Third party app name
    :param int limit
    :param int start
    :param int end
    :param str duration        
    """
    uri = f"/api/v1/sites/{site_id}/stats/calls/search"
    query_params={}
    if mac: query_params["mac"]=mac
    if app: query_params["app"]=app
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteClientStats(mist_session:_APISession, site_id:str, client_mac:str, wired:bool=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteClientStats
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str client_mac        
    
    QUERY PARAMS
    ------------
    :param bool wired        
    """
    uri = f"/api/v1/sites/{site_id}/stats/clients/{client_mac}"
    query_params={}
    if wired: query_params["wired"]=wired
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteDevicesStats(mist_session:_APISession, site_id:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d", type:str="ap", status:str="all") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteDevicesStats
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration
    :param str type(ap, switch, gateways, all)
    :param str status(all, connected, disconnected)        
    """
    uri = f"/api/v1/sites/{site_id}/stats/devices"
    query_params={}
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if type: query_params["type"]=type
    if status: query_params["status"]=status
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteDeviceStats(mist_session:_APISession, site_id:str, device_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteDeviceStats
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/stats/devices/{device_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteAllClientsStatsByDevice(mist_session:_APISession, site_id:str, device_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteAllClientsStatsByDevice
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/stats/devices/{device_id}/clients"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteDiscoveredAssets(mist_session:_APISession, site_id:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteDiscoveredAssets
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration        
    """
    uri = f"/api/v1/sites/{site_id}/stats/discovered_assets"
    query_params={}
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteDiscoveredSwitchesMetrics(mist_session:_APISession, site_id:str, scope:str="site", type:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteDiscoveredSwitchesMetrics
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str scope(site, switch) - metric scope, optional
    :param str type(inactive_wired_vlans, switch_ap_affinity, poe_compliance, version_compliance) - metric type, inactive_wired_vlans/switch_ap_affinity/poe_compliance/version_compliance, optional
    :param int limit
    :param int start
    :param int end
    :param str duration        
    """
    uri = f"/api/v1/sites/{site_id}/stats/discovered_switch_metrics/search"
    query_params={}
    if scope: query_params["scope"]=scope
    if type: query_params["type"]=type
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countSiteDiscoveredSwitches(mist_session:_APISession, site_id:str, distinct:str="system_name", page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteDiscoveredSwitches
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(system_name, version, model, mgmt_addr)
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration        
    """
    uri = f"/api/v1/sites/{site_id}/stats/discovered_switches/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteDiscoveredSwitchesMetrics(mist_session:_APISession, site_id:str, threshold:str=None, system_name:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteDiscoveredSwitchesMetrics
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str threshold - configurable # ap per switch threshold, default 12
    :param str system_name - system name for switch level metrics, optional        
    """
    uri = f"/api/v1/sites/{site_id}/stats/discovered_switches/metrics"
    query_params={}
    if threshold: query_params["threshold"]=threshold
    if system_name: query_params["system_name"]=system_name
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteDiscoveredSwitches(mist_session:_APISession, site_id:str, adopted:bool=None, system_name:str=None, hostname:str=None, vendor:str=None, model:str=None, version:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteDiscoveredSwitches
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param bool adopted
    :param str system_name
    :param str hostname
    :param str vendor
    :param str model
    :param str version
    :param int limit
    :param int start
    :param int end
    :param str duration        
    """
    uri = f"/api/v1/sites/{site_id}/stats/discovered_switches/search"
    query_params={}
    if adopted: query_params["adopted"]=adopted
    if system_name: query_params["system_name"]=system_name
    if hostname: query_params["hostname"]=hostname
    if vendor: query_params["vendor"]=vendor
    if model: query_params["model"]=model
    if version: query_params["version"]=version
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteAssetsOfInterest(mist_session:_APISession, site_id:str, duration:str="1d", start:int=None, end:int=None, page:int=1, limit:int=100) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteAssetsOfInterest
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str duration
    :param int start
    :param int end
    :param int page
    :param int limit        
    """
    uri = f"/api/v1/sites/{site_id}/stats/filtered_assets"
    query_params={}
    if duration: query_params["duration"]=duration
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteGatwayMetrics(mist_session:_APISession, site_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteGatwayMetrics
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/stats/gateways/metrics"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteClientsStatsByMap(mist_session:_APISession, site_id:str, map_id:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteClientsStatsByMap
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str map_id        
    
    QUERY PARAMS
    ------------
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration        
    """
    uri = f"/api/v1/sites/{site_id}/stats/maps/{map_id}/clients"
    query_params={}
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteDiscoveredAssetByMap(mist_session:_APISession, site_id:str, map_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteDiscoveredAssetByMap
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str map_id        
    """
    uri = f"/api/v1/sites/{site_id}/stats/maps/{map_id}/discovered_assets"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteSdkStatsByMap(mist_session:_APISession, site_id:str, map_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteSdkStatsByMap
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str map_id        
    """
    uri = f"/api/v1/sites/{site_id}/stats/maps/{map_id}/sdkclients"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteUnconnectedClientStats(mist_session:_APISession, site_id:str, map_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteUnconnectedClientStats
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str map_id        
    """
    uri = f"/api/v1/sites/{site_id}/stats/maps/{map_id}/unconnected_clients"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteMxEdgesStats(mist_session:_APISession, site_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteMxEdgesStats
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/stats/mxedges"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteMxEdgeStats(mist_session:_APISession, site_id:str, mxedge_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteMxEdgeStats
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str mxedge_id        
    """
    uri = f"/api/v1/sites/{site_id}/stats/mxedges/{mxedge_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countSiteByDisctinctAttributesOPorts(mist_session:_APISession, site_id:str, distinct:str="mac", full_duplex:bool=None, mac:str=None, neighbor_mac:str=None, neighbor_port_desc:str=None, neighbor_system_name:str=None, poe_disabled:bool=None, poe_mode:str=None, poe_on:bool=None, port_id:str=None, port_mac:str=None, power_draw:float=None, tx_pkts:int=None, rx_pkts:int=None, rx_bytes:int=None, tx_bps:int=None, rx_bps:int=None, tx_mcast_pkts:int=None, tx_bcast_pkts:int=None, rx_mcast_pkts:int=None, rx_bcast_pkts:int=None, speed:int=None, stp_state:str=None, stp_role:str=None, auth_state:str=None, up:bool=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteByDisctinctAttributesOPorts
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(port_id, port_mac, full_duplex, mac, neighbor_mac, neighbor_port_desc, neighbor_system_name, poe_disabled, poe_mode, poe_on, speed, up) - port_id, port_mac, full_duplex, mac, neighbor_macneighbor_port_desc, neighbor_system_name, poe_disabled, poe_mode, poe_on, speed, up
    :param bool full_duplex - indicates full or half duplex
    :param str mac - device identifier
    :param str neighbor_mac - Chassis identifier of the chassis type listed
    :param str neighbor_port_desc - Description supplied by the system on the interface E.g. “GigabitEthernet2/0/39”
    :param str neighbor_system_name - Name supplied by the system on the interface E.g. neighbor system name E.g. “Kumar-Acc-SW.mist.local”
    :param bool poe_disabled - is the POE configured not be disabled.
    :param str poe_mode - poe mode depending on class E.g. “802.3at”
    :param bool poe_on - is the device attached to POE
    :param str port_id - interface name
    :param str port_mac - interface mac address
    :param float power_draw - Amount of power being used by the interface at the time the command is executed. Unit in watts.
    :param int tx_pkts - Output packets
    :param int rx_pkts - Input packets
    :param int rx_bytes - Input bytes
    :param int tx_bps - Output rate
    :param int rx_bps - Input rate
    :param int tx_mcast_pkts - Multicast output packets
    :param int tx_bcast_pkts - Broadcast output packets
    :param int rx_mcast_pkts - Multicast input packets
    :param int rx_bcast_pkts - Broadcast input packets
    :param int speed - port speed
    :param str stp_state(forwarding, blocking, learning, listening, disabled) - if `up`==`true`
    :param str stp_role(designated, backup, alternate, root, root-prevented) - if `up`==`true`
    :param str auth_state(init, authenticated, authenticating, held) - if `up`==`true` && has Authenticator role
    :param bool up - indicates if interface is up
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration        
    """
    uri = f"/api/v1/sites/{site_id}/stats/ports/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if full_duplex: query_params["full_duplex"]=full_duplex
    if mac: query_params["mac"]=mac
    if neighbor_mac: query_params["neighbor_mac"]=neighbor_mac
    if neighbor_port_desc: query_params["neighbor_port_desc"]=neighbor_port_desc
    if neighbor_system_name: query_params["neighbor_system_name"]=neighbor_system_name
    if poe_disabled: query_params["poe_disabled"]=poe_disabled
    if poe_mode: query_params["poe_mode"]=poe_mode
    if poe_on: query_params["poe_on"]=poe_on
    if port_id: query_params["port_id"]=port_id
    if port_mac: query_params["port_mac"]=port_mac
    if power_draw: query_params["power_draw"]=power_draw
    if tx_pkts: query_params["tx_pkts"]=tx_pkts
    if rx_pkts: query_params["rx_pkts"]=rx_pkts
    if rx_bytes: query_params["rx_bytes"]=rx_bytes
    if tx_bps: query_params["tx_bps"]=tx_bps
    if rx_bps: query_params["rx_bps"]=rx_bps
    if tx_mcast_pkts: query_params["tx_mcast_pkts"]=tx_mcast_pkts
    if tx_bcast_pkts: query_params["tx_bcast_pkts"]=tx_bcast_pkts
    if rx_mcast_pkts: query_params["rx_mcast_pkts"]=rx_mcast_pkts
    if rx_bcast_pkts: query_params["rx_bcast_pkts"]=rx_bcast_pkts
    if speed: query_params["speed"]=speed
    if stp_state: query_params["stp_state"]=stp_state
    if stp_role: query_params["stp_role"]=stp_role
    if auth_state: query_params["auth_state"]=auth_state
    if up: query_params["up"]=up
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteSwOrGwPorts(mist_session:_APISession, site_id:str, full_duplex:bool=None, mac:str=None, neighbor_mac:str=None, neighbor_port_desc:str=None, neighbor_system_name:str=None, poe_disabled:bool=None, poe_mode:str=None, poe_on:bool=None, port_id:str=None, port_mac:str=None, power_draw:float=None, tx_pkts:int=None, rx_pkts:int=None, rx_bytes:int=None, tx_bps:int=None, rx_bps:int=None, tx_errors:int=None, rx_errors:int=None, tx_mcast_pkts:int=None, tx_bcast_pkts:int=None, rx_mcast_pkts:int=None, rx_bcast_pkts:int=None, speed:int=None, mac_limit:int=None, mac_count:int=None, up:bool=None, stp_state:str=None, stp_role:str=None, xcvr_part_number:str=None, auth_state:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteSwOrGwPorts
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param bool full_duplex - indicates full or half duplex
    :param str mac - device identifier
    :param str neighbor_mac - Chassis identifier of the chassis type listed
    :param str neighbor_port_desc - Description supplied by the system on the interface E.g. “GigabitEthernet2/0/39”
    :param str neighbor_system_name - Name supplied by the system on the interface E.g. neighbor system name E.g. “Kumar-Acc-SW.mist.local”
    :param bool poe_disabled - is the POE configured not be disabled.
    :param str poe_mode - poe mode depending on class E.g. “802.3at”
    :param bool poe_on - is the device attached to POE
    :param str port_id - interface name
    :param str port_mac - interface mac address
    :param float power_draw - Amount of power being used by the interface at the time the command is executed. Unit in watts.
    :param int tx_pkts - Output packets
    :param int rx_pkts - Input packets
    :param int rx_bytes - Input bytes
    :param int tx_bps - Output rate
    :param int rx_bps - Input rate
    :param int tx_errors - Output errors
    :param int rx_errors - Input errors
    :param int tx_mcast_pkts - Multicast output packets
    :param int tx_bcast_pkts - Broadcast output packets
    :param int rx_mcast_pkts - Multicast input packets
    :param int rx_bcast_pkts - Broadcast input packets
    :param int speed - port speed
    :param int mac_limit - Limit on number of dynamically learned macs
    :param int mac_count - Number of mac addresses in the forwarding table
    :param bool up - indicates if interface is up
    :param str stp_state(forwarding, blocking, learning, listening, disabled) - if `up`==`true`
    :param str stp_role(designated, backup, alternate, root, root-prevented) - if `up`==`true`
    :param str xcvr_part_number - Optic Slot Partnumber, Check for null/empty
    :param str auth_state(init, authenticated, authenticating, held) - if `up`==`true` && has Authenticator role
    :param int limit
    :param int start
    :param int end
    :param str duration        
    """
    uri = f"/api/v1/sites/{site_id}/stats/ports/search"
    query_params={}
    if full_duplex: query_params["full_duplex"]=full_duplex
    if mac: query_params["mac"]=mac
    if neighbor_mac: query_params["neighbor_mac"]=neighbor_mac
    if neighbor_port_desc: query_params["neighbor_port_desc"]=neighbor_port_desc
    if neighbor_system_name: query_params["neighbor_system_name"]=neighbor_system_name
    if poe_disabled: query_params["poe_disabled"]=poe_disabled
    if poe_mode: query_params["poe_mode"]=poe_mode
    if poe_on: query_params["poe_on"]=poe_on
    if port_id: query_params["port_id"]=port_id
    if port_mac: query_params["port_mac"]=port_mac
    if power_draw: query_params["power_draw"]=power_draw
    if tx_pkts: query_params["tx_pkts"]=tx_pkts
    if rx_pkts: query_params["rx_pkts"]=rx_pkts
    if rx_bytes: query_params["rx_bytes"]=rx_bytes
    if tx_bps: query_params["tx_bps"]=tx_bps
    if rx_bps: query_params["rx_bps"]=rx_bps
    if tx_errors: query_params["tx_errors"]=tx_errors
    if rx_errors: query_params["rx_errors"]=rx_errors
    if tx_mcast_pkts: query_params["tx_mcast_pkts"]=tx_mcast_pkts
    if tx_bcast_pkts: query_params["tx_bcast_pkts"]=tx_bcast_pkts
    if rx_mcast_pkts: query_params["rx_mcast_pkts"]=rx_mcast_pkts
    if rx_bcast_pkts: query_params["rx_bcast_pkts"]=rx_bcast_pkts
    if speed: query_params["speed"]=speed
    if mac_limit: query_params["mac_limit"]=mac_limit
    if mac_count: query_params["mac_count"]=mac_count
    if up: query_params["up"]=up
    if stp_state: query_params["stp_state"]=stp_state
    if stp_role: query_params["stp_role"]=stp_role
    if xcvr_part_number: query_params["xcvr_part_number"]=xcvr_part_number
    if auth_state: query_params["auth_state"]=auth_state
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteSdkStats(mist_session:_APISession, site_id:str, sdkclient_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteSdkStats
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str sdkclient_id        
    """
    uri = f"/api/v1/sites/{site_id}/stats/sdkclients/{sdkclient_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countSiteByDisctinctAttributesOfSwitchPorts(mist_session:_APISession, site_id:str, distinct:str="mac", full_duplex:bool=None, mac:str=None, neighbor_mac:str=None, neighbor_port_desc:str=None, neighbor_system_name:str=None, poe_disabled:bool=None, poe_mode:str=None, poe_on:bool=None, port_id:str=None, port_mac:str=None, power_draw:float=None, tx_pkts:int=None, rx_pkts:int=None, rx_bytes:int=None, tx_bps:int=None, rx_bps:int=None, tx_mcast_pkts:int=None, tx_bcast_pkts:int=None, rx_mcast_pkts:int=None, rx_bcast_pkts:int=None, speed:int=None, stp_state:str=None, stp_role:str=None, auth_state:str=None, up:bool=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteByDisctinctAttributesOfSwitchPorts
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(port_id, port_mac, full_duplex, mac, neighbor_mac, neighbor_port_desc, neighbor_system_name, poe_disabled, poe_mode, poe_on, speed, up) - port_id, port_mac, full_duplex, mac, neighbor_macneighbor_port_desc, neighbor_system_name, poe_disabled, poe_mode, poe_on, speed, up
    :param bool full_duplex - indicates full or half duplex
    :param str mac - device identifier
    :param str neighbor_mac - Chassis identifier of the chassis type listed
    :param str neighbor_port_desc - Description supplied by the system on the interface E.g. “GigabitEthernet2/0/39”
    :param str neighbor_system_name - Name supplied by the system on the interface E.g. neighbor system name E.g. “Kumar-Acc-SW.mist.local”
    :param bool poe_disabled - is the POE configured not be disabled.
    :param str poe_mode - poe mode depending on class E.g. “802.3at”
    :param bool poe_on - is the device attached to POE
    :param str port_id - interface name
    :param str port_mac - interface mac address
    :param float power_draw - Amount of power being used by the interface at the time the command is executed. Unit in watts.
    :param int tx_pkts - Output packets
    :param int rx_pkts - Input packets
    :param int rx_bytes - Input bytes
    :param int tx_bps - Output rate
    :param int rx_bps - Input rate
    :param int tx_mcast_pkts - Multicast output packets
    :param int tx_bcast_pkts - Broadcast output packets
    :param int rx_mcast_pkts - Multicast input packets
    :param int rx_bcast_pkts - Broadcast input packets
    :param int speed - port speed
    :param str stp_state(forwarding, blocking, learning, listening, disabled) - if `up`==`true`
    :param str stp_role(designated, backup, alternate, root, root-prevented) - if `up`==`true`
    :param str auth_state(init, authenticated, authenticating, held) - if `up`==`true`
    :param bool up - indicates if interface is up
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration        
    """
    uri = f"/api/v1/sites/{site_id}/stats/switch_ports/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if full_duplex: query_params["full_duplex"]=full_duplex
    if mac: query_params["mac"]=mac
    if neighbor_mac: query_params["neighbor_mac"]=neighbor_mac
    if neighbor_port_desc: query_params["neighbor_port_desc"]=neighbor_port_desc
    if neighbor_system_name: query_params["neighbor_system_name"]=neighbor_system_name
    if poe_disabled: query_params["poe_disabled"]=poe_disabled
    if poe_mode: query_params["poe_mode"]=poe_mode
    if poe_on: query_params["poe_on"]=poe_on
    if port_id: query_params["port_id"]=port_id
    if port_mac: query_params["port_mac"]=port_mac
    if power_draw: query_params["power_draw"]=power_draw
    if tx_pkts: query_params["tx_pkts"]=tx_pkts
    if rx_pkts: query_params["rx_pkts"]=rx_pkts
    if rx_bytes: query_params["rx_bytes"]=rx_bytes
    if tx_bps: query_params["tx_bps"]=tx_bps
    if rx_bps: query_params["rx_bps"]=rx_bps
    if tx_mcast_pkts: query_params["tx_mcast_pkts"]=tx_mcast_pkts
    if tx_bcast_pkts: query_params["tx_bcast_pkts"]=tx_bcast_pkts
    if rx_mcast_pkts: query_params["rx_mcast_pkts"]=rx_mcast_pkts
    if rx_bcast_pkts: query_params["rx_bcast_pkts"]=rx_bcast_pkts
    if speed: query_params["speed"]=speed
    if stp_state: query_params["stp_state"]=stp_state
    if stp_role: query_params["stp_role"]=stp_role
    if auth_state: query_params["auth_state"]=auth_state
    if up: query_params["up"]=up
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteSwitchPorts(mist_session:_APISession, site_id:str, full_duplex:bool=None, mac:str=None, neighbor_mac:str=None, neighbor_port_desc:str=None, neighbor_system_name:str=None, poe_disabled:bool=None, poe_mode:str=None, poe_on:bool=None, port_id:str=None, port_mac:str=None, power_draw:float=None, tx_pkts:int=None, rx_pkts:int=None, rx_bytes:int=None, tx_bps:int=None, rx_bps:int=None, tx_mcast_pkts:int=None, tx_bcast_pkts:int=None, rx_mcast_pkts:int=None, rx_bcast_pkts:int=None, speed:int=None, stp_state:str=None, stp_role:str=None, auth_state:str=None, up:bool=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteSwitchPorts
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param bool full_duplex - indicates full or half duplex
    :param str mac - device identifier
    :param str neighbor_mac - Chassis identifier of the chassis type listed
    :param str neighbor_port_desc - Description supplied by the system on the interface E.g. “GigabitEthernet2/0/39”
    :param str neighbor_system_name - Name supplied by the system on the interface E.g. neighbor system name E.g. “Kumar-Acc-SW.mist.local”
    :param bool poe_disabled - is the POE configured not be disabled.
    :param str poe_mode - poe mode depending on class E.g. “802.3at”
    :param bool poe_on - is the device attached to POE
    :param str port_id - interface name
    :param str port_mac - interface mac address
    :param float power_draw - Amount of power being used by the interface at the time the command is executed. Unit in watts.
    :param int tx_pkts - Output packets
    :param int rx_pkts - Input packets
    :param int rx_bytes - Input bytes
    :param int tx_bps - Output rate
    :param int rx_bps - Input rate
    :param int tx_mcast_pkts - Multicast output packets
    :param int tx_bcast_pkts - Broadcast output packets
    :param int rx_mcast_pkts - Multicast input packets
    :param int rx_bcast_pkts - Broadcast input packets
    :param int speed - port speed
    :param str stp_state(forwarding, blocking, learning, listening, disabled) - if `up`==`true`
    :param str stp_role(designated, backup, alternate, root, root-prevented) - if `up`==`true`
    :param str auth_state(init, authenticated, authenticating, held) - if `up`==`true` && has Authenticator role
    :param bool up - indicates if interface is up
    :param int limit
    :param int start
    :param int end
    :param str duration        
    """
    uri = f"/api/v1/sites/{site_id}/stats/switch_ports/search"
    query_params={}
    if full_duplex: query_params["full_duplex"]=full_duplex
    if mac: query_params["mac"]=mac
    if neighbor_mac: query_params["neighbor_mac"]=neighbor_mac
    if neighbor_port_desc: query_params["neighbor_port_desc"]=neighbor_port_desc
    if neighbor_system_name: query_params["neighbor_system_name"]=neighbor_system_name
    if poe_disabled: query_params["poe_disabled"]=poe_disabled
    if poe_mode: query_params["poe_mode"]=poe_mode
    if poe_on: query_params["poe_on"]=poe_on
    if port_id: query_params["port_id"]=port_id
    if port_mac: query_params["port_mac"]=port_mac
    if power_draw: query_params["power_draw"]=power_draw
    if tx_pkts: query_params["tx_pkts"]=tx_pkts
    if rx_pkts: query_params["rx_pkts"]=rx_pkts
    if rx_bytes: query_params["rx_bytes"]=rx_bytes
    if tx_bps: query_params["tx_bps"]=tx_bps
    if rx_bps: query_params["rx_bps"]=rx_bps
    if tx_mcast_pkts: query_params["tx_mcast_pkts"]=tx_mcast_pkts
    if tx_bcast_pkts: query_params["tx_bcast_pkts"]=tx_bcast_pkts
    if rx_mcast_pkts: query_params["rx_mcast_pkts"]=rx_mcast_pkts
    if rx_bcast_pkts: query_params["rx_bcast_pkts"]=rx_bcast_pkts
    if speed: query_params["speed"]=speed
    if stp_state: query_params["stp_state"]=stp_state
    if stp_role: query_params["stp_role"]=stp_role
    if auth_state: query_params["auth_state"]=auth_state
    if up: query_params["up"]=up
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteAdoptedSwitchesComplianceMetrics(mist_session:_APISession, site_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteAdoptedSwitchesComplianceMetrics
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/stats/switches/metrics"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteWxRulesUsage(mist_session:_APISession, site_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteWxRulesUsage
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/stats/wxrules"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteZonesStats(mist_session:_APISession, site_id:str, map_id:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteZonesStats
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str map_id        
    """
    uri = f"/api/v1/sites/{site_id}/stats/zones"
    query_params={}
    if map_id: query_params["map_id"]=map_id
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteZoneStats(mist_session:_APISession, site_id:str, zone_type:str, zone_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteZoneStats
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str zone_type(zones, rssizones)
    :param str zone_id        
    """
    uri = f"/api/v1/sites/{site_id}/stats/{zone_type}/{zone_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    