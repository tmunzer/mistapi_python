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
def triggerSiteSyntheticTest(mist_session:_APISession, site_id:str, body:object) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/synthetic-tests/trigger-site-synthetic-test
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/synthetic_test"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
@sync_async_compatible
def searchSiteSyntheticTest(mist_session:_APISession, site_id:str, mac:str=None, port_id:str=None, vlan_id:str=None, by:str=None, reason:str=None, type:str=None, protocol:str=None, tenant:str=None) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/synthetic-tests/search-site-synthetic-test
    
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
    port_id : str
    vlan_id : str
    by : str
    reason : str
    type : str{'arp', 'curl', 'dhcp', 'dhcp6', 'dns', 'lan_connectivity', 'radius', 'speedtest'}
      Synthetic test type
    protocol : str{'ping', 'traceroute'}
      Connectivity protocol
    tenant : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/synthetic_test/search"
    query_params={}
    if mac: query_params["mac"]=mac
    if port_id: query_params["port_id"]=port_id
    if vlan_id: query_params["vlan_id"]=vlan_id
    if by: query_params["by"]=by
    if reason: query_params["reason"]=reason
    if type: query_params["type"]=type
    if protocol: query_params["protocol"]=protocol
    if tenant: query_params["tenant"]=tenant
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    