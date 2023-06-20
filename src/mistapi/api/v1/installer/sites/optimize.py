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

def optimizeInstallerRrm(mist_session:_APISession, site_name:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/optimizeInstallerRrm
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_name : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/installer/sites/{site_name}/optimize"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    