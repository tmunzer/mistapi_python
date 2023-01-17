import requests
from requests.exceptions import HTTPError


try:
    from config import log_level
except:
    log_level = 6
finally:
    from .__console import Console
    console = Console(log_level)


class Req:

    def __init__(self):
        self._cloud_uri = ""
        self._session = requests.session()
        self.privileges = ""
        

    def _url(self, uri):
        """Generate the url with the host (in the object) and the uri
        Params: uri
        Return: url"""
        return "https://" + self._cloud_uri + uri

    def _gen_query(self, query:object, limit=None, page=None):
        html_query = "?"
        if query:
            for query_param in query:
                html_query += f"{query_param}={query[query_param]}&"
        if limit: html_query += f"limit={limit}&"
        if page: html_query += f"page={page}"
        return html_query


    def _response(self, resp, uri:str, multi_pages_result=None):
        if resp.status_code == 200:
            if multi_pages_result is None:
                result = resp.json()
            else: 
                result = multi_pages_result
            error = ""
            console.debug(f"Response Status Code: {resp.status_code}")
        else:
            result = ""
            error = resp.json()
            console.debug(f"Response Status Code: {resp.status_code}")
            console.debug(f"Response: {error}")
        return {"result": result, "status_code": resp.status_code, "error": error, "uri":uri}

    def mist_get(self, uri:str, query:object=None, page=None, limit=None):
        """GET HTTP Request
        Params: uri, HTTP query
        Return: HTTP response"""
        try:
            url = self._url(uri) + self._gen_query(query, page, limit)
            console.debug(f"Request > GET {url}")
            resp = self._session.get(url)
            resp.raise_for_status()
        except HTTPError as http_err:
            console.error(f'HTTP error occurred: {http_err}')  # Python 3.6
            console.error(f'HTTP error description: {resp.json()}')
        except Exception as err:
            console.error(f'Other error occurred: {err}')  # Python 3.6
        else: 
            if "X-Page-Limit" in resp.headers:
                content = resp.json()
                x_page_limit = int(resp.headers["X-Page-Limit"])
                x_page_page = int(resp.headers["X-Page-Page"])
                x_page_total = int(resp.headers["X-Page-Total"])
                if x_page_limit * x_page_page < x_page_total:
                    content+=self.mist_get(uri, query, page + 1, limit)["result"]
                return self._response(resp, uri, content)
            else:                
                return self._response(resp, uri)

    def mist_post(self, uri:str,  body:object=None):
        """POST HTTP Request
        Params: uri, HTTP body
        Return: HTTP response"""
        try: 
            url = self._url(uri)
            headers = {'Content-Type': "application/json"}
            console.debug(f"Request > POST {url}")
            console.debug(f"Request body: \r\n{body}")
            if type(body) == str:
                resp = self._session.post(url, data=body, headers=headers)
            elif type(body) == dict:
                resp = self._session.post(url, json=body, headers=headers)
            else: 
                resp = self._session.post(url, json=body, headers=headers)
            resp.raise_for_status()
        except HTTPError as http_err:
            console.error(f'HTTP error occurred: {http_err}')  # Python 3.6
            console.error(f'HTTP error description: {resp.json()}')
        except Exception as err:
            console.error(f'Other error occurred: {err}')  # Python 3.6
        else: 
            return self._response(resp, uri)

    def mist_put(self, uri:str, body:object=None):
        """PUT HTTP Request
        Params: uri, HTTP body
        Return: HTTP response"""
        try:
            url = self._url(uri)
            console.debug(f"Request > PUT {url}")
            console.debug(f"Request body: \r\n{body}")
            if type(body) == str:
                resp = self._session.put(url, data=body)
            elif type(body) == dict:
                resp = self._session.put(url, json=body)
            else: 
                resp = self._session.put(url, json=body)
            resp.raise_for_status()
        except HTTPError as http_err:
            console.error(f'HTTP error occurred: {http_err}')  # Python 3.6
            console.error(f'HTTP error description: {resp.json()}')
        except Exception as err:
            console.error(f'Other error occurred: {err}')  # Python 3.6
        else: 
            return self._response(resp, uri)

    def mist_delete(self, uri:str, query:object=None):
        """DELETE HTTP Request
        Params: uri
        Return: HTTP response"""
        try: 
            url = self._url(uri) + self._gen_query(query)
            console.debug(f"Request > DELETE {url}")
            resp = self._session.delete(url)
            resp.raise_for_status()
        except HTTPError as http_err:
            console.error(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            console.error(f'Other error occurred: {err}')  # Python 3.6
        else: 
            return self._response(resp, uri)


    def mist_post_file(self, uri:str, files=None):
        """POST HTTP Request
        Params: uri, HTTP body
        Return: HTTP response"""
        try:                 
            url = self._url(uri)
            console.debug(f"Request > POST {url}")
            resp = self.ses_sessionion.post(url, files=files)
            resp.raise_for_status()
        except HTTPError as http_err:
            console.error(f'HTTP error occurred: {http_err}')  # Python 3.6
            console.error(f'HTTP error description: {resp.json()}')
            return resp
        except Exception as err:
            console.error(f'Other error occurred: {err}')  # Python 3.6
        else: 
            return self._response(resp, uri)
