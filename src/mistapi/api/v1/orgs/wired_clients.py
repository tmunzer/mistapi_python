'''
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
'''

from typing import Union, Awaitable
from mistapi import APISession as _APISession
from mistapi.__decorator import sync_async_compatible
from mistapi.__api_response import APIResponse as _APIResponse
import deprecation

@sync_async_compatible
def countOrgWiredClients(mist_session:_APISession, org_id:str, distinct:str="mac", start:int=None, end:int=None, duration:str="1d", limit:int=100) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/wired/count-org-wired-clients
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'device_mac', 'mac', 'port_id', 'site_id', 'type', 'vlan'}, default: mac
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/wired_clients/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def searchOrgWiredClients(mist_session:_APISession, org_id:str, auth_state:str=None, auth_method:str=None, site_id:str=None, device_mac:str=None, mac:str=None, port_id:str=None, vlan:int=None, ip_address:str=None, manufacture:str=None, text:str=None, nacrule_id:str=None, dhcp_hostname:str=None, dhcp_fqdn:str=None, dhcp_client_identifier:str=None, dhcp_vendor_class_identifier:str=None, dhcp_request_params:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/wired/search-org-wired-clients
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    auth_state : str
    auth_method : str
    site_id : str
    device_mac : str
    mac : str
    port_id : str
    vlan : int
    ip_address : str
    manufacture : str
    text : str
    nacrule_id : str
    dhcp_hostname : str
    dhcp_fqdn : str
    dhcp_client_identifier : str
    dhcp_vendor_class_identifier : str
    dhcp_request_params : str
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/wired_clients/search"
    query_params={}
    if auth_state: query_params["auth_state"]=auth_state
    if auth_method: query_params["auth_method"]=auth_method
    if site_id: query_params["site_id"]=site_id
    if device_mac: query_params["device_mac"]=device_mac
    if mac: query_params["mac"]=mac
    if port_id: query_params["port_id"]=port_id
    if vlan: query_params["vlan"]=vlan
    if ip_address: query_params["ip_address"]=ip_address
    if manufacture: query_params["manufacture"]=manufacture
    if text: query_params["text"]=text
    if nacrule_id: query_params["nacrule_id"]=nacrule_id
    if dhcp_hostname: query_params["dhcp_hostname"]=dhcp_hostname
    if dhcp_fqdn: query_params["dhcp_fqdn"]=dhcp_fqdn
    if dhcp_client_identifier: query_params["dhcp_client_identifier"]=dhcp_client_identifier
    if dhcp_vendor_class_identifier: query_params["dhcp_vendor_class_identifier"]=dhcp_vendor_class_identifier
    if dhcp_request_params: query_params["dhcp_request_params"]=dhcp_request_params
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def reauthOrgDot1xWiredClient(mist_session:_APISession, org_id:str, client_mac:str) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/lan/reauth-org-dot1x-wired-client
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    client_mac : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/wired_clients/{client_mac}/coa"
    resp = mist_session.mist_post(uri=uri)
    return resp
    