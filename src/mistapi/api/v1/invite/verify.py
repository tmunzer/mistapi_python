from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse

def verifyAdminInvite(mist_session:_APISession, token:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/verifyAdminInvite
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str token        
    """
    uri = f"/api/v1/invite/verify/{token}"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    