'''
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
This module manages API responses
'''

from requests import Response
from mistapi.__logger import logger
from mistapi.__logger import console

class APIResponse:
    """
    Class used to pass API Responses

    Attributes
    ----------
    :attr str raw_data - raw HTTP Response payload
    :attr object data - JSON of the HTTP Response (if possible)
    :attr object error - HTTP errors (if any)
    :attr str url - URL of the HTTP Request
    :attr int status_code - HTTP Response status code
    """

    def __init__(self, url: str, response:Response) -> None:
        self.raw_data=""
        self.data={}
        self.error={}
        self.url=url
        self.headers = response.headers
        self.status_code=response.status_code

        logger.info(f"apiresponse:Response Status Code: {response.status_code}")
        console.debug(f"Response Status Code: {response.status_code}")

        try:
            if response.status_code == 200:
                self.raw_data = response.content
                self.data = response.json()
            else:
                self.raw_data = response.content
                self.error = response.json()
                logger.error(f"apiresponse:Response: {response}")
                console.debug(f"Response: {self.error}")
            logger.debug(f"apiresponse:HTTP Response processed")
        except Exception as err:
            logger.error(f"apiresponse:Unable to process HTTP Response: \r\n{err}")
