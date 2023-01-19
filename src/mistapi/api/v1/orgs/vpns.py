
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

def getOrgsVpns(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgsVpns
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/vpns"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgVpns(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgVpns
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/vpns"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgVpn(mist_session:_APISession, org_id:str, vpn_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgVpn
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str vpn_id        
    """
    uri = f"/api/v1/orgs/{org_id}/vpns/{vpn_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgVpn(mist_session:_APISession, org_id:str, vpn_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgVpn
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str vpn_id        
    """
    uri = f"/api/v1/orgs/{org_id}/vpns/{vpn_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgVpn(mist_session:_APISession, org_id:str, vpn_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgVpn
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str vpn_id        
    """
    uri = f"/api/v1/orgs/{org_id}/vpns/{vpn_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    