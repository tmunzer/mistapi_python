from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def deleteMspLogo(mist_session:_APISession, msp_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteMspLogo
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    """
    uri = f"/api/v1/msps/{msp_id}/logo"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def postMspLogo(mist_session:_APISession, msp_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/postMspLogo
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    """
    uri = f"/api/v1/msps/{msp_id}/logo"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    