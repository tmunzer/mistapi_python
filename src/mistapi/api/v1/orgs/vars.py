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


def searchOrgVars(
    mist_session: _APISession,
    org_id: str,
    site_id: str | None = None,
    var: str | None = None,
    src: str | None = None,
    limit: int | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/vars/search-org-vars

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    site_id : str
      Filter results by site identifier. Accepts multiple comma-separated values.
    var : str
      Filter variable results by variable name. Accepts multiple comma-separated values.
    src : str{'deviceprofile', 'site'}
      Filter results by source. enum: `deviceprofile`, `site`
    limit : int, default: 100
      Maximum number of results to return per page
    sort : str, default: timestamp
      On which field the list should be sorted, -prefix represents DESC order
    search_after : str
      Pagination cursor for retrieving subsequent pages of results. This value is automatically populated by Mist in the `next` URL from the previous response and should not be manually constructed.

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/vars/search"
    query_params: dict[str, str] = {}
    if site_id:
        query_params["site_id"] = str(site_id)
    if var:
        query_params["var"] = str(var)
    if src:
        query_params["src"] = str(src)
    if limit:
        query_params["limit"] = str(limit)
    if sort:
        query_params["sort"] = str(sort)
    if search_after:
        query_params["search_after"] = str(search_after)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
