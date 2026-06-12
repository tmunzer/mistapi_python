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


def countSiteZoneSessions(
    mist_session: _APISession,
    site_id: str,
    zone_type: str,
    distinct: str | None = None,
    user_type: str | None = None,
    user: str | None = None,
    scope_id: str | None = None,
    scope: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/zones/count-site-zone-sessions

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    zone_type : str{'rssizones', 'zones'}

    QUERY PARAMS
    ------------
    distinct : str{'scope', 'scope_id', 'user', 'user_type'}, default: scope_id
      Field used to group this count response. enum: `scope`, `scope_id`, `user`, `user_type`
    user_type : str{'asset', 'client', 'sdkclient'}
      Filter results by user type. enum: `asset`, `client`, `sdkclient`
    user : str
      Client MAC / Asset MAC / SDK UUID
    scope_id : str
      If `scope`==`map`/`zone`/`rssizone`, the scope id
    scope : str{'map', 'rssizone', 'site', 'zone'}, default: site
      Filter results by scope. enum: `map`, `rssizone`, `site`, `zone`
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

    uri = f"/api/v1/sites/{site_id}/{zone_type}/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if user_type:
        query_params["user_type"] = str(user_type)
    if user:
        query_params["user"] = str(user)
    if scope_id:
        query_params["scope_id"] = str(scope_id)
    if scope:
        query_params["scope"] = str(scope)
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
