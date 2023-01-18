from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def UnsubscribeSite(mist_session:_APISession, site_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/UnsubscribeSite
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/subscriptions"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def SubscribeSite(mist_session:_APISession, site_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/SubscribeSite
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/subscriptions"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    