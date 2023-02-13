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

def getOrgAssets(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgAssets
    
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
    uri = f"/api/v1/orgs/{org_id}/assets"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgAsset(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgAsset
    
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
    uri = f"/api/v1/orgs/{org_id}/assets"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def importOrgAssetsFile(mist_session:_APISession, org_id:str, file_path:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/importOrgAssets
    
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
    uri = f"/api/v1/orgs/{org_id}/assets/import"
    with open(file_path, "rb") as f:    
        files = {"file": f.read()}
        resp = mist_session.mist_post_file(uri=uri, files=files)
    
def importOrgAssets(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/importOrgAssets
    
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
    uri = f"/api/v1/orgs/{org_id}/assets/import"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgAsset(mist_session:_APISession, org_id:str, asset_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgAsset
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str asset_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/assets/{asset_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgAsset(mist_session:_APISession, org_id:str, asset_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgAsset
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str asset_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/assets/{asset_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgAsset(mist_session:_APISession, org_id:str, asset_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgAsset
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str asset_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/assets/{asset_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    