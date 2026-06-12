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


def countSiteMarvisConfigActions(
    mist_session: _APISession,
    site_id: str,
    distinct: str | None = None,
    mac: str | None = None,
    type: str | None = None,
    src: str | None = None,
    admin_id: str | None = None,
    op: str | None = None,
    port_id: str | None = None,
    vlan_ids: int | None = None,
    reason: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/marvis-configs/count-site-marvis-config-actions

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    distinct : str, default: mac
      Field to count by. enum: `mac`, `type`, `src`, `admin_id`, `op`, `port_id`, `reason`, `vlan_ids`
    mac : str
      Filter by device MAC address
    type : str
      Filter by config type (e.g. wired)
    src : str
      Filter by source of the config action (e.g. marvis)
    admin_id : str
      Filter by admin ID
    op : str
      Filter by operation type (e.g. disable_port, enable_port, update_mtu, add_vlans_to_port)
    port_id : str
      Filter by port identifier (e.g. ge-0/0/13)
    vlan_ids : int
      Filter by VLAN ID
    reason : str
      Filter by reason for the config action (e.g. rogue_dhcp_server_detected)
    limit : int, default: 100
      Maximum number of results to return per page
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    duration : str, default: 1d
      Time range duration for the query, using relative units such as `10m`, `7d`, or `2w`

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/marvis_configs/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if mac:
        query_params["mac"] = str(mac)
    if type:
        query_params["type"] = str(type)
    if src:
        query_params["src"] = str(src)
    if admin_id:
        query_params["admin_id"] = str(admin_id)
    if op:
        query_params["op"] = str(op)
    if port_id:
        query_params["port_id"] = str(port_id)
    if vlan_ids:
        query_params["vlan_ids"] = str(vlan_ids)
    if reason:
        query_params["reason"] = str(reason)
    if limit:
        query_params["limit"] = str(limit)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if duration:
        query_params["duration"] = str(duration)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def searchSiteMarvisConfigActions(
    mist_session: _APISession,
    site_id: str,
    mac: str | None = None,
    type: str | None = None,
    src: str | None = None,
    admin_id: str | None = None,
    op: str | None = None,
    port_id: str | None = None,
    vlan_ids: int | None = None,
    reason: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/marvis-configs/search-site-marvis-config-actions

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
      Filter by device MAC address
    type : str
      Filter by config type (e.g. wired)
    src : str
      Filter by source of the config action (e.g. marvis)
    admin_id : str
      Filter by admin ID
    op : str
      Filter by operation type (e.g. disable_port, enable_port, update_mtu, add_vlans_to_port)
    port_id : str
      Filter by port identifier (e.g. ge-0/0/13)
    vlan_ids : int
      Filter by VLAN ID
    reason : str
      Filter by reason for the config action (e.g. rogue_dhcp_server_detected)
    limit : int, default: 100
      Maximum number of results to return per page
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    duration : str, default: 1d
      Time range duration for the query, using relative units such as `10m`, `7d`, or `2w`

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/marvis_configs/search"
    query_params: dict[str, str] = {}
    if mac:
        query_params["mac"] = str(mac)
    if type:
        query_params["type"] = str(type)
    if src:
        query_params["src"] = str(src)
    if admin_id:
        query_params["admin_id"] = str(admin_id)
    if op:
        query_params["op"] = str(op)
    if port_id:
        query_params["port_id"] = str(port_id)
    if vlan_ids:
        query_params["vlan_ids"] = str(vlan_ids)
    if reason:
        query_params["reason"] = str(reason)
    if limit:
        query_params["limit"] = str(limit)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if duration:
        query_params["duration"] = str(duration)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def deleteSiteMarvisConfigAction(
    mist_session: _APISession, site_id: str, id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/marvis-configs/delete-site-marvis-config-action

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    id : str
      UUID of the Marvis Config Action

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/marvis_configs/{id}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp


def submitSiteMarvisConfigFeedback(
    mist_session: _APISession, site_id: str, id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/marvis-configs/submit-site-marvis-config-feedback

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    id : str
      UUID of the Marvis Config Action

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/marvis_configs/{id}/feedback"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
