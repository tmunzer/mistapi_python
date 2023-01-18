from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getMspOrgGroups(mist_session:_APISession, msp_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getMspOrgGroups
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    """
    uri = f"/api/v1/msps/{msp_id}/orggroups"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createMspOrgGroup(mist_session:_APISession, msp_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createMspOrgGroup
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id        
    """
    uri = f"/api/v1/msps/{msp_id}/orggroups"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getMspOrgGroup(mist_session:_APISession, msp_id:str, orggroup_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getMspOrgGroup
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id
    :param str orggroup_id        
    """
    uri = f"/api/v1/msps/{msp_id}/orggroups/{orggroup_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteMspOrgGroup(mist_session:_APISession, msp_id:str, orggroup_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteMspOrgGroup
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id
    :param str orggroup_id        
    """
    uri = f"/api/v1/msps/{msp_id}/orggroups/{orggroup_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateMspOrgGroup(mist_session:_APISession, msp_id:str, orggroup_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateMspOrgGroup
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str msp_id
    :param str orggroup_id        
    """
    uri = f"/api/v1/msps/{msp_id}/orggroups/{orggroup_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    