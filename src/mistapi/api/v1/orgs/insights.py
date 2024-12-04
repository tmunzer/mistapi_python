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

def getOrgSitesSle(mist_session:_APISession, org_id:str, sle:str=None, start:int=None, end:int=None, duration:str="1d", interval:str=None, limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgSitesSle
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    sle : str{'wan', 'wifi', 'wired'}
    start : int
    end : int
    duration : str, default: 1d
    interval : str
    limit : int, default: 100
    page : int, default: 1        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/insights/sites-sle"
    query_params={}
    if sle: query_params["sle"]=sle
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if interval: query_params["interval"]=interval
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getOrgSle(mist_session:_APISession, org_id:str, metric:str, sle:str=None, duration:str="1d", interval:str=None, start:int=None, end:int=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgSle
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
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
    uri = f"/api/v1/orgs/{org_id}/insights/{metric}"
    query_params={}
    if sle: query_params["sle"]=sle
    if duration: query_params["duration"]=duration
    if interval: query_params["interval"]=interval
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    