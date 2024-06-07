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

def countSiteWanUsage(mist_session:_APISession, site_id:str, mac:str=None, peer_mac:str=None, port_id:str=None, peer_port_id:str=None, policy:str=None, tenant:str=None, path_type:str=None, distinct:str="policy", page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteWanUsage
    
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
    distinct : str{'mac', 'peer_mac', 'port_id', 'peer_port_id', 'policy', 'tenant', 'path_type'}, default: policy
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
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteWanUsage(mist_session:_APISession, site_id:str, mac:str=None, peer_mac:str=None, port_id:str=None, peer_port_id:str=None, policy:str=None, tenant:str=None, path_type:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteWanUsage
    
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
    uri = f"/api/v1/sites/{site_id}/wan_usages/search"
    query_params={}
    if mac: query_params["mac"]=mac
    if peer_mac: query_params["peer_mac"]=peer_mac
    if port_id: query_params["port_id"]=port_id
    if peer_port_id: query_params["peer_port_id"]=peer_port_id
    if policy: query_params["policy"]=policy
    if tenant: query_params["tenant"]=tenant
    if path_type: query_params["path_type"]=path_type
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    