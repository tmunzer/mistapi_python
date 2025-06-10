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

def listOrgNacPortals(mist_session:_APISession, org_id:str, limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/nac-portals/list-org-nac-portals

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    limit : int, default: 100
    page : int, default: 1

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/nacportals"
    query_params:dict[str, str]={}
    if limit:
        query_params["limit"]=str(limit)
    if page:
        query_params["page"]=str(page)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp

def createOrgNacPortal(mist_session:_APISession, org_id:str, body:dict) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/nac-portals/create-org-nac-portal

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/nacportals"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp

def getOrgNacPortal(mist_session:_APISession, org_id:str, nacportal_id:str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/nac-portals/get-org-nac-portal

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    nacportal_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/nacportals/{nacportal_id}"
    query_params:dict[str, str]={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp

def deleteOrgNacPortal(mist_session:_APISession, org_id:str, nacportal_id:str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/nac-portals/delete-org-nac-portal

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    nacportal_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/nacportals/{nacportal_id}"
    query_params:dict[str, str]={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp

def updateOrgNacPortal(mist_session:_APISession, org_id:str, nacportal_id:str, body:dict) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/nac-portals/update-org-nac-portal

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    nacportal_id : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/nacportals/{nacportal_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp

def listOrgNacPortalSsoLatestFailures(mist_session:_APISession, org_id:str, nacportal_id:str, start:int|None=None, end:int|None=None, duration:str="1d", limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/nac-portals/list-org-nac-portal-sso-latest-failures

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    nacportal_id : str

    QUERY PARAMS
    ------------
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100
    page : int, default: 1

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/nacportals/{nacportal_id}/failures"
    query_params:dict[str, str]={}
    if start:
        query_params["start"]=str(start)
    if end:
        query_params["end"]=str(end)
    if duration:
        query_params["duration"]=str(duration)
    if limit:
        query_params["limit"]=str(limit)
    if page:
        query_params["page"]=str(page)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp

def deleteOrgNacPortalImage(mist_session:_APISession, org_id:str, nacportal_id:str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/nac-portals/delete-org-nac-portal-image

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    nacportal_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/nacportals/{nacportal_id}/portal_image"
    query_params:dict[str, str]={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp

def uploadOrgNacPortalImageFile(mist_session:_APISession, org_id:str, nacportal_id:str, file:str|None=None, json:str|None=None) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/nac-portals/upload-org-nac-portal-image

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    nacportal_id : str

    BODY PARAMS
    -----------
    file : str
        path to the file to upload. Binary file
    json : str
        JSON string describing the upload

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    multipart_form_data = {
        "file":file,
        "json":json,
    }
    uri = f"/api/v1/orgs/{org_id}/nacportals/{nacportal_id}/portal_image"
    resp = mist_session.mist_post_file(uri=uri, multipart_form_data=multipart_form_data)
    return resp

def updateOrgNacPortalTemplate(mist_session:_APISession, org_id:str, nacportal_id:str, body:dict) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/nac-portals/update-org-nac-portal-template

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    nacportal_id : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/nacportals/{nacportal_id}/portal_template"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp

def getOrgNacPortalSamlMetadata(mist_session:_APISession, org_id:str, nacportal_id:str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/nac-portals/get-org-nac-portal-saml-metadata

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    nacportal_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/nacportals/{nacportal_id}/saml_metadata"
    query_params:dict[str, str]={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp

def downloadOrgNacPortalSamlMetadata(mist_session:_APISession, org_id:str, nacportal_id:str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/nac-portals/download-org-nac-portal-saml-metadata

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    nacportal_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/nacportals/{nacportal_id}/saml_metadata.xml"
    query_params:dict[str, str]={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
