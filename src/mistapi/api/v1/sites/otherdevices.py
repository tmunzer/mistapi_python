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

@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.40.1", details="function replaced with listSiteOtherDevices")  
def getSiteOtherDevices(mist_session:_APISession, site_id:str, vendor:str=None, mac:str=None, serial:str=None, model:str=None, name:str=None, page:int=1, limit:int=100) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteOtherDevices
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str vendor
    :param str mac
    :param str serial
    :param str model
    :param str name
    :param int page
    :param int limit        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/otherdevices"
    query_params={}
    if vendor: query_params["vendor"]=vendor
    if mac: query_params["mac"]=mac
    if serial: query_params["serial"]=serial
    if model: query_params["model"]=model
    if name: query_params["name"]=name
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listSiteOtherDevices(mist_session:_APISession, site_id:str, vendor:str=None, mac:str=None, serial:str=None, model:str=None, name:str=None, page:int=1, limit:int=100) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteOtherDevices
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str vendor
    :param str mac
    :param str serial
    :param str model
    :param str name
    :param int page
    :param int limit        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/otherdevices"
    query_params={}
    if vendor: query_params["vendor"]=vendor
    if mac: query_params["mac"]=mac
    if serial: query_params["serial"]=serial
    if model: query_params["model"]=model
    if name: query_params["name"]=name
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countSiteOtherDevicesEvents(mist_session:_APISession, site_id:str, distinct:str="mac", start:int=None, end:int=None, duration:str="1d", limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteOtherDevicesEvents
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(mac, type, vendor, site_id)
    :param int start
    :param int end
    :param str duration
    :param int limit
    :param int page        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/otherdevices/events/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteOtherDevicesEvents(mist_session:_APISession, site_id:str, org_id:str=None, site_id:str=None, mac:str=None, device_mac:str=None, vendor:str=None, type:str=None, start:int=None, end:int=None, duration:str="1d", limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteOtherDevicesEvents
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str org_id - org id
    :param str site_id - site id
    :param str mac - mac
    :param str device_mac - mac of attached device
    :param str vendor - vendor name
    :param str type - event type
    :param int start
    :param int end
    :param str duration
    :param int limit
    :param int page        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/otherdevices/events/search"
    query_params={}
    if org_id: query_params["org_id"]=org_id
    if site_id: query_params["site_id"]=site_id
    if mac: query_params["mac"]=mac
    if device_mac: query_params["device_mac"]=device_mac
    if vendor: query_params["vendor"]=vendor
    if type: query_params["type"]=type
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    