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

def importOrgMapsFile(mist_session:_APISession, org_id:str, file_path:str="", csv_path:str="", body:dict={}) -> _APIResponse:
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
    :param dict body - JSON object to send to Mist Cloud (see API doc above for more details)
    :param str file_path - path to the file to upload
    :param str csv_path - path to the csv file to upload
    
    RETURN
    -----------
    :return APIResponse - response from the API call
    """
    uri = f"/api/v1/orgs/{org_id}/maps/import"
    resp = mist_session.mist_post_file(uri=uri, file=file_path, csv=csv_path, body=body)
    return resp
