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


def listOrgWebhooks(
    mist_session: _APISession, org_id: str, limit: int = 100, page: int = 1
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/webhooks/list-org-webhooks

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    limit : int, default: 100
    page : int, default: 1

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/webhooks"
    query_params: dict[str, str] = {}
    if limit:
        query_params["limit"] = str(limit)
    if page:
        query_params["page"] = str(page)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def createOrgWebhook(
    mist_session: _APISession, org_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/webhooks/create-org-webhook

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/webhooks"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def getOrgWebhook(
    mist_session: _APISession, org_id: str, webhook_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/webhooks/get-org-webhook

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    webhook_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/webhooks/{webhook_id}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def deleteOrgWebhook(
    mist_session: _APISession, org_id: str, webhook_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/webhooks/delete-org-webhook

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    webhook_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/webhooks/{webhook_id}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp


def updateOrgWebhook(
    mist_session: _APISession, org_id: str, webhook_id: str, body: dict
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/webhooks/update-org-webhook

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    webhook_id : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/webhooks/{webhook_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp


def countOrgWebhooksDeliveries(
    mist_session: _APISession,
    org_id: str,
    webhook_id: str,
    error: str | None = None,
    status_code: int | None = None,
    status: str | None = None,
    topic: str | None = None,
    distinct: str | None = None,
    start: int | None = None,
    end: int | None = None,
    duration: str = "1d",
    limit: int = 100,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/webhooks/count-org-webhooks-deliveries

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    webhook_id : str

    QUERY PARAMS
    ------------
    error : str
    status_code : int
    status : str{'failure', 'success'}
      Webhook delivery status
    topic : str{'alarms', 'audits', 'device-updowns', 'occupancy-alerts', 'ping'}
      Webhook topic
    distinct : str{'status', 'status_code', 'topic', 'webhook_id'}
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/webhooks/{webhook_id}/events/count"
    query_params: dict[str, str] = {}
    if error:
        query_params["error"] = str(error)
    if status_code:
        query_params["status_code"] = str(status_code)
    if status:
        query_params["status"] = str(status)
    if topic:
        query_params["topic"] = str(topic)
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


def searchOrgWebhooksDeliveries(
    mist_session: _APISession,
    org_id: str,
    webhook_id: str,
    error: str | None = None,
    status_code: int | None = None,
    status: str | None = None,
    topic: str | None = None,
    limit: int = 100,
    start: int | None = None,
    end: int | None = None,
    duration: str = "1d",
    sort: str = "timestamp",
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/webhooks/search-org-webhooks-deliveries

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    webhook_id : str

    QUERY PARAMS
    ------------
    error : str
    status_code : int
    status : str{'failure', 'success'}
      Webhook delivery status
    topic : str{'alarms', 'audits', 'device-updowns', 'occupancy-alerts', 'ping'}
      Webhook topic
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

    uri = f"/api/v1/orgs/{org_id}/webhooks/{webhook_id}/events/search"
    query_params: dict[str, str] = {}
    if error:
        query_params["error"] = str(error)
    if status_code:
        query_params["status_code"] = str(status_code)
    if status:
        query_params["status"] = str(status)
    if topic:
        query_params["topic"] = str(topic)
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


def pingOrgWebhook(
    mist_session: _APISession, org_id: str, webhook_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/webhooks/ping-org-webhook

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    webhook_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/webhooks/{webhook_id}/ping"
    resp = mist_session.mist_post(uri=uri)
    return resp
