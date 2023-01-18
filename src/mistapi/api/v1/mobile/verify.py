from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def activateSdkInvite(mist_session:_APISession, secret:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/activateSdkInvite
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str secret        
    """
    uri = f"/api/v1/mobile/verify/{secret}"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    