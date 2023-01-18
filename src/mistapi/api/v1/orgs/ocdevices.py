from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOrgJuniperDevicesCommand(mist_session:_APISession, org_id:str, site_id:str=None) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgJuniperDevicesCommand
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str site_id - site_id would be used for proxy config check of the site and automatic site assignment        
    """
    uri = f"/api/v1/orgs/{org_id}/ocdevices/outbound_ssh_cmd"
    query_params={}
    if site_id: query_params["site_id"]=site_id
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    