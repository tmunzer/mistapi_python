from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getSiteEvpnTopologies(mist_session:_APISession, site_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteEvpnTopologies
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/evpn_topologies"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createSiteEvpnTopology(mist_session:_APISession, site_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createSiteEvpnTopology
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id        
    """
    uri = f"/api/v1/sites/{site_id}/evpn_topologies"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getSiteEvpnTolopogy(mist_session:_APISession, site_id:str, evpn_topology_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getSiteEvpnTolopogy
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str evpn_topology_id        
    """
    uri = f"/api/v1/sites/{site_id}/evpn_topologies/{evpn_topology_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteSiteEvpnTopology(mist_session:_APISession, site_id:str, evpn_topology_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteSiteEvpnTopology
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str evpn_topology_id        
    """
    uri = f"/api/v1/sites/{site_id}/evpn_topologies/{evpn_topology_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateSiteEvpnTopology(mist_session:_APISession, site_id:str, evpn_topology_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateSiteEvpnTopology
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str site_id
    :param str evpn_topology_id        
    """
    uri = f"/api/v1/sites/{site_id}/evpn_topologies/{evpn_topology_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    