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

@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.41.5", details="function replaced with listInstallerListOfRenctlyClaimedDevices")  
def getInstallerListOfRenctlyClaimedDevices(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listInstallerListOfRenctlyClaimedDevices
    
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
    uri = f"/api/v1/installer/orgs/{org_id}/devices"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listInstallerListOfRenctlyClaimedDevices(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listInstallerListOfRenctlyClaimedDevices
    
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
    uri = f"/api/v1/installer/orgs/{org_id}/devices"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def claimInstallerDevices(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/claimInstallerDevices
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/installer/orgs/{org_id}/devices"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def unassignInstallerRecentlyClaimedDevice(mist_session:_APISession, org_id:str, device_mac:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/unassignInstallerRecentlyClaimedDevice
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    device_mac : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/installer/orgs/{org_id}/devices/{device_mac}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def provisionInstallerDevices(mist_session:_APISession, org_id:str, device_mac:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/provisionInstallerDevices
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    device_mac : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/installer/orgs/{org_id}/devices/{device_mac}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def startInstallerLocateDevice(mist_session:_APISession, org_id:str, device_mac:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/startInstallerLocateDevice
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    device_mac : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/installer/orgs/{org_id}/devices/{device_mac}/locate"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def stopInstallerLocateDevice(mist_session:_APISession, org_id:str, device_mac:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/stopInstallerLocateDevice
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    device_mac : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/installer/orgs/{org_id}/devices/{device_mac}/unlocate"
    resp = mist_session.mist_post(uri=uri)
    return resp
    
def deleteInstallerDeviceImage(mist_session:_APISession, org_id:str, image_name:str, device_mac:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteInstallerDeviceImage
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    image_name : str
    device_mac : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/installer/orgs/{org_id}/devices/{device_mac}/{image_name}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def addInstallerDeviceImageFile(mist_session:_APISession, org_id:str, image_name:str, device_mac:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/addInstallerDeviceImage
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    image_name : str
    device_mac : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    multipart_form_data = {
    }
    uri = f"/api/v1/installer/orgs/{org_id}/devices/{device_mac}/{image_name}"
    resp = mist_session.mist_post_file(uri=uri, multipart_form_data=multipart_form_data)
    return resp
