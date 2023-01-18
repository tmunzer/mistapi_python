from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getSiteLanguages(mist_session:_APISession) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteLanguages
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    """
    uri = f"/api/v1/const/languages"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    