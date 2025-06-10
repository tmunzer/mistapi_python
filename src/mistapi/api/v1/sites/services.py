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
def listSiteServicesDerived(mist_session:_APISession, site_id:str, resolve:bool=None) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/services/list-site-services-derived
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    resolve : bool        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/services/derived"
    query_params={}
    if resolve: query_params["resolve"]=resolve
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def countSiteServicePathEvents(mist_session:_APISession, site_id:str, distinct:str="type", type:str=None, text:str=None, vpn_name:str=None, vpn_path:str=None, policy:str=None, port_id:str=None, model:str=None, version:str=None, timestamp:float=None, mac:str=None, start:int=None, end:int=None, duration:str="1d", limit:int=100) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/services/count-site-service-path-events
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'mac', 'model', 'policy', 'port_id', 'site_id', 'type', 'vpn_name', 'vpn_path'}, default: type
    type : str
    text : str
    vpn_name : str
    vpn_path : str
    policy : str
    port_id : str
    model : str
    version : str
    timestamp : float
    mac : str
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/services/events/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if type: query_params["type"]=type
    if text: query_params["text"]=text
    if vpn_name: query_params["vpn_name"]=vpn_name
    if vpn_path: query_params["vpn_path"]=vpn_path
    if policy: query_params["policy"]=policy
    if port_id: query_params["port_id"]=port_id
    if model: query_params["model"]=model
    if version: query_params["version"]=version
    if timestamp: query_params["timestamp"]=timestamp
    if mac: query_params["mac"]=mac
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def searchSiteServicePathEvents(mist_session:_APISession, site_id:str, type:str=None, text:str=None, peer_port_id:str=None, peer_mac:str=None, vpn_name:str=None, vpn_path:str=None, policy:str=None, port_id:str=None, model:str=None, version:str=None, timestamp:float=None, mac:str=None, start:int=None, end:int=None, duration:str="1d", limit:int=100) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/services/search-site-service-path-events
    
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
    text : str
    peer_port_id : str
    peer_mac : str
    vpn_name : str
    vpn_path : str
    policy : str
    port_id : str
    model : str
    version : str
    timestamp : float
    mac : str
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/services/events/search"
    query_params={}
    if type: query_params["type"]=type
    if text: query_params["text"]=text
    if peer_port_id: query_params["peer_port_id"]=peer_port_id
    if peer_mac: query_params["peer_mac"]=peer_mac
    if vpn_name: query_params["vpn_name"]=vpn_name
    if vpn_path: query_params["vpn_path"]=vpn_path
    if policy: query_params["policy"]=policy
    if port_id: query_params["port_id"]=port_id
    if model: query_params["model"]=model
    if version: query_params["version"]=version
    if timestamp: query_params["timestamp"]=timestamp
    if mac: query_params["mac"]=mac
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    