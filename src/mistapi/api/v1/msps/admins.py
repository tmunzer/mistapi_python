
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

def getMspAdmins(mist_session:_APISession, msp_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getMspAdmins
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    """
    uri = f"/api/v1/msps/{msp_id}/admins"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getMspAdmin(mist_session:_APISession, msp_id:str, admin_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getMspAdmin
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id
    :param str admin_id        
    """
    uri = f"/api/v1/msps/{msp_id}/admins/{admin_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def revokeMspAdmin(mist_session:_APISession, msp_id:str, admin_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/revokeMspAdmin
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id
    :param str admin_id        
    """
    uri = f"/api/v1/msps/{msp_id}/admins/{admin_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateMspAdmin(mist_session:_APISession, msp_id:str, admin_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateMspAdmin
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id
    :param str admin_id        
    """
    uri = f"/api/v1/msps/{msp_id}/admins/{admin_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    