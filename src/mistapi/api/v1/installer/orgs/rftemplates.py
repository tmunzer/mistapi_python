from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse

def getInstallerRfTemplatesNames(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getInstallerRfTemplatesNames
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/installer/orgs/{org_id}/rftemplates"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    