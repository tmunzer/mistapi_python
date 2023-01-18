from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getSiteVBeacons(mist_session:_APISession, site_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteVBeacons
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/vbeacons"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createSiteVBeacon(mist_session:_APISession, site_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createSiteVBeacon
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/vbeacons"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteVBeacon(mist_session:_APISession, site_id:str, vbeacon_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteVBeacon
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str vbeacon_id        
    """
    uri = f"/api/v1/sites/{site_id}/vbeacons/{vbeacon_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteSiteVBeacon(mist_session:_APISession, site_id:str, vbeacon_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteSiteVBeacon
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str vbeacon_id        
    """
    uri = f"/api/v1/sites/{site_id}/vbeacons/{vbeacon_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateSiteVBeacon(mist_session:_APISession, site_id:str, vbeacon_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSiteVBeacon
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str vbeacon_id        
    """
    uri = f"/api/v1/sites/{site_id}/vbeacons/{vbeacon_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    