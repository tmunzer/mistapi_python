
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

def getApiTokens(mist_session:_APISession) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getApiTokens
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    """
    uri = f"/api/v1/self/apitokens"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createApiToken(mist_session:_APISession, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createApiToken
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    """
    uri = f"/api/v1/self/apitokens"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def deleteApiToken(mist_session:_APISession, apitoken_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteApiToken
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str apitoken_id        
    """
    uri = f"/api/v1/self/apitokens/{apitoken_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    