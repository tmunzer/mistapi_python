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

def countSiteNacClients(mist_session:_APISession, site_id:str, distinct:str="type", last_nacrule_id:str=None, nacrule_matched:bool=None, auth_type:str=None, last_vlan_id:str=None, last_nas_vendor:str=None, idp_id:str=None, last_ssid:str=None, last_username:str=None, timestamp:float=None, last_ap:str=None, mac:str=None, last_status:str=None, type:str=None, mdm_compliance_status:str=None, mdm_provider:str=None, start:int=None, end:int=None, duration:str="1d", limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteNacClients
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'auth_type', 'last_ap', 'last_nacrule_id', 'last_nas_vendor', 'last_ssid', 'last_status', 'last_username', 'last_vlan', 'mac', 'mdm_compliance', 'mdm_provider', 'type'}, default: type
      NAC Policy Rule ID, if matched
    last_nacrule_id : str
    nacrule_matched : bool
    auth_type : str
    last_vlan_id : str
    last_nas_vendor : str
    idp_id : str
    last_ssid : str
    last_username : str
    timestamp : float
    last_ap : str
    mac : str
    last_status : str
    type : str
    mdm_compliance_status : str
    mdm_provider : str
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
    uri = f"/api/v1/sites/{site_id}/nac_clients/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if last_nacrule_id: query_params["last_nacrule_id"]=last_nacrule_id
    if nacrule_matched: query_params["nacrule_matched"]=nacrule_matched
    if auth_type: query_params["auth_type"]=auth_type
    if last_vlan_id: query_params["last_vlan_id"]=last_vlan_id
    if last_nas_vendor: query_params["last_nas_vendor"]=last_nas_vendor
    if idp_id: query_params["idp_id"]=idp_id
    if last_ssid: query_params["last_ssid"]=last_ssid
    if last_username: query_params["last_username"]=last_username
    if timestamp: query_params["timestamp"]=timestamp
    if last_ap: query_params["last_ap"]=last_ap
    if mac: query_params["mac"]=mac
    if last_status: query_params["last_status"]=last_status
    if type: query_params["type"]=type
    if mdm_compliance_status: query_params["mdm_compliance_status"]=mdm_compliance_status
    if mdm_provider: query_params["mdm_provider"]=mdm_provider
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countSiteNacClientEvents(mist_session:_APISession, site_id:str, distinct:str=None, type:str=None, start:int=None, end:int=None, duration:str="1d", limit:int=100) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteNacClientEvents
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'ap', 'auth_type', 'dryrun_nacrule_id', 'mac', 'nacrule_id', 'nas_vendor', 'ssid', 'type', 'username', 'vlan'}
    type : str
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/nac_clients/events/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if type: query_params["type"]=type
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteNacClientEvents(mist_session:_APISession, site_id:str, type:str=None, nacrule_id:str=None, nacrule_matched:bool=None, dryrun_nacrule_id:str=None, dryrun_nacrule_matched:bool=None, auth_type:str=None, vlan:int=None, nas_vendor:str=None, bssid:str=None, idp_id:str=None, idp_role:str=None, idp_username:str=None, resp_attrs:list=None, ssid:str=None, username:str=None, ap:str=None, random_mac:bool=None, mac:str=None, timestamp:float=None, usermac_label:str=None, text:str=None, nas_ip:str=None, sort:str=None, ingress_vlan:str=None, start:int=None, end:int=None, duration:str="1d", limit:int=100) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteNacClientEvents
    
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
    nacrule_id : str
    nacrule_matched : bool
    dryrun_nacrule_id : str
    dryrun_nacrule_matched : bool
    auth_type : str
    vlan : int
    nas_vendor : str
    bssid : str
    idp_id : str
    idp_role : str
    idp_username : str
    resp_attrs : list
      Radius attributes returned by NAC to NAS Devive
    ssid : str
    username : str
    ap : str
    random_mac : bool
    mac : str
    timestamp : float
    usermac_label : str
    text : str
    nas_ip : str
    sort : str
    ingress_vlan : str
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/nac_clients/events/search"
    query_params={}
    if type: query_params["type"]=type
    if nacrule_id: query_params["nacrule_id"]=nacrule_id
    if nacrule_matched: query_params["nacrule_matched"]=nacrule_matched
    if dryrun_nacrule_id: query_params["dryrun_nacrule_id"]=dryrun_nacrule_id
    if dryrun_nacrule_matched: query_params["dryrun_nacrule_matched"]=dryrun_nacrule_matched
    if auth_type: query_params["auth_type"]=auth_type
    if vlan: query_params["vlan"]=vlan
    if nas_vendor: query_params["nas_vendor"]=nas_vendor
    if bssid: query_params["bssid"]=bssid
    if idp_id: query_params["idp_id"]=idp_id
    if idp_role: query_params["idp_role"]=idp_role
    if idp_username: query_params["idp_username"]=idp_username
    if resp_attrs: query_params["resp_attrs"]=resp_attrs
    if ssid: query_params["ssid"]=ssid
    if username: query_params["username"]=username
    if ap: query_params["ap"]=ap
    if random_mac: query_params["random_mac"]=random_mac
    if mac: query_params["mac"]=mac
    if timestamp: query_params["timestamp"]=timestamp
    if usermac_label: query_params["usermac_label"]=usermac_label
    if text: query_params["text"]=text
    if nas_ip: query_params["nas_ip"]=nas_ip
    if sort: query_params["sort"]=sort
    if ingress_vlan: query_params["ingress_vlan"]=ingress_vlan
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteNacClients(mist_session:_APISession, site_id:str, nacrule_id:str=None, nacrule_matched:bool=None, auth_type:str=None, vlan:str=None, nas_vendor:str=None, idp_id:str=None, ssid:str=None, username:str=None, timestamp:float=None, ap:str=None, mac:str=None, mxedge_id:str=None, nacrule_name:str=None, status:str=None, type:str=None, mdm_compliance:str=None, mdm_provider:str=None, sort:str=None, ingress_vlan:str=None, start:int=None, end:int=None, duration:str="1d", limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteNacClients
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    nacrule_id : str
    nacrule_matched : bool
    auth_type : str
    vlan : str
    nas_vendor : str
    idp_id : str
    ssid : str
    username : str
    timestamp : float
    ap : str
    mac : str
    mxedge_id : str
    nacrule_name : str
    status : str
    type : str
    mdm_compliance : str
    mdm_provider : str
    sort : str
    ingress_vlan : str
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
    uri = f"/api/v1/sites/{site_id}/nac_clients/search"
    query_params={}
    if nacrule_id: query_params["nacrule_id"]=nacrule_id
    if nacrule_matched: query_params["nacrule_matched"]=nacrule_matched
    if auth_type: query_params["auth_type"]=auth_type
    if vlan: query_params["vlan"]=vlan
    if nas_vendor: query_params["nas_vendor"]=nas_vendor
    if idp_id: query_params["idp_id"]=idp_id
    if ssid: query_params["ssid"]=ssid
    if username: query_params["username"]=username
    if timestamp: query_params["timestamp"]=timestamp
    if ap: query_params["ap"]=ap
    if mac: query_params["mac"]=mac
    if mxedge_id: query_params["mxedge_id"]=mxedge_id
    if nacrule_name: query_params["nacrule_name"]=nacrule_name
    if status: query_params["status"]=status
    if type: query_params["type"]=type
    if mdm_compliance: query_params["mdm_compliance"]=mdm_compliance
    if mdm_provider: query_params["mdm_provider"]=mdm_provider
    if sort: query_params["sort"]=sort
    if ingress_vlan: query_params["ingress_vlan"]=ingress_vlan
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    