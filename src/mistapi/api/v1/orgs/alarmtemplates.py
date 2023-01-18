from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOrgAlarmTemplates(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgAlarmTemplates
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/alarmtemplates"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgAlarmTemplate(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgAlarmTemplate
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/alarmtemplates"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def suppressOrgAlarm(mist_session:_APISession, org_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/suppressOrgAlarm
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/alarmtemplates/suppress"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def getOrgAlarmTemplate(mist_session:_APISession, org_id:str, alarmtemplate_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgAlarmTemplate
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str alarmtemplate_id        
    """
    uri = f"/api/v1/orgs/{org_id}/alarmtemplates/{alarmtemplate_id}"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def deleteOrgAlarmTemplate(mist_session:_APISession, org_id:str, alarmtemplate_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/deleteOrgAlarmTemplate
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str alarmtemplate_id        
    """
    uri = f"/api/v1/orgs/{org_id}/alarmtemplates/{alarmtemplate_id}"
    query_params={}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    
def updateOrgAlarmTemplate(mist_session:_APISession, org_id:str, alarmtemplate_id:str, body:object) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/updateOrgAlarmTemplate
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str alarmtemplate_id        
    """
    uri = f"/api/v1/orgs/{org_id}/alarmtemplates/{alarmtemplate_id}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    