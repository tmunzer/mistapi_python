from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getSiteCurrentChannelPlanning(mist_session:_APISession, site_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteCurrentChannelPlanning
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/rrm/current"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteCurrentRrmConsiderationsForAnApOnASpecificBand(mist_session:_APISession, site_id:str, device_id:str, band:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteCurrentRrmConsiderationsForAnApOnASpecificBand
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str device_id
    :param str band - radio band        
    """
    uri = f"/api/v1/sites/{site_id}/rrm/current/devices/{device_id}/band/{band}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteRrmEvents(mist_session:_APISession, site_id:str, band:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteRrmEvents
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str band(24, 5, 6)
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/sites/{site_id}/rrm/events"
    query_params={}
    if band: query_params["band"]=band
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def optimizeSiteRrm(mist_session:_APISession, site_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/optimizeSiteRrm
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/rrm/optimize"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    