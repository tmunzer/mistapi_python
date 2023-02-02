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

def getOrgMxEdges(mist_session:_APISession, org_id:str, for_sites:str="any") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgMxEdges
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str for_sites(any, true, false) - filter for site level mist edges        
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges"
    query_params={}
    if for_sites: query_params["for_sites"]=for_sites
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgMxEdge(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgMxEdge
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def assignOrgMxEdgeToSite(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/assignOrgMxEdgeToSite
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges/assign"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def claimOrgMxEdge(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/claimOrgMxEdge
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges/claim"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def unassignOrgMxEdgeFromSite(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/unassignOrgMxEdgeFromSite
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges/unassign"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgMxEdgeUpgrades(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgMxEdgeUpgrades
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges/upgrade"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def upgradeOrgMxEdges(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/upgradeOrgMxEdges
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges/upgrade"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgMxEdgeUpgrade(mist_session:_APISession, org_id:str, upgrade_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgMxEdgeUpgrade
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str upgrade_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges/upgrade/{upgrade_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getOrgMxEdgeUpgradeInfo(mist_session:_APISession, org_id:str, channel:str="stable") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgMxEdgeUpgradeInfo
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str channel(stable, beta, alpha) - upgrade channel to follow, stable (default) / beta / alpha        
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges/version"
    query_params={}
    if channel: query_params["channel"]=channel
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getOrgMxEdge(mist_session:_APISession, org_id:str, mxedge_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgMxEdge
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str mxedge_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges/{mxedge_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgMxEdge(mist_session:_APISession, org_id:str, mxedge_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgMxEdge
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str mxedge_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges/{mxedge_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgMxEdge(mist_session:_APISession, org_id:str, mxedge_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgMxEdge
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str mxedge_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges/{mxedge_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def restartOrgMxEdge(mist_session:_APISession, org_id:str, mxedge_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/restartOrgMxEdge
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str mxedge_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges/{mxedge_id}/restart"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def bounceOrgMxEdgeDataPorts(mist_session:_APISession, org_id:str, mxedge_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/bounceOrgMxEdgeDataPorts
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str mxedge_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges/{mxedge_id}/services/tunterm/bounce_port"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def controlOrgMxEdgeServices(mist_session:_APISession, org_id:str, mxedge_id:str, name:str, action:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/controlOrgMxEdgeServices
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str mxedge_id
    :param str name
    :param str action - restart or start or stop        
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges/{mxedge_id}/services/{name}/{action}"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def uploadOrgMxEdgeSupportFiles(mist_session:_APISession, org_id:str, mxedge_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/uploadOrgMxEdgeSupportFiles
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str mxedge_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges/{mxedge_id}/support"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def unregisterOrgMxEdge(mist_session:_APISession, org_id:str, mxedge_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/unregisterOrgMxEdge
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str mxedge_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges/{mxedge_id}/unregister"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def upgradeOrgMxEdge(mist_session:_APISession, org_id:str, mxedge_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/upgradeOrgMxEdge
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str mxedge_id        
    """
    uri = f"/api/v1/orgs/{org_id}/mxedges/{mxedge_id}/upgrade"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    