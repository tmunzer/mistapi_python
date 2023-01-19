
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

def getOAuth2UrlForLinking(mist_session:_APISession, provider:str, forward:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOAuth2UrlForLinking
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str provider        
    
    QUERY PARAMS
    ------------
    :param str forward        
    """
    uri = f"/api/v1/self/oauth/{provider}"
    query_params={}
    if forward: query_params["forward"]=forward
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def linkOAuth2MistAccount(mist_session:_APISession, provider:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/linkOAuth2MistAccount
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str provider        
    """
    uri = f"/api/v1/self/oauth/{provider}"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    