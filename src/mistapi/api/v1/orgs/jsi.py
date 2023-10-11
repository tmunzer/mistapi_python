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

@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.52.0", current_version="0.46.3", details="function replaced with listOrgJsiDevices")  
def getOrgJsiDevices(mist_session:_APISession, org_id:str, limit:int=100, page:int=1, model:str=None, serial:str=None, mac:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgJsiDevices
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    limit : int, default: 100
    page : int, default: 1
    model : str
    serial : str
    mac : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/jsi/devices"
    query_params={}
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    if model: query_params["model"]=model
    if serial: query_params["serial"]=serial
    if mac: query_params["mac"]=mac
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listOrgJsiDevices(mist_session:_APISession, org_id:str, limit:int=100, page:int=1, model:str=None, serial:str=None, mac:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgJsiDevices
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    limit : int, default: 100
    page : int, default: 1
    model : str
    serial : str
    mac : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/jsi/devices"
    query_params={}
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    if model: query_params["model"]=model
    if serial: query_params["serial"]=serial
    if mac: query_params["mac"]=mac
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def adoptOrgJsiDevice(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/adoptOrgJsiDevice
    
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
    uri = f"/api/v1/orgs/{org_id}/jsi/devices/outbound_ssh_cmd"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgJsiDeviceShellSession(mist_session:_APISession, org_id:str, device_mac:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgJsiDeviceShellSession
    
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
    uri = f"/api/v1/orgs/{org_id}/jsi/devices/{device_mac}/shell"
    resp = mist_session.mist_post(uri=uri)
    return resp
    
def upgradeOrgJsiDevice(mist_session:_APISession, org_id:str, device_mac:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/upgradeOrgJsiDevice
    
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
    uri = f"/api/v1/orgs/{org_id}/jsi/devices/{device_mac}/upgrade"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.52.0", current_version="0.46.3", details="function replaced with listOrgJsiPastPurchases")  
def getOrgJsiPastPurchases(mist_session:_APISession, org_id:str, limit:int=100, page:int=1, model:str=None, serial:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgJsiPastPurchases
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    limit : int, default: 100
    page : int, default: 1
    model : str
    serial : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/jsi/inventory"
    query_params={}
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    if model: query_params["model"]=model
    if serial: query_params["serial"]=serial
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listOrgJsiPastPurchases(mist_session:_APISession, org_id:str, limit:int=100, page:int=1, model:str=None, serial:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgJsiPastPurchases
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    limit : int, default: 100
    page : int, default: 1
    model : str
    serial : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/jsi/inventory"
    query_params={}
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    if model: query_params["model"]=model
    if serial: query_params["serial"]=serial
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    