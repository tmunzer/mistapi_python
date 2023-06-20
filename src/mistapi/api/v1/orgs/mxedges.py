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

@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.41.4", details="function replaced with listOrgMxEdges")  
def getOrgMxEdges(mist_session:_APISession, org_id:str, for_sites:str="any", limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgMxEdges
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    for_sites : str{'any', 'true', 'false'}, default: any
      filter for site level mist edges
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
    
def listOrgMxEdges(mist_session:_APISession, org_id:str, for_sites:str="any", limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgMxEdges
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    for_sites : str{'any', 'true', 'false'}, default: any
      filter for site level mist edges
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
    API doc: https://doc.mist-lab.fr/#operation/createOrgMxEdge
    
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
    API doc: https://doc.mist-lab.fr/#operation/assignOrgMxEdgeToSite
    
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
    API doc: https://doc.mist-lab.fr/#operation/claimOrgMxEdge
    
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
    
def unassignOrgMxEdgeFromSite(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/unassignOrgMxEdgeFromSite
    
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
    
@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.41.4", details="function replaced with listOrgMxEdgeUpgrades")  
def getOrgMxEdgeUpgrades(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgMxEdgeUpgrades
    
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
    
def listOrgMxEdgeUpgrades(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgMxEdgeUpgrades
    
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
    API doc: https://doc.mist-lab.fr/#operation/upgradeOrgMxEdges
    
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
    API doc: https://doc.mist-lab.fr/#operation/getOrgMxEdgeUpgrade
    
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
    
def getOrgMxEdgeUpgradeInfo(mist_session:_APISession, org_id:str, channel:str="stable") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgMxEdgeUpgradeInfo
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    channel : str{'stable', 'beta', 'alpha'}, default: stable
      upgrade channel to follow, stable (default) / beta / alpha        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges/version"
    query_params={}
    if channel: query_params["channel"]=channel
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getOrgMxEdge(mist_session:_APISession, org_id:str, mxedge_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgMxEdge
    
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
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgMxEdge
    
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
    API doc: https://doc.mist-lab.fr/#operation/updateOrgMxEdge
    
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
    
def restartOrgMxEdge(mist_session:_APISession, org_id:str, mxedge_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/restartOrgMxEdge
    
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
    API doc: https://doc.mist-lab.fr/#operation/bounceOrgMxEdgeDataPorts
    
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
    
def controlOrgMxEdgeServices(mist_session:_APISession, org_id:str, mxedge_id:str, name:str, action:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/controlOrgMxEdgeServices
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    mxedge_id : str
    name : str
    action : str
      restart or start or stop        
    
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
    API doc: https://doc.mist-lab.fr/#operation/uploadOrgMxEdgeSupportFiles
    
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
    API doc: https://doc.mist-lab.fr/#operation/unregisterOrgMxEdge
    
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
    
def upgradeOrgMxEdge(mist_session:_APISession, org_id:str, mxedge_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/upgradeOrgMxEdge
    
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
    uri = f"/api/v1/orgs/{org_id}/mxedges/{mxedge_id}/upgrade"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    