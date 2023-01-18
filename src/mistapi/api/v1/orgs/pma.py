from mistapi import APISession as _APISession
from mistapi.__api_response import Response

def getOrgPmaDashboards(mist_session:_APISession, org_id:str) -> Response:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgPmaDashboards
    
    PARMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    """
    uri = f"/api/v1/orgs/{org_id}/pma/dashboards"
    query_params={}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    