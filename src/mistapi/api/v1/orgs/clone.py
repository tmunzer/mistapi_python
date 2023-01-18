from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def cloneOrg(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/cloneOrg
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/clone"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    