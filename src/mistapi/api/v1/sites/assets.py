from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getSiteAssets(mist_session:_APISession, site_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteAssets
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/assets"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createSiteAsset(mist_session:_APISession, site_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createSiteAsset
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/assets"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def importSiteAssets(mist_session:_APISession, site_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/importSiteAssets
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/assets/import"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteAsset(mist_session:_APISession, site_id:str, asset_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteAsset
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str asset_id        
    """
    uri = f"/api/v1/sites/{site_id}/assets/{asset_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteSiteAsset(mist_session:_APISession, site_id:str, asset_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteSiteAsset
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str asset_id        
    """
    uri = f"/api/v1/sites/{site_id}/assets/{asset_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateSiteAsset(mist_session:_APISession, site_id:str, asset_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSiteAsset
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str asset_id        
    """
    uri = f"/api/v1/sites/{site_id}/assets/{asset_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    