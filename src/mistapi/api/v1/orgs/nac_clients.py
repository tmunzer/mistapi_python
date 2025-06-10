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

def countOrgNacClients(mist_session:_APISession, org_id:str, distinct:str="type", last_nacrule_id:str|None=None, nacrule_matched:bool|None=None, auth_type:str|None=None, last_vlan_id:str|None=None, last_nas_vendor:str|None=None, idp_id:str|None=None, last_ssid:str|None=None, last_username:str|None=None, timestamp:float|None=None, site_id:str|None=None, last_ap:str|None=None, mac:str|None=None, last_status:str|None=None, type:str|None=None, mdm_compliance_status:str|None=None, mdm_provider:str|None=None, start:int|None=None, end:int|None=None, duration:str="1d", limit:int=100) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/nac/count-org-nac-clients

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

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
    site_id : str
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

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/nac_clients/count"
    query_params:dict[str, str]={}
    if distinct:
        query_params["distinct"]=str(distinct)
    if last_nacrule_id:
        query_params["last_nacrule_id"]=str(last_nacrule_id)
    if nacrule_matched:
        query_params["nacrule_matched"]=str(nacrule_matched)
    if auth_type:
        query_params["auth_type"]=str(auth_type)
    if last_vlan_id:
        query_params["last_vlan_id"]=str(last_vlan_id)
    if last_nas_vendor:
        query_params["last_nas_vendor"]=str(last_nas_vendor)
    if idp_id:
        query_params["idp_id"]=str(idp_id)
    if last_ssid:
        query_params["last_ssid"]=str(last_ssid)
    if last_username:
        query_params["last_username"]=str(last_username)
    if timestamp:
        query_params["timestamp"]=str(timestamp)
    if site_id:
        query_params["site_id"]=str(site_id)
    if last_ap:
        query_params["last_ap"]=str(last_ap)
    if mac:
        query_params["mac"]=str(mac)
    if last_status:
        query_params["last_status"]=str(last_status)
    if type:
        query_params["type"]=str(type)
    if mdm_compliance_status:
        query_params["mdm_compliance_status"]=str(mdm_compliance_status)
    if mdm_provider:
        query_params["mdm_provider"]=str(mdm_provider)
    if start:
        query_params["start"]=str(start)
    if end:
        query_params["end"]=str(end)
    if duration:
        query_params["duration"]=str(duration)
    if limit:
        query_params["limit"]=str(limit)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp

def countOrgNacClientEvents(mist_session:_APISession, org_id:str, distinct:str|None=None, type:str|None=None, start:int|None=None, end:int|None=None, duration:str="1d", limit:int=100) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/nac/count-org-nac-client-events

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

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
    uri = f"/api/v1/orgs/{org_id}/nac_clients/events/count"
    query_params:dict[str, str]={}
    if distinct:
        query_params["distinct"]=str(distinct)
    if type:
        query_params["type"]=str(type)
    if start:
        query_params["start"]=str(start)
    if end:
        query_params["end"]=str(end)
    if duration:
        query_params["duration"]=str(duration)
    if limit:
        query_params["limit"]=str(limit)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp

def searchOrgNacClientEvents(mist_session:_APISession, org_id:str, type:str|None=None, nacrule_id:str|None=None, nacrule_matched:bool|None=None, dryrun_nacrule_id:str|None=None, dryrun_nacrule_matched:bool|None=None, auth_type:str|None=None, vlan:int|None=None, nas_vendor:str|None=None, bssid:str|None=None, idp_id:str|None=None, idp_role:str|None=None, idp_username:str|None=None, resp_attrs:list|None=None, ssid:str|None=None, username:str|None=None, site_id:str|None=None, ap:str|None=None, random_mac:bool|None=None, mac:str|None=None, timestamp:float|None=None, usermac_label:str|None=None, text:str|None=None, nas_ip:str|None=None, sort:str|None=None, ingress_vlan:str|None=None, start:int|None=None, end:int|None=None, duration:str="1d", limit:int=100) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/nac/search-org-nac-client-events

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
      Radius attributes returned by NAC to NAS derive
    ssid : str
    username : str
    site_id : str
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
    uri = f"/api/v1/orgs/{org_id}/nac_clients/events/search"
    query_params:dict[str, str]={}
    if type:
        query_params["type"]=str(type)
    if nacrule_id:
        query_params["nacrule_id"]=str(nacrule_id)
    if nacrule_matched:
        query_params["nacrule_matched"]=str(nacrule_matched)
    if dryrun_nacrule_id:
        query_params["dryrun_nacrule_id"]=str(dryrun_nacrule_id)
    if dryrun_nacrule_matched:
        query_params["dryrun_nacrule_matched"]=str(dryrun_nacrule_matched)
    if auth_type:
        query_params["auth_type"]=str(auth_type)
    if vlan:
        query_params["vlan"]=str(vlan)
    if nas_vendor:
        query_params["nas_vendor"]=str(nas_vendor)
    if bssid:
        query_params["bssid"]=str(bssid)
    if idp_id:
        query_params["idp_id"]=str(idp_id)
    if idp_role:
        query_params["idp_role"]=str(idp_role)
    if idp_username:
        query_params["idp_username"]=str(idp_username)
    if resp_attrs:
        query_params["resp_attrs"]=str(resp_attrs)
    if ssid:
        query_params["ssid"]=str(ssid)
    if username:
        query_params["username"]=str(username)
    if site_id:
        query_params["site_id"]=str(site_id)
    if ap:
        query_params["ap"]=str(ap)
    if random_mac:
        query_params["random_mac"]=str(random_mac)
    if mac:
        query_params["mac"]=str(mac)
    if timestamp:
        query_params["timestamp"]=str(timestamp)
    if usermac_label:
        query_params["usermac_label"]=str(usermac_label)
    if text:
        query_params["text"]=str(text)
    if nas_ip:
        query_params["nas_ip"]=str(nas_ip)
    if sort:
        query_params["sort"]=str(sort)
    if ingress_vlan:
        query_params["ingress_vlan"]=str(ingress_vlan)
    if start:
        query_params["start"]=str(start)
    if end:
        query_params["end"]=str(end)
    if duration:
        query_params["duration"]=str(duration)
    if limit:
        query_params["limit"]=str(limit)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp

def searchOrgNacClients(mist_session:_APISession, org_id:str, nacrule_id:str|None=None, nacrule_matched:bool|None=None, auth_type:str|None=None, vlan:str|None=None, nas_vendor:str|None=None, idp_id:str|None=None, ssid:str|None=None, username:str|None=None, timestamp:float|None=None, site_id:str|None=None, ap:str|None=None, mac:str|None=None, mdm_managed:bool|None=None, status:str|None=None, type:str|None=None, mdm_compliance:str|None=None, mdm_provider:str|None=None, sort:str|None=None, usermac_label:list|None=None, ingress_vlan:str|None=None, start:int|None=None, end:int|None=None, duration:str="1d", limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/nac/search-org-nac-clients

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

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
    site_id : str
    ap : str
    mac : str
    mdm_managed : bool
    status : str
    type : str
    mdm_compliance : str
    mdm_provider : str
    sort : str
    usermac_label : list
      Labels derived from usermac entry
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
    uri = f"/api/v1/orgs/{org_id}/nac_clients/search"
    query_params:dict[str, str]={}
    if nacrule_id:
        query_params["nacrule_id"]=str(nacrule_id)
    if nacrule_matched:
        query_params["nacrule_matched"]=str(nacrule_matched)
    if auth_type:
        query_params["auth_type"]=str(auth_type)
    if vlan:
        query_params["vlan"]=str(vlan)
    if nas_vendor:
        query_params["nas_vendor"]=str(nas_vendor)
    if idp_id:
        query_params["idp_id"]=str(idp_id)
    if ssid:
        query_params["ssid"]=str(ssid)
    if username:
        query_params["username"]=str(username)
    if timestamp:
        query_params["timestamp"]=str(timestamp)
    if site_id:
        query_params["site_id"]=str(site_id)
    if ap:
        query_params["ap"]=str(ap)
    if mac:
        query_params["mac"]=str(mac)
    if mdm_managed:
        query_params["mdm_managed"]=str(mdm_managed)
    if status:
        query_params["status"]=str(status)
    if type:
        query_params["type"]=str(type)
    if mdm_compliance:
        query_params["mdm_compliance"]=str(mdm_compliance)
    if mdm_provider:
        query_params["mdm_provider"]=str(mdm_provider)
    if sort:
        query_params["sort"]=str(sort)
    if usermac_label:
        query_params["usermac_label"]=str(usermac_label)
    if ingress_vlan:
        query_params["ingress_vlan"]=str(ingress_vlan)
    if start:
        query_params["start"]=str(start)
    if end:
        query_params["end"]=str(end)
    if duration:
        query_params["duration"]=str(duration)
    if limit:
        query_params["limit"]=str(limit)
    if page:
        query_params["page"]=str(page)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
