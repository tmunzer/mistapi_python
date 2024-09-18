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
    distinct : str{'ap', 'app', 'category', 'device_mac', 'port_id', 'service', 'src_ip', 'ssid', 'wcid', 'wlan_id app'}
      Default for wireless devices is `ap`. Default for wired devices is `device_mac`
    device_mac : str
    app : str
    wired : str        
    
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
    distinct : str{'by', 'device_name', 'eddystone_uid_instance', 'eddystone_uid_namespace', 'eddystone_url', 'ibeacon_major', 'ibeacon_minor', 'ibeacon_uuid', 'mac', 'map_id', 'name'}, default: map_id        
    
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
    
def troubleshootSiteCall(mist_session:_APISession, site_id:str, client_mac:str, meeting_id:str, mac:str=None, app:str=None, start:int=None, end:int=None, duration:str="1d", limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/troubleshootSiteCall
    
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
    meeting_id : str
    mac : str
    app : str
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
    uri = f"/api/v1/sites/{site_id}/stats/calls/client/{client_mac}/troubleshoot"
    query_params={}
    if meeting_id: query_params["meeting_id"]=meeting_id
    if mac: query_params["mac"]=mac
    if app: query_params["app"]=app
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
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
    app : str
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
    
def listSiteTroubleshootCalls(mist_session:_APISession, site_id:str, client_mac:str, ap:str=None, meeting_id:str=None, mac:str=None, app:str=None, start:int=None, end:int=None, duration:str="1d", limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteTroubleshootCalls
    
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
    ap : str
    meeting_id : str
    mac : str
    app : str
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
    uri = f"/api/v1/sites/{site_id}/stats/calls/troubleshoot"
    query_params={}
    if ap: query_params["ap"]=ap
    if meeting_id: query_params["meeting_id"]=meeting_id
    if mac: query_params["mac"]=mac
    if app: query_params["app"]=app
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listSiteWirelessClientsStats(mist_session:_APISession, site_id:str, wired:bool=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
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
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/clients"
    query_params={}
    if wired: query_params["wired"]=wired
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
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
    type : str{'all', 'ap', 'gateway', 'switch'}, default: ap
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
      metric scope
    type : str{'inactive_wired_vlans', 'poe_compliance', 'switch_ap_affinity', 'version_compliance'}
      metric type
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
    distinct : str{'mgmt_addr', 'model', 'system_name', 'version'}, default: system_name
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
    system_name : str        
    
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
    
def listSiteMxEdgesStats(mist_session:_APISession, site_id:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteMxEdgesStats
    
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
    uri = f"/api/v1/sites/{site_id}/stats/mxedges"
    query_params={}
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteMxEdgeStats(mist_session:_APISession, site_id:str, mxedge_id:str, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
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
    uri = f"/api/v1/sites/{site_id}/stats/mxedges/{mxedge_id}"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
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
    distinct : str{'full_duplex', 'mac', 'neighbor_mac', 'neighbor_port_desc', 'neighbor_system_name', 'poe_disabled', 'poe_mode', 'poe_on', 'port_id', 'port_mac', 'speed', 'up'}, default: mac
    full_duplex : bool
    mac : str
    neighbor_mac : str
    neighbor_port_desc : str
    neighbor_system_name : str
    poe_disabled : bool
    poe_mode : str
    poe_on : bool
    port_id : str
    port_mac : str
    power_draw : float
    tx_pkts : int
    rx_pkts : int
    rx_bytes : int
    tx_bps : int
    rx_bps : int
    tx_mcast_pkts : int
    tx_bcast_pkts : int
    rx_mcast_pkts : int
    rx_bcast_pkts : int
    speed : int
    stp_state : str{'blocking', 'disabled', 'forwarding', 'learning', 'listening'}
      if `up`==`true`
    stp_role : str{'alternate', 'backup', 'designated', 'root', 'root-prevented'}
      if `up`==`true`
    auth_state : str{'authenticated', 'authenticating', 'held', 'init'}
      if `up`==`true` && has Authenticator role
    up : bool
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
    
def searchSiteSwOrGwPorts(mist_session:_APISession, site_id:str, full_duplex:bool=None, mac:str=None, device_type:str=None, neighbor_mac:str=None, neighbor_port_desc:str=None, neighbor_system_name:str=None, poe_disabled:bool=None, poe_mode:str=None, poe_on:bool=None, port_id:str=None, port_mac:str=None, power_draw:float=None, tx_pkts:int=None, rx_pkts:int=None, rx_bytes:int=None, tx_bps:int=None, rx_bps:int=None, tx_errors:int=None, rx_errors:int=None, tx_mcast_pkts:int=None, tx_bcast_pkts:int=None, rx_mcast_pkts:int=None, rx_bcast_pkts:int=None, speed:int=None, mac_limit:int=None, mac_count:int=None, up:bool=None, active:bool=None, jitter:float=None, loss:float=None, latency:float=None, stp_state:str=None, stp_role:str=None, xcvr_part_number:str=None, auth_state:str=None, lte_imsi:str=None, lte_iccid:str=None, lte_imei:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
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
    mac : str
    device_type : str{'ap', 'ble', 'gateway', 'mxedge', 'nac', 'switch'}
      device type
    neighbor_mac : str
    neighbor_port_desc : str
    neighbor_system_name : str
    poe_disabled : bool
    poe_mode : str
    poe_on : bool
    port_id : str
    port_mac : str
    power_draw : float
    tx_pkts : int
    rx_pkts : int
    rx_bytes : int
    tx_bps : int
    rx_bps : int
    tx_errors : int
    rx_errors : int
    tx_mcast_pkts : int
    tx_bcast_pkts : int
    rx_mcast_pkts : int
    rx_bcast_pkts : int
    speed : int
    mac_limit : int
    mac_count : int
    up : bool
    active : bool
    jitter : float
    loss : float
    latency : float
    stp_state : str{'blocking', 'disabled', 'forwarding', 'learning', 'listening'}
      if `up`==`true`
    stp_role : str{'alternate', 'backup', 'designated', 'root', 'root-prevented'}
      if `up`==`true`
    xcvr_part_number : str
    auth_state : str{'authenticated', 'authenticating', 'held', 'init'}
      if `up`==`true` && has Authenticator role
    lte_imsi : str
    lte_iccid : str
    lte_imei : str
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
    if device_type: query_params["device_type"]=device_type
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
    if active: query_params["active"]=active
    if jitter: query_params["jitter"]=jitter
    if loss: query_params["loss"]=loss
    if latency: query_params["latency"]=latency
    if stp_state: query_params["stp_state"]=stp_state
    if stp_role: query_params["stp_role"]=stp_role
    if xcvr_part_number: query_params["xcvr_part_number"]=xcvr_part_number
    if auth_state: query_params["auth_state"]=auth_state
    if lte_imsi: query_params["lte_imsi"]=lte_imsi
    if lte_iccid: query_params["lte_iccid"]=lte_iccid
    if lte_imei: query_params["lte_imei"]=lte_imei
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
    distinct : str{'full_duplex', 'mac', 'neighbor_mac', 'neighbor_port_desc', 'neighbor_system_name', 'poe_disabled', 'poe_mode', 'poe_on', 'port_id', 'port_mac', 'speed', 'up'}, default: mac
    full_duplex : bool
    mac : str
    neighbor_mac : str
    neighbor_port_desc : str
    neighbor_system_name : str
    poe_disabled : bool
    poe_mode : str
    poe_on : bool
    port_id : str
    port_mac : str
    power_draw : float
    tx_pkts : int
    rx_pkts : int
    rx_bytes : int
    tx_bps : int
    rx_bps : int
    tx_mcast_pkts : int
    tx_bcast_pkts : int
    rx_mcast_pkts : int
    rx_bcast_pkts : int
    speed : int
    stp_state : str{'blocking', 'disabled', 'forwarding', 'learning', 'listening'}
      if `up`==`true`
    stp_role : str{'alternate', 'backup', 'designated', 'root', 'root-prevented'}
      if `up`==`true`
    auth_state : str{'authenticated', 'authenticating', 'held', 'init'}
      if `up`==`true`
    up : bool
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
    mac : str
    neighbor_mac : str
    neighbor_port_desc : str
    neighbor_system_name : str
    poe_disabled : bool
    poe_mode : str
    poe_on : bool
    port_id : str
    port_mac : str
    power_draw : float
    tx_pkts : int
    rx_pkts : int
    rx_bytes : int
    tx_bps : int
    rx_bps : int
    tx_mcast_pkts : int
    tx_bcast_pkts : int
    rx_mcast_pkts : int
    rx_bcast_pkts : int
    speed : int
    stp_state : str{'blocking', 'disabled', 'forwarding', 'learning', 'listening'}
      if `up`==`true`
    stp_role : str{'alternate', 'backup', 'designated', 'root', 'root-prevented'}
      if `up`==`true`
    auth_state : str{'authenticated', 'authenticating', 'held', 'init'}
      if `up`==`true` && has Authenticator role
    up : bool
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
    
def getSiteSwitchesMetrics(mist_session:_APISession, site_id:str, type:str=None, scope:str=None, switch_mac:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteSwitchesMetrics
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    type : str{'active_ports_summary'}
    scope : str{'site', 'switch'}
    switch_mac : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/stats/switches/metrics"
    query_params={}
    if type: query_params["type"]=type
    if scope: query_params["scope"]=scope
    if switch_mac: query_params["switch_mac"]=switch_mac
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
    zone_type : str{'rssizones', 'zones'}
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
    