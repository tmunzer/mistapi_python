from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOrg128TRegistrationCommands(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrg128TRegistrationCommands
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/128routers/register_cmd"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getOrgSsrUpgrades(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgSsrUpgrades
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/ssr/upgrade"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def upgradeOrgSsrs(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/upgradeOrgSsrs
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/ssr/upgrade"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def cancelOrgSsrUpgrade(mist_session:_APISession, org_id:str, upgrade_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/cancelOrgSsrUpgrade
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str upgrade_id        
    """
    uri = f"/api/v1/orgs/{org_id}/ssr/upgrade/{upgrade_id}/cancel"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgSsrUpgradeInfo(mist_session:_APISession, org_id:str, channel:str=None) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgSsrUpgradeInfo
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str channel        
    """
    uri = f"/api/v1/orgs/{org_id}/ssr/versions"
    query_params={}
    if channel: query_params["channel"]=channel
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    