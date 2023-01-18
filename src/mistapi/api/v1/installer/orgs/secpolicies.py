from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getInstallerSecPolicies(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getInstallerSecPolicies
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/installer/orgs/{org_id}/secpolicies"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    