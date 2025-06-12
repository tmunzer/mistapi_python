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


def listInstallerListOfRecentlyClaimedDevices(
    mist_session: _APISession,
    org_id: str,
    model: str | None = None,
    site_name: str | None = None,
    site_id: str | None = None,
    limit: int = 100,
    page: int = 1,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/installer/list-installer-list-of-recently-claimed-devices

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str

    QUERY PARAMS
    ------------
    model : str
    site_name : str
    site_id : str
    limit : int, default: 100
    page : int, default: 1

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/installer/orgs/{org_id}/devices"
    query_params: dict[str, str] = {}
    if model:
        query_params["model"] = str(model)
    if site_name:
        query_params["site_name"] = str(site_name)
    if site_id:
        query_params["site_id"] = str(site_id)
    if limit:
        query_params["limit"] = str(limit)
    if page:
        query_params["page"] = str(page)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def claimInstallerDevices(
    mist_session: _APISession, org_id: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/installer/claim-installer-devices

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

    uri = f"/api/v1/installer/orgs/{org_id}/devices"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def unassignInstallerRecentlyClaimedDevice(
    mist_session: _APISession, org_id: str, device_mac: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/installer/unassign-installer-recently-claimed-device

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

    uri = f"/api/v1/installer/orgs/{org_id}/devices/{device_mac}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp


def provisionInstallerDevices(
    mist_session: _APISession, org_id: str, device_mac: str, body: dict
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/installer/provision-installer-devices

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

    uri = f"/api/v1/installer/orgs/{org_id}/devices/{device_mac}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp


def startInstallerLocateDevice(
    mist_session: _APISession, org_id: str, device_mac: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/installer/start-installer-locate-device

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

    uri = f"/api/v1/installer/orgs/{org_id}/devices/{device_mac}/locate"
    resp = mist_session.mist_post(uri=uri)
    return resp


def stopInstallerLocateDevice(
    mist_session: _APISession, org_id: str, device_mac: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/installer/stop-installer-locate-device

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

    uri = f"/api/v1/installer/orgs/{org_id}/devices/{device_mac}/unlocate"
    resp = mist_session.mist_post(uri=uri)
    return resp


def deleteInstallerDeviceImage(
    mist_session: _APISession, org_id: str, image_name: str, device_mac: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/installer/delete-installer-device-image

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    image_name : str
    device_mac : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/installer/orgs/{org_id}/devices/{device_mac}/{image_name}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp


def addInstallerDeviceImageFile(
    mist_session: _APISession,
    org_id: str,
    image_name: str,
    device_mac: str,
    auto_deviceprofile_assignment: bool | None = None,
    csv: str | None = None,
    file: str | None = None,
    json: dict | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/installer/add-installer-device-image

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    image_name : str
    device_mac : str

    BODY PARAMS
    -----------
    auto_deviceprofile_assignment : bool
        Whether to auto assign device to deviceprofile by name
    csv : str
        path to the file to upload. CSV file for ap name mapping, optional
    file : str
        path to the file to upload. Ekahau or ibwave file
    json : dict

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    multipart_form_data = {
        "auto_deviceprofile_assignment": auto_deviceprofile_assignment,
        "csv": csv,
        "file": file,
        "json": json,
    }
    uri = f"/api/v1/installer/orgs/{org_id}/devices/{device_mac}/{image_name}"
    resp = mist_session.mist_post_file(uri=uri, multipart_form_data=multipart_form_data)
    return resp


def getInstallerDeviceVirtualChassis(
    mist_session: _APISession, org_id: str, fpc0_mac: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/installer/get-installer-device-virtual-chassis

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    fpc0_mac : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/installer/orgs/{org_id}/devices/{fpc0_mac}/vc"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def createInstallerVirtualChassis(
    mist_session: _APISession, org_id: str, fpc0_mac: str, body: dict | list
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/installer/create-installer-virtual-chassis

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    fpc0_mac : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/installer/orgs/{org_id}/devices/{fpc0_mac}/vc"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp


def updateInstallerVirtualChassisMember(
    mist_session: _APISession, org_id: str, fpc0_mac: str, body: dict
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/installer/update-installer-virtual-chassis-member

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    org_id : str
    fpc0_mac : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/installer/orgs/{org_id}/devices/{fpc0_mac}/vc"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
