from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getMxEdgeEventsDefinitions(mist_session:_APISession) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getMxEdgeEventsDefinitions
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    """
    uri = f"/api/v1/const/mxedge_events"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    