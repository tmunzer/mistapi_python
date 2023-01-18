from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def testSiteWlanTelstraSetup(mist_session:_APISession) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/testSiteWlanTelstraSetup
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    """
    uri = f"/api/v1/utils/test_telstra"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    