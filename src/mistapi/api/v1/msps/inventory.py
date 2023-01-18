from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getMspInventoryByMac(mist_session:_APISession, msp_id:str, device_mac:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getMspInventoryByMac
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id
    :param str device_mac        
    """
    uri = f"/api/v1/msps/{msp_id}/inventory/{device_mac}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    