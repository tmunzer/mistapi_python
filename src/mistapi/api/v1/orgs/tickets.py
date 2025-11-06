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


def listOrgTickets(
    mist_session: _APISession,
    org_id: str,
    start: str | None = None,
    end: str | None = None,
    duration: str = "1d",
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/tickets/list-org-tickets

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    start : str
    end : str
    duration : str, default: 1d

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/tickets"
    query_params: dict[str, str] = {}
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if duration:
        query_params["duration"] = str(duration)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def createOrgTicket(
    mist_session: _APISession, org_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/tickets/create-org-ticket

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

    uri = f"/api/v1/orgs/{org_id}/tickets"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def countOrgTickets(
    mist_session: _APISession, org_id: str, distinct: str = "status", limit: int = 100
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/tickets/count-org-tickets

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str{'status', 'type'}, default: status
    limit : int, default: 100

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/tickets/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if limit:
        query_params["limit"] = str(limit)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def getOrgTicket(
    mist_session: _APISession,
    org_id: str,
    ticket_id: str,
    start: str | None = None,
    end: str | None = None,
    duration: str = "1d",
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/tickets/get-org-ticket

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    ticket_id : str

    QUERY PARAMS
    ------------
    start : str
    end : str
    duration : str, default: 1d

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/tickets/{ticket_id}"
    query_params: dict[str, str] = {}
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if duration:
        query_params["duration"] = str(duration)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def updateOrgTicket(
    mist_session: _APISession, org_id: str, ticket_id: str, body: dict
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/tickets/update-org-ticket

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    ticket_id : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/tickets/{ticket_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp


def UploadOrgTicketAttachmentFile(
    mist_session: _APISession, org_id: str, ticket_id: str, file: str | None = None
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/tickets/upload-org-ticket-attachment

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    ticket_id : str

    BODY PARAMS
    -----------
    file : str
        path to the file to upload. Ekahau or ibwave file

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    multipart_form_data = {
        "file": file,
    }
    uri = f"/api/v1/orgs/{org_id}/tickets/{ticket_id}/attachments"
    resp = mist_session.mist_post_file(uri=uri, multipart_form_data=multipart_form_data)
    return resp


def GetOrgTicketAttachment(
    mist_session: _APISession,
    org_id: str,
    ticket_id: str,
    attachment_id: str,
    start: str | None = None,
    end: str | None = None,
    duration: str = "1d",
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/tickets/get-org-ticket-attachment

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    ticket_id : str
    attachment_id : str

    QUERY PARAMS
    ------------
    start : str
    end : str
    duration : str, default: 1d

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/tickets/{ticket_id}/attachments/{attachment_id}"
    query_params: dict[str, str] = {}
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    if duration:
        query_params["duration"] = str(duration)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def addOrgTicketCommentFile(
    mist_session: _APISession,
    org_id: str,
    ticket_id: str,
    comment: str | None = None,
    file: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/tickets/add-org-ticket-comment

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    ticket_id : str

    BODY PARAMS
    -----------
    comment : str
    file : str
        path to the file to upload.

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    multipart_form_data = {
        "comment": comment,
        "file": file,
    }
    uri = f"/api/v1/orgs/{org_id}/tickets/{ticket_id}/comments"
    resp = mist_session.mist_post_file(uri=uri, multipart_form_data=multipart_form_data)
    return resp


def addOrgTicketComment(
    mist_session: _APISession, org_id: str, ticket_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/tickets/add-org-ticket-comment

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    ticket_id : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/tickets/{ticket_id}/comments"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
