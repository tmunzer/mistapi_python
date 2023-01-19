from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse

def claimMspLicence(mist_session:_APISession, msp_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/claimMspLicence
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    """
    uri = f"/api/v1/msps/{msp_id}/claim"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    