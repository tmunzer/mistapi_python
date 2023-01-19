from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse

def recoverPassword(mist_session:_APISession, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/recoverPassword
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    """
    uri = f"/api/v1/recover"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    