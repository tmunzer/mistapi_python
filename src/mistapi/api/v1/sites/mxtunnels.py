from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def preemptSitesMxTunnel(mist_session:_APISession, site_id:str, mxtunnel_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/preemptSitesMxTunnel
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str mxtunnel_id        
    """
    uri = f"/api/v1/sites/{site_id}/mxtunnels/{mxtunnel_id}/preempt_aps"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    