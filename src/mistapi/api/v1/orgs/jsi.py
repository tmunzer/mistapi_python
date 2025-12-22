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


def listOrgJsiDevices(
    mist_session: _APISession,
    org_id: str,
    limit: int = 100,
    page: int = 1,
    model: str | None = None,
    serial: str | None = None,
    mac: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/jsi/list-org-jsi-devices

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
    model : str
    serial : str
    mac : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/jsi/devices"
    query_params: dict[str, str] = {}
    if limit:
        query_params["limit"] = str(limit)
    if page:
        query_params["page"] = str(page)
    if model:
        query_params["model"] = str(model)
    if serial:
        query_params["serial"] = str(serial)
    if mac:
        query_params["mac"] = str(mac)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def adoptOrgJsiDevice(mist_session: _APISession, org_id: str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/jsi/adopt-org-jsi-device

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

    uri = f"/api/v1/orgs/{org_id}/jsi/devices/outbound_ssh_cmd"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def createOrgJsiDeviceShellSession(
    mist_session: _APISession, org_id: str, device_mac: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/jsi/create-org-jsi-device-shell-session

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    device_mac : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/jsi/devices/{device_mac}/shell"
    resp = mist_session.mist_post(uri=uri)
    return resp


def upgradeOrgJsiDevice(
    mist_session: _APISession, org_id: str, device_mac: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/upgrade/upgrade-org-jsi-device

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    device_mac : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/jsi/devices/{device_mac}/upgrade"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def listOrgJsiPastPurchases(
    mist_session: _APISession,
    org_id: str,
    limit: int = 100,
    page: int = 1,
    model: str | None = None,
    serial: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/jsi/list-org-jsi-past-purchases

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
    model : str
    serial : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/jsi/inventory"
    query_params: dict[str, str] = {}
    if limit:
        query_params["limit"] = str(limit)
    if page:
        query_params["page"] = str(page)
    if model:
        query_params["model"] = str(model)
    if serial:
        query_params["serial"] = str(serial)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def countOrgJsiAssetsAndContracts(
    mist_session: _APISession,
    org_id: str,
    distinct: str | None = None,
    limit: int = 100,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/jsi/count-org-jsi-assets-and-contracts

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str{'account_id', 'claimed', 'has_support', 'eol_time', 'eos_time', 'version_time', 'model', 'sku', 'status', 'type', 'version', 'warranty_type'}
      Distinct attributes to count
    limit : int, default: 100

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/jsi/inventory/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if limit:
        query_params["limit"] = str(limit)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def searchOrgJsiAssetsAndContracts(
    mist_session: _APISession,
    org_id: str,
    claimed: bool | None = None,
    model: str | None = None,
    serial: str | None = None,
    sku: str | None = None,
    status: str = "all",
    warranty_type: str | None = None,
    eol_duration: str | None = None,
    eos_duration: str | None = None,
    has_support: bool | None = None,
    text: str | None = None,
    limit: int = 100,
    sort: str = "timestamp",
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/jsi/search-org-jsi-assets-and-contracts

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    claimed : bool
    model : str
    serial : str
    sku : str
    status : str{'all', 'connected', 'disconnected'}, default: all
      Device status
    warranty_type : str{'Standard Hardware Warranty', 'Enhanced Hardware Warranty', 'Dead On Arrival Warranty', 'Limited Lifetime Warranty', 'Software Warranty', 'Limited Lifetime Warranty for WLA', 'Warranty-JCPO EOL (DOA Not Included)', 'MIST Enhanced Hardware Warranty', 'MIST Standard Warranty', 'Determine Lifetime warranty'}
      Device warranty type
    eol_duration : str
    eos_duration : str
    has_support : bool
    text : str
    limit : int, default: 100
    sort : str, default: timestamp
    search_after : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/jsi/inventory/search"
    query_params: dict[str, str] = {}
    if claimed:
        query_params["claimed"] = str(claimed)
    if model:
        query_params["model"] = str(model)
    if serial:
        query_params["serial"] = str(serial)
    if sku:
        query_params["sku"] = str(sku)
    if status:
        query_params["status"] = str(status)
    if warranty_type:
        query_params["warranty_type"] = str(warranty_type)
    if eol_duration:
        query_params["eol_duration"] = str(eol_duration)
    if eos_duration:
        query_params["eos_duration"] = str(eos_duration)
    if has_support:
        query_params["has_support"] = str(has_support)
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
