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

def countOrgCallEvents(mist_session:_APISession, org_id:str, distinct:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countOrgCallEvents
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(type, app)        
    """
    uri = f"/api/v1/orgs/{org_id}/call/events/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchOrgCallEvents(mist_session:_APISession, org_id:str, type:str=None, ap:str=None, mac:str=None, app:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchOrgCallEvents
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str type - Event Type. See [getCallEventsDefinitions](#tag/Constants/operation/getCallEventsDefinitions)
    :param str ap
    :param str mac
    :param str app        
    """
    uri = f"/api/v1/orgs/{org_id}/call/events/search"
    query_params={}
    if type: query_params["type"]=type
    if ap: query_params["ap"]=ap
    if mac: query_params["mac"]=mac
    if app: query_params["app"]=app
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    