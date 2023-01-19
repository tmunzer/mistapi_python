
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

def getOrgEvpnTopologies(mist_session:_APISession, org_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgEvpnTopologies
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/evpn_topologies"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgEvpnTopology(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgEvpnTopology
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/evpn_topologies"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgEvpnTolopogy(mist_session:_APISession, org_id:str, evpn_topology_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgEvpnTolopogy
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str evpn_topology_id        
    """
    uri = f"/api/v1/orgs/{org_id}/evpn_topologies/{evpn_topology_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgEvpnTopology(mist_session:_APISession, org_id:str, evpn_topology_id:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgEvpnTopology
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str evpn_topology_id        
    """
    uri = f"/api/v1/orgs/{org_id}/evpn_topologies/{evpn_topology_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgEvpnTopology(mist_session:_APISession, org_id:str, evpn_topology_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgEvpnTopology
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str evpn_topology_id        
    """
    uri = f"/api/v1/orgs/{org_id}/evpn_topologies/{evpn_topology_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    