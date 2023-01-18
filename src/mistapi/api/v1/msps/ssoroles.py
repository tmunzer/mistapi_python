from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getMspSsoRoles(mist_session:_APISession, msp_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getMspSsoRoles
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    """
    uri = f"/api/v1/msps/{msp_id}/ssoroles"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createMspSsoRole(mist_session:_APISession, msp_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createMspSsoRole
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    """
    uri = f"/api/v1/msps/{msp_id}/ssoroles"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def deleteMspSsoRoles(mist_session:_APISession, msp_id:str, ssorole_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteMspSsoRoles
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id
    :param str ssorole_id        
    """
    uri = f"/api/v1/msps/{msp_id}/ssoroles/{ssorole_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateMspSsoRole(mist_session:_APISession, msp_id:str, ssorole_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateMspSsoRole
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id
    :param str ssorole_id        
    """
    uri = f"/api/v1/msps/{msp_id}/ssoroles/{ssorole_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    