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

def countSiteWanClients(mist_session:_APISession, site_id:str, distinct:str="mac", start:int=None, end:int=None, duration:str="1d", limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteWanClients
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'hostname', 'ip', 'mfg', 'mac'}, default: mac
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100
    page : int, default: 1        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/wan_clients/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteWanClientsEvents(mist_session:_APISession, site_id:str, type:str=None, mac:str=None, hostname:str=None, ip:str=None, mfg:str=None, start:int=None, end:int=None, duration:str="1d", limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteWanClientsEvents
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    type : str
      Event type, e.g. CLIENT_IP_ASSIGNED, CLIENT_IP_RENEWED, CLIENT_IP_EXPIRED
    mac : str
      partial / full MAC address
    hostname : str
      partial / full hostname
    ip : str
      client IP
    mfg : str
      Manufacture
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100
    page : int, default: 1        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/wan_clients/events/search"
    query_params={}
    if type: query_params["type"]=type
    if mac: query_params["mac"]=mac
    if hostname: query_params["hostname"]=hostname
    if ip: query_params["ip"]=ip
    if mfg: query_params["mfg"]=mfg
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteWanClients(mist_session:_APISession, site_id:str, mac:str=None, hostname:str=None, ip:str=None, mfg:str=None, start:int=None, end:int=None, duration:str="1d", limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteWanClients
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    mac : str
      partial / full MAC address
    hostname : str
      partial / full hostname
    ip : str
      client IP
    mfg : str
      Manufacture
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100
    page : int, default: 1        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/wan_clients/search"
    query_params={}
    if mac: query_params["mac"]=mac
    if hostname: query_params["hostname"]=hostname
    if ip: query_params["ip"]=ip
    if mfg: query_params["mfg"]=mfg
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    