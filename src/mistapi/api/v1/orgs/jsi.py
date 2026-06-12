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
    limit: int | None = None,
    page: int | None = None,
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
      Maximum number of results to return per page
    page : int, default: 1
      Select the page number to return when using page-based pagination; starts at `1`
    model : str
      Filter results by device model
    serial : str
      Filter results by device serial number
    mac : str
      Filter results by MAC address

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
    limit: int | None = None,
    page: int | None = None,
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
      Maximum number of results to return per page
    page : int, default: 1
      Select the page number to return when using page-based pagination; starts at `1`
    model : str
      Filter results by one or more device models. Supports comma-separated values
    serial : str
      Filter results by device serial number

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
    limit: int | None = None,
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
    distinct : str{'account_id', 'claimed', 'has_support', 'end_of_sale_time', 'eos_time', 'version_time', 'model', 'sku', 'status', 'type', 'version', 'warranty_type'}
      Field used to group this count response. enum: `account_id`, `claimed`, `has_support`, `end_of_sale_time`, `eos_time`, `version_time`, `model`, `sku`, `status`, `type`, `version`, `warranty_type`
    limit : int, default: 100
      Maximum number of results to return per page

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
    status: str | None = None,
    warranty_type: str | None = None,
    end_of_sale_after: str | None = None,
    end_of_sale_before: str | None = None,
    eos_after: str | None = None,
    eos_before: str | None = None,
    version_eos_after: str | None = None,
    version_eos_before: str | None = None,
    has_support: bool | None = None,
    sirt_id: str | None = None,
    pbn_id: str | None = None,
    text: str | None = None,
    limit: int | None = None,
    sort: str | None = None,
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
      Device claim status, `true` for claimed devices, `false` for all devices. Accepts multiple comma-separated boolean values.
    model : str
      Filter results by device model. Accepts multiple comma-separated values.
    serial : str
      Filter results by device serial number. Accepts multiple comma-separated values.
    sku : str
      Filter results by SKU. Accepts multiple comma-separated values.
    status : str{'all', 'connected', 'disconnected'}, default: all
      Device status. enum: `all`, `connected`, `disconnected`
    warranty_type : str{'Standard Hardware Warranty', 'Enhanced Hardware Warranty', 'Dead On Arrival Warranty', 'Limited Lifetime Warranty', 'Software Warranty', 'Limited Lifetime Warranty for WLA', 'Warranty-JCPO EOL (DOA Not Included)', 'MIST Enhanced Hardware Warranty', 'MIST Standard Warranty', 'Determine Lifetime warranty'}
      Device warranty type used to filter Juniper Support Insight inventory. enum: `Standard Hardware Warranty`, `Enhanced Hardware Warranty`, `Dead On Arrival Warranty`, `Limited Lifetime Warranty`, `Software Warranty`, `Limited Lifetime Warranty for WLA`, `Warranty-JCPO EOL (DOA Not Included)`, `MIST Enhanced Hardware Warranty`, `MIST Standard Warranty`, `Determine Lifetime warranty`
    end_of_sale_after : str
      Filter devices with End Of Sale date after this date
    end_of_sale_before : str
      Filter devices with End Of Sale date before this date
    eos_after : str
      Filter devices with End Of Support date after this date
    eos_before : str
      Filter devices with End Of Support date before this date
    version_eos_after : str
      Filter devices with OS Version End Of Support date after this date
    version_eos_before : str
      Filter devices with OS Version End Of Support date before this date
    has_support : bool
      Indicates if the device is covered under active support contract. Accepts multiple comma-separated boolean values.
    sirt_id : str
      To get the onboarded devices that are affected by the SIRT ID
    pbn_id : str
      To get the onboarded devices that are affected by the PBN ID
    text : str
      Wildcards for `serial`, `model`, `account_id`
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
    if end_of_sale_after:
        query_params["end_of_sale_after"] = str(end_of_sale_after)
    if end_of_sale_before:
        query_params["end_of_sale_before"] = str(end_of_sale_before)
    if eos_after:
        query_params["eos_after"] = str(eos_after)
    if eos_before:
        query_params["eos_before"] = str(eos_before)
    if version_eos_after:
        query_params["version_eos_after"] = str(version_eos_after)
    if version_eos_before:
        query_params["version_eos_before"] = str(version_eos_before)
    if has_support:
        query_params["has_support"] = str(has_support)
    if sirt_id:
        query_params["sirt_id"] = str(sirt_id)
    if pbn_id:
        query_params["pbn_id"] = str(pbn_id)
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


def countOrgJsiPbn(
    mist_session: _APISession,
    org_id: str,
    distinct: str,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/jsi/count-org-jsi-pbn

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str{'versions', 'models', 'customer_risk', 'bug_type'}
      Field to group by enum: `versions`, `models`, `customer_risk`, `bug_type`
    limit : int, default: 100
      Maximum number of results to return per page
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/jsi/pbn/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if limit:
        query_params["limit"] = str(limit)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def searchOrgJsiPbn(
    mist_session: _APISession,
    org_id: str,
    versions: str | None = None,
    models: str | None = None,
    customer_risk: str | None = None,
    id: str | None = None,
    bug_type: str | None = None,
    limit: int | None = None,
    page: int | None = None,
    search_after: str | None = None,
    start: str | None = None,
    end: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/jsi/search-org-jsi-pbn

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    versions : str
      OS versions to search for
    models : str
      Device models to search for
    customer_risk : str
      Customer risk level to filter by
    id : str
      PBN ID to search for
    bug_type : str
      Bug type to filter by
    limit : int, default: 100
      Maximum number of results to return per page
    page : int, default: 1
      Select the page number to return when using page-based pagination; starts at `1`
    search_after : str
      Pagination cursor for retrieving subsequent pages of results. This value is automatically populated by Mist in the `next` URL from the previous response and should not be manually constructed.
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/jsi/pbn/search"
    query_params: dict[str, str] = {}
    if versions:
        query_params["versions"] = str(versions)
    if models:
        query_params["models"] = str(models)
    if customer_risk:
        query_params["customer_risk"] = str(customer_risk)
    if id:
        query_params["id"] = str(id)
    if bug_type:
        query_params["bug_type"] = str(bug_type)
    if limit:
        query_params["limit"] = str(limit)
    if page:
        query_params["page"] = str(page)
    if search_after:
        query_params["search_after"] = str(search_after)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def countOrgJsiSirt(
    mist_session: _APISession,
    org_id: str,
    distinct: str,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/jsi/count-org-jsi-sirt

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str{'versions', 'models', 'severity', 'jsa_updated_date'}
      Field to group by. enum: `jsa_updated_date`, `models`, `severity`, `versions`
    limit : int, default: 100
      Maximum number of results to return per page
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/jsi/sirt/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if limit:
        query_params["limit"] = str(limit)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def searchOrgJsiSirt(
    mist_session: _APISession,
    org_id: str,
    severity: str | None = None,
    id: str | None = None,
    updated_after: str | None = None,
    updated_before: str | None = None,
    published_after: str | None = None,
    published_before: str | None = None,
    models: str | None = None,
    versions: str | None = None,
    text: str | None = None,
    limit: int | None = None,
    page: int | None = None,
    sort: str | None = None,
    search_after: str | None = None,
    start: str | None = None,
    end: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/jsi/search-org-jsi-sirt

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    severity : str
      Filter results by severity
    id : str
      Filter results by identifier
    updated_after : str
      JSA Updated date to be filtered after this date
    updated_before : str
      JSA Updated date to be filtered before this date
    published_after : str
      JSA Published date to be filtered after this date
    published_before : str
      JSA Published date to be filtered before this date
    models : str
      Filter results by models
    versions : str
      Software version affected by the SIRT
    text : str
      Wildcards search on os_version_affected, affected_models, severity, jsa_id
    limit : int, default: 100
      Maximum number of results to return per page
    page : int, default: 1
      Select the page number to return when using page-based pagination; starts at `1`
    sort : str, default: timestamp
      On which field the list should be sorted, -prefix represents DESC order
    search_after : str
      Pagination cursor for retrieving subsequent pages of results. This value is automatically populated by Mist in the `next` URL from the previous response and should not be manually constructed.
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/jsi/sirt/search"
    query_params: dict[str, str] = {}
    if severity:
        query_params["severity"] = str(severity)
    if id:
        query_params["id"] = str(id)
    if updated_after:
        query_params["updated_after"] = str(updated_after)
    if updated_before:
        query_params["updated_before"] = str(updated_before)
    if published_after:
        query_params["published_after"] = str(published_after)
    if published_before:
        query_params["published_before"] = str(published_before)
    if models:
        query_params["models"] = str(models)
    if versions:
        query_params["versions"] = str(versions)
    if text:
        query_params["text"] = str(text)
    if limit:
        query_params["limit"] = str(limit)
    if page:
        query_params["page"] = str(page)
    if sort:
        query_params["sort"] = str(sort)
    if search_after:
        query_params["search_after"] = str(search_after)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
