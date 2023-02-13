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

def getOrgCertificates(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgCertificates
    
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
    uri = f"/api/v1/orgs/{org_id}/cert"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def clearOrgCertificates(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/clearOrgCertificates
    
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
    uri = f"/api/v1/orgs/{org_id}/cert/regenerate"
    resp = mist_session.mist_post(uri=uri)
    return resp
    