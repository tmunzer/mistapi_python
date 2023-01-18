from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getSdkInvites(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSdkInvites
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/sdkinvites"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createSdkInvite(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createSdkInvite
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/sdkinvites"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSdkInvite(mist_session:_APISession, org_id:str, sdkinvite_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSdkInvite
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str sdkinvite_id        
    """
    uri = f"/api/v1/orgs/{org_id}/sdkinvites/{sdkinvite_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def revokeSdkInvite(mist_session:_APISession, org_id:str, sdkinvite_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/revokeSdkInvite
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str sdkinvite_id        
    """
    uri = f"/api/v1/orgs/{org_id}/sdkinvites/{sdkinvite_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateSdkInvite(mist_session:_APISession, org_id:str, sdkinvite_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSdkInvite
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str sdkinvite_id        
    """
    uri = f"/api/v1/orgs/{org_id}/sdkinvites/{sdkinvite_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def sendSdkInviteEmail(mist_session:_APISession, org_id:str, sdkinvite_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/sendSdkInviteEmail
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str sdkinvite_id        
    """
    uri = f"/api/v1/orgs/{org_id}/sdkinvites/{sdkinvite_id}/email"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSdkInviteQrCode(mist_session:_APISession, org_id:str, sdkinvite_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSdkInviteQrCode
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str sdkinvite_id        
    """
    uri = f"/api/v1/orgs/{org_id}/sdkinvites/{sdkinvite_id}/qrcode"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def sendSdkInviteSms(mist_session:_APISession, org_id:str, sdkinvite_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/sendSdkInviteSms
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str sdkinvite_id        
    """
    uri = f"/api/v1/orgs/{org_id}/sdkinvites/{sdkinvite_id}/sms"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    