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


def getSiteBeamCoverageOverview(
    mist_session: _APISession,
    site_id: str,
    map_id: str | None = None,
    type: str | None = None,
    client_type: str | None = None,
    duration: str = "1d",
    resolution: str = "default",
    start: str | None = None,
    end: str | None = None,
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/location/get-site-beam-coverage-overview

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    map_id : str
    type : str{'asset', 'client', 'sdkclient'}
    client_type : str
    duration : str, default: 1d
    resolution : str{'default', 'fine'}, default: default
    start : str
    end : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/location/coverage"
    query_params: dict[str, str] = {}
    if map_id:
        query_params["map_id"] = str(map_id)
    if type:
        query_params["type"] = str(type)
    if client_type:
        query_params["client_type"] = str(client_type)
    if duration:
        query_params["duration"] = str(duration)
    if resolution:
        query_params["resolution"] = str(resolution)
    if start:
        query_params["start"] = str(start)
    if end:
        query_params["end"] = str(end)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def getSiteMachineLearningCurrentStat(
    mist_session: _APISession, site_id: str, map_id: str | None = None
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/location/get-site-machine-learning-current-stat

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    QUERY PARAMS
    ------------
    map_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/location/ml/current"
    query_params: dict[str, str] = {}
    if map_id:
        query_params["map_id"] = str(map_id)
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def getSiteDefaultPlfForModels(mist_session: _APISession, site_id: str) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/location/get-site-default-plf-for-models

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/location/ml/defaults"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp


def clearSiteMlOverwriteForDevice(
    mist_session: _APISession, site_id: str, device_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/location/clear-site-ml-overwrite-for-device

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    device_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/location/ml/device/{device_id}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp


def overwriteSiteMlForDevice(
    mist_session: _APISession, site_id: str, device_id: str, body: dict
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/location/overwrite-site-ml-for-device

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    device_id : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/location/ml/device/{device_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp


def clearSiteMlOverwriteForMap(
    mist_session: _APISession, site_id: str, map_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/location/clear-site-ml-overwrite-for-map

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    map_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/location/ml/map/{map_id}"
    query_params: dict[str, str] = {}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp


def overwriteSiteMlForMap(
    mist_session: _APISession, site_id: str, map_id: str, body: dict
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/location/overwrite-site-ml-for-map

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    map_id : str

    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/location/ml/map/{map_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp


def resetSiteMlStatsByMap(
    mist_session: _APISession, site_id: str, map_id: str
) -> _APIResponse:
    """
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/sites/location/reset-site-ml-stats-by-map

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information

    PATH PARAMS
    -----------
    site_id : str
    map_id : str

    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """

    uri = f"/api/v1/sites/{site_id}/location/ml/reset/map/{map_id}"
    resp = mist_session.mist_post(uri=uri)
    return resp
