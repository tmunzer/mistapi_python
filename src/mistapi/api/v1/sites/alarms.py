from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def multiAckSiteAlarms(mist_session:_APISession, site_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/multiAckSiteAlarms
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/alarms/ack"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def ackSiteAllAlarms(mist_session:_APISession, site_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/ackSiteAllAlarms
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/alarms/ack_all"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def countSiteAlarms(mist_session:_APISession, site_id:str, distinct:str="type", ack_admin_name:str=None, acked:bool=None, type:str=None, severity:str=None, group:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/countSiteAlarms
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(type, acked, severity, group) - Group by and count the alarms by some distinct field
    :param str ack_admin_name - Name of the admins who have acked the alarms; accepts multiple values separated by comma
    :param bool acked
    :param str type - Key-name of the alarms; accepts multiple values separated by comma
    :param str severity - Alarm severity; accepts multiple values separated by comma
    :param str group - Alarm group name; accepts multiple values separated by comma
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
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
    
def getSiteAlarms(mist_session:_APISession, site_id:str, type:str=None, ack_admin_name:str=None, acked:bool=None, severity:str=None, group:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteAlarms
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    
    QUERY PARAMS
    ------------
    :param str type - Key-name of the alarms; accepts multiple values separated by comma
    :param str ack_admin_name - Name of the admins who have acked the alarms; accepts multiple values separated by comma
    :param bool acked
    :param str severity - Alarm severity; accepts multiple values separated by comma
    :param str group - Alarm group name; accepts multiple values separated by comma
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/sites/{site_id}/alarms/search"
    query_params={}
    if type: query_params["type"]=type
    if ack_admin_name: query_params["ack_admin_name"]=ack_admin_name
    if acked: query_params["acked"]=acked
    if severity: query_params["severity"]=severity
    if group: query_params["group"]=group
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def multiUnackSiteAlarms(mist_session:_APISession, site_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/multiUnackSiteAlarms
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/alarms/unack"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def unackSiteAllArlarms(mist_session:_APISession, site_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/unackSiteAllArlarms
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/alarms/unack_all"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def ackSiteAlarm(mist_session:_APISession, site_id:str, alarm_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/ackSiteAlarm
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str alarm_id        
    """
    uri = f"/api/v1/sites/{site_id}/alarms/{alarm_id}/ack"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def unackSiteAlarm(mist_session:_APISession, site_id:str, alarm_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/unackSiteAlarm
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str alarm_id        
    """
    uri = f"/api/v1/sites/{site_id}/alarms/{alarm_id}/unack"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    