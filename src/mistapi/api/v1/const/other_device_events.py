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

@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.41.0", details="function replaced with listOtherDeviceEventsDefinitions")  
def getOtherDeviceEventsDefinitions(mist_session:_APISession) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOtherDeviceEventsDefinitions
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/const/other_device_events"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listOtherDeviceEventsDefinitions(mist_session:_APISession) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOtherDeviceEventsDefinitions
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/const/other_device_events"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    