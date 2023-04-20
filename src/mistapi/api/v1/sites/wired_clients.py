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

def countSiteClientsWired(mist_session:_APISession, site_id:str, distinct:str="mac", mac:str=None, device_mac:str=None, port_id:str=None, vlan:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteClientsWired
    
    PARAMS
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
    :param str duration        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
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
    
def searchSiteClientsWired(mist_session:_APISession, site_id:str, device_mac:str=None, mac:str=None, port_id:str=None, vlan:str=None, ip_address:str=None, manufacture:str=None, text:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteClientsWired
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str device_mac - device mac
    :param str mac - client mac
    :param str port_id - port id
    :param str vlan - vlan
    :param str ip_address
    :param str manufacture - manufacture
    :param str text - single entry of hostname/mac
    :param int limit
    :param int start
    :param int end
    :param str duration        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/wired_clients/search"
    query_params={}
    if device_mac: query_params["device_mac"]=device_mac
    if mac: query_params["mac"]=mac
    if port_id: query_params["port_id"]=port_id
    if vlan: query_params["vlan"]=vlan
    if ip_address: query_params["ip_address"]=ip_address
    if manufacture: query_params["manufacture"]=manufacture
    if text: query_params["text"]=text
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    