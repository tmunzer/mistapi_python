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
    distinct : str{'type', 'nacrule_id', 'auth_type', 'vlan', 'nas_vendor', 'eap_type', 'username', 'ap', 'mac', 'ssid'}
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
    
def searcSitegNacClientEvents(mist_session:_APISession, site_id:str, type:str=None, nacrule_id:str=None, nacrule_matched:bool=None, auth_type:str=None, vlan:int=None, nas_vendor:str=None, bssid:str=None, eap_type:str=None, idp_id:str=None, idp_role:str=None, resp_attrs:list=None, ssid:str=None, username:str=None, ap:str=None, random_mac:bool=None, mac:str=None, timestamp:float=None, start:int=None, end:int=None, duration:str="1d", limit:int=100, page:int=1) -> _APIResponse:
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
    auth_type : str
      authentication type, e.g. “802.1X”, “MAB”, “DeviceAuth”
    vlan : int
      Vlan ID
    nas_vendor : str
      vendor of NAS device
    bssid : str
      SSID
    eap_type : str
      EAP type, e.g. “EAP-TTLS”, “EAP-TLS”
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
    if auth_type: query_params["auth_type"]=auth_type
    if vlan: query_params["vlan"]=vlan
    if nas_vendor: query_params["nas_vendor"]=nas_vendor
    if bssid: query_params["bssid"]=bssid
    if eap_type: query_params["eap_type"]=eap_type
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
    