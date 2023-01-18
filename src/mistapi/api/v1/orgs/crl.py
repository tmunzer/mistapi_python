from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOrgCrlFile(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgCrlFile
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/crl"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def truncateOrgCrlFile(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/truncateOrgCrlFile
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/crl/truncate"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    