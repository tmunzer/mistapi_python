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

def getOAuth2AuthorizationUrlForLogin(mist_session:_APISession, provider:str, forward:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOAuth2AuthorizationUrlForLogin
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str provider        
    
    QUERY PARAMS
    ------------
    :param str forward        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/login/oauth/{provider}"
    query_params={}
    if forward: query_params["forward"]=forward
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def unlinkOAuth2Provider(mist_session:_APISession, provider:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/unlinkOAuth2Provider
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str provider        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/login/oauth/{provider}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def loginOAuth2(mist_session:_APISession, provider:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/loginOAuth2
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str provider        
    
    BODY PARAMS
    -----------
    :param dict body - JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/login/oauth/{provider}"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    