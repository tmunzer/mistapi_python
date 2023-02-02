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

def getOrgJsiDevices(mist_session:_APISession, org_id:str, limit:int=100, page:int=1, model:str=None, serial:str=None, mac:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgJsiDevices
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param int limit
    :param int page
    :param str model
    :param str serial
    :param str mac        
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
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/jsi/devices/outbound_ssh_cmd"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgJsiDeviceShellSession(mist_session:_APISession, org_id:str, device_mac:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgJsiDeviceShellSession
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str device_mac        
    """
    uri = f"/api/v1/orgs/{org_id}/jsi/devices/{device_mac}/shell"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def upgradeOrgJsiDevice(mist_session:_APISession, org_id:str, device_mac:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/upgradeOrgJsiDevice
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str device_mac        
    """
    uri = f"/api/v1/orgs/{org_id}/jsi/devices/{device_mac}/upgrade"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgJsiPastPurchases(mist_session:_APISession, org_id:str, limit:int=100, page:int=1, model:str=None, serial:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgJsiPastPurchases
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param int limit
    :param int page
    :param str model
    :param str serial        
    """
    uri = f"/api/v1/orgs/{org_id}/jsi/inventory"
    query_params={}
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    if model: query_params["model"]=model
    if serial: query_params["serial"]=serial
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    