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

@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.37.8", details="function replaced with listOrgLogs")  
def getOrgLogs(mist_session:_APISession, org_id:str, site_id:str=None, admin_name:str=None, message:str=None, start:int=None, end:int=None, limit:int=100, page:int=1, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgLogs
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str site_id - site id
    :param str admin_name - admin name or email
    :param str message - message
    :param int start
    :param int end
    :param int limit
    :param int page
    :param str duration        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/logs"
    query_params={}
    if site_id: query_params["site_id"]=site_id
    if admin_name: query_params["admin_name"]=admin_name
    if message: query_params["message"]=message
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listOrgLogs(mist_session:_APISession, org_id:str, site_id:str=None, admin_name:str=None, message:str=None, start:int=None, end:int=None, limit:int=100, page:int=1, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgLogs
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str site_id - site id
    :param str admin_name - admin name or email
    :param str message - message
    :param int start
    :param int end
    :param int limit
    :param int page
    :param str duration        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/logs"
    query_params={}
    if site_id: query_params["site_id"]=site_id
    if admin_name: query_params["admin_name"]=admin_name
    if message: query_params["message"]=message
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countOrgLogsByDistinctAttributes(mist_session:_APISession, org_id:str, distinct:str, admin_id:str=None, admin_name:str=None, site_id:str=None, message:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countOrgLogsByDistinctAttributes
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(admin_id, admin_name, message, site_id)
    :param str admin_id
    :param str admin_name
    :param str site_id
    :param str message
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/logs/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if admin_id: query_params["admin_id"]=admin_id
    if admin_name: query_params["admin_name"]=admin_name
    if site_id: query_params["site_id"]=site_id
    if message: query_params["message"]=message
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    