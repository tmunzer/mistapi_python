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
def getMspSle(mist_session:_APISession, msp_id:str, metric:str, sle:str=None, duration:str="1d", interval:str=None, start:int=None, end:int=None) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/msps/sles/get-msp-sle
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    msp_id : str
    metric : str        
    
    QUERY PARAMS
    ------------
    sle : str
    duration : str, default: 1d
    interval : str
    start : int
    end : int        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/msps/{msp_id}/insights/{metric}"
    query_params={}
    if sle: query_params["sle"]=sle
    if duration: query_params["duration"]=duration
    if interval: query_params["interval"]=interval
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    