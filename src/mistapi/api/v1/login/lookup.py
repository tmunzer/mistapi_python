from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse

def lookup(mist_session:_APISession, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/lookup
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    """
    uri = f"/api/v1/login/lookup"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    