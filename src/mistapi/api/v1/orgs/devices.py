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


def listOrgDevices(mist_session: _APISession, org_id: str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/devices/list-org-devices

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

    uri = f"/api/v1/orgs/{org_id}/devices"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def countOrgDevices(
    mist_session: _APISession,
    org_id: str,
    distinct: str = "model",
    hostname: str | None = None,
    site_id: str | None = None,
    model: str | None = None,
    managed: str | None = None,
    mac: str | None = None,
    version: str | None = None,
    ip_address: str | None = None,
    mxtunnel_status: str | None = None,
    mxedge_id: str | None = None,
    lldp_system_name: str | None = None,
    lldp_system_desc: str | None = None,
    lldp_port_id: str | None = None,
    lldp_mgmt_addr: str | None = None,
    type: str = "ap",
    start: int | None = None,
    end: int | None = None,
    duration: str = "1d",
    limit: int = 100,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/devices/count-org-devices

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str{'hostname', 'ip', 'lldp_mgmt_addr', 'lldp_port_id', 'lldp_system_desc', 'lldp_system_name', 'mac', 'model', 'mxedge_id', 'mxtunnel_status', 'site_id', 'version'}, default: model
    hostname : str
    site_id : str
    model : str
    managed : str
    mac : str
    version : str
    ip_address : str
    mxtunnel_status : str{'down', 'up'}
      MxTunnel status, enum: `up`, `down`
    mxedge_id : str
    lldp_system_name : str
    lldp_system_desc : str
    lldp_port_id : str
    lldp_mgmt_addr : str
    type : str{'ap', 'gateway', 'switch'}, default: ap
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/devices/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if hostname:
        query_params["hostname"] = str(hostname)
    if site_id:
        query_params["site_id"] = str(site_id)
    if model:
        query_params["model"] = str(model)
    if managed:
        query_params["managed"] = str(managed)
    if mac:
        query_params["mac"] = str(mac)
    if version:
        query_params["version"] = str(version)
    if ip_address:
        query_params["ip_address"] = str(ip_address)
    if mxtunnel_status:
        query_params["mxtunnel_status"] = str(mxtunnel_status)
    if mxedge_id:
        query_params["mxedge_id"] = str(mxedge_id)
    if lldp_system_name:
        query_params["lldp_system_name"] = str(lldp_system_name)
    if lldp_system_desc:
        query_params["lldp_system_desc"] = str(lldp_system_desc)
    if lldp_port_id:
        query_params["lldp_port_id"] = str(lldp_port_id)
    if lldp_mgmt_addr:
        query_params["lldp_mgmt_addr"] = str(lldp_mgmt_addr)
    if type:
        query_params["type"] = str(type)
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


def countOrgDeviceEvents(
    mist_session: _APISession,
    org_id: str,
    distinct: str = "model",
    site_id: str | None = None,
    ap: str | None = None,
    apfw: str | None = None,
    model: str | None = None,
    text: str | None = None,
    timestamp: str | None = None,
    type: str | None = None,
    start: int | None = None,
    end: int | None = None,
    duration: str = "1d",
    limit: int = 100,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/devices/count-org-device-events

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str{'ap', 'apfw', 'model', 'org_id', 'site_id', 'text', 'timestamp', 'type'}, default: model
    site_id : str
    ap : str
    apfw : str
    model : str
    text : str
    timestamp : str
    type : str
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/devices/events/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if site_id:
        query_params["site_id"] = str(site_id)
    if ap:
        query_params["ap"] = str(ap)
    if apfw:
        query_params["apfw"] = str(apfw)
    if model:
        query_params["model"] = str(model)
    if text:
        query_params["text"] = str(text)
    if timestamp:
        query_params["timestamp"] = str(timestamp)
    if type:
        query_params["type"] = str(type)
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


def searchOrgDeviceEvents(
    mist_session: _APISession,
    org_id: str,
    mac: str | None = None,
    model: str | None = None,
    device_type: str = "ap",
    text: str | None = None,
    timestamp: str | None = None,
    type: str | None = None,
    last_by: str | None = None,
    includes: str | None = None,
    limit: int = 100,
    start: int | None = None,
    end: int | None = None,
    duration: str = "1d",
    sort: str = "timestamp",
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/devices/search-org-device-events

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
    model : str
    device_type : str{'all', 'ap', 'gateway', 'switch'}, default: ap
    text : str
    timestamp : str
    type : str
    last_by : str
    includes : str
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d
    sort : str, default: timestamp

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/devices/events/search"
    query_params: dict[str, str] = {}
    if mac:
        query_params["mac"] = str(mac)
    if model:
        query_params["model"] = str(model)
    if device_type:
        query_params["device_type"] = str(device_type)
    if text:
        query_params["text"] = str(text)
    if timestamp:
        query_params["timestamp"] = str(timestamp)
    if type:
        query_params["type"] = str(type)
    if last_by:
        query_params["last_by"] = str(last_by)
    if includes:
        query_params["includes"] = str(includes)
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
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def countOrgDeviceLastConfigs(
    mist_session: _APISession,
    org_id: str,
    type: str = "ap",
    distinct: str | None = None,
    start: int | None = None,
    end: int | None = None,
    duration: str = "1d",
    limit: int = 100,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/devices/count-org-device-last-configs

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    type : str{'ap', 'gateway', 'switch'}, default: ap
    distinct : str{'mac', 'name', 'site_id', 'version'}
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/devices/last_config/count"
    query_params: dict[str, str] = {}
    if type:
        query_params["type"] = str(type)
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


def searchOrgDeviceLastConfigs(
    mist_session: _APISession,
    org_id: str,
    type: str = "ap",
    mac: str | None = None,
    name: str | None = None,
    version: str | None = None,
    start: int | None = None,
    end: int | None = None,
    limit: int = 100,
    duration: str = "1d",
    sort: str = "timestamp",
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/devices/search-org-device-last-configs

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    type : str{'ap', 'gateway', 'switch'}, default: ap
    mac : str
    name : str
    version : str
    start : int
    end : int
    limit : int, default: 100
    duration : str, default: 1d
    sort : str, default: timestamp

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/devices/last_config/search"
    query_params: dict[str, str] = {}
    if type:
        query_params["type"] = str(type)
    if mac:
        query_params["mac"] = str(mac)
    if name:
        query_params["name"] = str(name)
    if version:
        query_params["version"] = str(version)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if limit:
        query_params["limit"] = str(limit)
    if duration:
        query_params["duration"] = str(duration)
    if sort:
        query_params["sort"] = str(sort)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def listOrgApsMacs(
    mist_session: _APISession, org_id: str, limit: int = 100, page: int = 1
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/devices/list-org-aps-macs

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

    uri = f"/api/v1/orgs/{org_id}/devices/radio_macs"
    query_params: dict[str, str] = {}
    if limit:
        query_params["limit"] = str(limit)
    if page:
        query_params["page"] = str(page)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def searchOrgDevices(
    mist_session: _APISession,
    org_id: str,
    band_24_bandwidth: int | None = None,
    band_24_channel: int | None = None,
    band_24_power: int | None = None,
    band_5_bandwidth: int | None = None,
    band_5_channel: int | None = None,
    band_5_power: int | None = None,
    band_6_bandwidth: int | None = None,
    band_6_channel: int | None = None,
    band_6_power: int | None = None,
    cpu: str | None = None,
    clustered: str | None = None,
    eth0_port_speed: int | None = None,
    evpntopo_id: str | None = None,
    ext_ip: str | None = None,
    hostname: str | None = None,
    ip_address: str | None = None,
    last_config_status: str | None = None,
    last_hostname: str | None = None,
    lldp_mgmt_addr: str | None = None,
    lldp_port_id: str | None = None,
    lldp_power_allocated: int | None = None,
    lldp_power_draw: int | None = None,
    lldp_system_desc: str | None = None,
    lldp_system_name: str | None = None,
    mac: str | None = None,
    model: str | None = None,
    mxedge_id: str | None = None,
    mxedge_ids: str | None = None,
    mxtunnel_status: str | None = None,
    node: str | None = None,
    node0_mac: str | None = None,
    node1_mac: str | None = None,
    power_constrained: bool | None = None,
    site_id: str | None = None,
    t128agent_version: str | None = None,
    version: str | None = None,
    type: str = "ap",
    limit: int = 100,
    start: int | None = None,
    end: int | None = None,
    duration: str = "1d",
    sort: str = "timestamp",
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/devices/search-org-devices

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    band_24_bandwidth : int
    band_24_channel : int
    band_24_power : int
    band_5_bandwidth : int
    band_5_channel : int
    band_5_power : int
    band_6_bandwidth : int
    band_6_channel : int
    band_6_power : int
    cpu : str
    clustered : str
    eth0_port_speed : int
    evpntopo_id : str
    ext_ip : str
    hostname : str
    ip_address : str
    last_config_status : str
    last_hostname : str
    lldp_mgmt_addr : str
    lldp_port_id : str
    lldp_power_allocated : int
    lldp_power_draw : int
    lldp_system_desc : str
    lldp_system_name : str
    mac : str
    model : str
    mxedge_id : str
    mxedge_ids : str
    mxtunnel_status : str{'down', 'up'}
      If `type`==`ap`, MxTunnel status, up / down
    node : str
    node0_mac : str
    node1_mac : str
    power_constrained : bool
    site_id : str
    t128agent_version : str
    version : str
    type : str{'ap', 'gateway', 'switch'}, default: ap
      Type of device. enum: `ap`, `gateway`, `switch`
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d
    sort : str, default: timestamp

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/devices/search"
    query_params: dict[str, str] = {}
    if band_24_bandwidth:
        query_params["band_24_bandwidth"] = str(band_24_bandwidth)
    if band_24_channel:
        query_params["band_24_channel"] = str(band_24_channel)
    if band_24_power:
        query_params["band_24_power"] = str(band_24_power)
    if band_5_bandwidth:
        query_params["band_5_bandwidth"] = str(band_5_bandwidth)
    if band_5_channel:
        query_params["band_5_channel"] = str(band_5_channel)
    if band_5_power:
        query_params["band_5_power"] = str(band_5_power)
    if band_6_bandwidth:
        query_params["band_6_bandwidth"] = str(band_6_bandwidth)
    if band_6_channel:
        query_params["band_6_channel"] = str(band_6_channel)
    if band_6_power:
        query_params["band_6_power"] = str(band_6_power)
    if cpu:
        query_params["cpu"] = str(cpu)
    if clustered:
        query_params["clustered"] = str(clustered)
    if eth0_port_speed:
        query_params["eth0_port_speed"] = str(eth0_port_speed)
    if evpntopo_id:
        query_params["evpntopo_id"] = str(evpntopo_id)
    if ext_ip:
        query_params["ext_ip"] = str(ext_ip)
    if hostname:
        query_params["hostname"] = str(hostname)
    if ip_address:
        query_params["ip_address"] = str(ip_address)
    if last_config_status:
        query_params["last_config_status"] = str(last_config_status)
    if last_hostname:
        query_params["last_hostname"] = str(last_hostname)
    if lldp_mgmt_addr:
        query_params["lldp_mgmt_addr"] = str(lldp_mgmt_addr)
    if lldp_port_id:
        query_params["lldp_port_id"] = str(lldp_port_id)
    if lldp_power_allocated:
        query_params["lldp_power_allocated"] = str(lldp_power_allocated)
    if lldp_power_draw:
        query_params["lldp_power_draw"] = str(lldp_power_draw)
    if lldp_system_desc:
        query_params["lldp_system_desc"] = str(lldp_system_desc)
    if lldp_system_name:
        query_params["lldp_system_name"] = str(lldp_system_name)
    if mac:
        query_params["mac"] = str(mac)
    if model:
        query_params["model"] = str(model)
    if mxedge_id:
        query_params["mxedge_id"] = str(mxedge_id)
    if mxedge_ids:
        query_params["mxedge_ids"] = str(mxedge_ids)
    if mxtunnel_status:
        query_params["mxtunnel_status"] = str(mxtunnel_status)
    if node:
        query_params["node"] = str(node)
    if node0_mac:
        query_params["node0_mac"] = str(node0_mac)
    if node1_mac:
        query_params["node1_mac"] = str(node1_mac)
    if power_constrained:
        query_params["power_constrained"] = str(power_constrained)
    if site_id:
        query_params["site_id"] = str(site_id)
    if t128agent_version:
        query_params["t128agent_version"] = str(t128agent_version)
    if version:
        query_params["version"] = str(version)
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
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def listOrgDevicesSummary(mist_session: _APISession, org_id: str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/devices/list-org-devices-summary

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

    uri = f"/api/v1/orgs/{org_id}/devices/summary"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def listOrgDeviceUpgrades(mist_session: _APISession, org_id: str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/upgrade/list-org-device-upgrades

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

    uri = f"/api/v1/orgs/{org_id}/devices/upgrade"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def upgradeOrgDevices(
    mist_session: _APISession, org_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/upgrade/upgrade-org-devices

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

    uri = f"/api/v1/orgs/{org_id}/devices/upgrade"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def getOrgDeviceUpgrade(
    mist_session: _APISession, org_id: str, upgrade_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/upgrade/get-org-device-upgrade

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    upgrade_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/devices/upgrade/{upgrade_id}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def cancelOrgDeviceUpgrade(
    mist_session: _APISession, org_id: str, upgrade_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/upgrade/cancel-org-device-upgrade

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    upgrade_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/devices/upgrade/{upgrade_id}/cancel"
    resp = mist_session.mist_post(uri=uri)
    return resp


def listOrgAvailableDeviceVersions(
    mist_session: _APISession, org_id: str, type: str = "ap", model: str | None = None
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/upgrade/list-org-available-device-versions

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    type : str{'ap', 'gateway', 'switch'}, default: ap
    model : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/devices/versions"
    query_params: dict[str, str] = {}
    if type:
        query_params["type"] = str(type)
    if model:
        query_params["model"] = str(model)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
