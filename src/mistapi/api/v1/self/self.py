
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

def getSelf(mist_session:_APISession) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSelf
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    """
    uri = f"/api/v1/self"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteSelf(mist_session:_APISession) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteSelf
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    """
    uri = f"/api/v1/self"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateSelf(mist_session:_APISession, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSelf
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    """
    uri = f"/api/v1/self"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    