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


def searchSiteFlows(
    mist_session: _APISession,
    site_id: str,
    start: str | None = None,
    end: str | None = None,
    limit: int | None = None,
    sort: str | None = None,
    device_mac: str | None = None,
    src_ip: str | None = None,
    dst_ip: str | None = None,
    src_port: str | None = None,
    dst_port: str | None = None,
    protocol: str | None = None,
    state: str | None = None,
    direction: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/lan/search-site-flows

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
    limit : int, default: 100
      Maximum number of results to return per page
    sort : str, default: timestamp
      On which field the list should be sorted, -prefix represents DESC order
    device_mac : str
      MAC address of the switch device to filter by
    src_ip : str
      Source IP address
    dst_ip : str
      Destination IP address
    src_port : str
      Source port
    dst_port : str
      Destination port
    protocol : str
      Protocol (e.g. `tcp`, `udp`, `icmp`)
    state : str
      Flow state
    direction : str
      Flow direction
    search_after : str
      Pagination cursor for retrieving subsequent pages of results. This value is automatically populated by Mist in the `next` URL from the previous response and should not be manually constructed.

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/flows/search"
    query_params: dict[str, str] = {}
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if limit:
        query_params["limit"] = str(limit)
    if sort:
        query_params["sort"] = str(sort)
    if device_mac:
        query_params["device_mac"] = str(device_mac)
    if src_ip:
        query_params["src_ip"] = str(src_ip)
    if dst_ip:
        query_params["dst_ip"] = str(dst_ip)
    if src_port:
        query_params["src_port"] = str(src_port)
    if dst_port:
        query_params["dst_port"] = str(dst_port)
    if protocol:
        query_params["protocol"] = str(protocol)
    if state:
        query_params["state"] = str(state)
    if direction:
        query_params["direction"] = str(direction)
    if search_after:
        query_params["search_after"] = str(search_after)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
