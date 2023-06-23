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

@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.41.8", details="function replaced with listMspLogs")  
def getMspLogs(mist_session:_APISession, msp_id:str, site_id:str=None, admin_name:str=None, message:str=None, sort:str=None, start:int=None, end:int=None, limit:int=100, page:int=1, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listMspLogs
    
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
      site id
    admin_name : str
      admin name or email
    message : str
      message
    sort : str{'timestamp', '-timestamp', 'site_id', 'admin_id'}
      sort order
    start : int
    end : int
    limit : int, default: 100
    page : int, default: 1
    duration : str, default: 1d        
    
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
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listMspLogs(mist_session:_APISession, msp_id:str, site_id:str=None, admin_name:str=None, message:str=None, sort:str=None, start:int=None, end:int=None, limit:int=100, page:int=1, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listMspLogs
    
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
      site id
    admin_name : str
      admin name or email
    message : str
      message
    sort : str{'timestamp', '-timestamp', 'site_id', 'admin_id'}
      sort order
    start : int
    end : int
    limit : int, default: 100
    page : int, default: 1
    duration : str, default: 1d        
    
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
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countMspLogs(mist_session:_APISession, msp_id:str, distinct:str="admin_name") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countMspLogs
    
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
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/msps/{msp_id}/logs/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    