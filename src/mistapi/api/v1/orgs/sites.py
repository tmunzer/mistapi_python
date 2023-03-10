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

def getOrgSites(mist_session:_APISession, org_id:str, limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/getOrgSites
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param int limit
    :param int page        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/sites"
    query_params={}
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def createOrgSite(mist_session:_APISession, org_id:str, body:object) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/createOrgSite
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/sites"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def countOrgSites(mist_session:_APISession, org_id:str, distinct:str="id", page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countOrgSites
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param str distinct(analytic_enabled, app_waking, asset_enabled, auto_upgrade_enabled, auto_upgrade_version, country_code, honeypot_enabled, id, locate_unconnected, mesh_enabled, name, rogue_enabled, remote_syslog_enabled, rtsa_enabled, vna_enabled, wifi_enabled)
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/sites/count"
    query_params={}
    if distinct: query_params["distinct"]=distinct
    if page: query_params["page"]=page
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def searchOrgSites(mist_session:_APISession, org_id:str, analytic_enabled:bool=None, app_waking:bool=None, asset_enabled:bool=None, auto_upgrade_enabled:bool=None, auto_upgrade_version:str=None, country_code:str=None, honeypot_enabled:bool=None, id:str=None, locate_unconnected:bool=None, mesh_enabled:bool=None, name:str=None, rogue_enabled:bool=None, remote_syslog_enabled:bool=None, rtsa_enabled:bool=None, vna_enabled:bool=None, wifi_enabled:bool=None, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/searchOrgSites
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param bool analytic_enabled - if Advanced Analytic feature is enabled
    :param bool app_waking - if App Waking feature is enabled
    :param bool asset_enabled - if Asset Tracking is enabled
    :param bool auto_upgrade_enabled - if Auto Upgrade feature is enabled
    :param str auto_upgrade_version - if Auto Upgrade feature is enabled
    :param str country_code - site country code
    :param bool honeypot_enabled - if Honeypot detection is enabled
    :param str id - site id
    :param bool locate_unconnected - if unconnected client are located
    :param bool mesh_enabled - if Mesh feature is enabled
    :param str name - site name
    :param bool rogue_enabled - if Rogue detection is enabled
    :param bool remote_syslog_enabled - if Remote Syslog is enabled
    :param bool rtsa_enabled - if managed mobility feature is enabled
    :param bool vna_enabled - if Virtual Network Assistant is enabled
    :param bool wifi_enabled - if WIFI feature is enabled
    :param int limit
    :param int start
    :param int end
    :param str duration        
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/sites/search"
    query_params={}
    if analytic_enabled: query_params["analytic_enabled"]=analytic_enabled
    if app_waking: query_params["app_waking"]=app_waking
    if asset_enabled: query_params["asset_enabled"]=asset_enabled
    if auto_upgrade_enabled: query_params["auto_upgrade_enabled"]=auto_upgrade_enabled
    if auto_upgrade_version: query_params["auto_upgrade_version"]=auto_upgrade_version
    if country_code: query_params["country_code"]=country_code
    if honeypot_enabled: query_params["honeypot_enabled"]=honeypot_enabled
    if id: query_params["id"]=id
    if locate_unconnected: query_params["locate_unconnected"]=locate_unconnected
    if mesh_enabled: query_params["mesh_enabled"]=mesh_enabled
    if name: query_params["name"]=name
    if rogue_enabled: query_params["rogue_enabled"]=rogue_enabled
    if remote_syslog_enabled: query_params["remote_syslog_enabled"]=remote_syslog_enabled
    if rtsa_enabled: query_params["rtsa_enabled"]=rtsa_enabled
    if vna_enabled: query_params["vna_enabled"]=vna_enabled
    if wifi_enabled: query_params["wifi_enabled"]=wifi_enabled
    if limit: query_params["limit"]=limit
    if start: query_params["start"]=start
    if end: query_params["end"]=end
    if duration: query_params["duration"]=duration
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def importOrgMapToSiteFile(mist_session:_APISession, org_id:str, site_name:str, file_path:str) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/importOrgMapToSite
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id
    :param str site_name        
    
    FILE PARAMS
    -----------
    :param str file_path - path to the file to upload
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/sites/{site_name}/maps/import"
    with open(file_path, "rb") as f:    
        files = {"file": f.read()}
        resp = mist_session.mist_post_file(uri=uri, files=files)
        return resp
    