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

@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.52.0", current_version="0.51.0", details="function replaced with listClientEventsDefinitions")
def getClientEventsDefinitions(mist_session:_APISession) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listClientEventsDefinitions
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/const/client_events"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listClientEventsDefinitions(mist_session:_APISession) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listClientEventsDefinitions
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/const/client_events"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    