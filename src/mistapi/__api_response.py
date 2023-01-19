from requests import Response
from mistapi.__logger import logger
from mistapi.__logger import console

class APIResponse:

    def __init__(self, url: str, response:Response) -> None:
        self.raw_data=""
        self.data={}
        self.error={}
        self.url=url
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
