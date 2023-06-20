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

def countSiteWanClientEvents(mist_session:_APISession, site_id:str, distinct:str="type") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteWanClientEvents
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'type', 'hostname', 'ip', 'mfg', 'mac'}, default: type        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/wan_client/events/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    