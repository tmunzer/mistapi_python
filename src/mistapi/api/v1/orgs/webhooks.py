from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOrgWebhooks(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgWebhooks
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/webhooks"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgWebhook(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgWebhook
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/webhooks"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgWebhook(mist_session:_APISession, org_id:str, webhook_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgWebhook
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str webhook_id        
    """
    uri = f"/api/v1/orgs/{org_id}/webhooks/{webhook_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgWebhook(mist_session:_APISession, org_id:str, webhook_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgWebhook
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str webhook_id        
    """
    uri = f"/api/v1/orgs/{org_id}/webhooks/{webhook_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgWebhook(mist_session:_APISession, org_id:str, webhook_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgWebhook
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str webhook_id        
    """
    uri = f"/api/v1/orgs/{org_id}/webhooks/{webhook_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    