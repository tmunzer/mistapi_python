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

def getSitePsks(mist_session:_APISession, site_id:str, ssid:str=None, role:str=None, name:str=None, page:int=1, limit:int=100) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSitePsks
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str ssid
    :param str role
    :param str name
    :param int page
    :param int limit        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/psks"
    query_params={}
    if ssid: query_params["ssid"]=ssid
    if role: query_params["role"]=role
    if name: query_params["name"]=name
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createSitePsk(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createSitePsk
    
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
    uri = f"/api/v1/sites/{site_id}/psks"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def updateSitePsks(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSitePsks
    
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
    uri = f"/api/v1/sites/{site_id}/psks"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def importSitePskFile(mist_session:_APISession, site_id:str, file_path:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/importSitePsk
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    FILE PARAMS
    -----------
    :param str file_path - path to the file to upload
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/psks/import"
    with open(file_path, "rb") as f:    
        files = {"file": f.read()}
        resp = mist_session.mist_post_file(uri=uri, files=files)
    
def importSitePsk(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/importSitePsk
    
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
    uri = f"/api/v1/sites/{site_id}/psks/import"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSitePsk(mist_session:_APISession, site_id:str, psk_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSitePsk
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str psk_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/psks/{psk_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteSitePsk(mist_session:_APISession, site_id:str, psk_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteSitePsk
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str psk_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/psks/{psk_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateSitePsk(mist_session:_APISession, site_id:str, psk_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSitePsk
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str psk_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/psks/{psk_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    