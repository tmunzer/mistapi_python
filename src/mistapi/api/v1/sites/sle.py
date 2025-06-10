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
def getSiteSleClassifierDetails(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, classifier:str, start:int=None, end:int=None, duration:str="1d") -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/sles/get-site-sle-classifier-details
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    scope : str{'ap', 'client', 'gateway', 'site', 'switch'}
    scope_id : str
    metric : str
    classifier : str        
    
    QUERY PARAMS
    ------------
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/classifier/{classifier}/summary"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def listSiteSleMetricClassifiers(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/sles/list-site-sle-metric-classifiers
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    scope : str{'ap', 'client', 'gateway', 'site', 'switch'}
    scope_id : str
    metric : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/classifiers"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def getSiteSleHistogram(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, start:int=None, end:int=None, duration:str="1d") -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/sles/get-site-sle-histogram
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    scope : str{'ap', 'client', 'gateway', 'site', 'switch'}
    scope_id : str
    metric : str        
    
    QUERY PARAMS
    ------------
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/histogram"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def getSiteSleImpactSummary(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, start:int=None, end:int=None, duration:str="1d", fields:str=None, classifier:str=None) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/sles/get-site-sle-impact-summary
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    scope : str{'ap', 'client', 'gateway', 'site', 'switch'}
    scope_id : str
    metric : str        
    
    QUERY PARAMS
    ------------
    start : int
    end : int
    duration : str, default: 1d
    fields : str{'ap', 'band', 'chassis', 'client', 'device_os', 'device_type', 'gateway', 'gateway_zones', 'interface', 'mxedge', 'peer_path', 'server', 'switch', 'vlan', 'wlan'}
    classifier : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/impact-summary"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if fields: query_params["fields"]=fields
    if classifier: query_params["classifier"]=classifier
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def listSiteSleImpactedApplications(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, start:int=None, end:int=None, duration:str="1d", classifier:str=None) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/sles/list-site-sle-impacted-applications
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    scope : str{'gateway', 'site', 'switch'}
    scope_id : str
    metric : str        
    
    QUERY PARAMS
    ------------
    start : int
    end : int
    duration : str, default: 1d
    classifier : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/impacted-applications"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if classifier: query_params["classifier"]=classifier
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def listSiteSleImpactedAps(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, start:int=None, end:int=None, duration:str="1d", classifier:str=None) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/sles/list-site-sle-impacted-aps
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    scope : str{'site'}
    scope_id : str
    metric : str        
    
    QUERY PARAMS
    ------------
    start : int
    end : int
    duration : str, default: 1d
    classifier : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/impacted-aps"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if classifier: query_params["classifier"]=classifier
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def listSiteSleImpactedChassis(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, start:int=None, end:int=None, duration:str="1d", classifier:str=None) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/sles/list-site-sle-impacted-chassis
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    scope : str{'gateway', 'site', 'switch'}
    scope_id : str
    metric : str        
    
    QUERY PARAMS
    ------------
    start : int
    end : int
    duration : str, default: 1d
    classifier : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/impacted-chassis"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if classifier: query_params["classifier"]=classifier
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def listSiteSleImpactedWiredClients(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, start:int=None, end:int=None, duration:str="1d", classifier:str=None) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/sles/list-site-sle-impacted-wired-clients
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    scope : str{'gateway', 'site', 'switch'}
    scope_id : str
    metric : str        
    
    QUERY PARAMS
    ------------
    start : int
    end : int
    duration : str, default: 1d
    classifier : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/impacted-clients"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if classifier: query_params["classifier"]=classifier
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def listSiteSleImpactedGateways(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, start:int=None, end:int=None, duration:str="1d", classifier:str=None) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/sles/list-site-sle-impacted-gateways
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    scope : str{'site'}
    scope_id : str
    metric : str        
    
    QUERY PARAMS
    ------------
    start : int
    end : int
    duration : str, default: 1d
    classifier : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/impacted-gateways"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if classifier: query_params["classifier"]=classifier
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def listSiteSleImpactedInterfaces(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, start:int=None, end:int=None, duration:str="1d", classifier:str=None) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/sles/list-site-sle-impacted-interfaces
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    scope : str{'gateway', 'site', 'switch'}
    scope_id : str
    metric : str        
    
    QUERY PARAMS
    ------------
    start : int
    end : int
    duration : str, default: 1d
    classifier : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/impacted-interfaces"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if classifier: query_params["classifier"]=classifier
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def listSiteSleImpactedSwitches(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, start:int=None, end:int=None, duration:str="1d", classifier:str=None) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/sles/list-site-sle-impacted-switches
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    scope : str{'site'}
    scope_id : str
    metric : str        
    
    QUERY PARAMS
    ------------
    start : int
    end : int
    duration : str, default: 1d
    classifier : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/impacted-switches"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if classifier: query_params["classifier"]=classifier
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def listSiteSleImpactedWirelessClients(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, start:int=None, end:int=None, duration:str="1d", classifier:str=None) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/sles/list-site-sle-impacted-wireless-clients
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    scope : str{'ap', 'site'}
    scope_id : str
    metric : str        
    
    QUERY PARAMS
    ------------
    start : int
    end : int
    duration : str, default: 1d
    classifier : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/impacted-users"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if classifier: query_params["classifier"]=classifier
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def getSiteSleSummary(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, start:int=None, end:int=None, duration:str="1d") -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/sles/get-site-sle-summary
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    scope : str{'ap', 'client', 'gateway', 'site', 'switch'}
    scope_id : str
    metric : str        
    
    QUERY PARAMS
    ------------
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/summary"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def getSiteSleThreshold(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/sles/get-site-sle-threshold
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    scope : str{'ap', 'client', 'gateway', 'site', 'switch'}
    scope_id : str
    metric : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/threshold"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
@sync_async_compatible
def replaceSiteSleThreshold(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, body:object) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/sles/replace-site-sle-threshold
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    scope : str{'ap', 'client', 'gateway', 'site', 'switch'}
    scope_id : str
    metric : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/threshold"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
@sync_async_compatible
def updateSiteSleThreshold(mist_session:_APISession, site_id:str, scope:str, scope_id:str, metric:str, body:object) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/sles/update-site-sle-threshold
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    scope : str{'ap', 'client', 'gateway', 'site', 'switch'}
    scope_id : str
    metric : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metric/{metric}/threshold"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
@sync_async_compatible
def listSiteSlesMetrics(mist_session:_APISession, site_id:str, scope:str, scope_id:str) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/sles/list-site-sles-metrics
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    scope : str{'ap', 'client', 'gateway', 'site', 'switch'}
    scope_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    