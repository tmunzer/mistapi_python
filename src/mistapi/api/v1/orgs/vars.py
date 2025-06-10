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

def searchOrgVars(mist_session:_APISession, org_id:str, site_id:str|None=None, var:str|None=None, src:str|None=None, limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/vars/search-org-vars

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    site_id : str
    var : str
    src : str{'deviceprofile', 'site'}
    limit : int, default: 100
    page : int, default: 1

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/vars/search"
    query_params:dict[str, str]={}
    if site_id:
        query_params["site_id"]=str(site_id)
    if var:
        query_params["var"]=str(var)
    if src:
        query_params["src"]=str(src)
    if limit:
        query_params["limit"]=str(limit)
    if page:
        query_params["page"]=str(page)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
