
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

def getSiteSsrUpgrade(mist_session:_APISession, site_id:str, upgrade_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteSsrUpgrade
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str upgrade_id        
    """
    uri = f"/api/v1/sites/{site_id}/ssr/upgrade/{upgrade_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def upgradeSiteSsr(mist_session:_APISession, site_id:str, device_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/upgradeSiteSsr
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id        
    """
    uri = f"/api/v1/sites/{site_id}/ssr/{device_id}/upgrade"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    