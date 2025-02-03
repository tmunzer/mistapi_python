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

def listInstallerSites(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/installer/list-installer-sites
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/installer/orgs/{org_id}/sites"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrUpdateInstallerSites(mist_session:_APISession, org_id:str, site_name:str, body:object) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/installer/create-or-update-installer-sites
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    site_name : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/installer/orgs/{org_id}/sites/{site_name}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def listInstallerMaps(mist_session:_APISession, org_id:str, site_name:str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/installer/list-installer-maps
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    site_name : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/installer/orgs/{org_id}/sites/{site_name}/maps"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def importInstallerMapFile(mist_session:_APISession, org_id:str, site_name:str, auto_deviceprofile_assignment:bool=None, csv:str=None, file:str=None, json:any=None) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/installer/import-installer-map
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    site_name : str        
    
    BODY PARAMS
    -----------
    auto_deviceprofile_assignment : bool
        Whether to auto assign device to deviceprofile by name
    csv : str
        path to the file to upload. CSV file for ap name mapping, optional
    file : str
        path to the file to upload. Ekahau or ibwave file
    json : any
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    multipart_form_data = {
        "auto_deviceprofile_assignment":auto_deviceprofile_assignment,
        "csv":csv,
        "file":file,
        "json":json,
    }
    uri = f"/api/v1/installer/orgs/{org_id}/sites/{site_name}/maps/import"
    resp = mist_session.mist_post_file(uri=uri, multipart_form_data=multipart_form_data)
    return resp

def deleteInstallerMap(mist_session:_APISession, org_id:str, site_name:str, map_id:str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/installer/delete-installer-map
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    site_name : str
    map_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/installer/orgs/{org_id}/sites/{site_name}/maps/{map_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def createInstallerMap(mist_session:_APISession, org_id:str, site_name:str, map_id:str, body:object) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/installer/create-installer-map
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    site_name : str
    map_id : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/installer/orgs/{org_id}/sites/{site_name}/maps/{map_id}"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def updateInstallerMap(mist_session:_APISession, org_id:str, site_name:str, map_id:str, body:object) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/installer/update-installer-map
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    site_name : str
    map_id : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/installer/orgs/{org_id}/sites/{site_name}/maps/{map_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    