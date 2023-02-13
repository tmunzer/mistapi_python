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

def UnsubscribeSite(mist_session:_APISession, site_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/UnsubscribeSite
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/subscriptions"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def SubscribeSite(mist_session:_APISession, site_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/SubscribeSite
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/subscriptions"
    resp = mist_session.mist_post(uri=uri)
    return resp
    