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

def getSiteInsightMetricsForClient(mist_session:_APISession, site_id:str, client_mac:str, metric:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d", interval:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteInsightMetricsForClient
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    client_mac : str
    metric : str        
    
    QUERY PARAMS
    ------------
    page : int, default: 1
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d
    interval : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/insights/client/{client_mac}/{metric}"
    query_params={}
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if interval: query_params["interval"]=interval
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteInsightMetricsForDevice(mist_session:_APISession, site_id:str, metric:str, device_mac:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d", interval:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteInsightMetricsForDevice
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    metric : str
    device_mac : str        
    
    QUERY PARAMS
    ------------
    page : int, default: 1
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d
    interval : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/insights/device/{device_mac}/{metric}"
    query_params={}
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if interval: query_params["interval"]=interval
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.44.2", details="function replaced with listSiteRogueAPs")  
def getSiteRogueAPs(mist_session:_APISession, site_id:str, type:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d", interval:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteRogueAPs
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    type : str{'honeypot', 'lan', 'others', 'spoof'}
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d
    interval : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/insights/rogues"
    query_params={}
    if type: query_params["type"]=type
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if interval: query_params["interval"]=interval
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listSiteRogueAPs(mist_session:_APISession, site_id:str, type:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d", interval:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteRogueAPs
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    type : str{'honeypot', 'lan', 'others', 'spoof'}
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d
    interval : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/insights/rogues"
    query_params={}
    if type: query_params["type"]=type
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if interval: query_params["interval"]=interval
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.44.2", details="function replaced with listSiteRogueClients")  
def getSiteRogueClients(mist_session:_APISession, site_id:str, limit:int=100, start:int=None, end:int=None, duration:str="1d", interval:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteRogueClients
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d
    interval : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/insights/rogues/clients"
    query_params={}
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if interval: query_params["interval"]=interval
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listSiteRogueClients(mist_session:_APISession, site_id:str, limit:int=100, start:int=None, end:int=None, duration:str="1d", interval:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteRogueClients
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d
    interval : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/insights/rogues/clients"
    query_params={}
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if interval: query_params["interval"]=interval
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteInsightMetrics(mist_session:_APISession, site_id:str, metric:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d", interval:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteInsightMetrics
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    metric : str        
    
    QUERY PARAMS
    ------------
    page : int, default: 1
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d
    interval : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/insights/{metric}"
    query_params={}
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if interval: query_params["interval"]=interval
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    