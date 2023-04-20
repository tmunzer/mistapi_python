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
import deprecation

@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.37.8", details="function replaced with listInstallerSites")  
def getInstallerSites(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listInstallerSites
    
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
    
def listInstallerSites(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listInstallerSites
    
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
    
    BODY PARAMS
    -----------
    :param dict body - JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/installer/orgs/{org_id}/sites/{site_name}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.37.8", details="function replaced with listInstallerMaps")  
def getInstallerMaps(mist_session:_APISession, org_id:str, site_name:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listInstallerMaps
    
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
    
def listInstallerMaps(mist_session:_APISession, org_id:str, site_name:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listInstallerMaps
    
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
    
def importInstallerMapFile(mist_session:_APISession, org_id:str, site_name:str, file_path:str="", csv_path:str="", body:dict={}) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/importInstallerMap
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str site_name        
    
    BODY PARAMS
    -----------
    :param dict body - JSON object to send to Mist Cloud (see API doc above for more details)
    :param str file_path - path to the file to upload
    :param str csv_path - path to the csv file to upload
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/installer/orgs/{org_id}/sites/{site_name}/maps/import"
    resp = mist_session.mist_post_file(uri=uri, file=file_path, csv=csv_path, body=body)
    return resp

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
    
    BODY PARAMS
    -----------
    :param dict body - JSON object to send to Mist Cloud (see API doc above for more details)
    
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
    
    BODY PARAMS
    -----------
    :param dict body - JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/installer/orgs/{org_id}/sites/{site_name}/maps/{map_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    