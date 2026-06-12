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


def getOrgInventory(
    mist_session: _APISession,
    org_id: str,
    serial: str | None = None,
    model: str | None = None,
    type: str | None = None,
    mac: str | None = None,
    site_id: str | None = None,
    vc_mac: str | None = None,
    vc: bool | None = None,
    unassigned: bool | None = None,
    modified_after: int | None = None,
    disconnected_before: int | None = None,
    limit: int | None = None,
    page: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/inventory/get-org-inventory

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    serial : str
      Filter results by device serial number. Accepts multiple comma-separated values.
    model : str
      Filter results by device model. Accepts multiple comma-separated values.
    type : str
      Filter results by type. enum: `ap`, `gateway`, `switch`. Accepts multiple comma-separated values.
    mac : str
      Filter results by MAC address. Accepts multiple comma-separated values.
    site_id : str
      Filter results by one site identifier. Use a single value; comma-separated values are not supported
    vc_mac : str
      Virtual Chassis MAC address. Accepts multiple comma-separated values.
    vc : bool
      To display Virtual Chassis members
    unassigned : bool, default: True
      To display Unassigned devices
    modified_after : int
      Filter on inventory last modified time, in epoch
    disconnected_before : int
      Filter results to devices that were last disconnected before this time, in epoch seconds
    limit : int, default: 100
      Maximum number of results to return per page
    page : int, default: 1
      Select the page number to return when using page-based pagination; starts at `1`

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/inventory"
    query_params: dict[str, str] = {}
    if serial:
        query_params["serial"] = str(serial)
    if model:
        query_params["model"] = str(model)
    if type:
        query_params["type"] = str(type)
    if mac:
        query_params["mac"] = str(mac)
    if site_id:
        query_params["site_id"] = str(site_id)
    if vc_mac:
        query_params["vc_mac"] = str(vc_mac)
    if vc:
        query_params["vc"] = str(vc)
    if unassigned:
        query_params["unassigned"] = str(unassigned)
    if modified_after:
        query_params["modified_after"] = str(modified_after)
    if disconnected_before:
        query_params["disconnected_before"] = str(disconnected_before)
    if limit:
        query_params["limit"] = str(limit)
    if page:
        query_params["page"] = str(page)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def addOrgInventory(
    mist_session: _APISession, org_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/inventory/add-org-inventory

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

    uri = f"/api/v1/orgs/{org_id}/inventory"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def updateOrgInventoryAssignment(
    mist_session: _APISession, org_id: str, body: dict
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/inventory/update-org-inventory-assignment

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

    uri = f"/api/v1/orgs/{org_id}/inventory"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp


def countOrgInventory(
    mist_session: _APISession,
    org_id: str,
    distinct: str | None = None,
    type: str | None = None,
    site_id: str | None = None,
    model: str | None = None,
    version: str | None = None,
    status: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/inventory/count-org-inventory

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str{'model', 'status', 'site_id', 'sku', 'version'}, default: model
      Field used to group this count response. enum: `model`, `status`, `site_id`, `sku`, `version`
    type : str{'ap', 'gateway', 'switch'}, default: ap
      Filter results by type. enum: `ap`, `gateway`, `switch`
    site_id : str
      Filter results by site identifier
    model : str
      Filter results by device model. Accepts multiple comma-separated values.
    version : str
      Filter results by software version
    status : str{'connected', 'disconnected'}
      Filter results by status. enum: `connected`, `disconnected`
    limit : int, default: 100
      Maximum number of results to return per page

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/inventory/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if type:
        query_params["type"] = str(type)
    if site_id:
        query_params["site_id"] = str(site_id)
    if model:
        query_params["model"] = str(model)
    if version:
        query_params["version"] = str(version)
    if status:
        query_params["status"] = str(status)
    if limit:
        query_params["limit"] = str(limit)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def createOrgGatewayHaCluster(
    mist_session: _APISession, org_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/inventory/create-org-gateway-ha-cluster

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

    uri = f"/api/v1/orgs/{org_id}/inventory/create_ha_cluster"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def deleteOrgGatewayHaCluster(
    mist_session: _APISession, org_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/inventory/delete-org-gateway-ha-cluster

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

    uri = f"/api/v1/orgs/{org_id}/inventory/delete_ha_cluster"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def reevaluateOrgAutoAssignment(mist_session: _APISession, org_id: str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/inventory/reevaluate-org-auto-assignment

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

    uri = f"/api/v1/orgs/{org_id}/inventory/reevaluate_auto_assignment"
    resp = mist_session.mist_post(uri=uri)
    return resp


def replaceOrgDevices(
    mist_session: _APISession, org_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/inventory/replace-org-devices

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

    uri = f"/api/v1/orgs/{org_id}/inventory/replace"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def searchOrgInventory(
    mist_session: _APISession,
    org_id: str,
    type: str | None = None,
    mac: str | None = None,
    model: str | None = None,
    name: str | None = None,
    site_id: str | None = None,
    serial: str | None = None,
    master: str | None = None,
    sku: str | None = None,
    version: str | None = None,
    status: str | None = None,
    text: str | None = None,
    limit: int | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/inventory/search-org-inventory

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    type : str{'ap', 'gateway', 'switch'}, default: ap
      Filter results by type. enum: `ap`, `gateway`, `switch`
    mac : str
      Filter by MAC address. Partial matches may use `*` wildcards (e.g. `*5b35*` matches `5c5b350e0001` and `5c5b35000301`). Accepts multiple comma-separated values.
    model : str
      Partial / full Device model. Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `AP4*` and `*P4*` match `AP43`). Suffix-only wildcards (e.g. `*43`) are not supported. Accepts multiple comma-separated values.
    name : str
      Device name. Always a partial match (e.g. `london` will match `london-1`, `london-2`, `my-london-device`...). Accepts multiple comma-separated values.
    site_id : str
      Filter inventory results by site identifier. Accepts multiple comma-separated values.
    serial : str
      Device serial number. Partial match allowed with wildcard * (e.g. `*123*` will match `AB123CD`, `12345`, `XY123`). Accepts multiple comma-separated values.
    master : str
      Filter inventory results by whether the device is the Virtual Chassis master
    sku : str
      Device SKU. Partial match allowed with wildcard * (e.g. `*2300*` will match `EX2300-F-12P`). Accepts multiple comma-separated values.
    version : str
      Device version. Partial match allowed with wildcard * (e.g. `2R3` will match `21.2R3-S3.5`). Accepts multiple comma-separated values.
    status : str
      Device status. enum: `connected`, `disconnected`. Accepts multiple comma-separated values.
    text : str
      Wildcards for name, mac, serial
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

    uri = f"/api/v1/orgs/{org_id}/inventory/search"
    query_params: dict[str, str] = {}
    if type:
        query_params["type"] = str(type)
    if mac:
        query_params["mac"] = str(mac)
    if model:
        query_params["model"] = str(model)
    if name:
        query_params["name"] = str(name)
    if site_id:
        query_params["site_id"] = str(site_id)
    if serial:
        query_params["serial"] = str(serial)
    if master:
        query_params["master"] = str(master)
    if sku:
        query_params["sku"] = str(sku)
    if version:
        query_params["version"] = str(version)
    if status:
        query_params["status"] = str(status)
    if text:
        query_params["text"] = str(text)
    if limit:
        query_params["limit"] = str(limit)
    if sort:
        query_params["sort"] = str(sort)
    if search_after:
        query_params["search_after"] = str(search_after)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
