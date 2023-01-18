from requests import Response

try:
    from config import log_level
except:
    log_level = 6
finally:
    from mistcli.__console import Console
    console = Console(log_level)

class APIResponse:

    def __init__(self, uri: str, response:Response) -> None:
        self.raw=""
        self.data={}
        self.error={}
        self.uri=uri
        self.status_code=response.status_code

        if response.status_code == 200:
            self.raw = response.content
            self.data = response.json()
            console.debug(f"Response Status Code: {response.status_code}")
        else:
            self.raw = response.content
            self.error = response.json()
            console.debug(f"Response Status Code: {response.status_code}")
            console.debug(f"Response: {self.error}")
