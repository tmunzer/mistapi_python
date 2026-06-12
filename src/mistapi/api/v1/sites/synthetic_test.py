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


def triggerSiteSyntheticTest(
    mist_session: _APISession, site_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/synthetic-tests/trigger-site-synthetic-test

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/synthetic_test"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def searchSiteSyntheticTest(
    mist_session: _APISession,
    site_id: str,
    mac: str | None = None,
    port_id: str | None = None,
    vlan_id: str | None = None,
    by: str | None = None,
    reason: str | None = None,
    type: str | None = None,
    protocol: str | None = None,
    tenant: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/synthetic-tests/search-site-synthetic-test

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
    port_id : str
      Filter results by port identifier
    vlan_id : str
      Filter results by VLAN ID
    by : str
      Entity who triggers the test
    reason : str
      Filter results by reason
    type : str{'arp', 'curl', 'dhcp', 'dhcp6', 'dns', 'lan_connectivity', 'radius', 'speedtest'}
      Synthetic test type used to filter results. enum: `arp`, `curl`, `dhcp`, `dhcp6`, `dns`, `lan_connectivity`, `radius`, `speedtest`
    protocol : str{'ping', 'traceroute'}
      Connectivity protocol used to filter synthetic test results. enum: `ping`, `traceroute`
    tenant : str
      Filter results by tenant network
    limit : int, default: 100
      Maximum number of results to return per page
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    duration : str, default: 1d
      Time range duration for the query, using relative units such as `10m`, `7d`, or `2w`
    search_after : str
      Pagination cursor for retrieving subsequent pages of results. This value is automatically populated by Mist in the `next` URL from the previous response and should not be manually constructed.

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/synthetic_test/search"
    query_params: dict[str, str] = {}
    if mac:
        query_params["mac"] = str(mac)
    if port_id:
        query_params["port_id"] = str(port_id)
    if vlan_id:
        query_params["vlan_id"] = str(vlan_id)
    if by:
        query_params["by"] = str(by)
    if reason:
        query_params["reason"] = str(reason)
    if type:
        query_params["type"] = str(type)
    if protocol:
        query_params["protocol"] = str(protocol)
    if tenant:
        query_params["tenant"] = str(tenant)
    if limit:
        query_params["limit"] = str(limit)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if duration:
        query_params["duration"] = str(duration)
    if search_after:
        query_params["search_after"] = str(search_after)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
