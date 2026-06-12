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


def listOrgMxEdges(
    mist_session: _APISession,
    org_id: str,
    for_site: str | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/mxedges/list-org-mx-edges

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    for_site : str{'any', 'false', 'true'}, default: any
      Filter for org/site level Mist Edges. enum: `any`, `false`, `true`
    limit : int, default: 100
      Maximum number of results to return per page
    page : int, default: 1
      Select the page number to return when using page-based pagination; starts at `1`

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/mxedges"
    query_params: dict[str, str] = {}
    if for_site:
        query_params["for_site"] = str(for_site)
    if limit:
        query_params["limit"] = str(limit)
    if page:
        query_params["page"] = str(page)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def createOrgMxEdge(
    mist_session: _APISession, org_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/mxedges/create-org-mx-edge

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

    uri = f"/api/v1/orgs/{org_id}/mxedges"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def assignOrgMxEdgeToSite(
    mist_session: _APISession, org_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/mxedges/assign-org-mx-edge-to-site

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

    uri = f"/api/v1/orgs/{org_id}/mxedges/assign"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def claimOrgMxEdge(
    mist_session: _APISession, org_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/mxedges/claim-org-mx-edge

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

    uri = f"/api/v1/orgs/{org_id}/mxedges/claim"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def countOrgMxEdges(
    mist_session: _APISession,
    org_id: str,
    distinct: str | None = None,
    mxedge_id: str | None = None,
    site_id: str | None = None,
    mxcluster_id: str | None = None,
    model: str | None = None,
    distro: str | None = None,
    tunterm_version: str | None = None,
    sort: str | None = None,
    stats: bool | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/mxedges/count-org-mx-edges

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str{'distro', 'model', 'mxcluster_id', 'site_id', 'tunterm_version'}, default: model
      Field used to group this count response. enum: `distro`, `model`, `mxcluster_id`, `site_id`, `tunterm_version`
    mxedge_id : str
      Filter results by Mist Edge identifier
    site_id : str
      Mist edge site id
    mxcluster_id : str
      Mist edge cluster id
    model : str
      Filter results by device model
    distro : str
      Debian code name (buster, bullseye)
    tunterm_version : str
      Filter results by tunnel termination version
    sort : str
      Field used to sort results
    stats : bool
      Whether to return device stats, default is false
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

    uri = f"/api/v1/orgs/{org_id}/mxedges/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if mxedge_id:
        query_params["mxedge_id"] = str(mxedge_id)
    if site_id:
        query_params["site_id"] = str(site_id)
    if mxcluster_id:
        query_params["mxcluster_id"] = str(mxcluster_id)
    if model:
        query_params["model"] = str(model)
    if distro:
        query_params["distro"] = str(distro)
    if tunterm_version:
        query_params["tunterm_version"] = str(tunterm_version)
    if sort:
        query_params["sort"] = str(sort)
    if stats:
        query_params["stats"] = str(stats)
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


def countOrgSiteMxEdgeEvents(
    mist_session: _APISession,
    org_id: str,
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
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/mxedges/count-org-site-mx-edge-events

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str{'mxcluster_id', 'mxedge_id', 'package', 'type'}, default: mxedge_id
      Field used to group this count response. enum: `mxcluster_id`, `mxedge_id`, `package`, `type`
    mxedge_id : str
      Filter results by Mist Edge identifier
    mxcluster_id : str
      Mist edge cluster id
    type : str
      See [List Device Events Definitions](/#operations/listDeviceEventsDefinitions)
    service : str
      Filter results by service name
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

    uri = f"/api/v1/orgs/{org_id}/mxedges/events/count"
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


def searchOrgMistEdgeEvents(
    mist_session: _APISession,
    org_id: str,
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
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/mxedges/search-org-mist-edge-events

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    mxedge_id : str
      Filter results by Mist Edge identifier
    mxcluster_id : str
      Mist edge cluster id
    type : str
      See [List Device Events Definitions](/#operations/listDeviceEventsDefinitions)
    service : str
      Filter results by service name
    component : str
      Filter results by component name
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

    uri = f"/api/v1/orgs/{org_id}/mxedges/events/search"
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


def searchOrgMxEdges(
    mist_session: _APISession,
    org_id: str,
    hostname: str | None = None,
    mxedge_id: str | None = None,
    mxcluster_id: str | None = None,
    model: str | None = None,
    distro: str | None = None,
    tunterm_version: str | None = None,
    site_id: str | None = None,
    stats: bool | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/mxedges/search-org-mx-edges

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    hostname : str
      Partial / full Device hostname. Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `my-london*` and `*london*` match `my-london-1`). Suffix-only wildcards (e.g. `*london-1`) are not supported. Accepts multiple comma-separated values.
    mxedge_id : str
      Filter results by Mist Edge identifier. Accepts multiple comma-separated values.
    mxcluster_id : str
      Mist edge cluster id. Accepts multiple comma-separated values.
    model : str
      Partial / full Device model. Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `AP4*` and `*P4*` match `AP43`). Suffix-only wildcards (e.g. `*43`) are not supported. Accepts multiple comma-separated values.
    distro : str
      Debian code name (buster, bullseye)
    tunterm_version : str
      Filter results by tunnel termination version
    site_id : str
      Mist edge site id
    stats : bool
      Whether to return device stats, default is false
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

    uri = f"/api/v1/orgs/{org_id}/mxedges/search"
    query_params: dict[str, str] = {}
    if hostname:
        query_params["hostname"] = str(hostname)
    if mxedge_id:
        query_params["mxedge_id"] = str(mxedge_id)
    if mxcluster_id:
        query_params["mxcluster_id"] = str(mxcluster_id)
    if model:
        query_params["model"] = str(model)
    if distro:
        query_params["distro"] = str(distro)
    if tunterm_version:
        query_params["tunterm_version"] = str(tunterm_version)
    if site_id:
        query_params["site_id"] = str(site_id)
    if stats:
        query_params["stats"] = str(stats)
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


def unassignOrgMxEdgeFromSite(
    mist_session: _APISession, org_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/mxedges/unassign-org-mx-edge-from-site

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

    uri = f"/api/v1/orgs/{org_id}/mxedges/unassign"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def listOrgMxEdgeUpgrades(mist_session: _APISession, org_id: str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/upgrade/list-org-mx-edge-upgrades

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/mxedges/upgrade"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def upgradeOrgMxEdges(
    mist_session: _APISession, org_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/upgrade/upgrade-org-mx-edges

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

    uri = f"/api/v1/orgs/{org_id}/mxedges/upgrade"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def getOrgMxEdgeUpgrade(
    mist_session: _APISession, org_id: str, upgrade_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/upgrade/get-org-mx-edge-upgrade

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    upgrade_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/mxedges/upgrade/{upgrade_id}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def updateOrgMxEdgeUpgrade(
    mist_session: _APISession, org_id: str, upgrade_id: str, body: dict
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/upgrade/update-org-mx-edge-upgrade

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    upgrade_id : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/mxedges/upgrade/{upgrade_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp


def cancelOrgMxEdgeUpgrade(
    mist_session: _APISession, org_id: str, upgrade_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/upgrade/cancel-org-mx-edge-upgrade

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    upgrade_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/mxedges/upgrade/{upgrade_id}/cancel"
    resp = mist_session.mist_post(uri=uri)
    return resp


def getOrgMxEdgeUpgradeInfo(
    mist_session: _APISession,
    org_id: str,
    channel: str | None = None,
    distro: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/mxedges/get-org-mx-edge-upgrade-info

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    channel : str{'alpha', 'beta', 'stable'}, default: stable
      Upgrade channel used to filter available versions. enum: `alpha`, `beta`, `stable`
    distro : str
      Filter results by distro

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/mxedges/versions"
    query_params: dict[str, str] = {}
    if channel:
        query_params["channel"] = str(channel)
    if distro:
        query_params["distro"] = str(distro)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def getOrgMxEdge(
    mist_session: _APISession, org_id: str, mxedge_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/mxedges/get-org-mx-edge

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    mxedge_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/mxedges/{mxedge_id}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def deleteOrgMxEdge(
    mist_session: _APISession, org_id: str, mxedge_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/mxedges/delete-org-mx-edge

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    mxedge_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/mxedges/{mxedge_id}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp


def updateOrgMxEdge(
    mist_session: _APISession, org_id: str, mxedge_id: str, body: dict
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/mxedges/update-org-mx-edge

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
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

    uri = f"/api/v1/orgs/{org_id}/mxedges/{mxedge_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp


def deleteOrgMxEdgeImage(
    mist_session: _APISession, org_id: str, mxedge_id: str, image_number: int
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/mxedges/delete-org-mx-edge-image

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    mxedge_id : str
    image_number : int

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/mxedges/{mxedge_id}/image/{image_number}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp


def addOrgMxEdgeImageFile(
    mist_session: _APISession,
    org_id: str,
    mxedge_id: str,
    image_number: int,
    file: str | None = None,
    json: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/mxedges/add-org-mx-edge-image

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    mxedge_id : str
    image_number : int

    BODY PARAMS
    -----------
    file : str
        path to the file to upload. Image file content uploaded as multipart form data
    json : str
        Optional JSON metadata submitted with the image upload

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    multipart_form_data = {
        "file": file,
        "json": json,
    }
    uri = f"/api/v1/orgs/{org_id}/mxedges/{mxedge_id}/image/{image_number}"
    resp = mist_session.mist_post_file(uri=uri, multipart_form_data=multipart_form_data)
    return resp


def restartOrgMxEdge(
    mist_session: _APISession, org_id: str, mxedge_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/mxedges/restart-org-mx-edge

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    mxedge_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/mxedges/{mxedge_id}/restart"
    resp = mist_session.mist_post(uri=uri)
    return resp


def bounceOrgMxEdgeDataPorts(
    mist_session: _APISession, org_id: str, mxedge_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/mxedges/bounce-org-mx-edge-data-ports

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
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

    uri = f"/api/v1/orgs/{org_id}/mxedges/{mxedge_id}/services/tunterm/bounce_port"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def disconnectOrgMxEdgeTuntermAps(
    mist_session: _APISession, org_id: str, mxedge_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/mxedges/disconnect-org-mx-edge-tunterm-aps

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
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

    uri = f"/api/v1/orgs/{org_id}/mxedges/{mxedge_id}/services/tunterm/disconnect_aps"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def controlOrgMxEdgeServices(
    mist_session: _APISession, org_id: str, mxedge_id: str, name: str, action: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/mxedges/control-org-mx-edge-services

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    mxedge_id : str
    name : str{'mxagent', 'mxdas', 'mxnacedge', 'mxocproxy', 'radsecproxy', 'tunterm'}
      enum: `mxagent`, `mxdas`, `mxnacedge`, `mxocproxy`, `radsecproxy`, `tunterm`
    action : str{'restart', 'start', 'stop'}
      Restart or start or stop

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/mxedges/{mxedge_id}/services/{name}/{action}"
    resp = mist_session.mist_post(uri=uri)
    return resp


def uploadOrgMxEdgeSupportFiles(
    mist_session: _APISession, org_id: str, mxedge_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/mxedges/upload-org-mx-edge-support-files

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    mxedge_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/mxedges/{mxedge_id}/support"
    resp = mist_session.mist_post(uri=uri)
    return resp


def unregisterOrgMxEdge(
    mist_session: _APISession, org_id: str, mxedge_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/mxedges/unregister-org-mx-edge

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    mxedge_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/mxedges/{mxedge_id}/unregister"
    resp = mist_session.mist_post(uri=uri)
    return resp


def getOrgMxEdgeVmParams(
    mist_session: _APISession, org_id: str, mxedge_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/mxedges/get-org-mx-edge-vm-params

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    mxedge_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/mxedges/{mxedge_id}/vm_params"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
