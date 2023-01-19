
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

def getSiteAnomalyEventsForClient(mist_session:_APISession, site_id:str, client_mac:str, metric:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteAnomalyEventsForClient
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str client_mac
    :param str metric        
    """
    uri = f"/api/v1/sites/{site_id}/anomaly/client/{client_mac}/{metric}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteAnomalyEventsforDevice(mist_session:_APISession, site_id:str, metric:str, device_mac:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteAnomalyEventsforDevice
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str metric
    :param str device_mac        
    """
    uri = f"/api/v1/sites/{site_id}/anomaly/device/{device_mac}/{metric}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getSiteAnomalyEvents(mist_session:_APISession, site_id:str, metric:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteAnomalyEvents
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str metric        
    """
    uri = f"/api/v1/sites/{site_id}/anomaly/{metric}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    