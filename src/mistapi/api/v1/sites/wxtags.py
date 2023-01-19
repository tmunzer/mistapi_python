
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

def getSiteWxTags(mist_session:_APISession, site_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteWxTags
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/wxtags"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createSiteWxTag(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createSiteWxTag
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/wxtags"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteApplicationList(mist_session:_APISession, site_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteApplicationList
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/wxtags/apps"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteWxTag(mist_session:_APISession, site_id:str, wxtag_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteWxTag
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str wxtag_id        
    """
    uri = f"/api/v1/sites/{site_id}/wxtags/{wxtag_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteSiteWxTag(mist_session:_APISession, site_id:str, wxtag_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteSiteWxTag
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str wxtag_id        
    """
    uri = f"/api/v1/sites/{site_id}/wxtags/{wxtag_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateSiteWxTag(mist_session:_APISession, site_id:str, wxtag_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSiteWxTag
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str wxtag_id        
    """
    uri = f"/api/v1/sites/{site_id}/wxtags/{wxtag_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def getSiteCurrentMatchingClientsOfAWxTag(mist_session:_APISession, site_id:str, wxtag_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteCurrentMatchingClientsOfAWxTag
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str wxtag_id        
    """
    uri = f"/api/v1/sites/{site_id}/wxtags/{wxtag_id}/clients"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    