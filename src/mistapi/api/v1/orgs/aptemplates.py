from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOrgAptemplates(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgAptemplates
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/aptemplates"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgAptemplate(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgAptemplate
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/aptemplates"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgAptemplate(mist_session:_APISession, org_id:str, aptemplate_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgAptemplate
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str aptemplate_id        
    """
    uri = f"/api/v1/orgs/{org_id}/aptemplates/{aptemplate_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgAptemplate(mist_session:_APISession, org_id:str, aptemplate_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgAptemplate
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str aptemplate_id        
    """
    uri = f"/api/v1/orgs/{org_id}/aptemplates/{aptemplate_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgAptemplate(mist_session:_APISession, org_id:str, aptemplate_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgAptemplate
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str aptemplate_id        
    """
    uri = f"/api/v1/orgs/{org_id}/aptemplates/{aptemplate_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    