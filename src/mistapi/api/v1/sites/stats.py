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


def getSiteStats(mist_session: _APISession, site_id: str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/get-site-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def listSiteSpectrumAnalysis(
    mist_session: _APISession,
    site_id: str,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/spectrum-analysis/list-site-spectrum-analysis

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

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/analyze_spectrum"
    query_params: dict[str, str] = {}
    if limit:
        query_params["limit"] = str(limit)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if duration:
        query_params["duration"] = str(duration)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def countSiteApps(
    mist_session: _APISession,
    site_id: str,
    distinct: str | None = None,
    device_mac: str | None = None,
    app: str | None = None,
    wired: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/apps/count-site-apps

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    distinct : str{'ap', 'app', 'category', 'device_mac', 'port_id', 'service', 'src_ip', 'ssid', 'wcid', 'wlan_id app'}
      Field used to group application statistics count results. enum: `ap`, `app`, `category`, `device_mac`, `port_id`, `service`, `src_ip`, `ssid`, `wcid`, `wlan_id`
    device_mac : str
      MAC of the device
    app : str
      Filter results by application name
    wired : str
      If a device is wired or wireless. Default is False.
    limit : int, default: 100
      Maximum number of results to return per page

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/apps/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if device_mac:
        query_params["device_mac"] = str(device_mac)
    if app:
        query_params["app"] = str(app)
    if wired:
        query_params["wired"] = str(wired)
    if limit:
        query_params["limit"] = str(limit)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def listSiteAssetsStats(
    mist_session: _APISession,
    site_id: str,
    map_id: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/assets/list-site-assets-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    map_id : str
      Filter assets by map UUID
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

    uri = f"/api/v1/sites/{site_id}/stats/assets"
    query_params: dict[str, str] = {}
    if map_id:
        query_params["map_id"] = str(map_id)
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


def countSiteAssets(
    mist_session: _APISession,
    site_id: str,
    distinct: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/assets/count-site-assets

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    distinct : str{'by', 'device_name', 'eddystone_uid_instance', 'eddystone_uid_namespace', 'eddystone_url', 'ibeacon_major', 'ibeacon_minor', 'ibeacon_uuid', 'mac', 'map_id', 'name'}, default: map_id
      Field used to group this count response. enum: `by`, `device_name`, `eddystone_uid_instance`, `eddystone_uid_namespace`, `eddystone_url`, `ibeacon_major`, `ibeacon_minor`, `ibeacon_uuid`, `mac`, `map_id`, `name`
    limit : int, default: 100
      Maximum number of results to return per page

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/assets/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if limit:
        query_params["limit"] = str(limit)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def searchSiteAssets(
    mist_session: _APISession,
    site_id: str,
    mac: str | None = None,
    map_id: str | None = None,
    ibeacon_uuid: str | None = None,
    ibeacon_major: int | None = None,
    ibeacon_minor: int | None = None,
    eddystone_uid_namespace: str | None = None,
    eddystone_uid_instance: str | None = None,
    eddystone_url: str | None = None,
    device_name: str | None = None,
    by: str | None = None,
    name: str | None = None,
    ap_mac: str | None = None,
    beam: str | None = None,
    rssi: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/assets/search-site-assets

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    mac : str
      Filter results by MAC address
    map_id : str
      Filter results by map identifier
    ibeacon_uuid : str
      Filter asset results by iBeacon UUID
    ibeacon_major : int
      Filter asset results by iBeacon major value
    ibeacon_minor : int
      Filter asset results by iBeacon minor value
    eddystone_uid_namespace : str
      Filter asset results by Eddystone UID namespace
    eddystone_uid_instance : str
      Filter asset results by Eddystone UID instance
    eddystone_url : str
      Filter asset results by Eddystone URL
    device_name : str
      Filter asset results by reporting device name
    by : str
      Select how the value should be returned
    name : str
      Filter results by name
    ap_mac : str
      Filter asset results by reporting AP MAC address
    beam : str
      Filter asset results by beam value
    rssi : str
      Filter asset results by RSSI value
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

    uri = f"/api/v1/sites/{site_id}/stats/assets/search"
    query_params: dict[str, str] = {}
    if mac:
        query_params["mac"] = str(mac)
    if map_id:
        query_params["map_id"] = str(map_id)
    if ibeacon_uuid:
        query_params["ibeacon_uuid"] = str(ibeacon_uuid)
    if ibeacon_major:
        query_params["ibeacon_major"] = str(ibeacon_major)
    if ibeacon_minor:
        query_params["ibeacon_minor"] = str(ibeacon_minor)
    if eddystone_uid_namespace:
        query_params["eddystone_uid_namespace"] = str(eddystone_uid_namespace)
    if eddystone_uid_instance:
        query_params["eddystone_uid_instance"] = str(eddystone_uid_instance)
    if eddystone_url:
        query_params["eddystone_url"] = str(eddystone_url)
    if device_name:
        query_params["device_name"] = str(device_name)
    if by:
        query_params["by"] = str(by)
    if name:
        query_params["name"] = str(name)
    if ap_mac:
        query_params["ap_mac"] = str(ap_mac)
    if beam:
        query_params["beam"] = str(beam)
    if rssi:
        query_params["rssi"] = str(rssi)
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


def getSiteAssetStats(
    mist_session: _APISession,
    site_id: str,
    asset_id: str,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/assets/get-site-asset-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    asset_id : str

    QUERY PARAMS
    ------------
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    duration : str, default: 1d
      Time range duration for the query, using relative units such as `10m`, `7d`, or `2w`

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/assets/{asset_id}"
    query_params: dict[str, str] = {}
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if duration:
        query_params["duration"] = str(duration)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def listSiteBeaconsStats(
    mist_session: _APISession,
    site_id: str,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/beacons/list-site-beacons-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

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

    uri = f"/api/v1/sites/{site_id}/stats/beacons"
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


def countSiteBgpStats(
    mist_session: _APISession,
    site_id: str,
    state: str | None = None,
    distinct: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/bgp-peers/count-site-bgp-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    state : str
      Filter peer results by state
    distinct : str
      Field used to group this count response
    limit : int, default: 100
      Maximum number of results to return per page

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/bgp_peers/count"
    query_params: dict[str, str] = {}
    if state:
        query_params["state"] = str(state)
    if distinct:
        query_params["distinct"] = str(distinct)
    if limit:
        query_params["limit"] = str(limit)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def searchSiteBgpStats(
    mist_session: _APISession,
    site_id: str,
    mac: str | None = None,
    neighbor_mac: str | None = None,
    vrf_name: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/bgp-peers/search-site-bgp-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    mac : str
      Filter results by MAC address
    neighbor_mac : str
      Filter peer results by neighbor MAC address
    vrf_name : str
      Filter peer results by VRF name
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

    uri = f"/api/v1/sites/{site_id}/stats/bgp_peers/search"
    query_params: dict[str, str] = {}
    if mac:
        query_params["mac"] = str(mac)
    if neighbor_mac:
        query_params["neighbor_mac"] = str(neighbor_mac)
    if vrf_name:
        query_params["vrf_name"] = str(vrf_name)
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


def troubleshootSiteCall(
    mist_session: _APISession,
    site_id: str,
    client_mac: str,
    meeting_id: str,
    mac: str | None = None,
    app: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/calls/troubleshoot-site-call

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
    meeting_id : str
      Filter results by meeting identifier
    mac : str
      Filter results by MAC address
    app : str
      Third party app name
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

    uri = f"/api/v1/sites/{site_id}/stats/calls/client/{client_mac}/troubleshoot"
    query_params: dict[str, str] = {}
    if meeting_id:
        query_params["meeting_id"] = str(meeting_id)
    if mac:
        query_params["mac"] = str(mac)
    if app:
        query_params["app"] = str(app)
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


def countSiteCalls(
    mist_session: _APISession,
    site_id: str,
    distinct: str | None = None,
    rating: int | None = None,
    app: str | None = None,
    start: str | None = None,
    end: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/calls/count-site-calls

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    distinct : str{'mac'}, default: mac
      Field used to group this count response. enum: `mac`
    rating : int
      Feedback rating (e.g. "rating=1" or "rating=1,2")
    app : str
      Filter application statistics by application name
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    limit : int, default: 100
      Maximum number of results to return per page

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/calls/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if rating:
        query_params["rating"] = str(rating)
    if app:
        query_params["app"] = str(app)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if limit:
        query_params["limit"] = str(limit)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def searchSiteCalls(
    mist_session: _APISession,
    site_id: str,
    mac: str | None = None,
    app: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/calls/search-site-calls

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    mac : str
      Filter results by MAC address
    app : str
      Third party app name
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

    uri = f"/api/v1/sites/{site_id}/stats/calls/search"
    query_params: dict[str, str] = {}
    if mac:
        query_params["mac"] = str(mac)
    if app:
        query_params["app"] = str(app)
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


def getSiteCallsSummary(
    mist_session: _APISession,
    site_id: str,
    ap_mac: str | None = None,
    app: str | None = None,
    start: str | None = None,
    end: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/calls/get-site-calls-summary

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    ap_mac : str
      Filter results by AP MAC address
    app : str
      Filter results by application name
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/calls/summary"
    query_params: dict[str, str] = {}
    if ap_mac:
        query_params["ap_mac"] = str(ap_mac)
    if app:
        query_params["app"] = str(app)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def listSiteTroubleshootCalls(
    mist_session: _APISession,
    site_id: str,
    ap: str | None = None,
    meeting_id: str | None = None,
    mac: str | None = None,
    app: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/calls/list-site-troubleshoot-calls

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    ap : str
      Filter results by AP MAC address
    meeting_id : str
      Filter results by meeting identifier
    mac : str
      Filter results by MAC address
    app : str
      Third party app name
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

    uri = f"/api/v1/sites/{site_id}/stats/calls/troubleshoot"
    query_params: dict[str, str] = {}
    if ap:
        query_params["ap"] = str(ap)
    if meeting_id:
        query_params["meeting_id"] = str(meeting_id)
    if mac:
        query_params["mac"] = str(mac)
    if app:
        query_params["app"] = str(app)
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


def listSiteWirelessClientsStats(
    mist_session: _APISession,
    site_id: str,
    wired: bool | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/clients-wireless/list-site-wireless-clients-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    wired : bool
      Filter results by whether the client is wired
    limit : int, default: 100
      Maximum number of results to return per page
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    duration : str, default: 1d
      Time range duration for the query, using relative units such as `10m`, `7d`, or `2w`

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/clients"
    query_params: dict[str, str] = {}
    if wired:
        query_params["wired"] = str(wired)
    if limit:
        query_params["limit"] = str(limit)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if duration:
        query_params["duration"] = str(duration)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def getSiteWirelessClientStats(
    mist_session: _APISession, site_id: str, client_mac: str, wired: bool | None = None
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/clients-wireless/get-site-wireless-client-stats

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
    wired : bool
      Filter results by whether the client is wired

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/clients/{client_mac}"
    query_params: dict[str, str] = {}
    if wired:
        query_params["wired"] = str(wired)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def listSiteDevicesStats(
    mist_session: _APISession,
    site_id: str,
    type: str | None = None,
    status: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/devices/list-site-devices-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    type : str, default: ap
      Filter results by type
    status : str{'all', 'connected', 'disconnected'}, default: all
      Filter results by status. enum: `all`, `connected`, `disconnected`
    limit : int, default: 100
      Maximum number of results to return per page
    page : int, default: 1
      Select the page number to return when using page-based pagination; starts at `1`

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/devices"
    query_params: dict[str, str] = {}
    if type:
        query_params["type"] = str(type)
    if status:
        query_params["status"] = str(status)
    if limit:
        query_params["limit"] = str(limit)
    if page:
        query_params["page"] = str(page)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def getSiteDeviceStats(
    mist_session: _APISession, site_id: str, device_id: str, fields: str | None = None
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/devices/get-site-device-stats

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
    fields : str
      List of additional fields requests, comma separated, or `fields=*` for all of them

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/devices/{device_id}"
    query_params: dict[str, str] = {}
    if fields:
        query_params["fields"] = str(fields)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def getSiteAllClientsStatsByDevice(
    mist_session: _APISession, site_id: str, device_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/devices/get-site-all-clients-stats-by-device

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    device_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/devices/{device_id}/clients"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def listSiteDiscoveredAssets(
    mist_session: _APISession,
    site_id: str,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/assets/list-site-discovered-assets

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

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

    uri = f"/api/v1/sites/{site_id}/stats/discovered_assets"
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


def searchSiteDiscoveredSwitchesMetrics(
    mist_session: _APISession,
    site_id: str,
    scope: str | None = None,
    type: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/discovered-switches/search-site-discovered-switches-metrics

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    scope : str{'site', 'switch'}, default: site
      Filter results by scope. enum: `site`, `switch`
    type : str{'inactive_wired_vlans', 'poe_compliance', 'switch_ap_affinity', 'version_compliance'}
      Metric type. enum: `inactive_wired_vlans`, `poe_compliance`, `switch_ap_affinity`, `version_compliance`
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

    uri = f"/api/v1/sites/{site_id}/stats/discovered_switch_metrics/search"
    query_params: dict[str, str] = {}
    if scope:
        query_params["scope"] = str(scope)
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
    if sort:
        query_params["sort"] = str(sort)
    if search_after:
        query_params["search_after"] = str(search_after)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def countSiteDiscoveredSwitches(
    mist_session: _APISession,
    site_id: str,
    distinct: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/discovered-switches/count-site-discovered-switches

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    distinct : str{'mgmt_addr', 'model', 'system_name', 'version'}, default: system_name
      Field used to group this count response. enum: `mgmt_addr`, `model`, `system_name`, `version`
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

    uri = f"/api/v1/sites/{site_id}/stats/discovered_switches/count"
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


def listSiteDiscoveredSwitchesMetrics(
    mist_session: _APISession,
    site_id: str,
    threshold: str | None = None,
    system_name: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/discovered-switches/list-site-discovered-switches-metrics

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    threshold : str
      Configurable # ap per switch threshold, default 12
    system_name : str
      System name for switch level metrics, optional

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/discovered_switches/metrics"
    query_params: dict[str, str] = {}
    if threshold:
        query_params["threshold"] = str(threshold)
    if system_name:
        query_params["system_name"] = str(system_name)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def searchSiteDiscoveredSwitches(
    mist_session: _APISession,
    site_id: str,
    adopted: bool | None = None,
    system_name: str | None = None,
    hostname: str | None = None,
    vendor: str | None = None,
    model: str | None = None,
    version: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/discovered-switches/search-site-discovered-switches

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    adopted : bool
      Filter results by whether the device is adopted
    system_name : str
      Filter discovered switch results by system name
    hostname : str
      Filter results by hostname
    vendor : str
      Filter results by vendor
    model : str
      Filter results by device model
    version : str
      Filter results by software version
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

    uri = f"/api/v1/sites/{site_id}/stats/discovered_switches/search"
    query_params: dict[str, str] = {}
    if adopted:
        query_params["adopted"] = str(adopted)
    if system_name:
        query_params["system_name"] = str(system_name)
    if hostname:
        query_params["hostname"] = str(hostname)
    if vendor:
        query_params["vendor"] = str(vendor)
    if model:
        query_params["model"] = str(model)
    if version:
        query_params["version"] = str(version)
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


def getSiteAssetsOfInterest(
    mist_session: _APISession,
    site_id: str,
    duration: str | None = None,
    start: str | None = None,
    end: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/assets/get-site-assets-of-interest

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    duration : str, default: 1d
      Time range duration for the query, using relative units such as `10m`, `7d`, or `2w`
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

    uri = f"/api/v1/sites/{site_id}/stats/filtered_assets"
    query_params: dict[str, str] = {}
    if duration:
        query_params["duration"] = str(duration)
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


def getSiteGatewayMetrics(mist_session: _APISession, site_id: str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/devices/get-site-gateway-metrics

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/gateways/metrics"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def getSiteWirelessClientsStatsByMap(
    mist_session: _APISession,
    site_id: str,
    map_id: str,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/clients-wireless/get-site-wireless-clients-stats-by-map

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    map_id : str

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

    uri = f"/api/v1/sites/{site_id}/stats/maps/{map_id}/clients"
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


def getSiteDiscoveredAssetByMap(
    mist_session: _APISession, site_id: str, map_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/assets/get-site-discovered-asset-by-map

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    map_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/maps/{map_id}/discovered_assets"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def getSiteSdkStatsByMap(
    mist_session: _APISession, site_id: str, map_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/clients-sdk/get-site-sdk-stats-by-map

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    map_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/maps/{map_id}/sdkclients"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def listSiteUnconnectedClientStats(
    mist_session: _APISession, site_id: str, map_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/clients-wireless/list-site-unconnected-client-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    map_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/maps/{map_id}/unconnected_clients"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def listSiteMxEdgesStats(
    mist_session: _APISession,
    site_id: str,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/mxedges/list-site-mx-edges-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

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

    uri = f"/api/v1/sites/{site_id}/stats/mxedges"
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


def getSiteMxEdgeStats(
    mist_session: _APISession,
    site_id: str,
    mxedge_id: str,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/mxedges/get-site-mx-edge-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    mxedge_id : str

    QUERY PARAMS
    ------------
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    duration : str, default: 1d
      Time range duration for the query, using relative units such as `10m`, `7d`, or `2w`

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/mxedges/{mxedge_id}"
    query_params: dict[str, str] = {}
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if duration:
        query_params["duration"] = str(duration)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def countSiteOspfStats(
    mist_session: _APISession,
    site_id: str,
    distinct: str | None = None,
    start: str | None = None,
    end: str | None = None,
    limit: int | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/ospf/count-site-ospf-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    distinct : str{'site_id', 'org_id', 'mac', 'peer_ip', 'port_id', 'state', 'vrf_name'}
      Field used to group this count response. enum: `site_id`, `org_id`, `mac`, `peer_ip`, `port_id`, `state`, `vrf_name`
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    limit : int, default: 100
      Maximum number of results to return per page
    sort : str, default: timestamp
      On which field the list should be sorted, -prefix represents DESC order
    search_after : str
      Pagination cursor for retrieving subsequent pages of results. This value is automatically populated by Mist in the `next` URL from the previous response and should not be manually constructed.

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/ospf_peers/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if limit:
        query_params["limit"] = str(limit)
    if sort:
        query_params["sort"] = str(sort)
    if search_after:
        query_params["search_after"] = str(search_after)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def searchSiteOspfStats(
    mist_session: _APISession,
    site_id: str,
    mac: str | None = None,
    vrf_name: str | None = None,
    peer_ip: str | None = None,
    start: str | None = None,
    end: str | None = None,
    limit: int | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/ospf/search-site-ospf-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    mac : str
      Filter results by MAC address
    vrf_name : str
      Filter peer results by VRF name
    peer_ip : str
      Filter peer results by peer IP address
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    limit : int, default: 100
      Maximum number of results to return per page
    sort : str, default: timestamp
      On which field the list should be sorted, -prefix represents DESC order
    search_after : str
      Pagination cursor for retrieving subsequent pages of results. This value is automatically populated by Mist in the `next` URL from the previous response and should not be manually constructed.

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/ospf_peers/search"
    query_params: dict[str, str] = {}
    if mac:
        query_params["mac"] = str(mac)
    if vrf_name:
        query_params["vrf_name"] = str(vrf_name)
    if peer_ip:
        query_params["peer_ip"] = str(peer_ip)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if limit:
        query_params["limit"] = str(limit)
    if sort:
        query_params["sort"] = str(sort)
    if search_after:
        query_params["search_after"] = str(search_after)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def countSiteSwOrGwPorts(
    mist_session: _APISession,
    site_id: str,
    distinct: str | None = None,
    full_duplex: bool | None = None,
    mac: str | None = None,
    neighbor_mac: str | None = None,
    neighbor_port_desc: str | None = None,
    neighbor_system_name: str | None = None,
    poe_disabled: bool | None = None,
    poe_mode: str | None = None,
    poe_on: bool | None = None,
    port_id: str | None = None,
    port_mac: str | None = None,
    power_draw: float | None = None,
    tx_pkts: int | None = None,
    rx_pkts: int | None = None,
    rx_bytes: int | None = None,
    tx_bps: int | None = None,
    rx_bps: int | None = None,
    tx_mcast_pkts: int | None = None,
    tx_bcast_pkts: int | None = None,
    rx_mcast_pkts: int | None = None,
    rx_bcast_pkts: int | None = None,
    speed: int | None = None,
    stp_state: str | None = None,
    stp_role: str | None = None,
    auth_state: str | None = None,
    up: bool | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/ports/count-site-sw-or-gw-ports

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    distinct : str{'full_duplex', 'mac', 'neighbor_mac', 'neighbor_port_desc', 'neighbor_system_name', 'poe_disabled', 'poe_mode', 'poe_on', 'port_id', 'port_mac', 'speed', 'up'}, default: mac
      Field used to group this count response. enum: `full_duplex`, `mac`, `neighbor_mac`, `neighbor_port_desc`, `neighbor_system_name`, `poe_disabled`, `poe_mode`, `poe_on`, `port_id`, `port_mac`, `speed`, `up`
    full_duplex : bool
      Indicates full or half duplex
    mac : str
      Filter results by MAC address
    neighbor_mac : str
      Chassis identifier of the chassis type listed
    neighbor_port_desc : str
      Description supplied by the system on the interface E.g. "GigabitEthernet2/0/39"
    neighbor_system_name : str
      Name supplied by the system on the interface E.g. neighbor system name E.g. "Kumar-Acc-SW.mist.local"
    poe_disabled : bool
      Is the POE configured not be disabled.
    poe_mode : str
      POE mode depending on class E.g. "802.3at"
    poe_on : bool
      Is the device attached to POE
    port_id : str
      Filter results by port identifier
    port_mac : str
      Filter results by port MAC address
    power_draw : float
      Amount of power being used by the interface at the time the command is executed. Unit in watts.
    tx_pkts : int
      Filter results by transmitted packet count
    rx_pkts : int
      Filter results by received packet count
    rx_bytes : int
      Filter results by received byte count
    tx_bps : int
      Filter results by transmit rate
    rx_bps : int
      Filter results by receive rate
    tx_mcast_pkts : int
      Filter results by transmitted multicast packet count
    tx_bcast_pkts : int
      Filter results by transmitted broadcast packet count
    rx_mcast_pkts : int
      Filter results by received multicast packet count
    rx_bcast_pkts : int
      Filter results by received broadcast packet count
    speed : int
      Filter results by port speed
    stp_state : str{'', 'blocking', 'disabled', 'forwarding', 'learning', 'listening'}
      STP state used to filter port results when `up`==`true`. enum: `""`, `blocking`, `disabled`, `forwarding`, `learning`, `listening`
    stp_role : str{'', 'alternate', 'backup', 'designated', 'disabled', 'root', 'root-prevented'}
      STP role used to filter port results when `up`==`true`. enum: `""`, `alternate`, `backup`, `designated`, `disabled`, `root`, `root-prevented`
    auth_state : str{'', 'authenticated', 'authenticating', 'held', 'init'}
      Authentication state used to filter port results when `up`==`true` and the port has an authenticator role. enum: `""`, `authenticated`, `authenticating`, `held`, `init`
    up : bool
      Indicates if interface is up
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

    uri = f"/api/v1/sites/{site_id}/stats/ports/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if full_duplex:
        query_params["full_duplex"] = str(full_duplex)
    if mac:
        query_params["mac"] = str(mac)
    if neighbor_mac:
        query_params["neighbor_mac"] = str(neighbor_mac)
    if neighbor_port_desc:
        query_params["neighbor_port_desc"] = str(neighbor_port_desc)
    if neighbor_system_name:
        query_params["neighbor_system_name"] = str(neighbor_system_name)
    if poe_disabled:
        query_params["poe_disabled"] = str(poe_disabled)
    if poe_mode:
        query_params["poe_mode"] = str(poe_mode)
    if poe_on:
        query_params["poe_on"] = str(poe_on)
    if port_id:
        query_params["port_id"] = str(port_id)
    if port_mac:
        query_params["port_mac"] = str(port_mac)
    if power_draw:
        query_params["power_draw"] = str(power_draw)
    if tx_pkts:
        query_params["tx_pkts"] = str(tx_pkts)
    if rx_pkts:
        query_params["rx_pkts"] = str(rx_pkts)
    if rx_bytes:
        query_params["rx_bytes"] = str(rx_bytes)
    if tx_bps:
        query_params["tx_bps"] = str(tx_bps)
    if rx_bps:
        query_params["rx_bps"] = str(rx_bps)
    if tx_mcast_pkts:
        query_params["tx_mcast_pkts"] = str(tx_mcast_pkts)
    if tx_bcast_pkts:
        query_params["tx_bcast_pkts"] = str(tx_bcast_pkts)
    if rx_mcast_pkts:
        query_params["rx_mcast_pkts"] = str(rx_mcast_pkts)
    if rx_bcast_pkts:
        query_params["rx_bcast_pkts"] = str(rx_bcast_pkts)
    if speed:
        query_params["speed"] = str(speed)
    if stp_state:
        query_params["stp_state"] = str(stp_state)
    if stp_role:
        query_params["stp_role"] = str(stp_role)
    if auth_state:
        query_params["auth_state"] = str(auth_state)
    if up:
        query_params["up"] = str(up)
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


def searchSiteSwOrGwPorts(
    mist_session: _APISession,
    site_id: str,
    device_type: str | None = None,
    auth_state: str | None = None,
    full_duplex: bool | None = None,
    lte_imsi: str | None = None,
    lte_iccid: str | None = None,
    lte_imei: str | None = None,
    mac: str | None = None,
    neighbor_mac: str | None = None,
    neighbor_port_desc: str | None = None,
    neighbor_system_name: str | None = None,
    poe_disabled: bool | None = None,
    poe_mode: str | None = None,
    poe_on: bool | None = None,
    poe_priority: str | None = None,
    port_id: str | None = None,
    port_mac: str | None = None,
    speed: int | None = None,
    stp_state: str | None = None,
    stp_role: str | None = None,
    up: bool | None = None,
    xcvr_part_number: str | None = None,
    limit: int | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/ports/search-site-sw-or-gw-ports

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    device_type : str{'switch', 'gateway', 'all'}, default: all
      Type of device. enum: `switch`, `gateway`, `all`
    auth_state : str{'', 'authenticated', 'authenticating', 'held', 'init'}
      Authentication state used to filter port results when `up`==`true` and the port has an authenticator role. enum: `""`, `authenticated`, `authenticating`, `held`, `init`
    full_duplex : bool
      Indicates full or half duplex
    lte_imsi : str
      LTE IMSI value, Check for null/empty
    lte_iccid : str
      LTE ICCID value, Check for null/empty
    lte_imei : str
      LTE IMEI value, Check for null/empty
    mac : str
      Filter results by MAC address
    neighbor_mac : str
      Chassis identifier of the chassis type listed
    neighbor_port_desc : str
      Description supplied by the system on the interface E.g. "GigabitEthernet2/0/39"
    neighbor_system_name : str
      Name supplied by the system on the interface E.g. neighbor system name E.g. "Kumar-Acc-SW.mist.local"
    poe_disabled : bool
      Is the POE configured not be disabled.
    poe_mode : str
      POE mode depending on class E.g. "802.3at"
    poe_on : bool
      Is the device attached to POE
    poe_priority : str{'low', 'high'}
      PoE priority used to filter switch port results. enum: `low`, `high`
    port_id : str
      Filter results by port identifier
    port_mac : str
      Filter results by port MAC address
    speed : int
      Filter results by port speed
    stp_state : str{'', 'blocking', 'disabled', 'forwarding', 'learning', 'listening'}
      STP state used to filter port results when `up`==`true`. enum: `""`, `blocking`, `disabled`, `forwarding`, `learning`, `listening`
    stp_role : str{'', 'alternate', 'backup', 'designated', 'disabled', 'root', 'root-prevented'}
      STP role used to filter port results when `up`==`true`. enum: `""`, `alternate`, `backup`, `designated`, `disabled`, `root`, `root-prevented`
    up : bool
      Indicates if interface is up
    xcvr_part_number : str
      Optic Slot Partnumber, Check for null/empty
    limit : int, default: 100
      Maximum number of results to return per page
    sort : str, default: timestamp
      On which field the list should be sorted, -prefix represents DESC order
    search_after : str
      Pagination cursor for retrieving subsequent pages of results. This value is automatically populated by Mist in the `next` URL from the previous response and should not be manually constructed.

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/ports/search"
    query_params: dict[str, str] = {}
    if device_type:
        query_params["device_type"] = str(device_type)
    if auth_state:
        query_params["auth_state"] = str(auth_state)
    if full_duplex:
        query_params["full_duplex"] = str(full_duplex)
    if lte_imsi:
        query_params["lte_imsi"] = str(lte_imsi)
    if lte_iccid:
        query_params["lte_iccid"] = str(lte_iccid)
    if lte_imei:
        query_params["lte_imei"] = str(lte_imei)
    if mac:
        query_params["mac"] = str(mac)
    if neighbor_mac:
        query_params["neighbor_mac"] = str(neighbor_mac)
    if neighbor_port_desc:
        query_params["neighbor_port_desc"] = str(neighbor_port_desc)
    if neighbor_system_name:
        query_params["neighbor_system_name"] = str(neighbor_system_name)
    if poe_disabled:
        query_params["poe_disabled"] = str(poe_disabled)
    if poe_mode:
        query_params["poe_mode"] = str(poe_mode)
    if poe_on:
        query_params["poe_on"] = str(poe_on)
    if poe_priority:
        query_params["poe_priority"] = str(poe_priority)
    if port_id:
        query_params["port_id"] = str(port_id)
    if port_mac:
        query_params["port_mac"] = str(port_mac)
    if speed:
        query_params["speed"] = str(speed)
    if stp_state:
        query_params["stp_state"] = str(stp_state)
    if stp_role:
        query_params["stp_role"] = str(stp_role)
    if up:
        query_params["up"] = str(up)
    if xcvr_part_number:
        query_params["xcvr_part_number"] = str(xcvr_part_number)
    if limit:
        query_params["limit"] = str(limit)
    if sort:
        query_params["sort"] = str(sort)
    if search_after:
        query_params["search_after"] = str(search_after)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def listSiteRssiZonesStats(mist_session: _APISession, site_id: str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/zones/list-site-rssi-zones-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/rssizones"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def getSiteRssiZoneStats(
    mist_session: _APISession, site_id: str, zone_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/zones/get-site-rssi-zone-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    zone_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/rssizones/{zone_id}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def getSiteSdkStats(
    mist_session: _APISession, site_id: str, sdkclient_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/clients-sdk/get-site-sdk-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    sdkclient_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/sdkclients/{sdkclient_id}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def getSiteSwitchesMetrics(
    mist_session: _APISession,
    site_id: str,
    type: str | None = None,
    scope: str | None = None,
    switch_mac: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/devices/get-site-switches-metrics

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    type : str{'active_ports_summary'}
      Filter results by type. enum: `active_ports_summary`
    scope : str{'site', 'switch'}
      Filter results by scope. enum: `site`, `switch`
    switch_mac : str
      Switch mac, used only with metric `type`==`active_ports_summary`

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/switches/metrics"
    query_params: dict[str, str] = {}
    if type:
        query_params["type"] = str(type)
    if scope:
        query_params["scope"] = str(scope)
    if switch_mac:
        query_params["switch_mac"] = str(switch_mac)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def getSiteWxRulesUsage(mist_session: _APISession, site_id: str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/wxrules/get-site-wx-rules-usage

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/wxrules"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def listSiteZonesStats(
    mist_session: _APISession,
    site_id: str,
    map_id: str | None = None,
    min_duration: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/zones/list-site-zones-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    map_id : str
      Filter results by map identifier
    min_duration : int
      Filter results by minimum duration

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/zones"
    query_params: dict[str, str] = {}
    if map_id:
        query_params["map_id"] = str(map_id)
    if min_duration:
        query_params["min_duration"] = str(min_duration)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def getSiteZoneStats(
    mist_session: _APISession, site_id: str, zone_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/stats/zones/get-site-zone-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    zone_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/stats/zones/{zone_id}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
