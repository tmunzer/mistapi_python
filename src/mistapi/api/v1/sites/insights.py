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

def getSiteInsightMetricsForClient(mist_session:_APISession, site_id:str, client_mac:str, metric:str, start:int=None, end:int=None, duration:str="1d", interval:str=None, limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/insights/get-site-insight-metrics-for-client
    
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
    start : int
    end : int
    duration : str, default: 1d
    interval : str
    limit : int, default: 100
    page : int, default: 1        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/insights/client/{client_mac}/{metric}"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if interval: query_params["interval"]=interval
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteInsightMetricsForDevice(mist_session:_APISession, site_id:str, metric:str, device_mac:str, start:int=None, end:int=None, duration:str="1d", interval:str=None, limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/insights/get-site-insight-metrics-for-device
    
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
    start : int
    end : int
    duration : str, default: 1d
    interval : str
    limit : int, default: 100
    page : int, default: 1        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/insights/device/{device_mac}/{metric}"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if interval: query_params["interval"]=interval
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countOrgClientFingerprints(mist_session:_APISession, site_id:str, distinct:str="family", start:int=None, end:int=None, duration:str="1d", limit:int=100) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/nac-fingerprints/count-org-client-fingerprints
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'family', 'model', 'os', 'os_type'}, default: family
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/insights/fingerprints/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchOrgClientFingerprints(mist_session:_APISession, site_id:str, family:str=None, client_type:str=None, model:str=None, mfg:str=None, os:str=None, os_type:str=None, mac:str=None, sort:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d", interval:str=None) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/nac-fingerprints/search-org-client-fingerprints
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    family : str
    client_type : str{'wireless', 'wired'}
      Whether client is wired or wireless
    model : str
    mfg : str
    os : str
    os_type : str
    mac : str
    sort : str
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
    uri = f"/api/v1/sites/{site_id}/insights/fingerprints/search"
    query_params={}
    if family: query_params["family"]=family
    if client_type: query_params["client_type"]=client_type
    if model: query_params["model"]=model
    if mfg: query_params["mfg"]=mfg
    if os: query_params["os"]=os
    if os_type: query_params["os_type"]=os_type
    if mac: query_params["mac"]=mac
    if sort: query_params["sort"]=sort
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if interval: query_params["interval"]=interval
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listSiteRogueAPs(mist_session:_APISession, site_id:str, type:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d", interval:str=None) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/rogues/list-site-rogue-a-ps
    
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
    
def listSiteRogueClients(mist_session:_APISession, site_id:str, limit:int=100, start:int=None, end:int=None, duration:str="1d", interval:str=None) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/rogues/list-site-rogue-clients
    
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
    
def getSiteInsightMetrics(mist_session:_APISession, site_id:str, metric:str, start:int=None, end:int=None, duration:str="1d", interval:str=None, limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/insights/get-site-insight-metrics
    
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
    start : int
    end : int
    duration : str, default: 1d
    interval : str
    limit : int, default: 100
    page : int, default: 1        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/insights/{metric}"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if interval: query_params["interval"]=interval
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    