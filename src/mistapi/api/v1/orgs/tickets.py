from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOrgTickets(mist_session:_APISession, org_id:str, start:int=None, end:int=None, duration:str="1d") -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgTickets
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)        
    """
    uri = f"/api/v1/orgs/{org_id}/tickets"
    query_params={}
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgTicket(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgTicket
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/tickets"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def countOrgTickets(mist_session:_APISession, org_id:str, distinct:str="status") -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/countOrgTickets
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(status, type)        
    """
    uri = f"/api/v1/orgs/{org_id}/tickets/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def getOrgTicket(mist_session:_APISession, org_id:str, ticket_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgTicket
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str ticket_id        
    """
    uri = f"/api/v1/orgs/{org_id}/tickets/{ticket_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def updateOrgTicket(mist_session:_APISession, org_id:str, ticket_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgTicket
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str ticket_id        
    """
    uri = f"/api/v1/orgs/{org_id}/tickets/{ticket_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    
def addOrgTicketComment(mist_session:_APISession, org_id:str, ticket_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/addOrgTicketComment
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str ticket_id        
    """
    uri = f"/api/v1/orgs/{org_id}/tickets/{ticket_id}/comments"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    