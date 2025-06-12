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
    port_id : str
    vlan_id : str
    by : str
    reason : str
    type : str{'arp', 'curl', 'dhcp', 'dhcp6', 'dns', 'lan_connectivity', 'radius', 'speedtest'}
      Synthetic test type
    protocol : str{'ping', 'traceroute'}
      Connectivity protocol
    tenant : str

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
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
