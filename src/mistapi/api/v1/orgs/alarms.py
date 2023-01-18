from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def multiAckOrgAlarms(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/multiAckOrgAlarms
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/alarms/ack"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def ackOrgAllAlarms(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/ackOrgAllAlarms
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/alarms/ack_all"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def countOrgAlarms(mist_session:_APISession, org_id:str, distinct:str=None, page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/countOrgAlarms
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str distinct
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/orgs/{org_id}/alarms/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchOrgAlarms(mist_session:_APISession, org_id:str, type:str=None, start:int=None, end:int=None, duration:str="1d", limit:int=100, page:int=1) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchOrgAlarms
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str type
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)
    :param int limit
    :param int page        
    """
    uri = f"/api/v1/orgs/{org_id}/alarms/search"
    query_params={}
    if type: query_params["type"]=type
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def multiUnackOrgAlarms(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/multiUnackOrgAlarms
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/alarms/unack"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def unackOrgAllArlarms(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/unackOrgAllArlarms
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/alarms/unack_all"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def ackOrgAlarm(mist_session:_APISession, org_id:str, alarm_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/ackOrgAlarm
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str alarm_id        
    """
    uri = f"/api/v1/orgs/{org_id}/alarms/{alarm_id}/ack"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    