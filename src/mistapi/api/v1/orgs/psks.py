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

def getOrgPsks(mist_session:_APISession, org_id:str, name:str=None, ssid:str=None, role:str=None, page:int=1, limit:int=100) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgPsks
    
    PARAMS
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
    
    RETURN
    -----------
    :return APIResponse - response from the API call
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
    
def createOrgPsk(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgPsk
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/psks"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def updateOrgMultiPsks(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgMultiPsks
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/psks"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def importOrgPskFile(mist_session:_APISession, org_id:str, file_path:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/importOrgPsk
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    FILE PARAMS
    -----------
    :param str file_path - path to the file to upload
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/psks/import"
    with open(file_path, "rb") as f:    
        files = {"file": f.read()}
        resp = mist_session.mist_post_file(uri=uri, files=files)
    
def importOrgPsk(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/importOrgPsk
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/psks/import"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgPsk(mist_session:_APISession, org_id:str, psk_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgPsk
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str psk_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/psks/{psk_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgPsk(mist_session:_APISession, org_id:str, psk_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgPsk
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str psk_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/psks/{psk_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgPsk(mist_session:_APISession, org_id:str, psk_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgPsk
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str psk_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/psks/{psk_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def deleteOrgPskOldPassphrase(mist_session:_APISession, org_id:str, psk_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgPskOldPassphrase
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str psk_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/psks/{psk_id}/delete_old_passphrase"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    