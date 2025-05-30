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

def searchSiteZoneSessions(mist_session:_APISession, site_id:str, zone_type:str, user_type:str|None=None, user:str|None=None, scope_id:str|None=None, scope:str="site", start:int|None=None, end:int|None=None, duration:str="1d", limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/zones/search-site-zone-sessions
    
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
    user_type : str{'asset', 'client', 'sdkclient'}
      User type, client (default) / sdkclient / asset
    user : str
    scope_id : str
    scope : str{'map', 'rssizone', 'site', 'zone'}, default: site
      Scope
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
    uri = f"/api/v1/sites/{site_id}/{zone_type}/visits/search"
    query_params={}
    if user_type: query_params["user_type"]=user_type
    if user: query_params["user"]=user
    if scope_id: query_params["scope_id"]=scope_id
    if scope: query_params["scope"]=scope
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    