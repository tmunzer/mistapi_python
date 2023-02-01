
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

def countOrgClientsWired(mist_session:_APISession, org_id:str, distinct:str="mac", page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countOrgClientsWired
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(port_id, vlan, mac, device_mac, site_id, type)
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration        
    """
    uri = f"/api/v1/orgs/{org_id}/wired_clients/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchOrgClientsWired(mist_session:_APISession, org_id:str, device_mac:str=None, mac:str=None, port_id:str=None, vlan:int=None, site_id:str=None, ip:str=None, manufacture:str=None, text:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchOrgClientsWired
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str device_mac - device mac
    :param str mac - client mac
    :param str port_id - port id
    :param int vlan - vlan
    :param str site_id - site id
    :param str ip - ip
    :param str manufacture - client manufacture
    :param str text - single entry of hostname/mac
    :param int limit
    :param int start
    :param int end
    :param str duration        
    """
    uri = f"/api/v1/orgs/{org_id}/wired_clients/search"
    query_params={}
    if device_mac: query_params["device_mac"]=device_mac
    if mac: query_params["mac"]=mac
    if port_id: query_params["port_id"]=port_id
    if vlan: query_params["vlan"]=vlan
    if site_id: query_params["site_id"]=site_id
    if ip: query_params["ip"]=ip
    if manufacture: query_params["manufacture"]=manufacture
    if text: query_params["text"]=text
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    