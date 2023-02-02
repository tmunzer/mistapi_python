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

def getCountryCodes(mist_session:_APISession) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getCountryCodes
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    """
    uri = f"/api/v1/const/countries"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    