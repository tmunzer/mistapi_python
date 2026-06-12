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
    distinct: str | None = None,
    hostname: str | None = None,
    site_id: str | None = None,
    model: str | None = None,
    managed: str | None = None,
    mac: str | None = None,
    version: str | None = None,
    ip: str | None = None,
    mxtunnel_status: str | None = None,
    mxedge_id: str | None = None,
    lldp_system_name: str | None = None,
    lldp_system_desc: str | None = None,
    lldp_port_id: str | None = None,
    lldp_mgmt_addr: str | None = None,
    type: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
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
      Field used to group this count response. enum: `hostname`, `ip`, `lldp_mgmt_addr`, `lldp_port_id`, `lldp_system_desc`, `lldp_system_name`, `mac`, `model`, `mxedge_id`, `mxtunnel_status`, `site_id`, `version`
    hostname : str
      Partial / full hostname
    site_id : str
      Filter results by site identifier
    model : str
      Filter results by device model. Accepts multiple comma-separated values.
    managed : str
      for switches and gateways, to filter on managed/unmanaged devices. Deprecated in favour of mist_configured. enum: `true`, `false`
    mac : str
      Filter results by MAC address
    version : str
      Filter results by software version
    ip : str
      Filter results by IPv4 address
    mxtunnel_status : str{'down', 'up'}
      MxTunnel status, enum: `up`, `down`
    mxedge_id : str
      Mist Edge id, if AP is connecting to a Mist Edge
    lldp_system_name : str
      Filter results by LLDP system name
    lldp_system_desc : str
      Filter results by LLDP system description
    lldp_port_id : str
      Filter results by LLDP port identifier
    lldp_mgmt_addr : str
      LLDP management IP address
    type : str{'ap', 'gateway', 'switch'}, default: ap
      Filter results by type. enum: `ap`, `gateway`, `switch`
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
    if ip:
        query_params["ip"] = str(ip)
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
    distinct: str | None = None,
    site_id: str | None = None,
    ap: str | None = None,
    apfw: str | None = None,
    model: str | None = None,
    text: str | None = None,
    type: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
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
      Field used to group this count response. enum: `ap`, `apfw`, `model`, `org_id`, `site_id`, `text`, `timestamp`, `type`
    site_id : str
      Filter results by site identifier
    ap : str
      Filter results by AP MAC address
    apfw : str
      Filter results by AP firmware version
    model : str
      Filter results by device model
    text : str
      Filter results by event message text
    type : str
      See [List Device Events Definitions](/#operations/listDeviceEventsDefinitions)
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
    device_type: str | None = None,
    text: str | None = None,
    type: str | None = None,
    last_by: str | None = None,
    includes: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
    search_after: str | None = None,
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
      Filter results by MAC address. Accepts multiple comma-separated values.
    model : str
      Filter results by device model. Accepts multiple comma-separated values.
    device_type : str, default: ap
      Filter results by device type. Accepts multiple comma-separated values.
    text : str
      Filter results by event message text
    type : str
      See [List Device Events Definitions](/#operations/listDeviceEventsDefinitions). Accepts multiple comma-separated values.
    last_by : str
      Return last/recent event for passed in field
    includes : str
      Keyword to include events from additional indices (e.g. ext_tunnel for prisma events)
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
    if search_after:
        query_params["search_after"] = str(search_after)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def countOrgDeviceLastConfigs(
    mist_session: _APISession,
    org_id: str,
    type: str | None = None,
    distinct: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
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
      Filter results by type. enum: `ap`, `gateway`, `switch`
    distinct : str{'mac', 'name', 'site_id', 'version'}
      Field used to group this count response. enum: `mac`, `name`, `site_id`, `version`
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
    device_type: str | None = None,
    mac: str | None = None,
    name: str | None = None,
    version: str | None = None,
    cert_expiry_duration: str | None = None,
    start: str | None = None,
    end: str | None = None,
    limit: int | None = None,
    duration: str | None = None,
    sort: str | None = None,
    search_after: str | None = None,
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
    device_type : str{'ap', 'gateway', 'switch', 'mxedge'}, default: ap
      Filter results by device type. enum: `ap`, `gateway`, `switch`, `mxedge`
    mac : str
      Filter results by MAC address. Accepts multiple comma-separated values.
    name : str
      Filter results by name. Accepts multiple comma-separated values.
    version : str
      Filter results by software version. Accepts multiple comma-separated values.
    cert_expiry_duration : str
      Duration for expiring cert queries (format: 2d/3h/172800 seconds)
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    limit : int, default: 100
      Maximum number of results to return per page
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

    uri = f"/api/v1/orgs/{org_id}/devices/last_config/search"
    query_params: dict[str, str] = {}
    if device_type:
        query_params["device_type"] = str(device_type)
    if mac:
        query_params["mac"] = str(mac)
    if name:
        query_params["name"] = str(name)
    if version:
        query_params["version"] = str(version)
    if cert_expiry_duration:
        query_params["cert_expiry_duration"] = str(cert_expiry_duration)
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
    if search_after:
        query_params["search_after"] = str(search_after)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def listOrgApsMacs(
    mist_session: _APISession,
    org_id: str,
    limit: int | None = None,
    page: int | None = None,
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
      Maximum number of results to return per page
    page : int, default: 1
      Select the page number to return when using page-based pagination; starts at `1`

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
    band_24_channel: int | None = None,
    band_5_channel: int | None = None,
    band_6_channel: int | None = None,
    band_24_bandwidth: int | None = None,
    band_5_bandwidth: int | None = None,
    band_6_bandwidth: int | None = None,
    band_24_power: int | None = None,
    band_5_power: int | None = None,
    band_6_power: int | None = None,
    clustered: bool | None = None,
    eth0_port_speed: int | None = None,
    evpntopo_id: str | None = None,
    ext_ip: str | None = None,
    hostname: str | None = None,
    ip: str | None = None,
    last_config_status: str | None = None,
    last_hostname: str | None = None,
    lldp_mgmt_addr: str | None = None,
    lldp_port_id: str | None = None,
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
    radius_stats: str | None = None,
    site_id: str | None = None,
    stats: bool | None = None,
    t128agent_version: str | None = None,
    type: str | None = None,
    version: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
    search_after: str | None = None,
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
        band_24_channel : int
          When `type`==`ap`, Channel of band_24. Accepts multiple comma-separated integer values.
        band_5_channel : int
          When `type`==`ap`, Channel of band_5. Accepts multiple comma-separated integer values.
        band_6_channel : int
          When `type`==`ap`, Channel of band_6. Accepts multiple comma-separated integer values.
        band_24_bandwidth : int
          When `type`==`ap`, Bandwidth of band_24. Accepts multiple comma-separated integer values.
        band_5_bandwidth : int
          When `type`==`ap`, Bandwidth of band_5. Accepts multiple comma-separated integer values.
        band_6_bandwidth : int
          When `type`==`ap`, Bandwidth of band_6. Accepts multiple comma-separated integer values.
        band_24_power : int
          When `type`==`ap`, Power of band_24. Accepts multiple comma-separated integer values.
        band_5_power : int
          When `type`==`ap`, Power of band_5. Accepts multiple comma-separated integer values.
        band_6_power : int
          When `type`==`ap`, Power of band_6. Accepts multiple comma-separated integer values.
        clustered : bool
          When `type`==`gateway`, true / false
        eth0_port_speed : int
          When `type`==`ap`, Port speed of eth0. Accepts multiple comma-separated integer values.
        evpntopo_id : str
          When `type`==`switch`, EVPN topology id
        ext_ip : str
          Partial / full Device external ip. Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `1.2.3.*` and `*.2.3.*` match `1.2.3.4`). Suffix-only wildcards (e.g. `*.2.3.4`) are not supported. Accepts multiple comma-separated values.
        hostname : str
          Partial / full Device hostname. Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `my-london*` and `*london*` match `my-london-1`). Suffix-only wildcards (e.g. `*london-1`) are not supported. Accepts multiple comma-separated values.
        ip : str
          Partial / full Device IP address. Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `10.100.10.*` and `*100.10.*` match `10.100.10.54`). Suffix-only wildcards (e.g. `*.54`) are not supported. Accepts multiple comma-separated values.
        last_config_status : str
          When `type`==`switch` or `type`==`gateway`, last configuration status
        last_hostname : str
          Last hostname of the device. Accepts multiple comma-separated values.
        lldp_mgmt_addr : str
          When `type`==`ap`, LLDP management IP address. Accepts multiple comma-separated values.
        lldp_port_id : str
          When `type`==`ap`, LLDP port id. Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `ge-0/0/*` and `*-0/0/*` match `ge-0/0/30`). Suffix-only wildcards (e.g. `*switch-01`) are not supported. Accepts multiple comma-separated values.
        lldp_system_desc : str
          When `type`==`ap`, LLDP system description. Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `Juniper Networks*` and `*Networks*` match `Juniper Networks, Inc.`). Suffix-only wildcards (e.g. `*switch-01`) are not supported
        lldp_system_name : str
          When `type`==`ap`, LLDP system name. Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `my-switch*` and `*switch*` match `my-switch-01`). Suffix-only wildcards (e.g. `*switch-01`) are not supported. Accepts multiple comma-separated values.
        mac : str
          Partial / full Device MAC address. Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `001122*` and `*1122*` match `001122334455`). Suffix-only wildcards (e.g. `*4455`) are not supported. Accepts multiple comma-separated values.
        model : str
          Partial / full Device model. Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `AP4*` and `*P4*` match `AP43`). Suffix-only wildcards (e.g. `*43`) are not supported. Accepts multiple comma-separated values.
        mxedge_id : str
          When `type`==`ap`, Mist Edge id, if AP is connecting to a Mist Edge. Accepts multiple comma-separated values.
        mxedge_ids : str
          When `type`==`ap`, Comma separated list of Mist Edge id, if AP is connecting to a Mist Edge
        mxtunnel_status : str{'down', 'up'}
          When `type`==`ap`, Mist Tunnel status used to filter results. enum: `down`, `up`
        node : str{'node0', 'node1'}
          When `type`==`gateway`. enum: `node0`, `node1`
        node0_mac : str
          When `type`==`gateway`, node0 MAC address
        node1_mac : str
          When `type`==`gateway`, node1 MAC address
        power_constrained : bool
          When `type`==`ap`, whether the AP is power constrained.
        radius_stats : str
          When `type`==`switch` or `type`==`gateway`, Key-value pairs where the key
    is the RADIUS server address and the value contains authentication statistics:
      * <server_address> (string): IP address of the RADIUS server as the key
      * `auth_accepts` (long): Number of accepted authentication requests
      * `auth_rejects` (long): Number of rejected authentication requests
      * `auth_timeouts` (long): Number of authentication timeouts
      * `auth_server_status` (string): Status of the server. Possible values: `up`, `down`, `unreachable`
        site_id : str
          Filter results by site identifier
        stats : bool
          Whether to return device stats
        t128agent_version : str
          When `type`==`gateway` (SSR only), version of 128T agent
        type : str{'ap', 'gateway', 'switch'}, default: ap
          Device type used to filter results. enum: `ap`, `gateway`, `switch`
        version : str
          Filter results by software version. Accepts multiple comma-separated values.
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

    uri = f"/api/v1/orgs/{org_id}/devices/search"
    query_params: dict[str, str] = {}
    if band_24_channel:
        query_params["band_24_channel"] = str(band_24_channel)
    if band_5_channel:
        query_params["band_5_channel"] = str(band_5_channel)
    if band_6_channel:
        query_params["band_6_channel"] = str(band_6_channel)
    if band_24_bandwidth:
        query_params["band_24_bandwidth"] = str(band_24_bandwidth)
    if band_5_bandwidth:
        query_params["band_5_bandwidth"] = str(band_5_bandwidth)
    if band_6_bandwidth:
        query_params["band_6_bandwidth"] = str(band_6_bandwidth)
    if band_24_power:
        query_params["band_24_power"] = str(band_24_power)
    if band_5_power:
        query_params["band_5_power"] = str(band_5_power)
    if band_6_power:
        query_params["band_6_power"] = str(band_6_power)
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
    if ip:
        query_params["ip"] = str(ip)
    if last_config_status:
        query_params["last_config_status"] = str(last_config_status)
    if last_hostname:
        query_params["last_hostname"] = str(last_hostname)
    if lldp_mgmt_addr:
        query_params["lldp_mgmt_addr"] = str(lldp_mgmt_addr)
    if lldp_port_id:
        query_params["lldp_port_id"] = str(lldp_port_id)
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
    if radius_stats:
        query_params["radius_stats"] = str(radius_stats)
    if site_id:
        query_params["site_id"] = str(site_id)
    if stats:
        query_params["stats"] = str(stats)
    if t128agent_version:
        query_params["t128agent_version"] = str(t128agent_version)
    if type:
        query_params["type"] = str(type)
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
    mist_session: _APISession,
    org_id: str,
    type: str | None = None,
    model: str | None = None,
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
      Filter results by type. enum: `ap`, `gateway`, `switch`
    model : str
      Fetch version for device model, use/combine with `type` as needed (for switch and gateway devices). Accepts multiple comma-separated values.

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
