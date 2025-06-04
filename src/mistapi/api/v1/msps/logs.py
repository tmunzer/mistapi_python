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

def listMspAuditLogs(mist_session:_APISession, msp_id:str, site_id:str=None, admin_name:str=None, message:str=None, sort:str=None, start:int=None, end:int=None, duration:str="1d", limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/msps/logs/list-msp-audit-logs
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    msp_id : str        
    
    QUERY PARAMS
    ------------
    site_id : str
    admin_name : str
    message : str
    sort : str{'-timestamp', 'admin_id', 'site_id', 'timestamp'}
      Sort order
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100
    page : int, default: 1        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/msps/{msp_id}/logs"
    query_params={}
    if site_id: query_params["site_id"]=site_id
    if admin_name: query_params["admin_name"]=admin_name
    if message: query_params["message"]=message
    if sort: query_params["sort"]=sort
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countMspAuditLogs(mist_session:_APISession, msp_id:str, distinct:str="admin_name", limit:int=100) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/msps/logs/count-msp-audit-logs
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    msp_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'admin_id', 'admin_name', 'message', 'org_id'}, default: admin_name
    limit : int, default: 100        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/msps/{msp_id}/logs/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    