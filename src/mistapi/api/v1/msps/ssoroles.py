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

def getMspSsoRoles(mist_session:_APISession, msp_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getMspSsoRoles
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/msps/{msp_id}/ssoroles"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createMspSsoRole(mist_session:_APISession, msp_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createMspSsoRole
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/msps/{msp_id}/ssoroles"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def deleteMspSsoRole(mist_session:_APISession, msp_id:str, ssorole_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteMspSsoRole
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id
    :param str ssorole_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/msps/{msp_id}/ssoroles/{ssorole_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateMspSsoRole(mist_session:_APISession, msp_id:str, ssorole_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateMspSsoRole
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id
    :param str ssorole_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/msps/{msp_id}/ssoroles/{ssorole_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    