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

@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.41.9", details="function replaced with listSiteVpnsDerived")  
def getSiteVpnsDerived(mist_session:_APISession, site_id:str, resolve:bool=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteVpnsDerived
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    resolve : bool
      whether resolve the site variables        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/vpns/derived"
    query_params={}
    if resolve: query_params["resolve"]=resolve
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listSiteVpnsDerived(mist_session:_APISession, site_id:str, resolve:bool=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listSiteVpnsDerived
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    site_id : str        
    
    QUERY PARAMS
    ------------
    resolve : bool
      whether resolve the site variables        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/sites/{site_id}/vpns/derived"
    query_params={}
    if resolve: query_params["resolve"]=resolve
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    