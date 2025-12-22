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
    unassigned: bool = False,
    modified_after: int | None = None,
    limit: int = 100,
    page: int = 1,
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
    model : str
    type : str{'ap', 'gateway', 'switch'}
    mac : str
    site_id : str
    vc_mac : str
    vc : bool
    unassigned : bool, default: True
    modified_after : int
    limit : int, default: 100
    page : int, default: 1

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
    type: str = "ap",
    distinct: str = "model",
    limit: int = 100,
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
    type : str{'ap', 'gateway', 'switch'}, default: ap
    distinct : str{'model', 'status', 'site_id', 'sku', 'version'}, default: model
    limit : int, default: 100

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/inventory/count"
    query_params: dict[str, str] = {}
    if type:
        query_params["type"] = str(type)
    if distinct:
        query_params["distinct"] = str(distinct)
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
    type: str = "ap",
    mac: str | None = None,
    vc_mac: str | None = None,
    master_mac: str | None = None,
    site_id: str | None = None,
    serial: str | None = None,
    master: str | None = None,
    sku: str | None = None,
    version: str | None = None,
    status: str | None = None,
    text: str | None = None,
    limit: int = 100,
    sort: str = "timestamp",
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
    mac : str
    vc_mac : str
    master_mac : str
    site_id : str
    serial : str
    master : str
    sku : str
    version : str
    status : str
    text : str
    limit : int, default: 100
    sort : str, default: timestamp
    search_after : str

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
    if vc_mac:
        query_params["vc_mac"] = str(vc_mac)
    if master_mac:
        query_params["master_mac"] = str(master_mac)
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
