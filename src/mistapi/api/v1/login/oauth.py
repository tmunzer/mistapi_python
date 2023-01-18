from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOAuth2AuthorizationUrlForLogin(mist_session:_APISession, provider:str, forward:str=None) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOAuth2AuthorizationUrlForLogin
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str provider        
    
    QUERY PARAMS
    ------------
    :param str forward        
    """
    uri = f"/api/v1/login/oauth/{provider}"
    query_params={}
    if forward: query_params["forward"]=forward
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def unlinkOAuth2Provider(mist_session:_APISession, provider:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/unlinkOAuth2Provider
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str provider        
    """
    uri = f"/api/v1/login/oauth/{provider}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def loginOAuth2(mist_session:_APISession, provider:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/loginOAuth2
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str provider        
    """
    uri = f"/api/v1/login/oauth/{provider}"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    