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
    distinct : str{'type', 'last_nacrule_id', 'auth_type', 'last_vlan_id', 'last_nas_vendor', 'last_username', 'last_ap', 'mac', 'last_ssid', 'last_status', 'mdm_compliance_status', 'mdm_provider'}, default: type
      NAC Policy Rule ID, if matched
    last_nacrule_id : str
      NAC Policy Rule ID, if matched
    nacrule_matched : bool
      NAC Policy Rule Matched
    auth_type : str
      authentication type, e.g. “eap-tls”, “eap-ttls”, “eap-teap”, “mab”, “device-auth”
    last_vlan_id : str
      Vlan ID
    last_nas_vendor : str
      vendor of NAS device
    idp_id : str
      SSO ID, if present and used
    last_ssid : str
      SSID
    last_username : str
      Username presented by the client
    timestamp : float
      start time, in epoch
    last_ap : str
      AP MAC connected to by client
    mac : str
      MAC address
    last_status : str
      Connection status of client i.e “permitted”, “denied, “session_ended”
    type : str
      Client type i.e. “wireless”, “wired” etc.
    mdm_compliance_status : str
      MDM compliancy of client i.e “compliant”, “not compliant”
    mdm_provider : str
      MDM provider of client’s organisation eg “intune”, “jamf”
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
    
def countSiteNacClientEvents(mist_session:_APISession, site_id:str, distinct:str=None, start:int=None, end:int=None, duration:str="1d", limit:int=100, page:int=1) -> _APIResponse:
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
    distinct : str{'type', 'nacrule_id', 'dryrun_nacrule_id', 'auth_type', 'vlan', 'nas_vendor', 'username', 'ap', 'mac', 'ssid'}
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
    uri = f"/api/v1/sites/{site_id}/nac_clients/events/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searcSitegNacClientEvents(mist_session:_APISession, site_id:str, type:str=None, nacrule_id:str=None, nacrule_matched:bool=None, dryrun_nacrule_id:str=None, dryrun_nacrule_matched:bool=None, auth_type:str=None, vlan:int=None, nas_vendor:str=None, bssid:str=None, idp_id:str=None, idp_role:str=None, resp_attrs:list=None, ssid:str=None, username:str=None, ap:str=None, random_mac:bool=None, mac:str=None, timestamp:float=None, start:int=None, end:int=None, duration:str="1d", limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searcSitegNacClientEvents
    
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
      event type, e.g. NAC_CLIENT_PERMIT
    nacrule_id : str
      NAC Policy Rule ID, if matched
    nacrule_matched : bool
      NAC Policy Rule Matched
    dryrun_nacrule_id : str
      NAC Policy Dry Run Rule ID, if present and matched
    dryrun_nacrule_matched : bool
      True - if dryrun rule present and matched with priority, False - if not matched or not present
    auth_type : str
      authentication type, e.g.  “eap-tls”, “eap-ttls”, “eap-teap”, “mab”, “device-auth”
    vlan : int
      Vlan ID
    nas_vendor : str
      vendor of NAS device
    bssid : str
      SSID
    idp_id : str
      SSO ID, if present and used
    idp_role : str
      IDP returned roles/groups for the user
    resp_attrs : list
      Radius attributes returned by NAC to NAS Devive
    ssid : str
      SSID
    username : str
      Username presented by the client
    ap : str
      AP MAC
    random_mac : bool
      AP random macMAC
    mac : str
      MAC address
    timestamp : float
      start time, in epoch
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
    if resp_attrs: query_params["resp_attrs"]=resp_attrs
    if ssid: query_params["ssid"]=ssid
    if username: query_params["username"]=username
    if ap: query_params["ap"]=ap
    if random_mac: query_params["random_mac"]=random_mac
    if mac: query_params["mac"]=mac
    if timestamp: query_params["timestamp"]=timestamp
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteNacClients(mist_session:_APISession, site_id:str, last_nacrule_id:str=None, nacrule_matched:bool=None, auth_type:str=None, last_vlan_id:str=None, last_nas_vendor:str=None, idp_id:str=None, last_ssid:str=None, last_username:str=None, timestamp:float=None, last_ap:str=None, mac:str=None, last_status:str=None, type:str=None, mdm_compliance_status:str=None, mdm_provider:str=None, start:int=None, end:int=None, duration:str="1d", limit:int=100, page:int=1) -> _APIResponse:
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
    last_nacrule_id : str
      NAC Policy Rule ID, if matched
    nacrule_matched : bool
      NAC Policy Rule Matched
    auth_type : str
      authentication type, e.g. “eap-tls”, “eap-ttls”, “eap-teap”, “mab”, “device-auth”
    last_vlan_id : str
      Vlan ID
    last_nas_vendor : str
      vendor of NAS device
    idp_id : str
      SSO ID, if present and used
    last_ssid : str
      SSID
    last_username : str
      Username presented by the client
    timestamp : float
      start time, in epoch
    last_ap : str
      AP MAC connected to by client
    mac : str
      MAC address
    last_status : str
      Connection status of client i.e “permitted”, “denied, “session_ended”
    type : str
      Client type i.e. “wireless”, “wired” etc.
    mdm_compliance_status : str
      MDM compliancy of client i.e “compliant”, “not compliant”
    mdm_provider : str
      MDM provider of client’s organisation eg “intune”, “jamf”
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
    