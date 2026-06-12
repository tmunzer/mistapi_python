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


def countOrgWirelessClients(
    mist_session: _APISession,
    org_id: str,
    distinct: str | None = None,
    mac: str | None = None,
    hostname: str | None = None,
    device: str | None = None,
    os: str | None = None,
    model: str | None = None,
    ap: str | None = None,
    vlan: str | None = None,
    ssid: str | None = None,
    ip: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/wireless/count-org-wireless-clients

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str{'ap', 'device', 'hostname', 'ip', 'mac', 'model', 'os', 'ssid', 'vlan'}, default: device
      Field used to group this count response. enum: `ap`, `device`, `hostname`, `ip`, `mac`, `model`, `os`, `ssid`, `vlan`
    mac : str
      Partial / full Client MAC address. Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `aabbcc*` and `*bbcc*` match `aabbccddeeff`). Suffix-only wildcards (e.g. `*bccddeeff`) are not supported. Accepts multiple comma-separated values.
    hostname : str
      Partial / full Client hostname. Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `everest*` and `*rest*` match `my-everest-client`). Suffix-only wildcards (e.g. `*everest`) are not supported. Accepts multiple comma-separated values.
    device : str
      Filter results by device type
    os : str
      Filter results by operating system
    model : str
      Filter results by device model
    ap : str
      Filter results by AP MAC address
    vlan : str
      Filter results by VLAN ID
    ssid : str
      Filter results by SSID
    ip : str
      Filter results by IPv4 address
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

    uri = f"/api/v1/orgs/{org_id}/clients/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if mac:
        query_params["mac"] = str(mac)
    if hostname:
        query_params["hostname"] = str(hostname)
    if device:
        query_params["device"] = str(device)
    if os:
        query_params["os"] = str(os)
    if model:
        query_params["model"] = str(model)
    if ap:
        query_params["ap"] = str(ap)
    if vlan:
        query_params["vlan"] = str(vlan)
    if ssid:
        query_params["ssid"] = str(ssid)
    if ip:
        query_params["ip"] = str(ip)
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


def countOrgWirelessClientEvents(
    mist_session: _APISession,
    org_id: str,
    distinct: str | None = None,
    type: str | None = None,
    reason_code: int | None = None,
    ssid: str | None = None,
    ap: str | None = None,
    proto: str | None = None,
    band: str | None = None,
    wlan_id: str | None = None,
    site_id: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/wireless/count-org-wireless-client-events

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str{'band', 'channel', 'proto', 'ssid', 'type', 'wlan_id'}
      Field used to group this count response. enum: `band`, `channel`, `proto`, `ssid`, `type`, `wlan_id`
    type : str
      See [List Device Events Definitions](/#operations/listDeviceEventsDefinitions). Accepts multiple comma-separated values.
    reason_code : int
      Reason code filter for association and disassociation events
    ssid : str
      Filter results by SSID
    ap : str
      Filter results by AP MAC address
    proto : str{'a', 'ac', 'ax', 'b', 'be', 'g', 'n'}
      802.11 protocol used to filter results. enum: `a`, `ac`, `ax`, `b`, `be`, `g`, `n`
    band : str{'24', '5', '5-dedicated', '5-selectable', '6', '6-dedicated', '6-selectable'}
      802.11 band used to filter radio results. enum: `24`, `5`, `5-dedicated`, `5-selectable`, `6`, `6-dedicated`, `6-selectable`
    wlan_id : str
      Filter results by WLAN identifier
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

    uri = f"/api/v1/orgs/{org_id}/clients/events/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if type:
        query_params["type"] = str(type)
    if reason_code:
        query_params["reason_code"] = str(reason_code)
    if ssid:
        query_params["ssid"] = str(ssid)
    if ap:
        query_params["ap"] = str(ap)
    if proto:
        query_params["proto"] = str(proto)
    if band:
        query_params["band"] = str(band)
    if wlan_id:
        query_params["wlan_id"] = str(wlan_id)
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


def searchOrgWirelessClientEvents(
    mist_session: _APISession,
    org_id: str,
    type: str | None = None,
    reason_code: str | None = None,
    ssid: str | None = None,
    ap: str | None = None,
    key_mgmt: str | None = None,
    proto: str | None = None,
    band: str | None = None,
    wlan_id: str | None = None,
    nacrule_id: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
    limit: int | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/wireless/search-org-wireless-client-events

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    type : str
      See [List Device Events Definitions](/#operations/listDeviceEventsDefinitions). Accepts multiple comma-separated values.
    reason_code : str
      Reason code filter for association and disassociation events. Accepts multiple comma-separated integer values.
    ssid : str
      Filter results by SSID. Accepts multiple comma-separated values.
    ap : str
      Filter results by AP MAC address. Accepts multiple comma-separated values.
    key_mgmt : str
      Key management protocol used to filter client events. enum: `WPA2-PSK`, `WPA2-PSK/CCMP`, `WPA2-PSK-FT`, `WPA2-PSK-SHA256`, `WPA3-EAP-SHA256`, `WPA3-EAP-SHA256/CCMP`, `WPA3-EAP-FT/GCMP256`, `WPA3-SAE-FT`, `WPA3-SAE-PSK`. Accepts multiple comma-separated values.
    proto : str
      802.11 protocol used to filter results. enum: `a`, `ac`, `ax`, `b`, `be`, `g`, `n`. Accepts multiple comma-separated values.
    band : str
      802.11 band used to filter radio results. enum: `24`, `5`, `5-dedicated`, `5-selectable`, `6`, `6-dedicated`, `6-selectable`. Accepts multiple comma-separated values.
    wlan_id : str
      Filter results by WLAN identifier
    nacrule_id : str
      Filter results by NAC rule identifier. Accepts multiple comma-separated values.
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    duration : str, default: 1d
      Time range duration for the query, using relative units such as `10m`, `7d`, or `2w`
    sort : str, default: timestamp
      On which field the list should be sorted, -prefix represents DESC order
    limit : int, default: 100
      Maximum number of results to return per page
    search_after : str
      Pagination cursor for retrieving subsequent pages of results. This value is automatically populated by Mist in the `next` URL from the previous response and should not be manually constructed.

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/clients/events/search"
    query_params: dict[str, str] = {}
    if type:
        query_params["type"] = str(type)
    if reason_code:
        query_params["reason_code"] = str(reason_code)
    if ssid:
        query_params["ssid"] = str(ssid)
    if ap:
        query_params["ap"] = str(ap)
    if key_mgmt:
        query_params["key_mgmt"] = str(key_mgmt)
    if proto:
        query_params["proto"] = str(proto)
    if band:
        query_params["band"] = str(band)
    if wlan_id:
        query_params["wlan_id"] = str(wlan_id)
    if nacrule_id:
        query_params["nacrule_id"] = str(nacrule_id)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if duration:
        query_params["duration"] = str(duration)
    if sort:
        query_params["sort"] = str(sort)
    if limit:
        query_params["limit"] = str(limit)
    if search_after:
        query_params["search_after"] = str(search_after)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def searchOrgWirelessClients(
    mist_session: _APISession,
    org_id: str,
    site_id: str | None = None,
    ap: str | None = None,
    band: str | None = None,
    device: str | None = None,
    hostname: str | None = None,
    ip: str | None = None,
    mac: str | None = None,
    model: str | None = None,
    os: str | None = None,
    psk_id: str | None = None,
    psk_name: str | None = None,
    ssid: str | None = None,
    text: str | None = None,
    username: str | None = None,
    vlan: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/wireless/search-org-wireless-clients

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
    ap : str
      Filter results by AP MAC address
    band : str
      Comma separated list of Radio band (e.g. `24,5`). enum: `24`, `5`, `6`
    device : str
      Comma separated list of Device type (e.g. `Mac,iPhone`). Case sensitive
    hostname : str
      Partial / full Client hostname. Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `everest*` and `*rest*` match `my-everest-client`). Suffix-only wildcards (e.g. `*everest`) are not supported. Accepts multiple comma-separated values.
    ip : str
      Partial / full Client IP address. Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `10.100.10.*` and `*100.10.*` match `10.100.10.54`). Suffix-only wildcards (e.g. `*.54`) are not supported. Accepts multiple comma-separated values.
    mac : str
      Partial / full Client MAC address. Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `aabbcc*` and `*bbcc*` match `aabbccddeeff`). Suffix-only wildcards (e.g. `*bccddeeff`) are not supported. Accepts multiple comma-separated values.
    model : str
      Only available for clients running the Marvis Client app, model, e.g. "MBP 15 late 2013", 6, 6s, "8+ GSM"
    os : str
      Only available for clients running the Marvis Client app, os, e.g. Sierra, Yosemite, Windows 10
    psk_id : str
      PSK identifier used to filter the results
    psk_name : str
      Only available for clients using PPSK authentication, the Name of the PSK
    ssid : str
      Filter results by SSID
    text : str
      Partial / full MAC address, hostname, username, psk_name or ip. Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `everest*` and `*rest*` match `my-everest-client`). Suffix-only wildcards (e.g. `*everest`) are not supported
    username : str
      Partial / full username. Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `johndoe*` and `*mycorp*` match `johndoe@mycorp.com`). Suffix-only wildcards (e.g. `*mycorp.com`) are not supported. Accepts multiple comma-separated values.
    vlan : str
      Filter results by VLAN ID
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

    uri = f"/api/v1/orgs/{org_id}/clients/search"
    query_params: dict[str, str] = {}
    if site_id:
        query_params["site_id"] = str(site_id)
    if ap:
        query_params["ap"] = str(ap)
    if band:
        query_params["band"] = str(band)
    if device:
        query_params["device"] = str(device)
    if hostname:
        query_params["hostname"] = str(hostname)
    if ip:
        query_params["ip"] = str(ip)
    if mac:
        query_params["mac"] = str(mac)
    if model:
        query_params["model"] = str(model)
    if os:
        query_params["os"] = str(os)
    if psk_id:
        query_params["psk_id"] = str(psk_id)
    if psk_name:
        query_params["psk_name"] = str(psk_name)
    if ssid:
        query_params["ssid"] = str(ssid)
    if text:
        query_params["text"] = str(text)
    if username:
        query_params["username"] = str(username)
    if vlan:
        query_params["vlan"] = str(vlan)
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


def countOrgWirelessClientsSessions(
    mist_session: _APISession,
    org_id: str,
    distinct: str | None = None,
    ap: str | None = None,
    band: str | None = None,
    client_family: str | None = None,
    client_manufacture: str | None = None,
    client_model: str | None = None,
    client_os: str | None = None,
    ssid: str | None = None,
    wlan_id: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/wireless/count-org-wireless-clients-sessions

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str{'ap', 'device', 'hostname', 'ip', 'model', 'os', 'ssid', 'vlan'}, default: device
      Field used to group this count response. enum: `ap`, `device`, `hostname`, `ip`, `model`, `os`, `ssid`, `vlan`
    ap : str
      Filter results by AP MAC address
    band : str{'24', '5', '5-dedicated', '5-selectable', '6', '6-dedicated', '6-selectable'}
      802.11 band used to filter radio results. enum: `24`, `5`, `5-dedicated`, `5-selectable`, `6`, `6-dedicated`, `6-selectable`
    client_family : str
      E.g. "Mac", "iPhone", "Apple watch"
    client_manufacture : str
      Filter results by client manufacturer, e.g. "Apple"
    client_model : str
      Filter results by client model, e.g. "8+", "XS"
    client_os : str
      E.g. "Mojave", "Windows 10", "Linux"
    ssid : str
      Filter results by SSID
    wlan_id : str
      Filter results by WLAN identifier
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

    uri = f"/api/v1/orgs/{org_id}/clients/sessions/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if ap:
        query_params["ap"] = str(ap)
    if band:
        query_params["band"] = str(band)
    if client_family:
        query_params["client_family"] = str(client_family)
    if client_manufacture:
        query_params["client_manufacture"] = str(client_manufacture)
    if client_model:
        query_params["client_model"] = str(client_model)
    if client_os:
        query_params["client_os"] = str(client_os)
    if ssid:
        query_params["ssid"] = str(ssid)
    if wlan_id:
        query_params["wlan_id"] = str(wlan_id)
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


def searchOrgWirelessClientSessions(
    mist_session: _APISession,
    org_id: str,
    ap: str | None = None,
    band: str | None = None,
    client_family: str | None = None,
    client_manufacture: str | None = None,
    client_model: str | None = None,
    client_username: str | None = None,
    client_os: str | None = None,
    ssid: str | None = None,
    wlan_id: str | None = None,
    psk_id: str | None = None,
    psk_name: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/wireless/search-org-wireless-client-sessions

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    ap : str
      Filter results by AP MAC address
    band : str
      802.11 band used to filter radio results. enum: `24`, `5`, `5-dedicated`, `5-selectable`, `6`, `6-dedicated`, `6-selectable`. Accepts multiple comma-separated values.
    client_family : str
      E.g. "Mac", "iPhone", "Apple watch". Accepts multiple comma-separated values.
    client_manufacture : str
      Filter results by client manufacturer, e.g. "Apple". Accepts multiple comma-separated values.
    client_model : str
      Filter results by client model, e.g. "8+", "XS". Accepts multiple comma-separated values.
    client_username : str
      Filter results by client username. Accepts multiple comma-separated values.
    client_os : str
      E.g. "Mojave", "Windows 10", "Linux". Accepts multiple comma-separated values.
    ssid : str
      Filter results by SSID. Accepts multiple comma-separated values.
    wlan_id : str
      Filter results by WLAN identifier
    psk_id : str
      PSK identifier used to filter the results
    psk_name : str
      Filter results by PSK name. Accepts multiple comma-separated values.
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

    uri = f"/api/v1/orgs/{org_id}/clients/sessions/search"
    query_params: dict[str, str] = {}
    if ap:
        query_params["ap"] = str(ap)
    if band:
        query_params["band"] = str(band)
    if client_family:
        query_params["client_family"] = str(client_family)
    if client_manufacture:
        query_params["client_manufacture"] = str(client_manufacture)
    if client_model:
        query_params["client_model"] = str(client_model)
    if client_username:
        query_params["client_username"] = str(client_username)
    if client_os:
        query_params["client_os"] = str(client_os)
    if ssid:
        query_params["ssid"] = str(ssid)
    if wlan_id:
        query_params["wlan_id"] = str(wlan_id)
    if psk_id:
        query_params["psk_id"] = str(psk_id)
    if psk_name:
        query_params["psk_name"] = str(psk_name)
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


def reauthOrgDot1xWirelessClient(
    mist_session: _APISession, org_id: str, client_mac: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/wi-fi/reauth-org-dot1x-wireless-client

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    client_mac : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/clients/{client_mac}/coa"
    resp = mist_session.mist_post(uri=uri)
    return resp
