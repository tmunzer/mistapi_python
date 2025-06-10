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

def listApiTokens(mist_session:_APISession) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/self/api-token/list-api-tokens

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/self/apitokens"
    query_params:dict[str, str]={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp

def createApiToken(mist_session:_APISession, body:dict) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/self/api-token/create-api-token

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/self/apitokens"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp

def getApiToken(mist_session:_APISession, apitoken_id:str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/self/api-token/get-api-token

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    apitoken_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/self/apitokens/{apitoken_id}"
    query_params:dict[str, str]={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp

def deleteApiToken(mist_session:_APISession, apitoken_id:str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/self/api-token/delete-api-token

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    apitoken_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/self/apitokens/{apitoken_id}"
    query_params:dict[str, str]={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp

def updateApiToken(mist_session:_APISession, apitoken_id:str, body:dict) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/self/api-token/update-api-token

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    apitoken_id : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/self/apitokens/{apitoken_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
