
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

def verifyRecoverPasssword(mist_session:_APISession, token:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/verifyRecoverPasssword
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str token        
    """
    uri = f"/api/v1/recover/verify/{token}"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    