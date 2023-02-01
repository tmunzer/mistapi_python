
'''
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
'''
from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse

def getOrgSitesSle(mist_session:_APISession, org_id:str, sle:str=None, start:int=None, end:int=None, limit:int=100, page:int=1, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgSitesSle
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str sle(wan, wired, wifi)
    :param int start
    :param int end
    :param int limit
    :param int page
    :param str duration        
    """
    uri = f"/api/v1/orgs/{org_id}/insights/sites-sle"
    query_params={}
    if sle: query_params["sle"]=sle
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getOrgSle(mist_session:_APISession, org_id:str, metric:str, sle:str=None, duration:str="1d", interval:str=None, start:int=None, end:int=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgSle
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str metric        
    
    QUERY PARAMS
    ------------
    :param str sle - see [/api/v1/const/insight_metrics](/#tag/Constants/operation/getSiteAvailableInsightMetrics) for more details
    :param str duration
    :param str interval(10m, 1h)
    :param int start
    :param int end        
    """
    uri = f"/api/v1/orgs/{org_id}/insights/{metric}"
    query_params={}
    if sle: query_params["sle"]=sle
    if duration: query_params["duration"]=duration
    if interval: query_params["interval"]=interval
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    