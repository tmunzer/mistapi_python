from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse

def getOrgSettings(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgSettings
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/setting"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def updateOrgSettings(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgSettings
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/setting"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def deleteOrgClientsBlocklist(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgClientsBlocklist
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/setting/blacklist"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def createOrgClientsBlocklist(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgClientsBlocklist
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/setting/blacklist"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def setupOrgCradlepointConnectionToMist(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/setupOrgCradlepointConnectionToMist
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/setting/cradlepoint/setup"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def syncOrgCradlepointRouters(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/syncOrgCradlepointRouters
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/setting/cradlepoint/sync"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def linkOrgToJuniperJuniperAccount(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/linkOrgToJuniperJuniperAccount
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/setting/juniper/link_accounts"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def unlinkOrgFromJuniperCustomerId(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/unlinkOrgFromJuniperCustomerId
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/setting/juniper/linked_account"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def setOrgCustomBucket(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/setOrgCustomBucket
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/setting/pcap_bucket/setup"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def verifyOrgCustomBucket(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/verifyOrgCustomBucket
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/setting/pcap_bucket/verify"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgOauthAppLinkedStatus(mist_session:_APISession, org_id:str, app_name:str, forward:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgOauthAppLinkedStatus
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str app_name - OAuth application name (Example : zoom, teams, etc..)        
    
    QUERY PARAMS
    ------------
    :param str forward - Mist portal url to which backend needs to redirect after succesful OAuth authorization. **Required** to get the `authorization_url`        
    """
    uri = f"/api/v1/orgs/{org_id}/setting/{app_name}/link"
    query_params={}
    if forward: query_params["forward"]=forward
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgOauthAppAuthorization(mist_session:_APISession, org_id:str, app_name:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgOauthAppAuthorization
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str app_name - OAuth application name (Example : zoom, teams, etc..)        
    """
    uri = f"/api/v1/orgs/{org_id}/setting/{app_name}/link"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    