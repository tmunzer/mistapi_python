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

def createMsp(mist_session:_APISession, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createMsp
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    """
    uri = f"/api/v1/msps"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getMspDetails(mist_session:_APISession, msp_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getMspDetails
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    """
    uri = f"/api/v1/msps/{msp_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteMsp(mist_session:_APISession, msp_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteMsp
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    """
    uri = f"/api/v1/msps/{msp_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateMsp(mist_session:_APISession, msp_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateMsp
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    """
    uri = f"/api/v1/msps/{msp_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    