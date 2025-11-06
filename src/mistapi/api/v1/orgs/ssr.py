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


def getOrg128TRegistrationCommands(
    mist_session: _APISession,
    org_id: str,
    ttl: int | None = None,
    asset_ids: list | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/devices/ssr/get-org128-t-registration-commands

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    ttl : int
    asset_ids : list
      When specified, only specified assets are allowed for registration. This parameter can and is preferred to be set in HTTP body, especially when the list is long, so that HTTP header size will never exceed limit.

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/128routers/register_cmd"
    query_params: dict[str, str] = {}
    if ttl:
        query_params["ttl"] = str(ttl)
    if asset_ids:
        query_params["asset_ids"] = str(asset_ids)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def listOrgSsrUpgrades(mist_session: _APISession, org_id: str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/upgrade/list-org-ssr-upgrades

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

    uri = f"/api/v1/orgs/{org_id}/ssr/upgrade"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def upgradeOrgSsrs(
    mist_session: _APISession, org_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/upgrade/upgrade-org-ssrs

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

    uri = f"/api/v1/orgs/{org_id}/ssr/upgrade"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def getOrgSsrUpgrade(
    mist_session: _APISession, org_id: str, upgrade_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/upgrade/get-org-ssr-upgrade

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

    uri = f"/api/v1/orgs/{org_id}/ssr/upgrade/{upgrade_id}/cancel"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def cancelOrgSsrUpgrade(
    mist_session: _APISession, org_id: str, upgrade_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/upgrade/cancel-org-ssr-upgrade

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

    uri = f"/api/v1/orgs/{org_id}/ssr/upgrade/{upgrade_id}/cancel"
    resp = mist_session.mist_post(uri=uri)
    return resp


def listOrgAvailableSsrVersions(
    mist_session: _APISession,
    org_id: str,
    channel: str = "stable",
    mac: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/utilities/upgrade/list-org-available-ssr-versions

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
      SSR version channel
    mac : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/ssr/versions"
    query_params: dict[str, str] = {}
    if channel:
        query_params["channel"] = str(channel)
    if mac:
        query_params["mac"] = str(mac)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
