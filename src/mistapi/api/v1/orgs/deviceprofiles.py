
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

def getOrgDeviceProfiles(mist_session:_APISession, org_id:str, type:str="ap") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgDeviceProfiles
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str type(ap, switch, gateway)        
    """
    uri = f"/api/v1/orgs/{org_id}/deviceprofiles"
    query_params={}
    if type: query_params["type"]=type
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgDeviceProfiles(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgDeviceProfiles
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/deviceprofiles"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgDeviceProfile(mist_session:_APISession, org_id:str, deviceprofile_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgDeviceProfile
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str deviceprofile_id        
    """
    uri = f"/api/v1/orgs/{org_id}/deviceprofiles/{deviceprofile_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgDeviceProfile(mist_session:_APISession, org_id:str, deviceprofile_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgDeviceProfile
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str deviceprofile_id        
    """
    uri = f"/api/v1/orgs/{org_id}/deviceprofiles/{deviceprofile_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgDeviceProfile(mist_session:_APISession, org_id:str, deviceprofile_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgDeviceProfile
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str deviceprofile_id        
    """
    uri = f"/api/v1/orgs/{org_id}/deviceprofiles/{deviceprofile_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def assignOrgDeviceProfileToDevices(mist_session:_APISession, org_id:str, deviceprofile_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/assignOrgDeviceProfileToDevices
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str deviceprofile_id        
    """
    uri = f"/api/v1/orgs/{org_id}/deviceprofiles/{deviceprofile_id}/assign"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def unassignOrgDeviceProfilesFromDevices(mist_session:_APISession, org_id:str, deviceprofile_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/unassignOrgDeviceProfilesFromDevices
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str deviceprofile_id        
    """
    uri = f"/api/v1/orgs/{org_id}/deviceprofiles/{deviceprofile_id}/unassign"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    