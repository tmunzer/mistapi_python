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

def getInstallerSites(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getInstallerSites
    
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
    uri = f"/api/v1/installer/orgs/{org_id}/sites"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrUpdateInstallerSites(mist_session:_APISession, org_id:str, site_name:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrUpdateInstallerSites
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str site_name        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/installer/orgs/{org_id}/sites/{site_name}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def getInstallerMaps(mist_session:_APISession, org_id:str, site_name:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getInstallerMaps
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str site_name        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/installer/orgs/{org_id}/sites/{site_name}/maps"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def importInstallerMapFile(mist_session:_APISession, org_id:str, site_name:str, file_path:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/importInstallerMap
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str site_name        
    
    FILE PARAMS
    -----------
    :param str file_path - path to the file to upload
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/installer/orgs/{org_id}/sites/{site_name}/maps/import"
    with open(file_path, "rb") as f:    
        files = {"file": f.read()}
        resp = mist_session.mist_post_file(uri=uri, files=files)
    
def deleteInstallerMap(mist_session:_APISession, org_id:str, site_name:str, map_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteInstallerMap
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str site_name
    :param str map_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/installer/orgs/{org_id}/sites/{site_name}/maps/{map_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def createInstallerMap(mist_session:_APISession, org_id:str, site_name:str, map_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createInstallerMap
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str site_name
    :param str map_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/installer/orgs/{org_id}/sites/{site_name}/maps/{map_id}"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def updateInstallerMap(mist_session:_APISession, org_id:str, site_name:str, map_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateInstallerMap
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str site_name
    :param str map_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/installer/orgs/{org_id}/sites/{site_name}/maps/{map_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    