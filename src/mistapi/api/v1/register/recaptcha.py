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
def getAdminRegistrationInfo(mist_session:_APISession, recaptcha_flavor:str="google") -> Union[_APIResponse, Awaitable[_APIResponse]]:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/admins/get-admin-registration-info
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    QUERY PARAMS
    ------------
    recaptcha_flavor : str{'google', 'hcaptcha'}, default: google        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/register/recaptcha"
    query_params={}
    if recaptcha_flavor: query_params["recaptcha_flavor"]=recaptcha_flavor
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    