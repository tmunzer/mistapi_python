
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

def generateQrCodeForVerification(mist_session:_APISession, by:str="qrcode") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/generateQrCodeForVerification
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    QUERY PARAMS
    ------------
    :param str by(qrcode)        
    """
    uri = f"/api/v1/self/two_factor/token"
    query_params={}
    if by: query_params["by"]=by
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def verifyTwoFactor(mist_session:_APISession, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/verifyTwoFactor
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    """
    uri = f"/api/v1/self/two_factor/verify"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    