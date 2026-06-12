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


def countOrgWiredClients(
    mist_session: _APISession,
    org_id: str,
    distinct: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/wired/count-org-wired-clients

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str{'device_mac', 'mac', 'port_id', 'site_id', 'type', 'vlan'}, default: mac
      Field used to group this count response. enum: `device_mac`, `mac`, `port_id`, `site_id`, `type`, `vlan`
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

    uri = f"/api/v1/orgs/{org_id}/wired_clients/count"
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


def searchOrgWiredClients(
    mist_session: _APISession,
    org_id: str,
    auth_state: str | None = None,
    auth_method: str | None = None,
    source: str | None = None,
    site_id: str | None = None,
    device_mac: str | None = None,
    mac: str | None = None,
    port_id: str | None = None,
    vlan: str | None = None,
    ip: str | None = None,
    manufacture: str | None = None,
    text: str | None = None,
    nacrule_id: str | None = None,
    dhcp_hostname: str | None = None,
    dhcp_fqdn: str | None = None,
    dhcp_client_identifier: str | None = None,
    dhcp_vendor_class_identifier: str | None = None,
    dhcp_request_params: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/wired/search-org-wired-clients

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    auth_state : str
      Filter results by auth state
    auth_method : str
      Filter results by authentication method. Accepts multiple comma-separated values.
    source : str
      Filter results by client learning source. enum: `lldp`, `mac`. Accepts multiple comma-separated values.
    site_id : str
      Filter results by site identifier
    device_mac : str
      Filter results by one or more gateway or switch MAC addresses where the client has connected. Supports comma-separated values
    mac : str
      Partial / full Client MAC address. Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `aabbcc*` and `*bbcc*` match `aabbccddeeff`). Suffix-only wildcards (e.g. `*bccddeeff`) are not supported. Accepts multiple comma-separated values.
    port_id : str
      Filter results by one or more port identifiers where the client has connected. Supports comma-separated values
    vlan : str
      Filter results by one or more VLAN IDs. Supports comma-separated values
    ip : str
      Filter results by one or more IPv4 addresses. Supports comma-separated values
    manufacture : str
      Filter results by manufacturer. Accepts multiple comma-separated values.
    text : str
      Partial / full Client MAC address, hostname or username. Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `aabbcc*` and `*bbcc*` match `aabbccddeeff`). Suffix-only wildcards (e.g. `*ddeeff`) are not supported
    nacrule_id : str
      Filter results by NAC rule identifier
    dhcp_hostname : str
      Filter results by DHCP hostname. Accepts multiple comma-separated values.
    dhcp_fqdn : str
      Filter results by DHCP FQDN
    dhcp_client_identifier : str
      Filter results by DHCP client identifier. Accepts multiple comma-separated values.
    dhcp_vendor_class_identifier : str
      DHCP Vendor Class Identifier. Accepts multiple comma-separated values.
    dhcp_request_params : str
      Filter results by DHCP request parameters. Accepts multiple comma-separated values.
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

    uri = f"/api/v1/orgs/{org_id}/wired_clients/search"
    query_params: dict[str, str] = {}
    if auth_state:
        query_params["auth_state"] = str(auth_state)
    if auth_method:
        query_params["auth_method"] = str(auth_method)
    if source:
        query_params["source"] = str(source)
    if site_id:
        query_params["site_id"] = str(site_id)
    if device_mac:
        query_params["device_mac"] = str(device_mac)
    if mac:
        query_params["mac"] = str(mac)
    if port_id:
        query_params["port_id"] = str(port_id)
    if vlan:
        query_params["vlan"] = str(vlan)
    if ip:
        query_params["ip"] = str(ip)
    if manufacture:
        query_params["manufacture"] = str(manufacture)
    if text:
        query_params["text"] = str(text)
    if nacrule_id:
        query_params["nacrule_id"] = str(nacrule_id)
    if dhcp_hostname:
        query_params["dhcp_hostname"] = str(dhcp_hostname)
    if dhcp_fqdn:
        query_params["dhcp_fqdn"] = str(dhcp_fqdn)
    if dhcp_client_identifier:
        query_params["dhcp_client_identifier"] = str(dhcp_client_identifier)
    if dhcp_vendor_class_identifier:
        query_params["dhcp_vendor_class_identifier"] = str(dhcp_vendor_class_identifier)
    if dhcp_request_params:
        query_params["dhcp_request_params"] = str(dhcp_request_params)
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


def reauthOrgDot1xWiredClient(
    mist_session: _APISession, org_id: str, client_mac: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/lan/reauth-org-dot1x-wired-client

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

    uri = f"/api/v1/orgs/{org_id}/wired_clients/{client_mac}/coa"
    resp = mist_session.mist_post(uri=uri)
    return resp
