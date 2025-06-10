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

def searchOrgEvents(mist_session:_APISession, org_id:str, type:str|None=None, start:int|None=None, end:int|None=None, duration:str="1d", limit:int=100) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/search-org-events

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
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
    uri = f"/api/v1/orgs/{org_id}/events/search"
    query_params:dict[str, str]={}
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

def countOrgSystemEvents(mist_session:_APISession, org_id:str, distinct:str|None=None, limit:int=100, start:int|None=None, end:int|None=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/events/count-org-system-events

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/events/system/count"
    query_params:dict[str, str]={}
    if distinct:
        query_params["distinct"]=str(distinct)
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

def searchOrgSystemEvents(mist_session:_APISession, org_id:str, limit:int=100, start:int|None=None, end:int|None=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/events/search-org-system-events

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/events/system/search"
    query_params:dict[str, str]={}
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
