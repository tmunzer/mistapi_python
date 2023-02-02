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

def get_next(mist_session: _APISession, response: _APIResponse) -> _APIResponse:
    """
    Generate the url with the host (in the object) and the uri

    :params APISession mist_session - mistapi session including authentication and Mist host information
    :return APIResponse response - response from a previous API call
    """
    if response.next:
        return mist_session.mist_get(response.next)
    else:
        return None
