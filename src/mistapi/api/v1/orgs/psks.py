from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOrgPsks(mist_session:_APISession, org_id:str, name:str=None, ssid:str=None, role:str=None, page:int=1, limit:int=100) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgPsks
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str name
    :param str ssid
    :param str role
    :param int page
    :param int limit        
    """
    uri = f"/api/v1/orgs/{org_id}/psks"
    query_params={}
    if name: query_params["name"]=name
    if ssid: query_params["ssid"]=ssid
    if role: query_params["role"]=role
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgPsk(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgPsk
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/psks"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def updateOrgMultiPsks(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgMultiPsks
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/psks"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def importOrgPsk(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/importOrgPsk
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/psks/import"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgPsk(mist_session:_APISession, org_id:str, psk_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgPsk
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str psk_id        
    """
    uri = f"/api/v1/orgs/{org_id}/psks/{psk_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgPsk(mist_session:_APISession, org_id:str, psk_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgPsk
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str psk_id        
    """
    uri = f"/api/v1/orgs/{org_id}/psks/{psk_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgPsk(mist_session:_APISession, org_id:str, psk_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgPsk
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str psk_id        
    """
    uri = f"/api/v1/orgs/{org_id}/psks/{psk_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def deleteOrgPskOldPassphrase(mist_session:_APISession, org_id:str, psk_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgPskOldPassphrase
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str psk_id        
    """
    uri = f"/api/v1/orgs/{org_id}/psks/{psk_id}/delete_old_passphrase"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    