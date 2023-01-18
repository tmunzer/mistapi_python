from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getMspLogs(mist_session:_APISession, msp_id:str, org_id:str=None, admin_name:str=None, message:str=None) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getMspLogs
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    
    QUERY PARAMS
    ------------
    :param str org_id
    :param str admin_name - admin name or email
    :param str message        
    """
    uri = f"/api/v1/msps/{msp_id}/logs"
    query_params={}
    if org_id: query_params["org_id"]=org_id
    if admin_name: query_params["admin_name"]=admin_name
    if message: query_params["message"]=message
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countMspLogs(mist_session:_APISession, msp_id:str, distinct:str="admin_name") -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/countMspLogs
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(admin_id, admin_name, message, org_id)        
    """
    uri = f"/api/v1/msps/{msp_id}/logs/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    