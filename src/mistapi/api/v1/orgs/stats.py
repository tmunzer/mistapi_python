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

def getOrgStats(mist_session:_APISession, org_id:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
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
    uri = f"/api/v1/orgs/{org_id}/stats"
    query_params={}
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.52.0", current_version="0.51.2", details="function replaced with listOrgAssetsStats")
def getOrgAssetsStats(mist_session:_APISession, org_id:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgAssetsStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
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
    uri = f"/api/v1/orgs/{org_id}/stats/assets"
    query_params={}
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listOrgAssetsStats(mist_session:_APISession, org_id:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgAssetsStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
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
    uri = f"/api/v1/orgs/{org_id}/stats/assets"
    query_params={}
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countOrgAssetsByDistanceField(mist_session:_APISession, org_id:str, distinct:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countOrgAssetsByDistanceField
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'site_id', 'mac', 'map_id', 'ibeacon_uuid', 'ibeacon_major', 'ibeacon_minor'}        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/stats/assets/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchOrgAssets(mist_session:_APISession, org_id:str, site_id:str=None, mac:str=None, device_name:str=None, name:str=None, map_id:str=None, ibeacon_uuid:str=None, ibeacon_major:str=None, ibeacon_minor:str=None, eddystone_uid_namespace:str=None, eddystone_uid_instance:str=None, eddystone_url:str=None, ap_mac:str=None, beam:int=None, rssi:int=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchOrgAssets
    
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
    device_name : str
    name : str
    map_id : str
    ibeacon_uuid : str
    ibeacon_major : str
    ibeacon_minor : str
    eddystone_uid_namespace : str
    eddystone_uid_instance : str
    eddystone_url : str
    ap_mac : str
    beam : int
    rssi : int
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/stats/assets/search"
    query_params={}
    if site_id: query_params["site_id"]=site_id
    if mac: query_params["mac"]=mac
    if device_name: query_params["device_name"]=device_name
    if name: query_params["name"]=name
    if map_id: query_params["map_id"]=map_id
    if ibeacon_uuid: query_params["ibeacon_uuid"]=ibeacon_uuid
    if ibeacon_major: query_params["ibeacon_major"]=ibeacon_major
    if ibeacon_minor: query_params["ibeacon_minor"]=ibeacon_minor
    if eddystone_uid_namespace: query_params["eddystone_uid_namespace"]=eddystone_uid_namespace
    if eddystone_uid_instance: query_params["eddystone_uid_instance"]=eddystone_uid_instance
    if eddystone_url: query_params["eddystone_url"]=eddystone_url
    if ap_mac: query_params["ap_mac"]=ap_mac
    if beam: query_params["beam"]=beam
    if rssi: query_params["rssi"]=rssi
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countOrgBgpStats(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countOrgBgpStats
    
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
    uri = f"/api/v1/orgs/{org_id}/stats/bgp_peers/count"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchOrgBgpStats(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchOrgBgpStats
    
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
    uri = f"/api/v1/orgs/{org_id}/stats/bgp_peers/search"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.52.0", current_version="0.51.2", details="function replaced with listOrgDevicesStats")
def getOrgDevicesStats(mist_session:_APISession, org_id:str, type:str="ap", status:str="all", site_id:str=None, mac:str=None, evpntopo_id:str=None, evpn_unused:str=None, fields:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgDevicesStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    type : str{'ap', 'switch', 'gateway', 'all'}, default: ap
    status : str{'all', 'connected', 'disconnected'}, default: all
    site_id : str
    mac : str
    evpntopo_id : str
    evpn_unused : str
    fields : str
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
    uri = f"/api/v1/orgs/{org_id}/stats/devices"
    query_params={}
    if type: query_params["type"]=type
    if status: query_params["status"]=status
    if site_id: query_params["site_id"]=site_id
    if mac: query_params["mac"]=mac
    if evpntopo_id: query_params["evpntopo_id"]=evpntopo_id
    if evpn_unused: query_params["evpn_unused"]=evpn_unused
    if fields: query_params["fields"]=fields
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listOrgDevicesStats(mist_session:_APISession, org_id:str, type:str="ap", status:str="all", site_id:str=None, mac:str=None, evpntopo_id:str=None, evpn_unused:str=None, fields:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgDevicesStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    type : str{'ap', 'switch', 'gateway', 'all'}, default: ap
    status : str{'all', 'connected', 'disconnected'}, default: all
    site_id : str
    mac : str
    evpntopo_id : str
    evpn_unused : str
    fields : str
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
    uri = f"/api/v1/orgs/{org_id}/stats/devices"
    query_params={}
    if type: query_params["type"]=type
    if status: query_params["status"]=status
    if site_id: query_params["site_id"]=site_id
    if mac: query_params["mac"]=mac
    if evpntopo_id: query_params["evpntopo_id"]=evpntopo_id
    if evpn_unused: query_params["evpn_unused"]=evpn_unused
    if fields: query_params["fields"]=fields
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.52.0", current_version="0.51.2", details="function replaced with listOrgMxEdgesStats")
def getOrgMxEdgesStats(mist_session:_APISession, org_id:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d", for_site:bool=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgMxEdgesStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    page : int, default: 1
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d
    for_site : bool        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/stats/mxedges"
    query_params={}
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if for_site: query_params["for_site"]=for_site
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listOrgMxEdgesStats(mist_session:_APISession, org_id:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d", for_site:bool=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgMxEdgesStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    page : int, default: 1
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d
    for_site : bool        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/stats/mxedges"
    query_params={}
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if for_site: query_params["for_site"]=for_site
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getOrgMxEdgeStats(mist_session:_APISession, org_id:str, mxedge_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgMxEdgeStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    mxedge_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/stats/mxedges/{mxedge_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getOrgOtherDeviceStats(mist_session:_APISession, org_id:str, device_mac:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgOtherDeviceStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    device_mac : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/stats/otherdevices/{device_mac}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchOrgSwOrGwPorts(mist_session:_APISession, org_id:str, full_duplex:bool=None, mac:str=None, neighbor_mac:str=None, neighbor_port_desc:str=None, neighbor_system_name:str=None, poe_disabled:bool=None, poe_mode:str=None, poe_on:bool=None, port_id:str=None, port_mac:str=None, power_draw:float=None, tx_pkts:int=None, rx_pkts:int=None, rx_bytes:int=None, tx_bps:int=None, rx_bps:int=None, tx_errors:int=None, rx_errors:int=None, tx_mcast_pkts:int=None, tx_bcast_pkts:int=None, rx_mcast_pkts:int=None, rx_bcast_pkts:int=None, speed:int=None, mac_limit:int=None, mac_count:int=None, up:bool=None, stp_state:str=None, stp_role:str=None, auth_state:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchOrgSwOrGwPorts
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
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
    stp_state : str{'forwarding', 'blocking', 'learning', 'listening', 'disabled'}
      if `up`==`true`
    stp_role : str{'designated', 'backup', 'alternate', 'root', 'root-prevented'}
      if `up`==`true`
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
    uri = f"/api/v1/orgs/{org_id}/stats/ports/search"
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
    if auth_state: query_params["auth_state"]=auth_state
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countOrgSwitchPorts(mist_session:_APISession, org_id:str, distinct:str="mac", full_duplex:bool=None, mac:str=None, neighbor_mac:str=None, neighbor_port_desc:str=None, neighbor_system_name:str=None, poe_disabled:bool=None, poe_mode:str=None, poe_on:bool=None, port_id:str=None, port_mac:str=None, power_draw:float=None, tx_pkts:int=None, rx_pkts:int=None, rx_bytes:int=None, tx_bps:int=None, rx_bps:int=None, tx_mcast_pkts:int=None, tx_bcast_pkts:int=None, rx_mcast_pkts:int=None, rx_bcast_pkts:int=None, speed:int=None, stp_state:str=None, stp_role:str=None, auth_state:str=None, up:bool=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countOrgSwitchPorts
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'port_id', 'port_mac', 'full_duplex', 'mac', 'neighbor_mac', 'neighbor_port_desc', 'neighbor_system_name', 'poe_disabled', 'poe_mode', 'poe_on', 'speed', 'up'}, default: mac
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
    stp_state : str{'forwarding', 'blocking', 'learning', 'listening', 'disabled'}
      if `up`==`true`
    stp_role : str{'designated', 'backup', 'alternate', 'root', 'root-prevented'}
      if `up`==`true`
    auth_state : str{'init', 'authenticated', 'authenticating', 'held'}
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
    uri = f"/api/v1/orgs/{org_id}/stats/switch_ports/count"
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
    
def countOrgTunnelsStats(mist_session:_APISession, org_id:str, distinct:str="wxtunnel_id", type:str="wxtunnel") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countOrgTunnelsStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'auth_algo', 'wxtunnel_id', 'ap', 'remote_ip', 'remote_port', 'state', 'mxedge_id', 'mxcluster_id', 'site_id', 'peer_mxedge_id', 'mac', 'node', 'peer_ip', 'peer_host', 'ip', 'tunnel_name', 'protocol', 'encrypt_algo', 'ike_version', 'last_event', 'up'}, default: wxtunnel_id
      - If `type`==`wxtunnel`: wxtunnel_id / ap / remote_ip / remote_port / state / mxedge_id / mxcluster_id / site_id / peer_mxedge_id; default is wxtunnel_id 
- If `type`==`wan`: mac / site_id / node / peer_ip / peer_host/ ip / tunnel_name / protocol / auth_algo / encrypt_algo / ike_version / last_event / up
    type : str{'wxtunnel', 'wan'}, default: wxtunnel        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/stats/tunnels/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if type: query_params["type"]=type
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchOrgTunnelsStats(mist_session:_APISession, org_id:str, mxcluster_id:str=None, site_id:str=None, wxtunnel_id:str=None, ap:str=None, mac:str=None, node:str=None, peer_ip:str=None, peer_host:str=None, ip:str=None, tunnel_name:str=None, protocol:str=None, auth_algo:str=None, encrypt_algo:str=None, ike_version:str=None, up:str=None, type:str="wxtunnel", limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchOrgTunnelsStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    mxcluster_id : str
    site_id : str
    wxtunnel_id : str
    ap : str
    mac : str
    node : str
    peer_ip : str
    peer_host : str
    ip : str
    tunnel_name : str
    protocol : str
    auth_algo : str
    encrypt_algo : str
    ike_version : str
    up : str
    type : str{'wxtunnel', 'wan'}, default: wxtunnel
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/stats/tunnels/search"
    query_params={}
    if mxcluster_id: query_params["mxcluster_id"]=mxcluster_id
    if site_id: query_params["site_id"]=site_id
    if wxtunnel_id: query_params["wxtunnel_id"]=wxtunnel_id
    if ap: query_params["ap"]=ap
    if mac: query_params["mac"]=mac
    if node: query_params["node"]=node
    if peer_ip: query_params["peer_ip"]=peer_ip
    if peer_host: query_params["peer_host"]=peer_host
    if ip: query_params["ip"]=ip
    if tunnel_name: query_params["tunnel_name"]=tunnel_name
    if protocol: query_params["protocol"]=protocol
    if auth_algo: query_params["auth_algo"]=auth_algo
    if encrypt_algo: query_params["encrypt_algo"]=encrypt_algo
    if ike_version: query_params["ike_version"]=ike_version
    if up: query_params["up"]=up
    if type: query_params["type"]=type
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countOrgPeerPathStats(mist_session:_APISession, org_id:str, distinct:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countOrgPeerPathStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str
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
    uri = f"/api/v1/orgs/{org_id}/stats/vpn_peers/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchOrgPeerPathStats(mist_session:_APISession, org_id:str, start:int=None, end:int=None, duration:str="1d", limit:int=100) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchOrgPeerPathStats
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/stats/vpn_peers/search"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    