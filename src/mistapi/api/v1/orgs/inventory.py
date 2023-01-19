from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse

def getOrgInventory(mist_session:_APISession, org_id:str, serial:str=None, model:str=None, type:str="ap", mac:str=None, site_id:str=None, vc_mac:str=None, vc:str=None, unassigned:bool=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgInventory
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str serial - device serial
    :param str model - device model
    :param str type(ap, switch, gateway)
    :param str mac - MAC address
    :param str site_id - site id if assigned, null if not assigned
    :param str vc_mac
    :param str vc
    :param bool unassigned        
    """
    uri = f"/api/v1/orgs/{org_id}/inventory"
    query_params={}
    if serial: query_params["serial"]=serial
    if model: query_params["model"]=model
    if type: query_params["type"]=type
    if mac: query_params["mac"]=mac
    if site_id: query_params["site_id"]=site_id
    if vc_mac: query_params["vc_mac"]=vc_mac
    if vc: query_params["vc"]=vc
    if unassigned: query_params["unassigned"]=unassigned
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def addOrgInventory(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/addOrgInventory
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/inventory"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def updateOrgInventoryAssignment(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgInventoryAssignment
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/inventory"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def reevaluateOrgAutoAssignment(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/reevaluateOrgAutoAssignment
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/inventory/reevaluate_auto_assignment"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def replaceOrgDevices(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/replaceOrgDevices
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/inventory/replace"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    