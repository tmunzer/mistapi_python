from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse

def countSiteClientsWired(mist_session:_APISession, site_id:str, distinct:str="mac", mac:str=None, device_mac:str=None, port_id:str=None, vlan:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteClientsWired
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(port_id, vlan, mac)
    :param str mac - client mac
    :param str device_mac - device mac
    :param str port_id - port id
    :param str vlan - vlan
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/sites/{site_id}/wired_clients/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if mac: query_params["mac"]=mac
    if device_mac: query_params["device_mac"]=device_mac
    if port_id: query_params["port_id"]=port_id
    if vlan: query_params["vlan"]=vlan
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteClientsWired(mist_session:_APISession, site_id:str, mac:str=None, ip_address:str=None, device_mac:str=None, port_id:str=None, vlan:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteClientsWired
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str mac - client mac
    :param str ip_address
    :param str device_mac - device mac
    :param str port_id - port id
    :param str vlan - vlan
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/sites/{site_id}/wired_clients/search"
    query_params={}
    if mac: query_params["mac"]=mac
    if ip_address: query_params["ip_address"]=ip_address
    if device_mac: query_params["device_mac"]=device_mac
    if port_id: query_params["port_id"]=port_id
    if vlan: query_params["vlan"]=vlan
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    