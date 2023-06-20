'''
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
This module manages API requests with Mist Cloud. It is used to 
* generate the URL based on the provided parameters
* add the required HTTP Headers to the request
* report error if any
'''

import requests
import os
import json
from requests.exceptions import HTTPError
from mistapi.__api_response import APIResponse
from mistapi.__logger import logger


class APIRequest:

    def __init__(self):
        self._cloud_uri = ""
        self._session = requests.session()
        self.privileges = ""
        

    def _url(self, uri) -> str:
        """
        Generate the url with the host (in the object) and the uri

        PARAMS
        -----------
        :param str uri - URI where to send the request to (e.g. "/api/v1/...")

        RETURN
        -----------
        :return str url - Full URL where to send the request to (e.g. "https://api.mist.com/api/v1/...")
        """
        logger.debug(f"apirequest:_url: https://{self._cloud_uri}{uri}")
        return f"https://{self._cloud_uri}{uri}"

    def _gen_query(self, query:object) -> str:
        logger.debug(f"apirequest:_gen_query: processing query {query}")
        html_query = "?"
        if query:
            for query_param in query:
                html_query += f"{query_param}={query[query_param]}&"
        logger.debug(f"apirequest:_gen_query: generated query: {html_query}")
        html_query = html_query[:-1]
        return html_query

    def mist_get(self, uri:str, query:object=None) -> APIResponse:
        """
        GET HTTP Request

        PARAMS
        -----------
        :param str uri - HTTP URI (e.g. "/api/v1/self") 
        :param object query - dict of HTTP Queries (e.g. {"page": 1, "limit":100})

        RETURN
        -----------
        :return APIResponse
        """
        try:
            url = self._url(uri) + self._gen_query(query)
            logger.info(f"apirequest:mist_get: sending request to {url}")
            resp = self._session.get(url)
            resp.raise_for_status()
        except HTTPError as http_err:
            logger.error(f'apirequest:mist_get: HTTP error occurred: {http_err}')  # Python 3.6
            logger.error(f'apirequest:mist_get: HTTP error description: {resp.json()}')
        except Exception as err:
            logger.error(f'apirequest:mist_get: Other error occurred: {err}')  # Python 3.6
            logger.error("apirequest:mist_get: Exception occurred", exc_info=True)
        finally:
            return APIResponse(url=url, response=resp)

    def mist_post(self, uri:str,  body:object=None) -> APIResponse:
        """
        POST HTTP Request

        PARAMS
        -----------
        :param str uri - HTTP URI (e.g. "/api/v1/self") 
        :param object body 

        RETURN
        -----------
        :return APIResponse
        """
        try: 
            url = self._url(uri)
            logger.info(f"apirequest:mist_post: sending request to {url}")
            headers = {'Content-Type': "application/json"}
            logger.debug(f"apirequest:mist_post: Request body: {body}")
            if type(body) == str:
                resp = self._session.post(url, data=body, headers=headers)
            else: 
                resp = self._session.post(url, json=body, headers=headers)
            resp.raise_for_status()
        except HTTPError as http_err:
            logger.error(f'apirequest:mist_post: HTTP error occurred: {http_err}')  # Python 3.6
            logger.error(f'apirequest:mist_post: HTTP error description: {resp.json()}')
        except Exception as err:
            logger.error(f'apirequest:mist_post: Other error occurred: {err}')  # Python 3.6
            logger.error("apirequest:mist_post: Exception occurred", exc_info=True)
        finally: 
            return APIResponse(url=url, response=resp)

    def mist_put(self, uri:str, body:object=None) -> APIResponse:
        """
        PUT HTTP Request

        PARAMS
        -----------
        :param str uri - HTTP URI (e.g. "/api/v1/self") 
        :param object body 

        RETURN
        -----------
        :return APIResponse
        """
        try:
            url = self._url(uri)
            logger.info(f"apirequest:mist_put: sending request to {url}")
            headers = {'Content-Type': "application/json"}
            logger.debug(f"apirequest:mist_put: Request body: {body}")
            if type(body) == str:
                resp = self._session.put(url, data=body, headers=headers)
            else: 
                resp = self._session.put(url, json=body, headers=headers)
            resp.raise_for_status()
        except HTTPError as http_err:
            logger.error(f'apirequest:mist_put: HTTP error occurred: {http_err}')  # Python 3.6
            logger.error(f'apirequest:mist_put: HTTP error description: {resp.json()}')
        except Exception as err:
            logger.error(f'apirequest:mist_put: Other error occurred: {err}')  # Python 3.6
            logger.error("apirequest:mist_put: Exception occurred", exc_info=True)
        finally: 
            return APIResponse(url=url, response=resp)

    def mist_delete(self, uri:str, query:object=None) -> APIResponse:
        """
        DELETE HTTP Request

        PARAMS
        -----------
        :param str uri - HTTP URI (e.g. "/api/v1/self") 

        RETURN
        -----------
        :return APIResponse
        """
        try: 
            url = self._url(uri) + self._gen_query(query)
            logger.info(f"apirequest:mist_delete: sending request to {url}")
            resp = self._session.delete(url)
            resp.raise_for_status()
        except HTTPError as http_err:
            logger.error(f'apirequest:mist_delete: HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            logger.error(f'apirequest:mist_delete: Other error occurred: {err}')  # Python 3.6
            logger.error("apirequest:mist_delete: Exception occurred", exc_info=True)
        else: 
            return APIResponse(url=url, response=resp)


    def mist_post_file(self, uri:str, multipart_form_data:dict={}) -> APIResponse:
        """
        POST HTTP Request

        PARAMS
        -----------
        :param str uri - HTTP URI (e.g. "/api/v1/self") 
        :param object multipart_form_data - dict of key/values to add include in the multipart form 

        RETURN
        -----------
        :return APIResponse
        """
        try:                 
            url = self._url(uri)
            logger.info(f"apirequest:mist_post_file: sending request to {url}")
            logger.debug(f"apirequest:mist_post_file: initial multipart_form_data: {multipart_form_data}")
            generated_multipart_form_data = {}
            for key in multipart_form_data:
                logger.debug(f"apirequest:mist_post_file: multipart_form_data: {key} = {multipart_form_data[key]}")
                if multipart_form_data[key]:
                    files = []
                    try:
                        if key in ["csv", "file"]:
                            f = open(multipart_form_data[key], 'rb') 
                            files.append(f)
                            generated_multipart_form_data[key] = (os.path.basename(multipart_form_data[key]), f, 'application/octet-stream')                            
                        else:
                            generated_multipart_form_data[key] = (None, json.dumps(multipart_form_data[key]), 'application/json')
                    except:
                        logger.error(f"apirequest:mist_post_file: multipart_form_data: Unable to parse JSON object {key} with value {multipart_form_data[key]}")            
            logger.debug(f"fapirequest:mist_post_file: inal multipart_form_data: {generated_multipart_form_data}")
            resp = self._session.post(url, files=generated_multipart_form_data)
            if files:
                for f in files:
                    f.close()
            resp.raise_for_status()
        except HTTPError as http_err:
            logger.error(f'apirequest:mist_post_file: HTTP error occurred: {http_err}')  # Python 3.6
            logger.error(f'apirequest:mist_post_file: HTTP error description: {resp.json()}')
            return resp
        except Exception as err:
            logger.error(f'apirequest:mist_post_file: Other error occurred: {err}')  # Python 3.6
            logger.error("apirequest:mist_post_file: Exception occurred", exc_info=True)
        else: 
            return APIResponse(url=url, response=resp)
