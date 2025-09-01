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
    distinct: str = "type",
    ack_admin_name: str | None = None,
    acked: bool | None = None,
    type: str | None = None,
    severity: str | None = None,
    group: str | None = None,
    start: int | None = None,
    end: int | None = None,
    duration: str = "1d",
    limit: int = 100,
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
      Group by and count the alarms by some distinct field
    ack_admin_name : str
    acked : bool
    type : str
    severity : str
    group : str
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100

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
    type: str | None = None,
    ack_admin_name: str | None = None,
    acked: bool | None = None,
    severity: str | None = None,
    group: str | None = None,
    limit: int = 100,
    start: int | None = None,
    end: int | None = None,
    duration: str = "1d",
    sort: str = "timestamp",
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
    type : str
    ack_admin_name : str
    acked : bool
    severity : str
    group : str
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

    uri = f"/api/v1/sites/{site_id}/alarms/search"
    query_params: dict[str, str] = {}
    if type:
        query_params["type"] = str(type)
    if ack_admin_name:
        query_params["ack_admin_name"] = str(ack_admin_name)
    if acked:
        query_params["acked"] = str(acked)
    if severity:
        query_params["severity"] = str(severity)
    if group:
        query_params["group"] = str(group)
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
