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


def countOrgAuditLogs(
    mist_session: _APISession,
    org_id: str,
    distinct: str | None = None,
    admin_id: str | None = None,
    admin_name: str | None = None,
    site_id: str | None = None,
    message: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/logs/count-org-audit-logs

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str{'admin_id', 'admin_name', 'message', 'site_id'}, default: admin_name
      Field used to group this count response. enum: `admin_id`, `admin_name`, `message`, `site_id`
    admin_id : str
      Filter audit log results by administrator identifier
    admin_name : str
      Filter audit log results by one or more administrator names. Supports comma-separated values
    site_id : str
      Filter results by site identifier
    message : str
      Filter log results by message text
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

    uri = f"/api/v1/orgs/{org_id}/logs/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if admin_id:
        query_params["admin_id"] = str(admin_id)
    if admin_name:
        query_params["admin_name"] = str(admin_name)
    if site_id:
        query_params["site_id"] = str(site_id)
    if message:
        query_params["message"] = str(message)
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


def listOrgAuditLogs(
    mist_session: _APISession,
    org_id: str,
    site_id: str | None = None,
    admin_name: str | None = None,
    message: str | None = None,
    sort: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/logs/list-org-audit-logs

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
      Filter results by site identifier. Accepts multiple comma-separated values.
    admin_name : str
      Filter results by one or more administrator names or email addresses. Supports comma-separated values
    message : str
      Filter results by one or more message text values. Supports comma-separated values
    sort : str{'-timestamp', 'admin_id', 'site_id', 'timestamp'}
      Field used to sort results; a leading `-` indicates descending order. enum: `-timestamp`, `admin_id`, `site_id`, `timestamp`
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

    uri = f"/api/v1/orgs/{org_id}/logs/search"
    query_params: dict[str, str] = {}
    if site_id:
        query_params["site_id"] = str(site_id)
    if admin_name:
        query_params["admin_name"] = str(admin_name)
    if message:
        query_params["message"] = str(message)
    if sort:
        query_params["sort"] = str(sort)
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
