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


def getSiteInsightMetrics(
    mist_session: _APISession,
    site_id: str,
    metrics: str,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    interval: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/insights/get-site-insight-metrics

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    metrics : str
      Comma separated Metric names, e.g. `num_clients,num_aps`. See possible values at [List Insight Metrics](/#operations/listInsightMetrics)
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

    uri = f"/api/v1/sites/{site_id}/insights"
    query_params: dict[str, str] = {}
    if metrics:
        query_params["metrics"] = str(metrics)
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


def getSiteInsightMetricsForAP(
    mist_session: _APISession,
    site_id: str,
    device_id: str,
    metrics: str,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    interval: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/insights/get-site-insight-metrics-for-a-p

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    device_id : str

    QUERY PARAMS
    ------------
    metrics : str
      Comma separated Metric names, e.g. `num_clients,num_stressed_clients`. See possible values at [List Insight Metrics](/#operations/listInsightMetrics)
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

    uri = f"/api/v1/sites/{site_id}/insights/ap/{device_id}/stats"
    query_params: dict[str, str] = {}
    if metrics:
        query_params["metrics"] = str(metrics)
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


def getSiteInsightMetricsForClient(
    mist_session: _APISession,
    site_id: str,
    client_mac: str,
    metrics: str,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    interval: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/insights/get-site-insight-metrics-for-client

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    client_mac : str

    QUERY PARAMS
    ------------
    metrics : str
      Comma separated Metric names, e.g. `top-app-by-num_client,top-app-by-bytes`. See possible values at [List Insight Metrics](/#operations/listInsightMetrics)
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

    uri = f"/api/v1/sites/{site_id}/insights/client/{client_mac}"
    query_params: dict[str, str] = {}
    if metrics:
        query_params["metrics"] = str(metrics)
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


def getSiteInsightMetricsForDevice(
    mist_session: _APISession,
    site_id: str,
    metric: str,
    device_mac: str,
    port_id: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    interval: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/insights/get-site-insight-metrics-for-device

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    metric : str
      See [List Insight Metrics](/#operations/listInsightMetrics) for available metrics
    device_mac : str

    QUERY PARAMS
    ------------
    port_id : str
      Port ID of the device, e.g. `ge-0/0/1`. Can be used with metrics related to interfaces, e.g. `rx_bytes`.
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

    uri = f"/api/v1/sites/{site_id}/insights/device/{device_mac}/{metric}"
    query_params: dict[str, str] = {}
    if port_id:
        query_params["port_id"] = str(port_id)
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


def getSiteInsightMetricsForGateway(
    mist_session: _APISession,
    site_id: str,
    device_id: str,
    metrics: str,
    port_id: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    interval: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/insights/get-site-insight-metrics-for-gateway

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    device_id : str

    QUERY PARAMS
    ------------
    metrics : str
      Comma separated Metric names, e.g. `tx_bps,rx_bps`. See possible values at [List Insight Metrics](/#operations/listInsightMetrics)
    port_id : str
      Port ID of the gateway device, e.g. `ge-0/0/1`
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

    uri = f"/api/v1/sites/{site_id}/insights/gateway/{device_id}/stats"
    query_params: dict[str, str] = {}
    if metrics:
        query_params["metrics"] = str(metrics)
    if port_id:
        query_params["port_id"] = str(port_id)
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


def getSiteInsightMetricsForMxEdge(
    mist_session: _APISession,
    site_id: str,
    metric: str,
    device_mac: str,
    port_id: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    interval: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/insights/get-site-insight-metrics-for-mx-edge

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    metric : str
      See [List Insight Metrics](/#operations/listInsightMetrics) for available metrics
    device_mac : str

    QUERY PARAMS
    ------------
    port_id : str
      Port ID of the MxEdge device, e.g. `port0`. Can be used with metrics related to interfaces, e.g. `rx_bytes`.
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

    uri = f"/api/v1/sites/{site_id}/insights/mxedge/{device_mac}/{metric}"
    query_params: dict[str, str] = {}
    if port_id:
        query_params["port_id"] = str(port_id)
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


def listSiteRogueAPs(
    mist_session: _APISession,
    site_id: str,
    type: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    interval: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/rogues/list-site-rogue-a-ps

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    type : str{'honeypot', 'lan', 'others', 'spoof'}
      Rogue classification used to filter the results. enum: `honeypot`, `lan`, `others`, `spoof`
    limit : int, default: 100
      Maximum number of results to return per page
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    duration : str, default: 1d
      Time range duration for the query, using relative units such as `10m`, `7d`, or `2w`
    interval : str
      Aggregation works by giving a time range plus interval (e.g. 1d, 1h, 10m) where aggregation function would be applied to.

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/insights/rogues"
    query_params: dict[str, str] = {}
    if type:
        query_params["type"] = str(type)
    if limit:
        query_params["limit"] = str(limit)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if duration:
        query_params["duration"] = str(duration)
    if interval:
        query_params["interval"] = str(interval)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def listSiteRogueClients(
    mist_session: _APISession,
    site_id: str,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    interval: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/rogues/list-site-rogue-clients

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    limit : int, default: 100
      Maximum number of results to return per page
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    duration : str, default: 1d
      Time range duration for the query, using relative units such as `10m`, `7d`, or `2w`
    interval : str
      Aggregation works by giving a time range plus interval (e.g. 1d, 1h, 10m) where aggregation function would be applied to.

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/insights/rogues/clients"
    query_params: dict[str, str] = {}
    if limit:
        query_params["limit"] = str(limit)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if duration:
        query_params["duration"] = str(duration)
    if interval:
        query_params["interval"] = str(interval)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def getSiteInsightMetricsForSwitch(
    mist_session: _APISession,
    site_id: str,
    metric: str,
    device_mac: str,
    port_id: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    interval: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/insights/get-site-insight-metrics-for-switch

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    metric : str
      See [List Insight Metrics](/#operations/listInsightMetrics) for available metrics
    device_mac : str

    QUERY PARAMS
    ------------
    port_id : str
      Port ID of the switch device, e.g. `ge-0/0/1`. Can be used with metrics related to interfaces, e.g. `rx_bytes`.
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

    uri = f"/api/v1/sites/{site_id}/insights/switch/{device_mac}/{metric}"
    query_params: dict[str, str] = {}
    if port_id:
        query_params["port_id"] = str(port_id)
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
