from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse

def getOrgNacTags(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgNacTags
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/nactags"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgNacTag(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgNacTag
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/nactags"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgNacTag(mist_session:_APISession, org_id:str, nactag_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgNacTag
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str nactag_id        
    """
    uri = f"/api/v1/orgs/{org_id}/nactags/{nactag_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def DeleteOrgNacTag(mist_session:_APISession, org_id:str, nactag_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/DeleteOrgNacTag
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str nactag_id        
    """
    uri = f"/api/v1/orgs/{org_id}/nactags/{nactag_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgNacTag(mist_session:_APISession, org_id:str, nactag_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgNacTag
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str nactag_id        
    """
    uri = f"/api/v1/orgs/{org_id}/nactags/{nactag_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    