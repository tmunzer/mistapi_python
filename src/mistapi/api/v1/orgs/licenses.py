
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

def getOrgLicencesSummary(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgLicencesSummary
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/licenses"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def moveOrDeleteOrgLicenseToAnotherOrg(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/moveOrDeleteOrgLicenseToAnotherOrg
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/licenses"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def getOrgLicencesBySite(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgLicencesBySite
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/licenses/usages"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    