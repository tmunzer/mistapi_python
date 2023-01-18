from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOrgServicePolicies(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgServicePolicies
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/servicepolicies"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgServicePolicy(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgServicePolicy
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/servicepolicies"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgServicePolicy(mist_session:_APISession, org_id:str, servicepolicy_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgServicePolicy
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str servicepolicy_id        
    """
    uri = f"/api/v1/orgs/{org_id}/servicepolicies/{servicepolicy_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgServicePolicy(mist_session:_APISession, org_id:str, servicepolicy_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgServicePolicy
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str servicepolicy_id        
    """
    uri = f"/api/v1/orgs/{org_id}/servicepolicies/{servicepolicy_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgServicePolicy(mist_session:_APISession, org_id:str, servicepolicy_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgServicePolicy
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str servicepolicy_id        
    """
    uri = f"/api/v1/orgs/{org_id}/servicepolicies/{servicepolicy_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    