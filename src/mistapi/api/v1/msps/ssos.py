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

def getMspSso(mist_session:_APISession, msp_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getMspSso
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    """
    uri = f"/api/v1/msps/{msp_id}/ssos"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createMspSso(mist_session:_APISession, msp_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createMspSso
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    """
    uri = f"/api/v1/msps/{msp_id}/ssos"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def deleteMspSso(mist_session:_APISession, msp_id:str, sso_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteMspSso
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id
    :param str sso_id        
    """
    uri = f"/api/v1/msps/{msp_id}/ssos/{sso_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateMspSso(mist_session:_APISession, msp_id:str, sso_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateMspSso
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id
    :param str sso_id        
    """
    uri = f"/api/v1/msps/{msp_id}/ssos/{sso_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def getMspSsoLatestFailures(mist_session:_APISession, msp_id:str, sso_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getMspSsoLatestFailures
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id
    :param str sso_id        
    """
    uri = f"/api/v1/msps/{msp_id}/ssos/{sso_id}/failures"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getMspSsoSamlMetadata(mist_session:_APISession, msp_id:str, sso_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getMspSsoSamlMetadata
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id
    :param str sso_id        
    """
    uri = f"/api/v1/msps/{msp_id}/ssos/{sso_id}/metadata"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def downloadMspSsoSamlMetadata(mist_session:_APISession, msp_id:str, sso_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/downloadMspSsoSamlMetadata
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id
    :param str sso_id        
    """
    uri = f"/api/v1/msps/{msp_id}/ssos/{sso_id}/metadata.xml"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    