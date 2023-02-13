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

def getSiteWlans(mist_session:_APISession, site_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteWlans
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/wlans"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createSiteWlan(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createSiteWlan
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/wlans"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteWlanDerived(mist_session:_APISession, site_id:str, resolve:bool=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteWlanDerived
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param bool resolve - whether to resolve SITE_VARS        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/wlans/derived"
    query_params={}
    if resolve: query_params["resolve"]=resolve
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteWlan(mist_session:_APISession, site_id:str, wlan_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteWlan
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str wlan_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/wlans/{wlan_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteSiteWlan(mist_session:_APISession, site_id:str, wlan_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteSiteWlan
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str wlan_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/wlans/{wlan_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateSiteWlan(mist_session:_APISession, site_id:str, wlan_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSiteWlan
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str wlan_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/wlans/{wlan_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def uploadSiteWlanPortalImageFile(mist_session:_APISession, site_id:str, wlan_id:str, file_path:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/uploadSiteWlanPortalImage
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str wlan_id        
    
    FILE PARAMS
    -----------
    :param str file_path - path to the file to upload
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/wlans/{wlan_id}/portal_image"
    with open(file_path, "rb") as f:    
        files = {"file": f.read()}
        resp = mist_session.mist_post_file(uri=uri, files=files)
    
def updateSiteWlanPortalTemplate(mist_session:_APISession, site_id:str, wlan_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSiteWlanPortalTemplate
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str wlan_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/wlans/{wlan_id}/portal_template"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    