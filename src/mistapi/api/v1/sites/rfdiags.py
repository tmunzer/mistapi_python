
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

def getSiteSiteRfdiagRecording(mist_session:_APISession, site_id:str, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteSiteRfdiagRecording
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration        
    """
    uri = f"/api/v1/sites/{site_id}/rfdiags"
    query_params={}
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def startSiteRecording(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/startSiteRecording
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/rfdiags"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteRfdiagRecording(mist_session:_APISession, site_id:str, rfdiag_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteRfdiagRecording
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str rfdiag_id        
    """
    uri = f"/api/v1/sites/{site_id}/rfdiags/{rfdiag_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteSiteRfdiagRecording(mist_session:_APISession, site_id:str, rfdiag_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteSiteRfdiagRecording
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str rfdiag_id        
    """
    uri = f"/api/v1/sites/{site_id}/rfdiags/{rfdiag_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateSiteRfdiagRecording(mist_session:_APISession, site_id:str, rfdiag_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSiteRfdiagRecording
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str rfdiag_id        
    """
    uri = f"/api/v1/sites/{site_id}/rfdiags/{rfdiag_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def downloadSiteRfdiagRecording(mist_session:_APISession, site_id:str, rfdiag_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/downloadSiteRfdiagRecording
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str rfdiag_id        
    """
    uri = f"/api/v1/sites/{site_id}/rfdiags/{rfdiag_id}/download"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def stopSiteRfdiagRecording(mist_session:_APISession, site_id:str, rfdiag_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/stopSiteRfdiagRecording
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str rfdiag_id        
    """
    uri = f"/api/v1/sites/{site_id}/rfdiags/{rfdiag_id}/stop"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    