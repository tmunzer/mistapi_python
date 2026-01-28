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


def listSiteMxEdges(
    mist_session: _APISession,
    site_id: str,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/mxedges/list-site-mx-edges

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

    uri = f"/api/v1/sites/{site_id}/mxedges"
    query_params: dict[str, str] = {}
    if limit:
        query_params["limit"] = str(limit)
    if page:
        query_params["page"] = str(page)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def countSiteMxEdgeEvents(
    mist_session: _APISession,
    site_id: str,
    distinct: str | None = None,
    mxedge_id: str | None = None,
    mxcluster_id: str | None = None,
    type: str | None = None,
    service: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/mxedges/count-site-mx-edge-events

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    distinct : str{'mxcluster_id', 'mxedge_id', 'package', 'type'}, default: mxedge_id
    mxedge_id : str
    mxcluster_id : str
    type : str
    service : str
    start : str
    end : str
    duration : str, default: 1d
    limit : int, default: 100

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/mxedges/events/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if mxedge_id:
        query_params["mxedge_id"] = str(mxedge_id)
    if mxcluster_id:
        query_params["mxcluster_id"] = str(mxcluster_id)
    if type:
        query_params["type"] = str(type)
    if service:
        query_params["service"] = str(service)
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


def searchSiteMistEdgeEvents(
    mist_session: _APISession,
    site_id: str,
    mxedge_id: str | None = None,
    mxcluster_id: str | None = None,
    type: str | None = None,
    service: str | None = None,
    component: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/mxedges/search-site-mist-edge-events

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    mxedge_id : str
    mxcluster_id : str
    type : str
    service : str
    component : str
    limit : int, default: 10
    start : str
    end : str
    duration : str, default: 1d
    sort : str, default: timestamp
    search_after : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/mxedges/events/search"
    query_params: dict[str, str] = {}
    if mxedge_id:
        query_params["mxedge_id"] = str(mxedge_id)
    if mxcluster_id:
        query_params["mxcluster_id"] = str(mxcluster_id)
    if type:
        query_params["type"] = str(type)
    if service:
        query_params["service"] = str(service)
    if component:
        query_params["component"] = str(component)
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


def getSiteMxEdge(
    mist_session: _APISession, site_id: str, mxedge_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/mxedges/get-site-mx-edge

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    mxedge_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/mxedges/{mxedge_id}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def deleteSiteMxEdge(
    mist_session: _APISession, site_id: str, mxedge_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/mxedges/delete-site-mx-edge

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    mxedge_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/mxedges/{mxedge_id}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp


def updateSiteMxEdge(
    mist_session: _APISession, site_id: str, mxedge_id: str, body: dict
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/mxedges/update-site-mx-edge

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    mxedge_id : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/mxedges/{mxedge_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp


def uploadSiteMxEdgeSupportFiles(
    mist_session: _APISession, site_id: str, mxedge_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/mxedges/upload-site-mx-edge-support-files

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    mxedge_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/mxedges/{mxedge_id}/support"
    resp = mist_session.mist_post(uri=uri)
    return resp
