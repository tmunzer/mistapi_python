from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getTrafficTypes(mist_session:_APISession) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getTrafficTypes
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    """
    uri = f"/api/v1/const/traffic_types"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    