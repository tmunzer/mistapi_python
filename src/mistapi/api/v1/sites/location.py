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

def getSiteBeamCoverageOverview(mist_session:_APISession, site_id:str, map_id:str=None, type:str="sdkclient", duration:str="1h", resolution:str="default", client_type:str=None, start:int=None, end:int=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteBeamCoverageOverview
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str map_id - map_id (filter by map_id)
    :param str type(sdkclient, client, asset)
    :param str duration(1d, 5h, 1h, 30m) - where the start time will be calculated (with end time is now)
    :param str resolution(default, fine)
    :param str client_type - client_type (as filter. optional)
    :param int start
    :param int end        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
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
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str map_id - map_id (as filter, optional)        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
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
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
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
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
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
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/location/ml/device/{device_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def clearSiteMlOverwriteForMap(mist_session:_APISession, site_id:str, map_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/clearSiteMlOverwriteForMap
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str map_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
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
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str map_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/location/ml/map/{map_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def resetSiteMlStatsByMap(mist_session:_APISession, site_id:str, map_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/resetSiteMlStatsByMap
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str map_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/location/ml/reset/map/{map_id}"
    resp = mist_session.mist_post(uri=uri)
    return resp
    
def getSiteMachineLearningEvents(mist_session:_APISession, site_id:str, device_id:str=None, map_ip:str=None, client_type:str=None, duration:str=None, start:int=None, end:int=None, interval:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteMachineLearningEvents
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str device_id - device_id (as filter, optional)
    :param str map_ip - map_id (as filter, optional)
    :param str client_type - client_type (as filter, optional)
    :param str duration - instead of start, you can use 1d, 30m, 5h, where the start will be calculated
    :param int start
    :param int end
    :param str interval        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
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
    