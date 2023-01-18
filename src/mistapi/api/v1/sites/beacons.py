from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getSiteBeacons(mist_session:_APISession, site_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteBeacons
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/beacons"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createSiteBeacon(mist_session:_APISession, site_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createSiteBeacon
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/beacons"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteBeacon(mist_session:_APISession, site_id:str, beacon_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteBeacon
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str beacon_id        
    """
    uri = f"/api/v1/sites/{site_id}/beacons/{beacon_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteSiteBeacons(mist_session:_APISession, site_id:str, beacon_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteSiteBeacons
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str beacon_id        
    """
    uri = f"/api/v1/sites/{site_id}/beacons/{beacon_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateSiteBeacons(mist_session:_APISession, site_id:str, beacon_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSiteBeacons
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str beacon_id        
    """
    uri = f"/api/v1/sites/{site_id}/beacons/{beacon_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    