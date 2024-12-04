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
import deprecation

def listSiteRssiZones(mist_session:_APISession, site_id:str, limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteRssiZones
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    limit : int, default: 100
    page : int, default: 1        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/rssizones"
    query_params={}
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createSiteRssiZone(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createSiteRssiZone
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/rssizones"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteRssiZone(mist_session:_APISession, site_id:str, rssizone_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteRssiZone
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    rssizone_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/rssizones/{rssizone_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteSiteRssiZone(mist_session:_APISession, site_id:str, rssizone_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteSiteRssiZone
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    rssizone_id : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/rssizones/{rssizone_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateSiteRssiZone(mist_session:_APISession, site_id:str, rssizone_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSiteRssiZone
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    rssizone_id : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/rssizones/{rssizone_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    