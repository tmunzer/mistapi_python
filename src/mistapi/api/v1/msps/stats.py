from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getMspOrgLicenses(mist_session:_APISession, msp_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getMspOrgLicenses
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    """
    uri = f"/api/v1/msps/{msp_id}/stats/licenses"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getMspOrgStats(mist_session:_APISession, msp_id:str, page:int=1, limit:int=100) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getMspOrgStats
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    
    QUERY PARAMS
    ------------
    :param int page
    :param int limit        
    """
    uri = f"/api/v1/msps/{msp_id}/stats/orgs"
    query_params={}
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    