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

def listSiteRoamingEvents(mist_session:_APISession, site_id:str, type:str|None=None, limit:int=100, start:int|None=None, end:int|None=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/events/list-site-roaming-events

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    type : str{'fail', 'none', 'success'}
      Event type
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/events/fast_roam"
    query_params:dict[str, str]={}
    if type:
        query_params["type"]=str(type)
    if limit:
        query_params["limit"]=str(limit)
    if start:
        query_params["start"]=str(start)
    if end:
        query_params["end"]=str(end)
    if duration:
        query_params["duration"]=str(duration)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp

def countSiteSystemEvents(mist_session:_APISession, site_id:str, distinct:str="type", type:str|None=None, start:int|None=None, end:int|None=None, duration:str="1d", limit:int=100) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/events/count-site-system-events

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    distinct : str{'type'}, default: type
    type : str
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/events/system/count"
    query_params:dict[str, str]={}
    if distinct:
        query_params["distinct"]=str(distinct)
    if type:
        query_params["type"]=str(type)
    if start:
        query_params["start"]=str(start)
    if end:
        query_params["end"]=str(end)
    if duration:
        query_params["duration"]=str(duration)
    if limit:
        query_params["limit"]=str(limit)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp

def searchSiteSystemEvents(mist_session:_APISession, site_id:str, type:str|None=None, limit:int=100, start:int|None=None, end:int|None=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/events/search-site-system-events

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
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/events/system/search"
    query_params:dict[str, str]={}
    if type:
        query_params["type"]=str(type)
    if limit:
        query_params["limit"]=str(limit)
    if start:
        query_params["start"]=str(start)
    if end:
        query_params["end"]=str(end)
    if duration:
        query_params["duration"]=str(duration)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
