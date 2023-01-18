from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def updateOrgCradlepointRouterData(mist_session:_APISession, org_id:str, device_mac:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgCradlepointRouterData
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str device_mac        
    """
    uri = f"/api/v1/orgs/{org_id}/otherdeivces/{device_mac}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    