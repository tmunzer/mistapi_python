
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

def getSiteApps(mist_session:_APISession, site_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteApps
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/apps"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    