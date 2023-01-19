
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

def getOrgAlarmTemplates(mist_session:_APISession, org_id:str) -> _APIResponse:
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
    
def createOrgAlarmTemplate(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
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
    
def suppressOrgAlarm(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
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
    
def getOrgAlarmTemplate(mist_session:_APISession, org_id:str, alarmtemplate_id:str) -> _APIResponse:
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
    
def deleteOrgAlarmTemplate(mist_session:_APISession, org_id:str, alarmtemplate_id:str) -> _APIResponse:
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
    
def updateOrgAlarmTemplate(mist_session:_APISession, org_id:str, alarmtemplate_id:str, body:object) -> _APIResponse:
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
    