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


def countSiteWiredClients(
    mist_session: _APISession,
    site_id: str,
    distinct: str | None = None,
    mac: str | None = None,
    device_mac: str | None = None,
    port_id: str | None = None,
    vlan: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/clients/wired/count-site-wired-clients

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    distinct : str{'mac', 'port_id', 'vlan'}, default: mac
      Field used to group this count response. enum: `mac`, `port_id`, `vlan`
    mac : str
      Filter results by MAC address
    device_mac : str
      Filter results by device MAC address
    port_id : str
      Filter results by port identifier
    vlan : str
      Filter results by VLAN ID
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

    uri = f"/api/v1/sites/{site_id}/wired_clients/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if mac:
        query_params["mac"] = str(mac)
    if device_mac:
        query_params["device_mac"] = str(device_mac)
    if port_id:
        query_params["port_id"] = str(port_id)
    if vlan:
        query_params["vlan"] = str(vlan)
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


def searchSiteWiredClients(
    mist_session: _APISession,
    site_id: str,
    device_mac: str | None = None,
    mac: str | None = None,
    ip: str | None = None,
    port_id: str | None = None,
    source: str | None = None,
    vlan: str | None = None,
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
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/clients/wired/search-site-wired-clients

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    device_mac : str
      Filter results by device MAC address
    mac : str
      Filter results by MAC address
    ip : str
      Filter results by IP address
    port_id : str
      Filter results by port identifier
    source : str{'lldp', 'mac'}
      Filter results by client learning source. enum: `lldp`, `mac`
    vlan : str
      Filter results by VLAN ID
    manufacture : str
      Filter results by manufacturer
    text : str
      Single entry of hostname/mac
    nacrule_id : str
      Filter results by NAC rule identifier
    dhcp_hostname : str
      Filter results by DHCP hostname
    dhcp_fqdn : str
      Filter results by DHCP FQDN
    dhcp_client_identifier : str
      Filter results by DHCP client identifier
    dhcp_vendor_class_identifier : str
      DHCP Vendor Class Identifier
    dhcp_request_params : str
      Filter results by DHCP request parameters
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

    uri = f"/api/v1/sites/{site_id}/wired_clients/search"
    query_params: dict[str, str] = {}
    if device_mac:
        query_params["device_mac"] = str(device_mac)
    if mac:
        query_params["mac"] = str(mac)
    if ip:
        query_params["ip"] = str(ip)
    if port_id:
        query_params["port_id"] = str(port_id)
    if source:
        query_params["source"] = str(source)
    if vlan:
        query_params["vlan"] = str(vlan)
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


def reauthSiteDot1xWiredClient(
    mist_session: _APISession, site_id: str, client_mac: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/lan/reauth-site-dot1x-wired-client

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    client_mac : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/wired_clients/{client_mac}/coa"
    resp = mist_session.mist_post(uri=uri)
    return resp
