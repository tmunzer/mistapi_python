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

def importOrgMapsFile(mist_session:_APISession, org_id:str, auto_deviceprofile_assignment:bool=None, csv:str=None, file:str=None, json:dict=None) -> _APIResponse:
    """
    API doc: https://doc.mist-lab.fr/#operation/importOrgMaps
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    BODY PARAMS
    -----------
    :param bool auto_deviceprofile_assignment - boolean, whether to auto assign device to deviceprofile by name
    :param str csv - path to the file to upload. csv file for ap name mapping, optional
    :param str file - path to the file to upload. 
    :param dict json - 
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    multipart_form_data = {
        "auto_deviceprofile_assignment":auto_deviceprofile_assignment,
        "csv":csv,
        "file":file,
        "json":json,
    }
    uri = f"/api/v1/orgs/{org_id}/maps/import"
    resp = mist_session.mist_post_file(uri=uri, multipart_form_data=multipart_form_data)
    return resp
