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

def listMspSsoRoles(mist_session:_APISession, msp_id:str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/msps/sso-roles/list-msp-sso-roles

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    msp_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/msps/{msp_id}/ssoroles"
    query_params:dict[str, str]={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp

def createMspSsoRole(mist_session:_APISession, msp_id:str, body:dict) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/msps/sso-roles/create-msp-sso-role

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    msp_id : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/msps/{msp_id}/ssoroles"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp

def deleteMspSsoRole(mist_session:_APISession, msp_id:str, ssorole_id:str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/msps/sso-roles/delete-msp-sso-role

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    msp_id : str
    ssorole_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/msps/{msp_id}/ssoroles/{ssorole_id}"
    query_params:dict[str, str]={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp

def updateMspSsoRole(mist_session:_APISession, msp_id:str, ssorole_id:str, body:dict) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/msps/sso-roles/update-msp-sso-role

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    msp_id : str
    ssorole_id : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/msps/{msp_id}/ssoroles/{ssorole_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
