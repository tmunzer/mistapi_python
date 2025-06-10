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
def countSiteWanUsage(mist_session:_APISession, site_id:str, mac:str=None, peer_mac:str=None, port_id:str=None, peer_port_id:str=None, policy:str=None, tenant:str=None, path_type:str=None, distinct:str="policy", start:int=None, end:int=None, duration:str="1d", limit:int=100) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/wan-usages/count-site-wan-usage
    
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
    peer_mac : str
    port_id : str
    peer_port_id : str
    policy : str
    tenant : str
    path_type : str
    distinct : str{'mac', 'path_type', 'peer_mac', 'peer_port_id', 'policy', 'port_id', 'tenant'}, default: policy
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/wan_usages/count"
    query_params={}
    if mac: query_params["mac"]=mac
    if peer_mac: query_params["peer_mac"]=peer_mac
    if port_id: query_params["port_id"]=port_id
    if peer_port_id: query_params["peer_port_id"]=peer_port_id
    if policy: query_params["policy"]=policy
    if tenant: query_params["tenant"]=tenant
    if path_type: query_params["path_type"]=path_type
    if distinct: query_params["distinct"]=distinct
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def searchSiteWanUsage(mist_session:_APISession, site_id:str, mac:str=None, peer_mac:str=None, port_id:str=None, peer_port_id:str=None, policy:str=None, tenant:str=None, path_type:str=None, start:int=None, end:int=None, duration:str="1d", limit:int=100, page:int=1) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/wan-usages/search-site-wan-usage
    
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
    peer_mac : str
    port_id : str
    peer_port_id : str
    policy : str
    tenant : str
    path_type : str
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
    uri = f"/api/v1/sites/{site_id}/wan_usages/search"
    query_params={}
    if mac: query_params["mac"]=mac
    if peer_mac: query_params["peer_mac"]=peer_mac
    if port_id: query_params["port_id"]=port_id
    if peer_port_id: query_params["peer_port_id"]=peer_port_id
    if policy: query_params["policy"]=policy
    if tenant: query_params["tenant"]=tenant
    if path_type: query_params["path_type"]=path_type
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    