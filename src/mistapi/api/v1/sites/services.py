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

@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.52.0", current_version="0.47.5", details="function replaced with listSiteServicesDerived")  
def getSiteServicesDerived(mist_session:_APISession, site_id:str, resolve:bool=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteServicesDerived
    
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
      whether resolve the site variables        
    
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
    
def listSiteServicesDerived(mist_session:_APISession, site_id:str, resolve:bool=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteServicesDerived
    
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
      whether resolve the site variables        
    
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
    
def countSiteServicePathEvents(mist_session:_APISession, site_id:str, distinct:str="type", type:str=None, text:str=None, vpn_name:str=None, vpn_path:str=None, policy:str=None, port_id:str=None, model:str=None, version:str=None, timestamp:float=None, mac:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteServicePathEvents
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'type', 'mac', 'vpn_name', 'vpn_path', 'policy', 'port_id', 'model', 'site_id'}, default: type
    type : str
      Event type, e.g. GW_SERVICE_PATH_DOWN
    text : str
      Description of the event including the reason it is triggered
    vpn_name : str
      Peer name
    vpn_path : str
      Peer path name
    policy : str
      Service policy associated with that specific path
    port_id : str
      Network interface
    model : str
      Device model
    version : str
      Device firmware version
    timestamp : float
      Start time, in epoch
    mac : str
      MAC address        
    
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
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteServicePathEvents(mist_session:_APISession, site_id:str, type:str=None, text:str=None, vpn_name:str=None, vpn_path:str=None, policy:str=None, port_id:str=None, model:str=None, version:str=None, timestamp:float=None, mac:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteServicePathEvents
    
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
      Event type, e.g. GW_SERVICE_PATH_DOWN
    text : str
      Description of the event including the reason it is triggered
    vpn_name : str
      Peer name
    vpn_path : str
      Peer path name
    policy : str
      Service policy associated with that specific path
    port_id : str
      Network interface
    model : str
      Device model
    version : str
      Device firmware version
    timestamp : float
      Start time, in epoch
    mac : str
      MAC address        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/services/events/search"
    query_params={}
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
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    