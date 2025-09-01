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
    distinct: str = "device",
    mac: str | None = None,
    hostname: str | None = None,
    device: str | None = None,
    os: str | None = None,
    model: str | None = None,
    ap: str | None = None,
    vlan: str | None = None,
    ssid: str | None = None,
    ip_address: str | None = None,
    start: int | None = None,
    end: int | None = None,
    duration: str = "1d",
    limit: int = 100,
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
    mac : str
    hostname : str
    device : str
    os : str
    model : str
    ap : str
    vlan : str
    ssid : str
    ip_address : str
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100

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
    if ip_address:
        query_params["ip_address"] = str(ip_address)
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
    start: int | None = None,
    end: int | None = None,
    duration: str = "1d",
    limit: int = 100,
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
    type : str
    reason_code : int
    ssid : str
    ap : str
    proto : str{'a', 'ac', 'ax', 'b', 'g', 'n'}
      a / b / g / n / ac / ax
    band : str{'24', '5', '6'}
      802.11 Band
    wlan_id : str
    site_id : str
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100

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
    reason_code: int | None = None,
    ssid: str | None = None,
    ap: str | None = None,
    key_mgmt: str | None = None,
    proto: str | None = None,
    band: str | None = None,
    wlan_id: str | None = None,
    nacrule_id: str | None = None,
    start: int | None = None,
    end: int | None = None,
    duration: str = "1d",
    sort: str = "timestamp",
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
    reason_code : int
    ssid : str
    ap : str
    key_mgmt : str{'WPA2-PSK', 'WPA2-PSK-FT', 'WPA3-EAP-SHA256'}
      Key Management Protocol, e.g. WPA2-PSK, WPA3-SAE, WPA2-Enterprise
    proto : str{'a', 'ac', 'ax', 'b', 'g', 'n'}
      a / b / g / n / ac / ax
    band : str{'24', '5', '6'}
      802.11 Band
    wlan_id : str
    nacrule_id : str
    start : int
    end : int
    duration : str, default: 1d
    sort : str, default: timestamp

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
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def searchOrgWirelessClients(
    mist_session: _APISession,
    org_id: str,
    site_id: str | None = None,
    mac: str | None = None,
    ip_address: str | None = None,
    hostname: str | None = None,
    band: str | None = None,
    device: str | None = None,
    os: str | None = None,
    model: str | None = None,
    ap: str | None = None,
    psk_id: str | None = None,
    psk_name: str | None = None,
    username: str | None = None,
    vlan: str | None = None,
    ssid: str | None = None,
    text: str | None = None,
    limit: int = 100,
    start: int | None = None,
    end: int | None = None,
    duration: str = "1d",
    sort: str = "timestamp",
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
    mac : str
    ip_address : str
    hostname : str
    band : str
    device : str
    os : str
    model : str
    ap : str
    psk_id : str
    psk_name : str
    username : str
    vlan : str
    ssid : str
    text : str
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

    uri = f"/api/v1/orgs/{org_id}/clients/search"
    query_params: dict[str, str] = {}
    if site_id:
        query_params["site_id"] = str(site_id)
    if mac:
        query_params["mac"] = str(mac)
    if ip_address:
        query_params["ip_address"] = str(ip_address)
    if hostname:
        query_params["hostname"] = str(hostname)
    if band:
        query_params["band"] = str(band)
    if device:
        query_params["device"] = str(device)
    if os:
        query_params["os"] = str(os)
    if model:
        query_params["model"] = str(model)
    if ap:
        query_params["ap"] = str(ap)
    if psk_id:
        query_params["psk_id"] = str(psk_id)
    if psk_name:
        query_params["psk_name"] = str(psk_name)
    if username:
        query_params["username"] = str(username)
    if vlan:
        query_params["vlan"] = str(vlan)
    if ssid:
        query_params["ssid"] = str(ssid)
    if text:
        query_params["text"] = str(text)
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


def countOrgWirelessClientsSessions(
    mist_session: _APISession,
    org_id: str,
    distinct: str = "device",
    ap: str | None = None,
    band: str | None = None,
    client_family: str | None = None,
    client_manufacture: str | None = None,
    client_model: str | None = None,
    client_os: str | None = None,
    ssid: str | None = None,
    wlan_id: str | None = None,
    start: int | None = None,
    end: int | None = None,
    duration: str = "1d",
    limit: int = 100,
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
    ap : str
    band : str{'24', '5', '6'}
      802.11 Band
    client_family : str
    client_manufacture : str
    client_model : str
    client_os : str
    ssid : str
    wlan_id : str
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100

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
    limit: int = 100,
    start: int | None = None,
    end: int | None = None,
    duration: str = "1d",
    sort: str = "timestamp",
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
    band : str{'24', '5', '6'}
      802.11 Band
    client_family : str
    client_manufacture : str
    client_model : str
    client_username : str
    client_os : str
    ssid : str
    wlan_id : str
    psk_id : str
    psk_name : str
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
