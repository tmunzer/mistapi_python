
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

def getMspTickets(mist_session:_APISession, msp_id:str, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getMspTickets
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    
    QUERY PARAMS
    ------------
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/msps/{msp_id}/tickets"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countMspTickets(mist_session:_APISession, msp_id:str, distinct:str="status") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countMspTickets
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(status, type, org_id)        
    """
    uri = f"/api/v1/msps/{msp_id}/tickets/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    