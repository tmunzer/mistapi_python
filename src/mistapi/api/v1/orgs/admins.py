from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOrgAdmins(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgAdmins
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/admins"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def revokeOrgAdmin(mist_session:_APISession, org_id:str, admin_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/revokeOrgAdmin
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str admin_id        
    """
    uri = f"/api/v1/orgs/{org_id}/admins/{admin_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgAdmin(mist_session:_APISession, org_id:str, admin_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgAdmin
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str admin_id        
    """
    uri = f"/api/v1/orgs/{org_id}/admins/{admin_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    