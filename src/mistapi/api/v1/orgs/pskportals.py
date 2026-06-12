"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
"""

from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse


def listOrgPskPortals(
    mist_session: _APISession,
    org_id: str,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/psk-portals/list-org-psk-portals

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
      Maximum number of results to return per page
    page : int, default: 1
      Select the page number to return when using page-based pagination; starts at `1`

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/pskportals"
    query_params: dict[str, str] = {}
    if limit:
        query_params["limit"] = str(limit)
    if page:
        query_params["page"] = str(page)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def createOrgPskPortal(
    mist_session: _APISession, org_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/psk-portals/create-org-psk-portal

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

    uri = f"/api/v1/orgs/{org_id}/pskportals"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def listOrgPskPortalLogs(
    mist_session: _APISession,
    org_id: str,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/psk-portals/list-org-psk-portal-logs

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    duration : str, default: 1d
      Time range duration for the query, using relative units such as `10m`, `7d`, or `2w`
    limit : int, default: 100
      Maximum number of results to return per page
    page : int, default: 1
      Select the page number to return when using page-based pagination; starts at `1`

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/pskportals/logs"
    query_params: dict[str, str] = {}
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if duration:
        query_params["duration"] = str(duration)
    if limit:
        query_params["limit"] = str(limit)
    if page:
        query_params["page"] = str(page)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def countOrgPskPortalLogs(
    mist_session: _APISession,
    org_id: str,
    distinct: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/psk-portals/count-org-psk-portal-logs

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str{'admin_id', 'admin_name', 'psk_id', 'psk_name', 'pskportal_id', 'user_id'}, default: pskportal_id
      Field used to group this count response. enum: `admin_id`, `admin_name`, `psk_id`, `psk_name`, `pskportal_id`, `user_id`
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    duration : str, default: 1d
      Time range duration for the query, using relative units such as `10m`, `7d`, or `2w`
    limit : int, default: 100
      Maximum number of results to return per page

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/pskportals/logs/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if duration:
        query_params["duration"] = str(duration)
    if limit:
        query_params["limit"] = str(limit)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def searchOrgPskPortalLogs(
    mist_session: _APISession,
    org_id: str,
    psk_name: str | None = None,
    psk_id: str | None = None,
    pskportal_id: str | None = None,
    id: str | None = None,
    admin_name: str | None = None,
    admin_id: str | None = None,
    name_id: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/psk-portals/search-org-psk-portal-logs

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    psk_name : str
      Filter PSK portal log results by PSK name
    psk_id : str
      Filter PSK portal log results by PSK identifier
    pskportal_id : str
      Filter PSK portal log results by PSK portal identifier
    id : str
      Filter results by identifier
    admin_name : str
      Filter audit log results by administrator name
    admin_id : str
      Filter audit log results by administrator identifier
    name_id : str
      Filter results by name id
    limit : int, default: 100
      Maximum number of results to return per page
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    duration : str, default: 1d
      Time range duration for the query, using relative units such as `10m`, `7d`, or `2w`
    sort : str, default: timestamp
      On which field the list should be sorted, -prefix represents DESC order
    search_after : str
      Pagination cursor for retrieving subsequent pages of results. This value is automatically populated by Mist in the `next` URL from the previous response and should not be manually constructed.

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/pskportals/logs/search"
    query_params: dict[str, str] = {}
    if psk_name:
        query_params["psk_name"] = str(psk_name)
    if psk_id:
        query_params["psk_id"] = str(psk_id)
    if pskportal_id:
        query_params["pskportal_id"] = str(pskportal_id)
    if id:
        query_params["id"] = str(id)
    if admin_name:
        query_params["admin_name"] = str(admin_name)
    if admin_id:
        query_params["admin_id"] = str(admin_id)
    if name_id:
        query_params["name_id"] = str(name_id)
    if limit:
        query_params["limit"] = str(limit)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if duration:
        query_params["duration"] = str(duration)
    if sort:
        query_params["sort"] = str(sort)
    if search_after:
        query_params["search_after"] = str(search_after)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def getOrgPskPortal(
    mist_session: _APISession, org_id: str, pskportal_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/psk-portals/get-org-psk-portal

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    pskportal_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/pskportals/{pskportal_id}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def deleteOrgPskPortal(
    mist_session: _APISession, org_id: str, pskportal_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/psk-portals/delete-org-psk-portal

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    pskportal_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/pskportals/{pskportal_id}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp


def updateOrgPskPortal(
    mist_session: _APISession, org_id: str, pskportal_id: str, body: dict
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/psk-portals/update-org-psk-portal

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    pskportal_id : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/pskportals/{pskportal_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp


def deleteOrgPskPortalImage(
    mist_session: _APISession, org_id: str, pskportal_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/psk-portals/delete-org-psk-portal-image

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    pskportal_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/pskportals/{pskportal_id}/portal_image"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp


def uploadOrgPskPortalImageFile(
    mist_session: _APISession,
    org_id: str,
    pskportal_id: str,
    file: str | None = None,
    json: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/psk-portals/upload-org-psk-portal-image

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    pskportal_id : str

    BODY PARAMS
    -----------
    file : str
        path to the file to upload. Image binary payload to upload for the PSK portal
    json : str
        Metadata JSON string describing the PSK portal image upload

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    multipart_form_data = {
        "file": file,
        "json": json,
    }
    uri = f"/api/v1/orgs/{org_id}/pskportals/{pskportal_id}/portal_image"
    resp = mist_session.mist_post_file(uri=uri, multipart_form_data=multipart_form_data)
    return resp


def updateOrgPskPortalTemplate(
    mist_session: _APISession, org_id: str, pskportal_id: str, body: dict
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/psk-portals/update-org-psk-portal-template

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    pskportal_id : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/pskportals/{pskportal_id}/portal_template"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
