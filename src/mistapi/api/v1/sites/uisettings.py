from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getSiteCurdSettings(mist_session:_APISession, site_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteCurdSettings
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/uisettings"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createSiteCurdSettings(mist_session:_APISession, site_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createSiteCurdSettings
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/uisettings"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteDerivedCurdSetting(mist_session:_APISession, site_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteDerivedCurdSetting
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/uisettings/derived"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteCurdSetting(mist_session:_APISession, site_id:str, uisetting_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteCurdSetting
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str uisetting_id        
    """
    uri = f"/api/v1/sites/{site_id}/uisettings/{uisetting_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteSiteCurdSetting(mist_session:_APISession, site_id:str, uisetting_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteSiteCurdSetting
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str uisetting_id        
    """
    uri = f"/api/v1/sites/{site_id}/uisettings/{uisetting_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateSiteCurdSetting(mist_session:_APISession, site_id:str, uisetting_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSiteCurdSetting
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str uisetting_id        
    """
    uri = f"/api/v1/sites/{site_id}/uisettings/{uisetting_id}"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    