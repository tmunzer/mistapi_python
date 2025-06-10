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
def troubleshootOrg(mist_session:_APISession, org_id:str, mac:str=None, site_id:str=None, start:int=None, end:int=None, type:str=None) -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/marvis/troubleshoot-org
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    mac : str
    site_id : str
    start : int
    end : int
    type : str{'wan', 'wired', 'wireless'}
      When troubleshooting site, type of network to troubleshoot        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/troubleshoot"
    query_params={}
    if mac: query_params["mac"]=mac
    if site_id: query_params["site_id"]=site_id
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if type: query_params["type"]=type
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    