from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOrgNetworkTemplates(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgNetworkTemplates
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/networktemplates"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgNetworkTemplate(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgNetworkTemplate
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/networktemplates"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgNetworkTemplate(mist_session:_APISession, org_id:str, networktemplate_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgNetworkTemplate
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str networktemplate_id        
    """
    uri = f"/api/v1/orgs/{org_id}/networktemplates/{networktemplate_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgNetworkTemplate(mist_session:_APISession, org_id:str, networktemplate_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgNetworkTemplate
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str networktemplate_id        
    """
    uri = f"/api/v1/orgs/{org_id}/networktemplates/{networktemplate_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgNetworkTemplates(mist_session:_APISession, org_id:str, networktemplate_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgNetworkTemplates
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str networktemplate_id        
    """
    uri = f"/api/v1/orgs/{org_id}/networktemplates/{networktemplate_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    