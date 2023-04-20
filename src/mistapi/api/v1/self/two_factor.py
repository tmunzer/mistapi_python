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

def generateQrCodeForVerification(mist_session:_APISession, by:str="qrcode") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/generateQrCodeForVerification
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    QUERY PARAMS
    ------------
    :param str by(qrcode)        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/self/two_factor/token"
    query_params={}
    if by: query_params["by"]=by
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def verifyTwoFactor(mist_session:_APISession, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/verifyTwoFactor
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    BODY PARAMS
    -----------
    :param dict body - JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/self/two_factor/verify"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    