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


def listSiteWebhooks(
    mist_session: _APISession, site_id: str, limit: int = 100, page: int = 1
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/webhooks/list-site-webhooks

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    limit : int, default: 100
    page : int, default: 1

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/webhooks"
    query_params: dict[str, str] = {}
    if limit:
        query_params["limit"] = str(limit)
    if page:
        query_params["page"] = str(page)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def createSiteWebhook(
    mist_session: _APISession, site_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/webhooks/create-site-webhook

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

    uri = f"/api/v1/sites/{site_id}/webhooks"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def getSiteWebhook(
    mist_session: _APISession, site_id: str, webhook_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/webhooks/get-site-webhook

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    webhook_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/webhooks/{webhook_id}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def deleteSiteWebhook(
    mist_session: _APISession, site_id: str, webhook_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/webhooks/delete-site-webhook

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    webhook_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/webhooks/{webhook_id}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp


def updateSiteWebhook(
    mist_session: _APISession, site_id: str, webhook_id: str, body: dict
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/webhooks/update-site-webhook

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
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

    uri = f"/api/v1/sites/{site_id}/webhooks/{webhook_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp


def countSiteWebhooksDeliveries(
    mist_session: _APISession,
    site_id: str,
    webhook_id: str,
    error: str | None = None,
    status_code: int | None = None,
    status: str | None = None,
    topic: str | None = None,
    distinct: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str = "1d",
    limit: int = 100,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/webhooks/count-site-webhooks-deliveries

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
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
    start : str
    end : str
    duration : str, default: 1d
    limit : int, default: 100

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/webhooks/{webhook_id}/events/count"
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


def searchSiteWebhooksDeliveries(
    mist_session: _APISession,
    site_id: str,
    webhook_id: str,
    error: str | None = None,
    status_code: int | None = None,
    status: str | None = None,
    topic: str | None = None,
    limit: int = 100,
    start: str | None = None,
    end: str | None = None,
    duration: str = "1d",
    sort: str = "timestamp",
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/webhooks/search-site-webhooks-deliveries

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
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
    start : str
    end : str
    duration : str, default: 1d
    sort : str, default: timestamp

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/webhooks/{webhook_id}/events/search"
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


def pingSiteWebhook(
    mist_session: _APISession, site_id: str, webhook_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/webhooks/ping-site-webhook

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    webhook_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/webhooks/{webhook_id}/ping"
    resp = mist_session.mist_post(uri=uri)
    return resp
