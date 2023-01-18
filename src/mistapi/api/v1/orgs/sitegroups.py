from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOrgSiteGroups(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgSiteGroups
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/sitegroups"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgSiteGroup(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgSiteGroup
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/sitegroups"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgSiteGroup(mist_session:_APISession, org_id:str, sitegroup_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgSiteGroup
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str sitegroup_id        
    """
    uri = f"/api/v1/orgs/{org_id}/sitegroups/{sitegroup_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgSiteGroup(mist_session:_APISession, org_id:str, sitegroup_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgSiteGroup
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str sitegroup_id        
    """
    uri = f"/api/v1/orgs/{org_id}/sitegroups/{sitegroup_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgSiteGroup(mist_session:_APISession, org_id:str, sitegroup_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgSiteGroup
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str sitegroup_id        
    """
    uri = f"/api/v1/orgs/{org_id}/sitegroups/{sitegroup_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    