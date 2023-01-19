
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

def troubleshootOrgClient(mist_session:_APISession, org_id:str, mac:str=None, site_id:str=None, start:int=None, end:int=None, type:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/troubleshootOrgClient
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str mac - **required** when troubleshooting device
    :param str site_id - **required** when troubleshooting site
    :param int start
    :param int end
    :param str type(wireless, wired, wan) - when troubleshooting site, type of network to troubleshoot        
    """
    uri = f"/api/v1/orgs/{org_id}/troubleshoot"
    query_params={}
    if mac: query_params["mac"]=mac
    if site_id: query_params["site_id"]=site_id
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if type: query_params["type"]=type
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    