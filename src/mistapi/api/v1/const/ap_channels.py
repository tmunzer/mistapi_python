
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

def getApChannels(mist_session:_APISession, country_code:str=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getApChannels
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    QUERY PARAMS
    ------------
    :param str country_code        
    """
    uri = f"/api/v1/const/ap_channels"
    query_params={}
    if country_code: query_params["country_code"]=country_code
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    