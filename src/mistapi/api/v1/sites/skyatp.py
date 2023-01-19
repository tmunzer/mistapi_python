
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

def countSiteByDistringAttributesOfSkyatpEvents(mist_session:_APISession, site_id:str, distinct:str="type", type:str=None, mac:str=None, device_mac:str=None, threat_level:int=None, ip_address:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteByDistringAttributesOfSkyatpEvents
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(type, mac, device_mac, threat_level)
    :param str type - event type, e.g. cc, fs, mw
    :param str mac - client MAC
    :param str device_mac - device MAC
    :param int threat_level - threat level
    :param str ip_address
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/sites/{site_id}/skyatp/events/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if type: query_params["type"]=type
    if mac: query_params["mac"]=mac
    if device_mac: query_params["device_mac"]=device_mac
    if threat_level: query_params["threat_level"]=threat_level
    if ip_address: query_params["ip_address"]=ip_address
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteSkyatpEvents(mist_session:_APISession, site_id:str, type:str=None, mac:str=None, device_mac:str=None, threat_level:int=None, ip_address:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteSkyatpEvents
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str type - event type, e.g. cc, fs, mw
    :param str mac - client MAC
    :param str device_mac - device MAC
    :param int threat_level - threat level
    :param str ip_address
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/sites/{site_id}/skyatp/events/search"
    query_params={}
    if type: query_params["type"]=type
    if mac: query_params["mac"]=mac
    if device_mac: query_params["device_mac"]=device_mac
    if threat_level: query_params["threat_level"]=threat_level
    if ip_address: query_params["ip_address"]=ip_address
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    