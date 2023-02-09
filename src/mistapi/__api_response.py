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

    PARAMS
    -----------
    :param str raw_data - raw HTTP Response payload
    :param object data - JSON of the HTTP Response (if possible)
    :param object error - HTTP errors (if any)
    :param str url - URL of the HTTP Request
    :param str url - URI of the HTTP Request
    :param int status_code - HTTP Response status code
    """

    def __init__(self, response:Response, url: str,) -> None:
        self.raw_data=""
        self.data={}
        self.error={}
        self.url=url
        self.next=None
        self.headers = response.headers
        self.status_code=response.status_code

        logger.info(f"apiresponse:Response Status Code: {response.status_code}")
        console.debug(f"Response Status Code: {response.status_code}")

        try:
            if response.status_code == 200:
                self.raw_data = response.content
                self.data = response.json()
                self._check_next()
            else:
                self.raw_data = response.content
                self.error = response.json()
                logger.error(f"apiresponse:Response: {response}")
                console.debug(f"Response: {self.error}")
            logger.debug(f"apiresponse:HTTP Response processed")
        except Exception as err:
            logger.error(f"apiresponse:Unable to process HTTP Response: \r\n{err}")

    def _check_next(self) -> None:
        logger.debug(f"apiresponse:in  > _check_next")
        if "next" in self.data:
            self.next = self.data["next"]
            logger.debug(f"apiresponse:set next to {self.next}")
        else:
            total = self.headers.get("X-Page-Total")
            limit = self.headers.get("X-Page-Limit")
            page = self.headers.get("X-Page-Page")
            if total and limit and page:
                try:
                    total=int(total)
                    limit=int(limit)
                    page=int(page)
                except:
                    logger.error(f"apiresponse:Unable to convert total({total})/limit({limit})/page({page}) to int")
                    console.error(f"Unable to convert total({total})/limit({limit})/page({page}) to int")
                if limit * page < total:
                    uri = f"/api/{self.url.split('/api/')[1]}"
                    self.next= uri.replace(f"page={page}", f"page={page+1}")
                    logger.debug(f"apiresponse:set next to {self.next}")

