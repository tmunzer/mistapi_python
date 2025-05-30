'''
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
'''

from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse
import deprecation

def listOrgMxEdges(mist_session:_APISession, org_id:str, for_sites:str="any", limit:int=100, page:int=1) -> _APIResponse:
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
    for_sites : str{'any', 'false', 'true'}, default: any
      Filter for site level mist edges
    limit : int, default: 100
    page : int, default: 1        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges"
    query_params={}
    if for_sites: query_params["for_sites"]=for_sites
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgMxEdge(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
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
    
def assignOrgMxEdgeToSite(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
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
    
def claimOrgMxEdge(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
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
    
def countOrgMxEdges(mist_session:_APISession, org_id:str, distinct:str="model", mxedge_id:str|None=None, site_id:str|None=None, mxcluster_id:str|None=None, model:str|None=None, distro:str|None=None, tunterm_version:str|None=None, sort:str|None=None, stats:bool|None=None, start:int|None=None, end:int|None=None, duration:str="1d", limit:int=100) -> _APIResponse:
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
    mxedge_id : str
    site_id : str
    mxcluster_id : str
    model : str
    distro : str
    tunterm_version : str
    sort : str
    stats : bool
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if mxedge_id: query_params["mxedge_id"]=mxedge_id
    if site_id: query_params["site_id"]=site_id
    if mxcluster_id: query_params["mxcluster_id"]=mxcluster_id
    if model: query_params["model"]=model
    if distro: query_params["distro"]=distro
    if tunterm_version: query_params["tunterm_version"]=tunterm_version
    if sort: query_params["sort"]=sort
    if stats: query_params["stats"]=stats
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def countOrgSiteMxEdgeEvents(mist_session:_APISession, org_id:str, distinct:str="mxedge_id", mxedge_id:str|None=None, mxcluster_id:str|None=None, type:str|None=None, service:str|None=None, start:int|None=None, end:int|None=None, duration:str="1d", limit:int=100) -> _APIResponse:
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
    mxedge_id : str
    mxcluster_id : str
    type : str
    service : str
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges/events/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if mxedge_id: query_params["mxedge_id"]=mxedge_id
    if mxcluster_id: query_params["mxcluster_id"]=mxcluster_id
    if type: query_params["type"]=type
    if service: query_params["service"]=service
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchOrgMistEdgeEvents(mist_session:_APISession, org_id:str, mxedge_id:str|None=None, mxcluster_id:str|None=None, type:str|None=None, service:str|None=None, component:str|None=None, start:int|None=None, end:int|None=None, duration:str="1d", limit:int=100) -> _APIResponse:
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
    mxcluster_id : str
    type : str
    service : str
    component : str
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges/events/search"
    query_params={}
    if mxedge_id: query_params["mxedge_id"]=mxedge_id
    if mxcluster_id: query_params["mxcluster_id"]=mxcluster_id
    if type: query_params["type"]=type
    if service: query_params["service"]=service
    if component: query_params["component"]=component
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchOrgMxEdges(mist_session:_APISession, org_id:str, mxedge_id:str|None=None, site_id:str|None=None, mxcluster_id:str|None=None, model:str|None=None, distro:str|None=None, tunterm_version:str|None=None, sort:str|None=None, stats:bool|None=None, start:int|None=None, end:int|None=None, duration:str="1d", limit:int=100, page:int=1) -> _APIResponse:
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
    mxedge_id : str
    site_id : str
    mxcluster_id : str
    model : str
    distro : str
    tunterm_version : str
    sort : str
    stats : bool
    start : int
    end : int
    duration : str, default: 1d
    limit : int, default: 100
    page : int, default: 1        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges/search"
    query_params={}
    if mxedge_id: query_params["mxedge_id"]=mxedge_id
    if site_id: query_params["site_id"]=site_id
    if mxcluster_id: query_params["mxcluster_id"]=mxcluster_id
    if model: query_params["model"]=model
    if distro: query_params["distro"]=distro
    if tunterm_version: query_params["tunterm_version"]=tunterm_version
    if sort: query_params["sort"]=sort
    if stats: query_params["stats"]=stats
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def unassignOrgMxEdgeFromSite(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
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
    
def listOrgMxEdgeUpgrades(mist_session:_APISession, org_id:str) -> _APIResponse:
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
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def upgradeOrgMxEdges(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
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
    
def getOrgMxEdgeUpgrade(mist_session:_APISession, org_id:str, upgrade_id:str) -> _APIResponse:
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
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getOrgMxEdgeUpgradeInfo(mist_session:_APISession, org_id:str, channel:str="stable", distro:str|None=None) -> _APIResponse:
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
      Upgrade channel to follow, stable (default) / beta / alpha
    distro : str        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges/version"
    query_params={}
    if channel: query_params["channel"]=channel
    if distro: query_params["distro"]=distro
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getOrgMxEdge(mist_session:_APISession, org_id:str, mxedge_id:str) -> _APIResponse:
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
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgMxEdge(mist_session:_APISession, org_id:str, mxedge_id:str) -> _APIResponse:
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
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgMxEdge(mist_session:_APISession, org_id:str, mxedge_id:str, body:object) -> _APIResponse:
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
    
def deleteOrgMxEdgeImage(mist_session:_APISession, org_id:str, mxedge_id:str, image_number:int) -> _APIResponse:
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
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def addOrgMxEdgeImage(mist_session:_APISession, org_id:str, mxedge_id:str, image_number:int, body:object) -> _APIResponse:
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
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges/{mxedge_id}/image/{image_number}"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def restartOrgMxEdge(mist_session:_APISession, org_id:str, mxedge_id:str) -> _APIResponse:
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
    
def bounceOrgMxEdgeDataPorts(mist_session:_APISession, org_id:str, mxedge_id:str, body:object) -> _APIResponse:
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
    
def disconnectOrgMxEdgeTuntermAps(mist_session:_APISession, org_id:str, mxedge_id:str, body:object) -> _APIResponse:
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
    
def controlOrgMxEdgeServices(mist_session:_APISession, org_id:str, mxedge_id:str, name:str, action:str) -> _APIResponse:
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
    
def uploadOrgMxEdgeSupportFiles(mist_session:_APISession, org_id:str, mxedge_id:str) -> _APIResponse:
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
    
def unregisterOrgMxEdge(mist_session:_APISession, org_id:str, mxedge_id:str) -> _APIResponse:
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
    