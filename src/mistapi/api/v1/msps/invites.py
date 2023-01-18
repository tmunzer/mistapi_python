from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def inviteMspAdmin(mist_session:_APISession, msp_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/inviteMspAdmin
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    """
    uri = f"/api/v1/msps/{msp_id}/invites"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def uninviteMspAdmin(mist_session:_APISession, msp_id:str, invite_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/uninviteMspAdmin
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id
    :param str invite_id        
    """
    uri = f"/api/v1/msps/{msp_id}/invites/{invite_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateMspAdminInvite(mist_session:_APISession, msp_id:str, invite_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateMspAdminInvite
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id
    :param str invite_id        
    """
    uri = f"/api/v1/msps/{msp_id}/invites/{invite_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    