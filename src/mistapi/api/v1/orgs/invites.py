
'''
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
'''
from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse

def inviteOrgAdmin(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/inviteOrgAdmin
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/invites"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def uninviteOrgAdmin(mist_session:_APISession, org_id:str, invite_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/uninviteOrgAdmin
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str invite_id        
    """
    uri = f"/api/v1/orgs/{org_id}/invites/{invite_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgAdminInvite(mist_session:_APISession, org_id:str, invite_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgAdminInvite
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str invite_id        
    """
    uri = f"/api/v1/orgs/{org_id}/invites/{invite_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    