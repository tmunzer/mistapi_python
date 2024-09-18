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

def countSiteZoneSessions(mist_session:_APISession, site_id:str, zone_type:str, distinct:str="scope_id", user_type:str=None, user:str=None, scope_id:str=None, scope:str="site", page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteZoneSessions
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    zone_type : str{'rssizones', 'zones'}        
    
    QUERY PARAMS
    ------------
    distinct : str{'scope', 'scope_id', 'user', 'user_type'}, default: scope_id
    user_type : str{'asset', 'client', 'sdkclient'}
      user type
    user : str
    scope_id : str
    scope : str{'map', 'rssizone', 'site', 'zone'}, default: site
      scope
    page : int, default: 1
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/{zone_type}/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if user_type: query_params["user_type"]=user_type
    if user: query_params["user"]=user
    if scope_id: query_params["scope_id"]=scope_id
    if scope: query_params["scope"]=scope
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    