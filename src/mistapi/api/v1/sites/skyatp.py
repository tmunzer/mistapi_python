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

def countSiteSkyatpEvents(mist_session:_APISession, site_id:str, distinct:str="type", type:str=None, mac:str=None, device_mac:str=None, threat_level:int=None, ip_address:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteSkyatpEvents
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'device_mac', 'mac', 'threat_level', 'type'}, default: type
    type : str
    mac : str
    device_mac : str
    threat_level : int
    ip_address : str
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/skyatp/events/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if type: query_params["type"]=type
    if mac: query_params["mac"]=mac
    if device_mac: query_params["device_mac"]=device_mac
    if threat_level: query_params["threat_level"]=threat_level
    if ip_address: query_params["ip_address"]=ip_address
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteSkyatpEvents(mist_session:_APISession, site_id:str, type:str=None, mac:str=None, device_mac:str=None, threat_level:int=None, ip_address:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteSkyatpEvents
    
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
    mac : str
    device_mac : str
    threat_level : int
    ip_address : str
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/skyatp/events/search"
    query_params={}
    if type: query_params["type"]=type
    if mac: query_params["mac"]=mac
    if device_mac: query_params["device_mac"]=device_mac
    if threat_level: query_params["threat_level"]=threat_level
    if ip_address: query_params["ip_address"]=ip_address
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    