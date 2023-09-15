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
import deprecation

@deprecation.deprecated(deprecated_in="0.37.7", removed_in="0.60.0", current_version="0.44.2", details="function replaced with listOrgSites")  
def getOrgSites(mist_session:_APISession, org_id:str, limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgSites
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    limit : int, default: 100
    page : int, default: 1        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/sites"
    query_params={}
    if limit: query_params["limit"]=limit
    if page: query_params["page"]=page
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    
def listOrgSites(mist_session:_APISession, org_id:str, limit:int=100, page:int=1) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/listOrgSites
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    limit : int, default: 100
    page : int, default: 1        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
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
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    BODY PARAMS
    -----------
    body : dict
        JSON object to send to Mist Cloud (see API doc above for more details)
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/sites"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    
def countOrgSites(mist_session:_APISession, org_id:str, distinct:str="id", page:int=1, limit:int=100, start:int=None, end:int=None, duration:str="1d") -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/countOrgSites
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    distinct : str{'analytic_enabled', 'app_waking', 'asset_enabled', 'auto_upgrade_enabled', 'auto_upgrade_version', 'country_code', 'honeypot_enabled', 'id', 'locate_unconnected', 'mesh_enabled', 'name', 'rogue_enabled', 'remote_syslog_enabled', 'rtsa_enabled', 'vna_enabled', 'wifi_enabled'}, default: id
    page : int, default: 1
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
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
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str        
    
    QUERY PARAMS
    ------------
    analytic_enabled : bool
      if Advanced Analytic feature is enabled
    app_waking : bool
      if App Waking feature is enabled
    asset_enabled : bool
      if Asset Tracking is enabled
    auto_upgrade_enabled : bool
      if Auto Upgrade feature is enabled
    auto_upgrade_version : str
      if Auto Upgrade feature is enabled
    country_code : str
      site country code
    honeypot_enabled : bool
      if Honeypot detection is enabled
    id : str
      site id
    locate_unconnected : bool
      if unconnected client are located
    mesh_enabled : bool
      if Mesh feature is enabled
    name : str
      site name
    rogue_enabled : bool
      if Rogue detection is enabled
    remote_syslog_enabled : bool
      if Remote Syslog is enabled
    rtsa_enabled : bool
      if managed mobility feature is enabled
    vna_enabled : bool
      if Virtual Network Assistant is enabled
    wifi_enabled : bool
      if WIFI feature is enabled
    limit : int, default: 100
    start : int
    end : int
    duration : str, default: 1d        
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
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
    
def importOrgMapToSiteFile(mist_session:_APISession, org_id:str, site_name:str, auto_deviceprofile_assignment:bool=None, csv:str=None, file:str=None, json:dict=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/importOrgMapToSite
    
    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    org_id : str
    site_name : str        
    
    BODY PARAMS
    -----------
    auto_deviceprofile_assignment : bool
        whether to auto assign device to deviceprofile by name
    csv : str
        path to the file to upload. csv file for ap name mapping, optional
    file : str
        path to the file to upload. ekahau or ibwave file
    json : dict
        import_all_floorplans : bool
        import_height : bool, default: True
        import_orientation : bool, default: True
        vendor_name : {'ekahau', 'ibwave'}
    
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    """
    multipart_form_data = {
        "auto_deviceprofile_assignment":auto_deviceprofile_assignment,
        "csv":csv,
        "file":file,
        "json":json,
    }
    uri = f"/api/v1/orgs/{org_id}/sites/{site_name}/maps/import"
    resp = mist_session.mist_post_file(uri=uri, multipart_form_data=multipart_form_data)
    return resp
