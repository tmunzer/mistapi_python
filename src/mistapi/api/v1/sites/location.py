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

def getSiteBeamCoverageOverview(mist_session:_APISession, site_id:str, map_id:str=None, type:str="sdkclient", duration:str="1h", resolution:str="default", client_type:str=None, start:int=None, end:int=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteBeamCoverageOverview
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    map_id : str
      map_id (filter by map_id)
    type : str{'sdkclient', 'client', 'asset'}, default: sdkclient
    duration : str{'1d', '5h', '1h', '30m'}, default: 1h
      where the start time will be calculated (with end time is now)
    resolution : str{'default', 'fine'}, default: default
    client_type : str
      client_type (as filter. optional)
    start : int
    end : int        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/location/coverage"
    query_params={}
    if map_id: query_params["map_id"]=map_id
    if type: query_params["type"]=type
    if duration: query_params["duration"]=duration
    if resolution: query_params["resolution"]=resolution
    if client_type: query_params["client_type"]=client_type
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteMachineLearningCurrentStat(mist_session:_APISession, site_id:str, map_id:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteMachineLearningCurrentStat
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    map_id : str
      map_id (as filter, optional)        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/location/ml/current"
    query_params={}
    if map_id: query_params["map_id"]=map_id
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteDefaultPlfForModels(mist_session:_APISession, site_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteDefaultPlfForModels
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/location/ml/defaults"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def clearSiteMlOverwriteForDevice(mist_session:_APISession, site_id:str, device_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/clearSiteMlOverwriteForDevice
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    device_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/location/ml/device/{device_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def overwriteSiteMlForDevice(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/overwriteSiteMlForDevice
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    device_id : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/location/ml/device/{device_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def clearSiteMlOverwriteForMap(mist_session:_APISession, site_id:str, map_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/clearSiteMlOverwriteForMap
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    map_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/location/ml/map/{map_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def overwriteSiteMlForMap(mist_session:_APISession, site_id:str, map_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/overwriteSiteMlForMap
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    map_id : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/location/ml/map/{map_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def resetSiteMlStatsByMap(mist_session:_APISession, site_id:str, map_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/resetSiteMlStatsByMap
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    map_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/location/ml/reset/map/{map_id}"
    resp = mist_session.mist_post(uri=uri)
    return resp
    
def getSiteMachineLearningEvents(mist_session:_APISession, site_id:str, device_id:str=None, map_ip:str=None, client_type:str=None, duration:str=None, start:int=None, end:int=None, interval:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteMachineLearningEvents
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    device_id : str
      device_id (as filter, optional)
    map_ip : str
      map_id (as filter, optional)
    client_type : str
      client_type (as filter, optional)
    duration : str
      instead of start, you can use 1d, 30m, 5h, where the start will be calculated
    start : int
    end : int
    interval : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/location/ml/updates"
    query_params={}
    if device_id: query_params["device_id"]=device_id
    if map_ip: query_params["map_ip"]=map_ip
    if client_type: query_params["client_type"]=client_type
    if duration: query_params["duration"]=duration
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if interval: query_params["interval"]=interval
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    