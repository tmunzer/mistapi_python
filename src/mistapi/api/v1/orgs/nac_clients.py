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


def countOrgNacClients(
    mist_session: _APISession,
    org_id: str,
    distinct: str | None = None,
    last_nacrule_id: str | None = None,
    nacrule_matched: bool | None = None,
    auth_type: str | None = None,
    last_vlan_id: str | None = None,
    last_nas_vendor: str | None = None,
    idp_id: str | None = None,
    last_ssid: str | None = None,
    last_username: str | None = None,
    site_id: str | None = None,
    last_ap: str | None = None,
    mac: str | None = None,
    last_status: str | None = None,
    type: str | None = None,
    mdm_compliance_status: str | None = None,
    mdm_provider: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/nac/count-org-nac-clients

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str{'ap', 'auth_type', 'device_mac', 'edr_managed', 'edr_provider', 'edr_status', 'family', 'hostname', 'idp_id', 'mfg', 'mdm_compliance', 'mdm_managed', 'mdm_provider', 'model', 'mxedge_id', 'nacrule_matched', 'nacrule_name', 'nacrule_id', 'nas_ip', 'nas_vendor', 'os', 'site_id', 'ssid', 'status', 'type', 'usermac_label', 'username', 'vlan'}, default: type
      Field used to group this count response. enum: `ap`, `auth_type`, `device_mac`, `edr_managed`, `edr_provider`, `edr_status`, `family`, `hostname`, `idp_id`, `mfg`, `mdm_compliance`, `mdm_managed`, `mdm_provider`, `model`, `mxedge_id`, `nacrule_matched`, `nacrule_name`, `nacrule_id`, `nas_ip`, `nas_vendor`, `os`, `site_id`, `ssid`, `status`, `type`, `usermac_label`, `username`, `vlan`
    last_nacrule_id : str
      NAC Policy Rule ID, if matched
    nacrule_matched : bool
      NAC Policy Rule Matched
    auth_type : str
      Authentication type, e.g. "eap-tls", "eap-peap", "eap-ttls", "eap-teap", "mab", "psk", "device-auth"
    last_vlan_id : str
      Filter results by last VLAN ID
    last_nas_vendor : str
      Vendor of NAS device
    idp_id : str
      SSO ID, if present and used
    last_ssid : str
      Filter results by last SSID
    last_username : str
      Username presented by the client
    site_id : str
      Filter results by site identifier
    last_ap : str
      AP MAC connected to by client
    mac : str
      Filter results by MAC address
    last_status : str
      Connection status of client i.e "permitted", "denied, "session_ended"
    type : str
      Client type i.e. "wireless", "wired" etc. Accepts multiple comma-separated values.
    mdm_compliance_status : str
      MDM compliance of client i.e "compliant", "not compliant"
    mdm_provider : str
      MDM provider of client’s organization eg "intune", "jamf"
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

    uri = f"/api/v1/orgs/{org_id}/nac_clients/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if last_nacrule_id:
        query_params["last_nacrule_id"] = str(last_nacrule_id)
    if nacrule_matched:
        query_params["nacrule_matched"] = str(nacrule_matched)
    if auth_type:
        query_params["auth_type"] = str(auth_type)
    if last_vlan_id:
        query_params["last_vlan_id"] = str(last_vlan_id)
    if last_nas_vendor:
        query_params["last_nas_vendor"] = str(last_nas_vendor)
    if idp_id:
        query_params["idp_id"] = str(idp_id)
    if last_ssid:
        query_params["last_ssid"] = str(last_ssid)
    if last_username:
        query_params["last_username"] = str(last_username)
    if site_id:
        query_params["site_id"] = str(site_id)
    if last_ap:
        query_params["last_ap"] = str(last_ap)
    if mac:
        query_params["mac"] = str(mac)
    if last_status:
        query_params["last_status"] = str(last_status)
    if type:
        query_params["type"] = str(type)
    if mdm_compliance_status:
        query_params["mdm_compliance_status"] = str(mdm_compliance_status)
    if mdm_provider:
        query_params["mdm_provider"] = str(mdm_provider)
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


def countOrgNacClientEvents(
    mist_session: _APISession,
    org_id: str,
    distinct: str | None = None,
    type: str | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    limit: int | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/nac/count-org-nac-client-events

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    distinct : str{'ap', 'auth_type', 'dryrun_nacrule_id', 'mac', 'nacrule_id', 'nas_vendor', 'ssid', 'type', 'username', 'vlan'}
      Field used to group this count response. enum: `ap`, `auth_type`, `dryrun_nacrule_id`, `mac`, `nacrule_id`, `nas_vendor`, `ssid`, `type`, `username`, `vlan`
    type : str
      See [List Device Events Definitions](/#operations/listNacEventsDefinitions). Accepts multiple comma-separated values.
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

    uri = f"/api/v1/orgs/{org_id}/nac_clients/events/count"
    query_params: dict[str, str] = {}
    if distinct:
        query_params["distinct"] = str(distinct)
    if type:
        query_params["type"] = str(type)
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


def searchOrgNacClientEvents(
    mist_session: _APISession,
    org_id: str,
    type: str | None = None,
    nacrule_id: str | None = None,
    nacrule_matched: bool | None = None,
    dryrun_nacrule_id: str | None = None,
    dryrun_nacrule_matched: bool | None = None,
    auth_type: str | None = None,
    vlan: int | None = None,
    nas_vendor: str | None = None,
    bssid: str | None = None,
    idp_id: str | None = None,
    idp_role: str | None = None,
    idp_username: str | None = None,
    resp_attrs: list | None = None,
    ssid: str | None = None,
    username: str | None = None,
    site_id: str | None = None,
    ap: str | None = None,
    random_mac: bool | None = None,
    mac: str | None = None,
    usermac_label: str | None = None,
    text: str | None = None,
    nas_ip: str | None = None,
    ingress_vlan: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/nac/search-org-nac-client-events

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    type : str
      See [List Device Events Definitions](/#operations/listNacEventsDefinitions). Accepts multiple comma-separated values.
    nacrule_id : str
      NAC Policy Rule ID, if matched. Accepts multiple comma-separated values.
    nacrule_matched : bool
      NAC Policy Rule Matched
    dryrun_nacrule_id : str
      NAC Policy Dry Run Rule ID, if present and matched
    dryrun_nacrule_matched : bool
      True - if dryrun rule present and matched with priority, False - if not matched or not present
    auth_type : str
      Authentication type, e.g. "eap-tls", "eap-peap", "eap-ttls", "eap-teap", "mab", "psk", "device-auth". Accepts multiple comma-separated values.
    vlan : int
      Filter results by VLAN ID. Accepts multiple comma-separated integer values.
    nas_vendor : str
      Vendor of NAS device
    bssid : str
      Filter results by BSSID
    idp_id : str
      SSO ID, if present and used
    idp_role : str
      IDP returned roles/groups for the user
    idp_username : str
      Username presented to the Identity Provider
    resp_attrs : list
      RADIUS attributes returned by NAC to NAS derive
    ssid : str
      Filter results by SSID
    username : str
      Filter results by username. Accepts multiple comma-separated values.
    site_id : str
      Filter results by one site identifier. Use a single value; comma-separated values are not supported
    ap : str
      Filter results by AP MAC address
    random_mac : bool
      Filter results by whether the client is using a randomized MAC address. Accepts multiple comma-separated boolean values.
    mac : str
      Filter results by one MAC address. Use a single value; comma-separated values are not supported
    usermac_label : str
      Labels derived from usermac entry
    text : str
      Partial / full MAC address, username, device_mac or ap
    nas_ip : str
      IP address of NAS device. Accepts multiple comma-separated values.
    ingress_vlan : str
      Vendor specific VLAN ID in RADIUS requests
    limit : int, default: 100
      Maximum number of results to return per page
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    duration : str, default: 1d
      Time range duration for the query, using relative units such as `10m`, `7d`, or `2w`
    sort : str, default: wxid
      On which field the list should be sorted, -prefix represents DESC order.
    search_after : str
      Pagination cursor for retrieving subsequent pages of results. This value is automatically populated by Mist in the `next` URL from the previous response and should not be manually constructed.

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/nac_clients/events/search"
    query_params: dict[str, str] = {}
    if type:
        query_params["type"] = str(type)
    if nacrule_id:
        query_params["nacrule_id"] = str(nacrule_id)
    if nacrule_matched:
        query_params["nacrule_matched"] = str(nacrule_matched)
    if dryrun_nacrule_id:
        query_params["dryrun_nacrule_id"] = str(dryrun_nacrule_id)
    if dryrun_nacrule_matched:
        query_params["dryrun_nacrule_matched"] = str(dryrun_nacrule_matched)
    if auth_type:
        query_params["auth_type"] = str(auth_type)
    if vlan:
        query_params["vlan"] = str(vlan)
    if nas_vendor:
        query_params["nas_vendor"] = str(nas_vendor)
    if bssid:
        query_params["bssid"] = str(bssid)
    if idp_id:
        query_params["idp_id"] = str(idp_id)
    if idp_role:
        query_params["idp_role"] = str(idp_role)
    if idp_username:
        query_params["idp_username"] = str(idp_username)
    if resp_attrs:
        query_params["resp_attrs"] = str(resp_attrs)
    if ssid:
        query_params["ssid"] = str(ssid)
    if username:
        query_params["username"] = str(username)
    if site_id:
        query_params["site_id"] = str(site_id)
    if ap:
        query_params["ap"] = str(ap)
    if random_mac:
        query_params["random_mac"] = str(random_mac)
    if mac:
        query_params["mac"] = str(mac)
    if usermac_label:
        query_params["usermac_label"] = str(usermac_label)
    if text:
        query_params["text"] = str(text)
    if nas_ip:
        query_params["nas_ip"] = str(nas_ip)
    if ingress_vlan:
        query_params["ingress_vlan"] = str(ingress_vlan)
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


def searchOrgNacClients(
    mist_session: _APISession,
    org_id: str,
    ap: str | None = None,
    auth_type: str | None = None,
    cert_expiry_duration: str | None = None,
    edr_managed: bool | None = None,
    edr_provider: str | None = None,
    edr_status: str | None = None,
    family: str | None = None,
    hostname: str | None = None,
    idp_id: str | None = None,
    mac: str | None = None,
    mdm_compliance: str | None = None,
    mdm_provider: str | None = None,
    mdm_managed: bool | None = None,
    mfg: str | None = None,
    model: str | None = None,
    nacrule_name: str | None = None,
    nacrule_id: str | None = None,
    nacrule_matched: bool | None = None,
    nas_vendor: str | None = None,
    nas_ip: str | None = None,
    ingress_vlan: str | None = None,
    os: str | None = None,
    ssid: str | None = None,
    status: str | None = None,
    text: str | None = None,
    type: str | None = None,
    usermac_label: list | None = None,
    username: str | None = None,
    vlan: str | None = None,
    site_id: str | None = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
    duration: str | None = None,
    sort: str | None = None,
    search_after: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/nac/search-org-nac-clients

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    ap : str
      MAC address of the AP the client is/was connected to
    auth_type : str
      Authentication type, e.g. "eap-tls", "eap-peap", "eap-ttls", "eap-teap", "mab", "psk", "device-auth". Accepts multiple comma-separated values.
    cert_expiry_duration : str
      Filter by certificate expiry within a specific duration from now (e.g., "7d" for 7 days, "1m" for 1 month). Accepts multiple comma-separated values.
    edr_managed : bool
      Filters NAC clients that are integrated with EDR providers
    edr_provider : str{'crowdstrike', 'sentinelone'}
      EDR provider used to filter NAC clients. enum: `crowdstrike`, `sentinelone`
    edr_status : str{'sentinelone_healthy', 'sentinelone_infected', 'crowdstrike_low', 'crowdstrike_medium', 'crowdstrike_high', 'crowdstrike_critical', 'crowdstrike_informational'}
      EDR status used to filter NAC clients. enum: `sentinelone_healthy`, `sentinelone_infected`, `crowdstrike_low`, `crowdstrike_medium`, `crowdstrike_high`, `crowdstrike_critical`, `crowdstrike_informational`
    family : str
      Partial / full Client family (e.g. "Phone/Tablet/Wearable", "Access Point"). Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `Surveillance*` and `*urveillance*` match `Surveillance Camera`). Suffix-only wildcards (e.g. `*Camera`) are not supported. Accepts multiple comma-separated values.
    hostname : str
      Partial / full Client hostname. Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `everest*` and `*rest*` match `my-everest-client`). Suffix-only wildcards (e.g. `*everest`) are not supported. Accepts multiple comma-separated values.
    idp_id : str
      SSO ID, if present and used
    mac : str
      Partial / full Client MAC address. Use a single value; comma-separated values are not supported. Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `aabbcc*` and `*bbcc*` match `aabbccddeeff`). Suffix-only wildcards (e.g. `*bccddeeff`) are not supported
    mdm_compliance : str
      MDM compliance of client i.e "compliant", "not compliant"
    mdm_provider : str
      MDM provider of client’s organization eg "intune", "jamf"
    mdm_managed : bool
      Filters NAC clients that are managed by MDM providers
    mfg : str
      Partial / full Client manufacturer (e.g. "apple", "cisco", "juniper"). Use `prefix*` for prefix search or `*substring*` for contains search (e.g. `Raspberry Pi*` and `*Pi*` match `Raspberry Pi Trading Ltd`). Suffix-only wildcards (e.g. `*Ltd`) are not supported. Accepts multiple comma-separated values.
    model : str
      Client model, e.g. "iPhone 12", "MX100"
    nacrule_name : str
      NAC Policy Rule Name matched
    nacrule_id : str
      NAC Policy Rule ID, if matched
    nacrule_matched : bool
      NAC Policy Rule Matched
    nas_vendor : str
      Vendor of NAS device
    nas_ip : str
      IP address of NAS device. Accepts multiple comma-separated values.
    ingress_vlan : str
      Vendor specific VLAN ID in RADIUS requests
    os : str
      Client OS, e.g. "iOS 18.1", "Android", "Windows", "Linux"
    ssid : str
      Filter results by SSID
    status : str{'permitted', 'session_started', 'session_stopped', 'denied'}
      Client connection status used to filter results. enum: `permitted`, `session_started`, `session_stopped`, `denied`
    text : str
      partial / full MAC address, last_username, device_mac, nas_ip or last_ap
    type : str
      Client type i.e. "wireless", "wired" etc. Accepts multiple comma-separated values.
    usermac_label : list
      Labels derived from usermac entry
    username : str
      Filter results by username
    vlan : str
      Filter results by VLAN ID
    site_id : str
      Filter results by one site identifier. Use a single value; comma-separated values are not supported
    limit : int, default: 100
      Maximum number of results to return per page
    start : str
      Lower bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d` or `-1w`
    end : str
      Upper bound of the time range, as an epoch timestamp in seconds or a relative value such as `-1d`, `-2h`, or `now`
    duration : str, default: 1d
      Time range duration for the query, using relative units such as `10m`, `7d`, or `2w`
    sort : str, default: wxid
      On which field the list should be sorted, -prefix represents DESC order.
    search_after : str
      Pagination cursor for retrieving subsequent pages of results. This value is automatically populated by Mist in the `next` URL from the previous response and should not be manually constructed.

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/nac_clients/search"
    query_params: dict[str, str] = {}
    if ap:
        query_params["ap"] = str(ap)
    if auth_type:
        query_params["auth_type"] = str(auth_type)
    if cert_expiry_duration:
        query_params["cert_expiry_duration"] = str(cert_expiry_duration)
    if edr_managed:
        query_params["edr_managed"] = str(edr_managed)
    if edr_provider:
        query_params["edr_provider"] = str(edr_provider)
    if edr_status:
        query_params["edr_status"] = str(edr_status)
    if family:
        query_params["family"] = str(family)
    if hostname:
        query_params["hostname"] = str(hostname)
    if idp_id:
        query_params["idp_id"] = str(idp_id)
    if mac:
        query_params["mac"] = str(mac)
    if mdm_compliance:
        query_params["mdm_compliance"] = str(mdm_compliance)
    if mdm_provider:
        query_params["mdm_provider"] = str(mdm_provider)
    if mdm_managed:
        query_params["mdm_managed"] = str(mdm_managed)
    if mfg:
        query_params["mfg"] = str(mfg)
    if model:
        query_params["model"] = str(model)
    if nacrule_name:
        query_params["nacrule_name"] = str(nacrule_name)
    if nacrule_id:
        query_params["nacrule_id"] = str(nacrule_id)
    if nacrule_matched:
        query_params["nacrule_matched"] = str(nacrule_matched)
    if nas_vendor:
        query_params["nas_vendor"] = str(nas_vendor)
    if nas_ip:
        query_params["nas_ip"] = str(nas_ip)
    if ingress_vlan:
        query_params["ingress_vlan"] = str(ingress_vlan)
    if os:
        query_params["os"] = str(os)
    if ssid:
        query_params["ssid"] = str(ssid)
    if status:
        query_params["status"] = str(status)
    if text:
        query_params["text"] = str(text)
    if type:
        query_params["type"] = str(type)
    if usermac_label:
        query_params["usermac_label"] = str(usermac_label)
    if username:
        query_params["username"] = str(username)
    if vlan:
        query_params["vlan"] = str(vlan)
    if site_id:
        query_params["site_id"] = str(site_id)
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


def sendOrgNacClientCoA(
    mist_session: _APISession, org_id: str, client_mac: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/orgs/clients/nac/send-org-nac-client-co-a

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    client_mac : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/orgs/{org_id}/nac_clients/{client_mac}/coa"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
