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

from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse

def get_next(mist_session: _APISession, response: _APIResponse) -> _APIResponse:
    """
    Get the next page when previous response does not include all the items

    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    :param APIResponse response - mistapi previous response to use

    RETURN
    -----------
    :return APIResponse - response from the API call passed in parameteer
    """
    if response.next:
        return mist_session.mist_get(response.next)
    else:
        return None

def get_all(mist_session: _APISession, response: _APIResponse) -> list:
    """
    Retrieve and return all the items after a first request

    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    :param APIResponse response - mistapi previous response to use

    RETURN
    -----------
    :return list - list of all the items
    """
    if type(response.data) == list:
        data = response.data
        while response.next:
            response = get_next(mist_session, response)
            data += response.data
        return data
    else:
        return None
