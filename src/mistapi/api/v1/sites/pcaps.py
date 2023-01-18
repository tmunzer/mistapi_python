from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getSitePacketCaptures(mist_session:_APISession, site_id:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d", client_mac:str=None) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSitePacketCaptures
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)
    :param str client_mac - optional client mac filter        
    """
    uri = f"/api/v1/sites/{site_id}/pcaps"
    query_params={}
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if client_mac: query_params["client_mac"]=client_mac
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteCapturingStatus(mist_session:_APISession, site_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteCapturingStatus
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/pcaps/capture"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def stopSitePacketCapture(mist_session:_APISession, site_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/stopSitePacketCapture
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/pcaps/capture"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def startSitePacketCapture(mist_session:_APISession, site_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/startSitePacketCapture
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/pcaps/capture"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    