"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
This module manages API responses
"""

from requests import Response
from mistapi.__logger import logger, console


class APIResponse:
    """
    Class used to pass API Responses
    """

    def __init__(
        self,
        response: Response,
        url: str,
        proxy_error: bool = False
    ) -> None:
        """
        PARAMS
        -----------
        response : requests.Response
            Response from the request
        url : str
            URL of the HTTP Request
        """
        self.raw_data = ""
        self.data = {}
        self.url = url
        self.next = None
        self.headers = None
        self.status_code = None
        self.proxy_error = proxy_error
        
        if response:
            self.headers = response.headers
            self.status_code = response.status_code

            logger.info(
                f"apiresponse:__init__:response status code: {response.status_code}"
            )
            console.debug(f"Response Status Code: {response.status_code}")

            try:
                self.raw_data = response.content
                self.data = response.json()
                self._check_next()
                logger.debug(f"apiresponse:__init__:HTTP response processed")
                if self.status_code >= 400 or (
                    isinstance(self.data, dict) and self.data.get("error")
                ):
                    logger.error(f"apiresponse:__init__:response = {response}")
                    console.debug(f"Response: {self.data}")
            except Exception as err:
                logger.error(
                    f"apiresponse:__init__:unable to process HTTP Response: \r\n{err}"
                )

    def _check_next(self) -> None:
        logger.debug(f"apiresponse:_check_next")
        if "next" in self.data:
            self.next = self.data["next"]
            logger.debug(f"apiresponse:_check_next:set next to {self.next}")
        else:
            total = self.headers.get("X-Page-Total")
            limit = self.headers.get("X-Page-Limit")
            page = self.headers.get("X-Page-Page")
            if total and limit and page:
                try:
                    total = int(total)
                    limit = int(limit)
                    page = int(page)
                except:
                    logger.error(
                        f"apiresponse:_check_next:"
                        f"unable to convert total({total})/limit({limit})/page({page}) to int"
                    )
                    logger.error(
                        "apirequest:mist_post_file:Exception occurred", exc_info=True
                    )
                    console.error(
                        f"Unable to convert total "
                        f"({total})/limit({limit})/page({page}) to int"
                    )
                if limit * page < total:
                    uri = f"/api/{self.url.split('/api/')[1]}"
                    self.next = uri.replace(f"page={page}", f"page={page+1}")
                    logger.debug(f"apiresponse:_check_next:set next to {self.next}")
