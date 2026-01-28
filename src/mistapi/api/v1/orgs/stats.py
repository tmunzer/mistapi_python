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


def getOrgStats(
    mist_session: _APISession,
    org_id: str,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/stats/get-org-stats

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
    end : str
    duration : str, default: 1d
    limit : int, default: 100
    page : int, default: 1

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/stats"
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
    end : str
    duration : str, default: 1d
    limit : int, default: 100
    page : int, default: 1

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
    limit : int, default: 100

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
    mac : str
    device_name : str
    name : str
    map_id : str
    ibeacon_uuid : str
    ibeacon_major : str
    ibeacon_minor : str
    eddystone_uid_namespace : str
    eddystone_uid_instance : str
    eddystone_url : str
    ap_mac : str
    beam : int
    rssi : int
    limit : int, default: 100
    start : str
    end : str
    duration : str, default: 1d
    sort : str, default: timestamp
    search_after : str

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
    distinct : str
    limit : int, default: 100

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
    neighbor_mac : str
    site_id : str
    vrf_name : str
    limit : int, default: 100
    start : str
    end : str
    duration : str, default: 1d
    sort : str, default: timestamp
    search_after : str

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
    type : str{'all', 'ap', 'gateway', 'switch'}, default: ap
    status : str{'all', 'connected', 'disconnected'}, default: all
    site_id : str
    mac : str
    evpntopo_id : str
    evpn_unused : str
    fields : str
    start : str
    end : str
    duration : str, default: 1d
    limit : int, default: 100
    page : int, default: 1

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
      Filter for site level mist edges
    start : str
    end : str
    duration : str, default: 1d
    limit : int, default: 100
    page : int, default: 1

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
    start : str
    end : str
    limit : int, default: 100
    sort : str, default: timestamp
    search_after : str

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
    mac : str
    vrf_name : str
    peer_ip : str
    start : str
    end : str
    limit : int, default: 100
    sort : str, default: timestamp
    search_after : str

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
    full_duplex : bool
    mac : str
    neighbor_mac : str
    neighbor_port_desc : str
    neighbor_system_name : str
    poe_disabled : bool
    poe_mode : str
    poe_on : bool
    port_id : str
    port_mac : str
    power_draw : float
    tx_pkts : int
    rx_pkts : int
    rx_bytes : int
    tx_bps : int
    rx_bps : int
    tx_mcast_pkts : int
    tx_bcast_pkts : int
    rx_mcast_pkts : int
    rx_bcast_pkts : int
    speed : int
    stp_state : str{'blocking', 'disabled', 'forwarding', 'learning', 'listening'}
      If `up`==`true`
    stp_role : str{'alternate', 'backup', 'designated', 'root', 'root-prevented'}
      If `up`==`true`
    auth_state : str{'authenticated', 'authenticating', 'held', 'init'}
      If `up`==`true` && has Authenticator role
    up : bool
    site_id : str
    start : str
    end : str
    duration : str, default: 1d
    limit : int, default: 100

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
    full_duplex: bool | None = None,
    mac: str | None = None,
    neighbor_mac: str | None = None,
    neighbor_port_desc: str | None = None,
    neighbor_system_name: str | None = None,
    poe_disabled: bool | None = None,
    poe_priority: str | None = None,
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
    tx_errors: int | None = None,
    rx_errors: int | None = None,
    tx_mcast_pkts: int | None = None,
    tx_bcast_pkts: int | None = None,
    rx_mcast_pkts: int | None = None,
    rx_bcast_pkts: int | None = None,
    speed: int | None = None,
    mac_limit: int | None = None,
    mac_count: int | None = None,
    up: bool | None = None,
    stp_state: str | None = None,
    stp_role: str | None = None,
    auth_state: str | None = None,
    optics_bias_current: float | None = None,
    optics_tx_power: float | None = None,
    optics_rx_power: float | None = None,
    optics_module_temperature: float | None = None,
    optics_module_voltage: float | None = None,
    type: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
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
    full_duplex : bool
    mac : str
    neighbor_mac : str
    neighbor_port_desc : str
    neighbor_system_name : str
    poe_disabled : bool
    poe_priority : str{'low', 'high'}
      PoE priority.
    poe_mode : str
    poe_on : bool
    port_id : str
    port_mac : str
    power_draw : float
    tx_pkts : int
    rx_pkts : int
    rx_bytes : int
    tx_bps : int
    rx_bps : int
    tx_errors : int
    rx_errors : int
    tx_mcast_pkts : int
    tx_bcast_pkts : int
    rx_mcast_pkts : int
    rx_bcast_pkts : int
    speed : int
    mac_limit : int
    mac_count : int
    up : bool
    stp_state : str{'blocking', 'disabled', 'forwarding', 'learning', 'listening'}
      If `up`==`true`
    stp_role : str{'alternate', 'backup', 'designated', 'root', 'root-prevented'}
      If `up`==`true`
    auth_state : str{'authenticated', 'authenticating', 'held', 'init'}
      If `up`==`true` && has Authenticator role
    optics_bias_current : float
    optics_tx_power : float
    optics_rx_power : float
    optics_module_temperature : float
    optics_module_voltage : float
    type : str{'switch', 'gateway', 'all'}, default: all
      Type of device. enum: `switch`, `gateway`, `all`
    limit : int, default: 100
    start : str
    end : str
    duration : str, default: 1d
    sort : str, default: timestamp
    search_after : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/stats/ports/search"
    query_params: dict[str, str] = {}
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
    if poe_priority:
        query_params["poe_priority"] = str(poe_priority)
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
    if tx_errors:
        query_params["tx_errors"] = str(tx_errors)
    if rx_errors:
        query_params["rx_errors"] = str(rx_errors)
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
    if mac_limit:
        query_params["mac_limit"] = str(mac_limit)
    if mac_count:
        query_params["mac_count"] = str(mac_count)
    if up:
        query_params["up"] = str(up)
    if stp_state:
        query_params["stp_state"] = str(stp_state)
    if stp_role:
        query_params["stp_role"] = str(stp_role)
    if auth_state:
        query_params["auth_state"] = str(auth_state)
    if optics_bias_current:
        query_params["optics_bias_current"] = str(optics_bias_current)
    if optics_tx_power:
        query_params["optics_tx_power"] = str(optics_tx_power)
    if optics_rx_power:
        query_params["optics_rx_power"] = str(optics_rx_power)
    if optics_module_temperature:
        query_params["optics_module_temperature"] = str(optics_module_temperature)
    if optics_module_voltage:
        query_params["optics_module_voltage"] = str(optics_module_voltage)
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


def listOrgSiteStats(
    mist_session: _APISession,
    org_id: str,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
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
    start : str
    end : str
    duration : str, default: 1d
    limit : int, default: 100
    page : int, default: 1

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/stats/sites"
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
          - If `type`==`wxtunnel`: wxtunnel_id / ap / remote_ip / remote_port / state / mxedge_id / mxcluster_id / site_id / peer_mxedge_id; default is wxtunnel_id
    - If `type`==`wan`: mac / site_id / node / peer_ip / peer_host/ ip / tunnel_name / protocol / auth_algo / encrypt_algo / ike_version / last_event / up
        type : str{'wan', 'wxtunnel'}, default: wxtunnel
        limit : int, default: 100

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
    site_id : str
    wxtunnel_id : str
    ap : str
    mac : str
    node : str
    peer_ip : str
    peer_host : str
    ip : str
    tunnel_name : str
    protocol : str
    auth_algo : str
    encrypt_algo : str
    ike_version : str
    up : str
    type : str{'wan', 'wxtunnel'}, default: wxtunnel
    limit : int, default: 100
    start : str
    end : str
    duration : str, default: 5m
    sort : str, default: timestamp
    search_after : str

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
    start : str
    end : str
    duration : str, default: 1d
    limit : int, default: 100

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
    site_id : str
    type : str{'ipsec', 'svr'}
    limit : int, default: 100
    start : str
    end : str
    duration : str, default: 1d
    sort : str, default: timestamp
    search_after : str

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
