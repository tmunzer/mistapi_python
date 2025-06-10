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

def generateSecretFor2faVerification(mist_session:_APISession, by:str="qrcode") -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/self/mfa/generate-secret-for2fa-verification

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    QUERY PARAMS
    ------------
    by : str{'qrcode'}, default: qrcode
      If `by`==`qrcode`, returns the secret as a qrcode image

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/self/two_factor/token"
    query_params:dict[str, str]={}
    if by:
        query_params["by"]=str(by)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp

def verifyTwoFactor(mist_session:_APISession, body:dict) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/self/mfa/verify-two-factor

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
    uri = f"/api/v1/self/two_factor/verify"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
