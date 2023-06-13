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

@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.40.1", details="function replaced with listSdkTemplates")  
def getSdkTemplates(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSdkTemplates
    
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
    uri = f"/api/v1/orgs/{org_id}/sdktemplates"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listSdkTemplates(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSdkTemplates
    
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
    uri = f"/api/v1/orgs/{org_id}/sdktemplates"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createSdkTemplate(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createSdkTemplate
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    BODY PARAMS
    -----------
    :param dict body - JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/sdktemplates"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSdkTemplate(mist_session:_APISession, org_id:str, sdktemplate_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSdkTemplate
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str sdktemplate_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/sdktemplates/{sdktemplate_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteSdkTemplate(mist_session:_APISession, org_id:str, sdktemplate_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteSdkTemplate
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str sdktemplate_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/sdktemplates/{sdktemplate_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateSdkTemplate(mist_session:_APISession, org_id:str, sdktemplate_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSdkTemplate
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str sdktemplate_id        
    
    BODY PARAMS
    -----------
    :param dict body - JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/sdktemplates/{sdktemplate_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    