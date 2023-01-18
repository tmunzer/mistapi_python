from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def updateSelfEmail(mist_session:_APISession, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSelfEmail
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    """
    uri = f"/api/v1/self/update"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def verifySelfEmail(mist_session:_APISession, token:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/verifySelfEmail
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str token        
    """
    uri = f"/api/v1/self/update/verify/{token}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    