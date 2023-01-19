
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
    
    PARMS
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
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/psks"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def updateSitePsks(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSitePsks
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/psks"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def importSitePsk(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/importSitePsk
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/psks/import"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSitePsk(mist_session:_APISession, site_id:str, psk_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSitePsk
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str psk_id        
    """
    uri = f"/api/v1/sites/{site_id}/psks/{psk_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteSitePsk(mist_session:_APISession, site_id:str, psk_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteSitePsk
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str psk_id        
    """
    uri = f"/api/v1/sites/{site_id}/psks/{psk_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateSitePsk(mist_session:_APISession, site_id:str, psk_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSitePsk
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str psk_id        
    """
    uri = f"/api/v1/sites/{site_id}/psks/{psk_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    