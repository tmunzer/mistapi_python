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

def countSiteCallEvents(mist_session:_APISession, site_id:str, distinct:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteCallEvents
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'type', 'app'}        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/call/events/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteCallEvents(mist_session:_APISession, site_id:str, type:str=None, ap:str=None, mac:str=None, app:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteCallEvents
    
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
      Event Type. See [listCallEventsDefinitions](/#operation/listCallEventsDefinitions)
    ap : str
    mac : str
    app : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/call/events/search"
    query_params={}
    if type: query_params["type"]=type
    if ap: query_params["ap"]=ap
    if mac: query_params["mac"]=mac
    if app: query_params["app"]=app
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    