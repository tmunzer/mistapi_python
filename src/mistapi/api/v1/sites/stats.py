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

def getSiteStats(mist_session:_APISession, site_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countSiteApps(mist_session:_APISession, site_id:str, distinct:str=None, device_mac:str=None, app:str=None, wired:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteApps
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'ap', 'wcid', 'ssid', 'wlan_id app', 'device_mac', 'src_ip', 'port_id', 'app', 'category', 'service'}
      Default for wireless devices is `ap`. Default for wired devices is `device_mac`
    device_mac : str
      MAC of the device
    app : str
      Application name
    wired : str
      If a device is wired or wireless. Default is False.        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/apps/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if device_mac: query_params["device_mac"]=device_mac
    if app: query_params["app"]=app
    if wired: query_params["wired"]=wired
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.41.5", details="function replaced with listSiteAssetsStats")  
def getSiteAssetsStats(mist_session:_APISession, site_id:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteAssetsStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
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
    uri = f"/api/v1/sites/{site_id}/stats/assets"
    query_params={}
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listSiteAssetsStats(mist_session:_APISession, site_id:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteAssetsStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
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
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
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
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'mac', 'map_id', 'ibeacon_uuid', 'ibeacon_major', 'ibeacon_minor', 'eddystone_uid_namespace', 'eddystone_uid_instance', 'eddystone_url', 'by', 'name', 'device_name'}, default: map_id        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/assets/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteAssets(mist_session:_APISession, site_id:str, mac:str=None, map_id:str=None, ibeacon_uuid:str=None, ibeacon_major:int=None, ibeacon_minor:int=None, eddystone_uid_namespace:str=None, eddystone_uid_instance:str=None, eddystone_url:str=None, device_name:str=None, by:str=None, name:str=None, ap_mac:str=None, beam:str=None, rssi:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteAssets
    
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
    map_id : str
    ibeacon_uuid : str
    ibeacon_major : int
    ibeacon_minor : int
    eddystone_uid_namespace : str
    eddystone_uid_instance : str
    eddystone_url : str
    device_name : str
    by : str
    name : str
    ap_mac : str
    beam : str
    rssi : str
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
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
    
@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.41.5", details="function replaced with listSiteBeaconsStats")  
def getSiteBeaconsStats(mist_session:_APISession, site_id:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteBeaconsStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
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
    uri = f"/api/v1/sites/{site_id}/stats/beacons"
    query_params={}
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listSiteBeaconsStats(mist_session:_APISession, site_id:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteBeaconsStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
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
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    state : str
    distinct : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
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
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/bgp_peers/search"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countSiteCalls(mist_session:_APISession, site_id:str, distrinct:str="mac", rating:int=None, app:str=None, start:str=None, end:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteCalls
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distrinct : str{'mac'}, default: mac
    rating : int
      feedback rating (e.g. "rating=1" or "rating=1,2")
    app : str
    start : str
    end : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/calls/count"
    query_params={}
    if distrinct: query_params["distrinct"]=distrinct
    if rating: query_params["rating"]=rating
    if app: query_params["app"]=app
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteCalls(mist_session:_APISession, site_id:str, mac:str=None, app:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteCalls
    
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
      device identifier
    app : str
      Third party app name
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
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
    
@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.41.5", details="function replaced with listSiteWirelessClientsStats")  
def getSiteWirelessClientsStats(mist_session:_APISession, site_id:str, wired:bool=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteWirelessClientsStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    wired : bool        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/clients"
    query_params={}
    if wired: query_params["wired"]=wired
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listSiteWirelessClientsStats(mist_session:_APISession, site_id:str, wired:bool=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteWirelessClientsStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    wired : bool        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/clients"
    query_params={}
    if wired: query_params["wired"]=wired
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteWirelessClientStats(mist_session:_APISession, site_id:str, client_mac:str, wired:bool=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteWirelessClientStats
    
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
    wired : bool        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/clients/{client_mac}"
    query_params={}
    if wired: query_params["wired"]=wired
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.41.5", details="function replaced with listSiteDevicesStats")  
def getSiteDevicesStats(mist_session:_APISession, site_id:str, type:str="ap", status:str="all", page:int=1, limit:int=100) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteDevicesStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    type : str{'ap', 'switch', 'gateway', 'all'}, default: ap
    status : str{'all', 'connected', 'disconnected'}, default: all
    page : int, default: 1
    limit : int, default: 100        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/devices"
    query_params={}
    if type: query_params["type"]=type
    if status: query_params["status"]=status
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listSiteDevicesStats(mist_session:_APISession, site_id:str, type:str="ap", status:str="all", page:int=1, limit:int=100) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteDevicesStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    type : str{'ap', 'switch', 'gateway', 'all'}, default: ap
    status : str{'all', 'connected', 'disconnected'}, default: all
    page : int, default: 1
    limit : int, default: 100        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/devices"
    query_params={}
    if type: query_params["type"]=type
    if status: query_params["status"]=status
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteDeviceStats(mist_session:_APISession, site_id:str, device_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteDeviceStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    device_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/devices/{device_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteAllClientsStatsByDevice(mist_session:_APISession, site_id:str, device_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteAllClientsStatsByDevice
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    device_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/devices/{device_id}/clients"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.41.5", details="function replaced with listSiteDiscoveredAssets")  
def getSiteDiscoveredAssets(mist_session:_APISession, site_id:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteDiscoveredAssets
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
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
    uri = f"/api/v1/sites/{site_id}/stats/discovered_assets"
    query_params={}
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listSiteDiscoveredAssets(mist_session:_APISession, site_id:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteDiscoveredAssets
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
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
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    scope : str{'site', 'switch'}, default: site
      metric scope, optional
    type : str{'inactive_wired_vlans', 'switch_ap_affinity', 'poe_compliance', 'version_compliance'}
      metric type, inactive_wired_vlans/switch_ap_affinity/poe_compliance/version_compliance, optional
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
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
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'system_name', 'version', 'model', 'mgmt_addr'}, default: system_name
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
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    threshold : str
      configurable # ap per switch threshold, default 12
    system_name : str
      system name for switch level metrics, optional        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
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
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    adopted : bool
    system_name : str
    hostname : str
    vendor : str
    model : str
    version : str
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
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
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    duration : str, default: 1d
    start : int
    end : int
    page : int, default: 1
    limit : int, default: 100        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
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
    
def getSiteGatewayMetrics(mist_session:_APISession, site_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteGatewayMetrics
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/gateways/metrics"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteWirelessClientsStatsByMap(mist_session:_APISession, site_id:str, map_id:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteWirelessClientsStatsByMap
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    map_id : str        
    
    QUERY PARAMS
    ------------
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
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    map_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/maps/{map_id}/discovered_assets"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteSdkStatsByMap(mist_session:_APISession, site_id:str, map_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteSdkStatsByMap
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    map_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/maps/{map_id}/sdkclients"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.41.5", details="function replaced with listSiteUnconnectedClientStats")  
def getSiteUnconnectedClientStats(mist_session:_APISession, site_id:str, map_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteUnconnectedClientStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    map_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/maps/{map_id}/unconnected_clients"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listSiteUnconnectedClientStats(mist_session:_APISession, site_id:str, map_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteUnconnectedClientStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    map_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/maps/{map_id}/unconnected_clients"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.41.5", details="function replaced with listSiteMxEdgesStats")  
def getSiteMxEdgesStats(mist_session:_APISession, site_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteMxEdgesStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/mxedges"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listSiteMxEdgesStats(mist_session:_APISession, site_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteMxEdgesStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/mxedges"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteMxEdgeStats(mist_session:_APISession, site_id:str, mxedge_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteMxEdgeStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    mxedge_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/mxedges/{mxedge_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countSiteSwOrGwPorts(mist_session:_APISession, site_id:str, distinct:str="mac", full_duplex:bool=None, mac:str=None, neighbor_mac:str=None, neighbor_port_desc:str=None, neighbor_system_name:str=None, poe_disabled:bool=None, poe_mode:str=None, poe_on:bool=None, port_id:str=None, port_mac:str=None, power_draw:float=None, tx_pkts:int=None, rx_pkts:int=None, rx_bytes:int=None, tx_bps:int=None, rx_bps:int=None, tx_mcast_pkts:int=None, tx_bcast_pkts:int=None, rx_mcast_pkts:int=None, rx_bcast_pkts:int=None, speed:int=None, stp_state:str=None, stp_role:str=None, auth_state:str=None, up:bool=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteSwOrGwPorts
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'port_id', 'port_mac', 'full_duplex', 'mac', 'neighbor_mac', 'neighbor_port_desc', 'neighbor_system_name', 'poe_disabled', 'poe_mode', 'poe_on', 'speed', 'up'}, default: mac
      port_id, port_mac, full_duplex, mac, neighbor_macneighbor_port_desc, neighbor_system_name, poe_disabled, poe_mode, poe_on, speed, up
    full_duplex : bool
      indicates full or half duplex
    mac : str
      device identifier
    neighbor_mac : str
      Chassis identifier of the chassis type listed
    neighbor_port_desc : str
      Description supplied by the system on the interface E.g. “GigabitEthernet2/0/39”
    neighbor_system_name : str
      Name supplied by the system on the interface E.g. neighbor system name E.g. “Kumar-Acc-SW.mist.local”
    poe_disabled : bool
      is the POE configured not be disabled.
    poe_mode : str
      poe mode depending on class E.g. “802.3at”
    poe_on : bool
      is the device attached to POE
    port_id : str
      interface name
    port_mac : str
      interface mac address
    power_draw : float
      Amount of power being used by the interface at the time the command is executed. Unit in watts.
    tx_pkts : int
      Output packets
    rx_pkts : int
      Input packets
    rx_bytes : int
      Input bytes
    tx_bps : int
      Output rate
    rx_bps : int
      Input rate
    tx_mcast_pkts : int
      Multicast output packets
    tx_bcast_pkts : int
      Broadcast output packets
    rx_mcast_pkts : int
      Multicast input packets
    rx_bcast_pkts : int
      Broadcast input packets
    speed : int
      port speed
    stp_state : str{'forwarding', 'blocking', 'learning', 'listening', 'disabled'}
      if `up`==`true`
    stp_role : str{'designated', 'backup', 'alternate', 'root', 'root-prevented'}
      if `up`==`true`
    auth_state : str{'init', 'authenticated', 'authenticating', 'held'}
      if `up`==`true` && has Authenticator role
    up : bool
      indicates if interface is up
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
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    full_duplex : bool
      indicates full or half duplex
    mac : str
      device identifier
    neighbor_mac : str
      Chassis identifier of the chassis type listed
    neighbor_port_desc : str
      Description supplied by the system on the interface E.g. “GigabitEthernet2/0/39”
    neighbor_system_name : str
      Name supplied by the system on the interface E.g. neighbor system name E.g. “Kumar-Acc-SW.mist.local”
    poe_disabled : bool
      is the POE configured not be disabled.
    poe_mode : str
      poe mode depending on class E.g. “802.3at”
    poe_on : bool
      is the device attached to POE
    port_id : str
      interface name
    port_mac : str
      interface mac address
    power_draw : float
      Amount of power being used by the interface at the time the command is executed. Unit in watts.
    tx_pkts : int
      Output packets
    rx_pkts : int
      Input packets
    rx_bytes : int
      Input bytes
    tx_bps : int
      Output rate
    rx_bps : int
      Input rate
    tx_errors : int
      Output errors
    rx_errors : int
      Input errors
    tx_mcast_pkts : int
      Multicast output packets
    tx_bcast_pkts : int
      Broadcast output packets
    rx_mcast_pkts : int
      Multicast input packets
    rx_bcast_pkts : int
      Broadcast input packets
    speed : int
      port speed
    mac_limit : int
      Limit on number of dynamically learned macs
    mac_count : int
      Number of mac addresses in the forwarding table
    up : bool
      indicates if interface is up
    stp_state : str{'forwarding', 'blocking', 'learning', 'listening', 'disabled'}
      if `up`==`true`
    stp_role : str{'designated', 'backup', 'alternate', 'root', 'root-prevented'}
      if `up`==`true`
    xcvr_part_number : str
      Optic Slot Partnumber, Check for null/empty
    auth_state : str{'init', 'authenticated', 'authenticating', 'held'}
      if `up`==`true` && has Authenticator role
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
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
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    sdkclient_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/sdkclients/{sdkclient_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countSiteSwitchPorts(mist_session:_APISession, site_id:str, distinct:str="mac", full_duplex:bool=None, mac:str=None, neighbor_mac:str=None, neighbor_port_desc:str=None, neighbor_system_name:str=None, poe_disabled:bool=None, poe_mode:str=None, poe_on:bool=None, port_id:str=None, port_mac:str=None, power_draw:float=None, tx_pkts:int=None, rx_pkts:int=None, rx_bytes:int=None, tx_bps:int=None, rx_bps:int=None, tx_mcast_pkts:int=None, tx_bcast_pkts:int=None, rx_mcast_pkts:int=None, rx_bcast_pkts:int=None, speed:int=None, stp_state:str=None, stp_role:str=None, auth_state:str=None, up:bool=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteSwitchPorts
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'port_id', 'port_mac', 'full_duplex', 'mac', 'neighbor_mac', 'neighbor_port_desc', 'neighbor_system_name', 'poe_disabled', 'poe_mode', 'poe_on', 'speed', 'up'}, default: mac
      port_id, port_mac, full_duplex, mac, neighbor_macneighbor_port_desc, neighbor_system_name, poe_disabled, poe_mode, poe_on, speed, up
    full_duplex : bool
      indicates full or half duplex
    mac : str
      device identifier
    neighbor_mac : str
      Chassis identifier of the chassis type listed
    neighbor_port_desc : str
      Description supplied by the system on the interface E.g. “GigabitEthernet2/0/39”
    neighbor_system_name : str
      Name supplied by the system on the interface E.g. neighbor system name E.g. “Kumar-Acc-SW.mist.local”
    poe_disabled : bool
      is the POE configured not be disabled.
    poe_mode : str
      poe mode depending on class E.g. “802.3at”
    poe_on : bool
      is the device attached to POE
    port_id : str
      interface name
    port_mac : str
      interface mac address
    power_draw : float
      Amount of power being used by the interface at the time the command is executed. Unit in watts.
    tx_pkts : int
      Output packets
    rx_pkts : int
      Input packets
    rx_bytes : int
      Input bytes
    tx_bps : int
      Output rate
    rx_bps : int
      Input rate
    tx_mcast_pkts : int
      Multicast output packets
    tx_bcast_pkts : int
      Broadcast output packets
    rx_mcast_pkts : int
      Multicast input packets
    rx_bcast_pkts : int
      Broadcast input packets
    speed : int
      port speed
    stp_state : str{'forwarding', 'blocking', 'learning', 'listening', 'disabled'}
      if `up`==`true`
    stp_role : str{'designated', 'backup', 'alternate', 'root', 'root-prevented'}
      if `up`==`true`
    auth_state : str{'init', 'authenticated', 'authenticating', 'held'}
      if `up`==`true`
    up : bool
      indicates if interface is up
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
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    full_duplex : bool
      indicates full or half duplex
    mac : str
      device identifier
    neighbor_mac : str
      Chassis identifier of the chassis type listed
    neighbor_port_desc : str
      Description supplied by the system on the interface E.g. “GigabitEthernet2/0/39”
    neighbor_system_name : str
      Name supplied by the system on the interface E.g. neighbor system name E.g. “Kumar-Acc-SW.mist.local”
    poe_disabled : bool
      is the POE configured not be disabled.
    poe_mode : str
      poe mode depending on class E.g. “802.3at”
    poe_on : bool
      is the device attached to POE
    port_id : str
      interface name
    port_mac : str
      interface mac address
    power_draw : float
      Amount of power being used by the interface at the time the command is executed. Unit in watts.
    tx_pkts : int
      Output packets
    rx_pkts : int
      Input packets
    rx_bytes : int
      Input bytes
    tx_bps : int
      Output rate
    rx_bps : int
      Input rate
    tx_mcast_pkts : int
      Multicast output packets
    tx_bcast_pkts : int
      Broadcast output packets
    rx_mcast_pkts : int
      Multicast input packets
    rx_bcast_pkts : int
      Broadcast input packets
    speed : int
      port speed
    stp_state : str{'forwarding', 'blocking', 'learning', 'listening', 'disabled'}
      if `up`==`true`
    stp_role : str{'designated', 'backup', 'alternate', 'root', 'root-prevented'}
      if `up`==`true`
    auth_state : str{'init', 'authenticated', 'authenticating', 'held'}
      if `up`==`true` && has Authenticator role
    up : bool
      indicates if interface is up
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
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
    
def getSiteWiredClientAndParentInterface(mist_session:_APISession, site_id:str, device_id:str, port_id:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteWiredClientAndParentInterface
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    device_id : str        
    
    QUERY PARAMS
    ------------
    port_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/switch_wired_clients/{device_id}/search"
    query_params={}
    if port_id: query_params["port_id"]=port_id
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteAdoptedSwitchesComplianceMetrics(mist_session:_APISession, site_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteAdoptedSwitchesComplianceMetrics
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/switches/metrics"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteWxRulesUsage(mist_session:_APISession, site_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteWxRulesUsage
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/wxrules"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.41.5", details="function replaced with listSiteZonesStats")  
def getSiteZonesStats(mist_session:_APISession, site_id:str, map_id:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteZonesStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    map_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/zones"
    query_params={}
    if map_id: query_params["map_id"]=map_id
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listSiteZonesStats(mist_session:_APISession, site_id:str, map_id:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteZonesStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    map_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/zones"
    query_params={}
    if map_id: query_params["map_id"]=map_id
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteZoneStats(mist_session:_APISession, site_id:str, zone_type:str, zone_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteZoneStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    zone_type : str{'zones', 'rssizones'}
    zone_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/{zone_type}/{zone_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    