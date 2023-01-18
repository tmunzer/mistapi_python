from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getSiteWebhooks(mist_session:_APISession, site_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteWebhooks
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/webhooks"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createSiteWebhook(mist_session:_APISession, site_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createSiteWebhook
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/webhooks"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteWebhook(mist_session:_APISession, site_id:str, webhook_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteWebhook
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str webhook_id        
    """
    uri = f"/api/v1/sites/{site_id}/webhooks/{webhook_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteSiteWebhook(mist_session:_APISession, site_id:str, webhook_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteSiteWebhook
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str webhook_id        
    """
    uri = f"/api/v1/sites/{site_id}/webhooks/{webhook_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateSiteWebhook(mist_session:_APISession, site_id:str, webhook_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSiteWebhook
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str webhook_id        
    """
    uri = f"/api/v1/sites/{site_id}/webhooks/{webhook_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def pingSiteWebhook(mist_session:_APISession, site_id:str, webhook_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/pingSiteWebhook
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str webhook_id        
    """
    uri = f"/api/v1/sites/{site_id}/webhooks/{webhook_id}/ping"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    