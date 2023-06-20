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

def multiAckSiteAlarms(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/multiAckSiteAlarms
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/alarms/ack"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def ackSiteAllAlarms(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/ackSiteAllAlarms
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/alarms/ack_all"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def countSiteAlarms(mist_session:_APISession, site_id:str, distinct:str="type", ack_admin_name:str=None, acked:bool=None, type:str=None, severity:str=None, group:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteAlarms
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'type', 'acked', 'severity', 'group'}, default: type
      Group by and count the alarms by some distinct field
    ack_admin_name : str
      Name of the admins who have acked the alarms; accepts multiple values separated by comma
    acked : bool
    type : str
      Key-name of the alarms; accepts multiple values separated by comma
    severity : str
      Alarm severity; accepts multiple values separated by comma
    group : str
      Alarm group name; accepts multiple values separated by comma
    page : int, default: 1
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/alarms/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if ack_admin_name: query_params["ack_admin_name"]=ack_admin_name
    if acked: query_params["acked"]=acked
    if type: query_params["type"]=type
    if severity: query_params["severity"]=severity
    if group: query_params["group"]=group
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchSiteAlarms(mist_session:_APISession, site_id:str, type:str=None, ack_admin_name:str=None, acked:bool=None, severity:str=None, group:str=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchSiteAlarms
    
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
      Key-name of the alarms; accepts multiple values separated by comma
    ack_admin_name : str
      Name of the admins who have acked the alarms; accepts multiple values separated by comma
    acked : bool
    severity : str
      Alarm severity; accepts multiple values separated by comma
    group : str
      Alarm group name; accepts multiple values separated by comma
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/alarms/search"
    query_params={}
    if type: query_params["type"]=type
    if ack_admin_name: query_params["ack_admin_name"]=ack_admin_name
    if acked: query_params["acked"]=acked
    if severity: query_params["severity"]=severity
    if group: query_params["group"]=group
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def multiUnackSiteAlarms(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/multiUnackSiteAlarms
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/alarms/unack"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def unackSiteAllArlarms(mist_session:_APISession, site_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/unackSiteAllArlarms
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/alarms/unack_all"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def ackSiteAlarm(mist_session:_APISession, site_id:str, alarm_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/ackSiteAlarm
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    alarm_id : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/alarms/{alarm_id}/ack"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def unackSiteAlarm(mist_session:_APISession, site_id:str, alarm_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/unackSiteAlarm
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str
    alarm_id : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/alarms/{alarm_id}/unack"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    