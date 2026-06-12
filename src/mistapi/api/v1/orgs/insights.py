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


def getOrgMarvisClientInsights(
    mist_session: _APISession,
    org_id: str,
    marvisclient_id: str,
    duration: str | None = None,
    interval: str | None = None,
    start: str | None = None,
    end: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/marvis/get-org-marvis-client-insights

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    marvisclient_id : str
      Marvis Client device UUID

    QUERY PARAMS
    ------------
    duration : str, default: 1d
      Time range duration for the query, using relative units such as `10m`, `7d`, or `2w`
    interval : str
      Aggregation works by giving a time range plus interval (e.g. 1d, 1h, 10m) where aggregation function would be applied to.
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    limit : int, default: 100
      Maximum number of results to return per page
    page : int, default: 1
      Select the page number to return when using page-based pagination; starts at `1`

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/insights/marvisclient/{marvisclient_id}/marvisclient-metrics"
    query_params: dict[str, str] = {}
    if duration:
        query_params["duration"] = str(duration)
    if interval:
        query_params["interval"] = str(interval)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if limit:
        query_params["limit"] = str(limit)
    if page:
        query_params["page"] = str(page)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def getOrgSitesSle(
    mist_session: _APISession,
    org_id: str,
    sle: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    interval: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/sles/get-org-sites-sle

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    sle : str{'wan', 'wifi', 'wired'}
      Filter insights by SLE name. enum: `wan`, `wifi`, `wired`
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    duration : str, default: 1d
      Time range duration for the query, using relative units such as `10m`, `7d`, or `2w`
    interval : str
      Aggregation works by giving a time range plus interval (e.g. 1d, 1h, 10m) where aggregation function would be applied to.
    limit : int, default: 100
      Maximum number of results to return per page
    page : int, default: 1
      Select the page number to return when using page-based pagination; starts at `1`

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/insights/sites-sle"
    query_params: dict[str, str] = {}
    if sle:
        query_params["sle"] = str(sle)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if duration:
        query_params["duration"] = str(duration)
    if interval:
        query_params["interval"] = str(interval)
    if limit:
        query_params["limit"] = str(limit)
    if page:
        query_params["page"] = str(page)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def getOrgSle(
    mist_session: _APISession,
    org_id: str,
    metric: str,
    sle: str | None = None,
    duration: str | None = None,
    interval: str | None = None,
    start: str | None = None,
    end: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/sles/get-org-sle

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    metric : str
      See [List Insight Metrics](/#operations/listInsightMetrics) for available metrics

    QUERY PARAMS
    ------------
    sle : str
      See [List Insight Metrics](/#operations/listInsightMetrics) for more details
    duration : str, default: 1d
      Time range duration for the query, using relative units such as `10m`, `7d`, or `2w`
    interval : str
      Aggregation works by giving a time range plus interval (e.g. 1d, 1h, 10m) where aggregation function would be applied to.
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/insights/{metric}"
    query_params: dict[str, str] = {}
    if sle:
        query_params["sle"] = str(sle)
    if duration:
        query_params["duration"] = str(duration)
    if interval:
        query_params["interval"] = str(interval)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
