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

def getGatawayDefaultConfig(mist_session:_APISession, model:str=None, ha:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getGatawayDefaultConfig
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    QUERY PARAMS
    ------------
    :param str model - model the default gateway config is intended (as the default LAN/WAN port can differ)
    :param str ha - whether the config is intended for HA        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/const/default_gateway_config"
    query_params={}
    if model: query_params["model"]=model
    if ha: query_params["ha"]=ha
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    