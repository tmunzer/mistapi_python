from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse

def getSiteAvailableInsightMetrics(mist_session:_APISession) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteAvailableInsightMetrics
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    """
    uri = f"/api/v1/const/insight_metrics"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    