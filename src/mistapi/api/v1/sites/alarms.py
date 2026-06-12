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


def AckSiteMultipleAlarms(
    mist_session: _APISession, site_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/alarms/ack-site-multiple-alarms

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

    uri = f"/api/v1/sites/{site_id}/alarms/ack"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def ackSiteAllAlarms(
    mist_session: _APISession, site_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/alarms/ack-site-all-alarms

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

    uri = f"/api/v1/sites/{site_id}/alarms/ack_all"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def countSiteAlarms(
    mist_session: _APISession,
    site_id: str,
    distinct: str | None = None,
    ack_admin_name: str | None = None,
    acked: bool | None = None,
    type: str | None = None,
    severity: str | None = None,
    group: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/alarms/count-site-alarms

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    distinct : str{'acked', 'group', 'severity', 'type'}, default: type
      Field used to group this count response. enum: `acked`, `group`, `severity`, `type`
    ack_admin_name : str
      Name of the admins who have acked the alarms; accepts multiple values separated by comma
    acked : bool
      Filter alarm results by whether the alarm has been acknowledged
    type : str
      Key-name of the alarms; accepts multiple values separated by comma
    severity : str
      Alarm severity; accepts multiple values separated by comma
    group : str
      Alarm group name; accepts multiple values separated by comma
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

    uri = f"/api/v1/sites/{site_id}/alarms/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if ack_admin_name:
        query_params["ack_admin_name"] = str(ack_admin_name)
    if acked:
        query_params["acked"] = str(acked)
    if type:
        query_params["type"] = str(type)
    if severity:
        query_params["severity"] = str(severity)
    if group:
        query_params["group"] = str(group)
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


def searchSiteAlarms(
    mist_session: _APISession,
    site_id: str,
    group: str | None = None,
    severity: str | None = None,
    type: str | None = None,
    ack_admin_name: str | None = None,
    acked: bool | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/alarms/search-site-alarms

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    group : str{'certificate_expiry', 'infrastructure', 'marvis', 'security'}
      Alarm group used to filter alarm results. enum: `certificate_expiry`, `infrastructure`, `marvis`, `security`. The `marvis` group is used to retrieve AI-driven network issue detections. Known Marvis alarm types include: `bad_cable`, `bad_wan_uplink`, `dns_failure`, `arp_failure`, `auth_failure`, `dhcp_failure`, `missing_vlan`, `negotiation_mismatch`, `port_flap`. Results include resolution status (`status`, `resolved_time`) and affected entity details.
    severity : str{'critical', 'info', 'warn'}
      Alarm severity used to filter results. enum: `critical`, `info`, `warn`
    type : str
      Filter alarms by alarm type. Accepts multiple values separated by comma. Use [List Alarm Definitions](/#operations/listAlarmDefinitions) to get the list of possible alarm types
    ack_admin_name : str
      Name of the admins who have acked the alarms; accepts multiple values separated by comma
    acked : bool
      Filter alarm results by whether the alarm has been acknowledged
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

    uri = f"/api/v1/sites/{site_id}/alarms/search"
    query_params: dict[str, str] = {}
    if group:
        query_params["group"] = str(group)
    if severity:
        query_params["severity"] = str(severity)
    if type:
        query_params["type"] = str(type)
    if ack_admin_name:
        query_params["ack_admin_name"] = str(ack_admin_name)
    if acked:
        query_params["acked"] = str(acked)
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


def unackSiteMultipleAlarms(
    mist_session: _APISession, site_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/alarms/unack-site-multiple-alarms

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

    uri = f"/api/v1/sites/{site_id}/alarms/unack"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def unackSiteAllAlarms(
    mist_session: _APISession, site_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/alarms/unack-site-all-alarms

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

    uri = f"/api/v1/sites/{site_id}/alarms/unack_all"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def ackSiteAlarm(
    mist_session: _APISession, site_id: str, alarm_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/alarms/ack-site-alarm

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    alarm_id : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/alarms/{alarm_id}/ack"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def unackSiteAlarm(
    mist_session: _APISession, site_id: str, alarm_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/alarms/unack-site-alarm

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    alarm_id : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/alarms/{alarm_id}/unack"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
