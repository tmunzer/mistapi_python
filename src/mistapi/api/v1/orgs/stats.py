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


def getOrgStats(mist_session: _APISession, org_id: str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/stats/get-org-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/stats"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def listOrgAssetsStats(
    mist_session: _APISession,
    org_id: str,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/stats/assets/list-org-assets-stats

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

    uri = f"/api/v1/orgs/{org_id}/stats/assets"
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


def countOrgAssetsByDistanceField(
    mist_session: _APISession,
    org_id: str,
    distinct: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/stats/assets/count-org-assets-by-distance-field

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str{'ibeacon_major', 'ibeacon_minor', 'ibeacon_uuid', 'mac', 'map_id', 'site_id'}
      Field used to group this count response. enum: `ibeacon_major`, `ibeacon_minor`, `ibeacon_uuid`, `mac`, `map_id`, `site_id`
    limit : int, default: 100
      Maximum number of results to return per page

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/stats/assets/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if limit:
        query_params["limit"] = str(limit)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def searchOrgAssets(
    mist_session: _APISession,
    org_id: str,
    site_id: str | None = None,
    mac: str | None = None,
    device_name: str | None = None,
    name: str | None = None,
    map_id: str | None = None,
    ibeacon_uuid: str | None = None,
    ibeacon_major: str | None = None,
    ibeacon_minor: str | None = None,
    eddystone_uid_namespace: str | None = None,
    eddystone_uid_instance: str | None = None,
    eddystone_url: str | None = None,
    ap_mac: str | None = None,
    beam: int | None = None,
    rssi: int | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/stats/assets/search-org-assets

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
      Filter results by site identifier
    mac : str
      Filter results by MAC address. Accepts multiple comma-separated values.
    device_name : str
      Filter asset results by reporting device name
    name : str
      Filter results by name. Accepts multiple comma-separated values.
    map_id : str
      Filter results by map identifier
    ibeacon_uuid : str
      Filter asset results by iBeacon UUID. Accepts multiple comma-separated values.
    ibeacon_major : str
      Filter asset results by iBeacon major value. Accepts multiple comma-separated values.
    ibeacon_minor : str
      Filter asset results by iBeacon minor value. Accepts multiple comma-separated values.
    eddystone_uid_namespace : str
      Filter asset results by Eddystone UID namespace
    eddystone_uid_instance : str
      Filter asset results by Eddystone UID instance
    eddystone_url : str
      Filter asset results by Eddystone URL
    ap_mac : str
      Filter asset results by reporting AP MAC address. Accepts multiple comma-separated values.
    beam : int
      Filter asset results by beam value. Accepts multiple comma-separated integer values.
    rssi : int
      Filter asset results by RSSI value. Accepts multiple comma-separated integer values.
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

    uri = f"/api/v1/orgs/{org_id}/stats/assets/search"
    query_params: dict[str, str] = {}
    if site_id:
        query_params["site_id"] = str(site_id)
    if mac:
        query_params["mac"] = str(mac)
    if device_name:
        query_params["device_name"] = str(device_name)
    if name:
        query_params["name"] = str(name)
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


def countOrgBgpStats(
    mist_session: _APISession,
    org_id: str,
    state: str | None = None,
    distinct: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/stats/bgp-peers/count-org-bgp-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

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

    uri = f"/api/v1/orgs/{org_id}/stats/bgp_peers/count"
    query_params: dict[str, str] = {}
    if state:
        query_params["state"] = str(state)
    if distinct:
        query_params["distinct"] = str(distinct)
    if limit:
        query_params["limit"] = str(limit)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def searchOrgBgpStats(
    mist_session: _APISession,
    org_id: str,
    mac: str | None = None,
    neighbor_mac: str | None = None,
    site_id: str | None = None,
    vrf_name: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/stats/bgp-peers/search-org-bgp-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    mac : str
      Filter results by MAC address. Accepts multiple comma-separated values.
    neighbor_mac : str
      Filter peer results by neighbor MAC address
    site_id : str
      Filter results by site identifier
    vrf_name : str
      Filter peer results by VRF name. Accepts multiple comma-separated values.
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

    uri = f"/api/v1/orgs/{org_id}/stats/bgp_peers/search"
    query_params: dict[str, str] = {}
    if mac:
        query_params["mac"] = str(mac)
    if neighbor_mac:
        query_params["neighbor_mac"] = str(neighbor_mac)
    if site_id:
        query_params["site_id"] = str(site_id)
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


def listOrgDevicesStats(
    mist_session: _APISession,
    org_id: str,
    type: str | None = None,
    status: str | None = None,
    site_id: str | None = None,
    mac: str | None = None,
    evpntopo_id: str | None = None,
    evpn_unused: str | None = None,
    fields: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/stats/devices/list-org-devices-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    type : str{'all', 'ap', 'switch', 'gateway'}, default: ap
      Filter results by one device type. Use a single value; comma-separated values are not supported. enum: `all`, `ap`, `gateway`, `switch`
    status : str
      Filter results by status. enum: `all`, `connected`, `disconnected`. Accepts multiple comma-separated values.
    site_id : str
      Filter results by site identifier. Accepts multiple comma-separated values.
    mac : str
      Filter results by MAC address. Accepts multiple comma-separated values.
    evpntopo_id : str
      Filter results by evpntopo id
    evpn_unused : str
      If `evpn_unused`==`true`, find EVPN eligible switches which don’t belong to any EVPN Topology yet
    fields : str
      List of additional fields requests, comma separated, or `fields=*` for all of them
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

    uri = f"/api/v1/orgs/{org_id}/stats/devices"
    query_params: dict[str, str] = {}
    if type:
        query_params["type"] = str(type)
    if status:
        query_params["status"] = str(status)
    if site_id:
        query_params["site_id"] = str(site_id)
    if mac:
        query_params["mac"] = str(mac)
    if evpntopo_id:
        query_params["evpntopo_id"] = str(evpntopo_id)
    if evpn_unused:
        query_params["evpn_unused"] = str(evpn_unused)
    if fields:
        query_params["fields"] = str(fields)
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


def deleteOrgMarvisClient(mist_session: _APISession, org_id: str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/marvis/delete-org-marvis-client

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/stats/marvisclients"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp


def countOrgMarvisClientsStats(
    mist_session: _APISession,
    org_id: str,
    distinct: str | None = None,
    device_id: str | None = None,
    wifi_mac: str | None = None,
    wifi_ip: str | None = None,
    hostname: str | None = None,
    model: str | None = None,
    mfg: str | None = None,
    serial: str | None = None,
    os_type: str | None = None,
    os_version: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/stats/marvis-clients/count-org-marvis-clients-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str, default: os_type
      Field to count by. enum: `device_id`, `wifi_mac`, `wifi_ip`, `hostname`, `model`, `mfg`, `serial`, `os_type`, `os_version`
    device_id : str
      Filter by Marvis Client installation device UUID
    wifi_mac : str
      Filter by device Wi-Fi MAC address
    wifi_ip : str
      Filter by device Wi-Fi IP address
    hostname : str
      Filter by device hostname
    model : str
      Filter by device model
    mfg : str
      Filter by device manufacturer
    serial : str
      Filter by device serial number
    os_type : str
      Filter by device OS type or platform
    os_version : str
      Filter by device OS version
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

    uri = f"/api/v1/orgs/{org_id}/stats/marvisclients/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if device_id:
        query_params["device_id"] = str(device_id)
    if wifi_mac:
        query_params["wifi_mac"] = str(wifi_mac)
    if wifi_ip:
        query_params["wifi_ip"] = str(wifi_ip)
    if hostname:
        query_params["hostname"] = str(hostname)
    if model:
        query_params["model"] = str(model)
    if mfg:
        query_params["mfg"] = str(mfg)
    if serial:
        query_params["serial"] = str(serial)
    if os_type:
        query_params["os_type"] = str(os_type)
    if os_version:
        query_params["os_version"] = str(os_version)
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


def searchOrgMarvisClientsStats(
    mist_session: _APISession,
    org_id: str,
    device_id: str | None = None,
    wifi_mac: str | None = None,
    wifi_ip: str | None = None,
    hostname: str | None = None,
    model: str | None = None,
    mfg: str | None = None,
    serial: str | None = None,
    os_type: str | None = None,
    os_version: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/stats/marvis-clients/search-org-marvis-clients-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    device_id : str
      Filter by Marvis Client installation device UUID
    wifi_mac : str
      Filter by device Wi-Fi MAC address
    wifi_ip : str
      Filter by device Wi-Fi IP address
    hostname : str
      Filter by device hostname
    model : str
      Filter by device model
    mfg : str
      Filter by device manufacturer
    serial : str
      Filter by device serial number
    os_type : str
      Filter by device OS type or platform
    os_version : str
      Filter by device OS version
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

    uri = f"/api/v1/orgs/{org_id}/stats/marvisclients/search"
    query_params: dict[str, str] = {}
    if device_id:
        query_params["device_id"] = str(device_id)
    if wifi_mac:
        query_params["wifi_mac"] = str(wifi_mac)
    if wifi_ip:
        query_params["wifi_ip"] = str(wifi_ip)
    if hostname:
        query_params["hostname"] = str(hostname)
    if model:
        query_params["model"] = str(model)
    if mfg:
        query_params["mfg"] = str(mfg)
    if serial:
        query_params["serial"] = str(serial)
    if os_type:
        query_params["os_type"] = str(os_type)
    if os_version:
        query_params["os_version"] = str(os_version)
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


def listOrgMxEdgesStats(
    mist_session: _APISession,
    org_id: str,
    for_site: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/stats/mxedges/list-org-mx-edges-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    for_site : str{'any', 'true', 'false'}
      Filter for site level Mist Edges. enum: `any`, `true`, `false`
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

    uri = f"/api/v1/orgs/{org_id}/stats/mxedges"
    query_params: dict[str, str] = {}
    if for_site:
        query_params["for_site"] = str(for_site)
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


def getOrgMxEdgeStats(
    mist_session: _APISession, org_id: str, mxedge_id: str, for_site: bool | None = None
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/stats/mxedges/get-org-mx-edge-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    mxedge_id : str

    QUERY PARAMS
    ------------
    for_site : bool
      Filter results by whether the object is scoped to a site

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/stats/mxedges/{mxedge_id}"
    query_params: dict[str, str] = {}
    if for_site:
        query_params["for_site"] = str(for_site)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def countOrgOspfStats(
    mist_session: _APISession,
    org_id: str,
    distinct: str | None = None,
    start: str | None = None,
    end: str | None = None,
    limit: int | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/stats/ospf/count-org-ospf-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

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

    uri = f"/api/v1/orgs/{org_id}/stats/ospf_peers/count"
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


def searchOrgOspfStats(
    mist_session: _APISession,
    org_id: str,
    site_id: str | None = None,
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
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/stats/ospf/search-org-ospf-stats

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
      Filter results by site identifier
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

    uri = f"/api/v1/orgs/{org_id}/stats/ospf_peers/search"
    query_params: dict[str, str] = {}
    if site_id:
        query_params["site_id"] = str(site_id)
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


def getOrgOtherDeviceStats(
    mist_session: _APISession, org_id: str, device_mac: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/stats/other-devices/get-org-other-device-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    device_mac : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/stats/otherdevices/{device_mac}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def countOrgSwOrGwPorts(
    mist_session: _APISession,
    org_id: str,
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
    site_id: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/stats/ports/count-org-sw-or-gw-ports

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str{'full_duplex', 'mac', 'neighbor_mac', 'neighbor_port_desc', 'neighbor_system_name', 'poe_disabled', 'poe_mode', 'poe_on', 'port_id', 'port_mac', 'speed', 'up'}, default: mac
      Field used to group this count response. enum: `full_duplex`, `mac`, `neighbor_mac`, `neighbor_port_desc`, `neighbor_system_name`, `poe_disabled`, `poe_mode`, `poe_on`, `port_id`, `port_mac`, `speed`, `up`
    full_duplex : bool
      Indicates full or half duplex
    mac : str
      Filter results by MAC address. Accepts multiple comma-separated values.
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
    site_id : str
      Filter results by site identifier
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

    uri = f"/api/v1/orgs/{org_id}/stats/ports/count"
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
    if site_id:
        query_params["site_id"] = str(site_id)
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


def searchOrgSwOrGwPorts(
    mist_session: _APISession,
    org_id: str,
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
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/stats/ports/search-org-sw-or-gw-ports

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    device_type : str
      Type of device. enum: `switch`, `gateway`, `all`. Accepts multiple comma-separated values.
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
      Filter results by MAC address. Accepts multiple comma-separated values.
    neighbor_mac : str
      Chassis identifier of the chassis type listed. Accepts multiple comma-separated values.
    neighbor_port_desc : str
      Description supplied by the system on the interface E.g. "GigabitEthernet2/0/39". Accepts multiple comma-separated values.
    neighbor_system_name : str
      Name supplied by the system on the interface E.g. neighbor system name E.g. "Kumar-Acc-SW.mist.local". Accepts multiple comma-separated values.
    poe_disabled : bool
      Is the POE configured not be disabled.
    poe_mode : str
      POE mode depending on class E.g. "802.3at"
    poe_on : bool
      Is the device attached to POE
    poe_priority : str{'low', 'high'}
      PoE priority used to filter switch port results. enum: `low`, `high`
    port_id : str
      Filter results by port identifier. Accepts multiple comma-separated values.
    port_mac : str
      Filter results by port MAC address. Accepts multiple comma-separated values.
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

    uri = f"/api/v1/orgs/{org_id}/stats/ports/search"
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


def listOrgSiteStats(
    mist_session: _APISession,
    org_id: str,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/stats/sites/list-org-site-stats

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

    uri = f"/api/v1/orgs/{org_id}/stats/sites"
    query_params: dict[str, str] = {}
    if limit:
        query_params["limit"] = str(limit)
    if page:
        query_params["page"] = str(page)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def countOrgTunnelsStats(
    mist_session: _APISession,
    org_id: str,
    distinct: str | None = None,
    type: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/stats/tunnels/count-org-tunnels-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str{'ap', 'auth_algo', 'encrypt_algo', 'ike_version', 'ip', 'last_event', 'mac', 'mxcluster_id', 'mxedge_id', 'node', 'peer_host', 'peer_ip', 'peer_mxedge_id', 'protocol', 'remote_ip', 'remote_port', 'site_id', 'state', 'tunnel_name', 'up', 'wxtunnel_id'}, default: wxtunnel_id
      Field used to group tunnel statistics count results. enum: `ap`, `auth_algo`, `encrypt_algo`, `ike_version`, `ip`, `last_event`, `mac`, `mxcluster_id`, `mxedge_id`, `node`, `peer_host`, `peer_ip`, `peer_mxedge_id`, `protocol`, `remote_ip`, `remote_port`, `site_id`, `state`, `tunnel_name`, `up`, `wxtunnel_id`
    type : str{'wan', 'wxtunnel'}, default: wxtunnel
      Filter results by type. enum: `wan`, `wxtunnel`
    limit : int, default: 100
      Maximum number of results to return per page

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/stats/tunnels/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if type:
        query_params["type"] = str(type)
    if limit:
        query_params["limit"] = str(limit)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def searchOrgTunnelsStats(
    mist_session: _APISession,
    org_id: str,
    mxcluster_id: str | None = None,
    site_id: str | None = None,
    wxtunnel_id: str | None = None,
    ap: str | None = None,
    mac: str | None = None,
    node: str | None = None,
    peer_ip: str | None = None,
    peer_host: str | None = None,
    ip: str | None = None,
    tunnel_name: str | None = None,
    protocol: str | None = None,
    auth_algo: str | None = None,
    encrypt_algo: str | None = None,
    ike_version: str | None = None,
    up: str | None = None,
    type: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/stats/tunnels/search-org-tunnels-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    mxcluster_id : str
      Filter results by mxcluster id when `type`==`wxtunnel`
    site_id : str
      Filter results by site identifier
    wxtunnel_id : str
      Filter results by wxtunnel id when `type`==`wxtunnel`
    ap : str
      Filter results by AP MAC address when `type`==`wxtunnel`
    mac : str
      Filter results by MAC address when `type`==`wan`
    node : str
      Filter results by node when `type`==`wan`
    peer_ip : str
      Filter results by peer ip when `type`==`wan`
    peer_host : str
      Filter results by peer host when `type`==`wan`
    ip : str
      Filter results by IP address when `type`==`wan`
    tunnel_name : str
      Filter results by tunnel name when `type`==`wan`
    protocol : str
      Filter results by protocol when `type`==`wan`
    auth_algo : str
      Filter results by auth algo when `type`==`wan`
    encrypt_algo : str
      Filter results by encrypt algo when `type`==`wan`
    ike_version : str
      Filter results by ike version when `type`==`wan`
    up : str
      Filter results by up when `type`==`wan`
    type : str{'wan', 'wxtunnel'}, default: wxtunnel
      Filter results by type. enum: `wan`, `wxtunnel`
    limit : int, default: 100
      Maximum number of results to return per page
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    duration : str, default: 5m
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

    uri = f"/api/v1/orgs/{org_id}/stats/tunnels/search"
    query_params: dict[str, str] = {}
    if mxcluster_id:
        query_params["mxcluster_id"] = str(mxcluster_id)
    if site_id:
        query_params["site_id"] = str(site_id)
    if wxtunnel_id:
        query_params["wxtunnel_id"] = str(wxtunnel_id)
    if ap:
        query_params["ap"] = str(ap)
    if mac:
        query_params["mac"] = str(mac)
    if node:
        query_params["node"] = str(node)
    if peer_ip:
        query_params["peer_ip"] = str(peer_ip)
    if peer_host:
        query_params["peer_host"] = str(peer_host)
    if ip:
        query_params["ip"] = str(ip)
    if tunnel_name:
        query_params["tunnel_name"] = str(tunnel_name)
    if protocol:
        query_params["protocol"] = str(protocol)
    if auth_algo:
        query_params["auth_algo"] = str(auth_algo)
    if encrypt_algo:
        query_params["encrypt_algo"] = str(encrypt_algo)
    if ike_version:
        query_params["ike_version"] = str(ike_version)
    if up:
        query_params["up"] = str(up)
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


def countOrgPeerPathStats(
    mist_session: _APISession,
    org_id: str,
    distinct: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/stats/vpn-peers/count-org-peer-path-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str
      Field used to group this count response
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

    uri = f"/api/v1/orgs/{org_id}/stats/vpn_peers/count"
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


def searchOrgPeerPathStats(
    mist_session: _APISession,
    org_id: str,
    mac: str | None = None,
    site_id: str | None = None,
    type: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/stats/vpn-peers/search-org-peer-path-stats

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    mac : str
      Filter results by MAC address. Accepts multiple comma-separated values.
    site_id : str
      Filter results by site identifier
    type : str
      VPN implementation type used to filter the results. enum: `ipsec`, `svr`. Accepts multiple comma-separated values.
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

    uri = f"/api/v1/orgs/{org_id}/stats/vpn_peers/search"
    query_params: dict[str, str] = {}
    if mac:
        query_params["mac"] = str(mac)
    if site_id:
        query_params["site_id"] = str(site_id)
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
