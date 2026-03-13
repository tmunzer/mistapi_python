"""
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
"""

import json
import os
import re
import time
import urllib.parse
from collections.abc import Callable
from typing import Any

import requests
from requests.exceptions import HTTPError

from mistapi.__api_response import APIResponse
from mistapi.__logger import logger
from mistapi.__models.privilege import Privileges


class APIRequest:
    """
    Class handling API Request to the Mist Cloud
    """

    _MAX_429_RETRIES: int = 3
    _DEFAULT_RETRY_AFTER: int = 5

    def __init__(self) -> None:
        self._cloud_uri: str = ""
        self._session = requests.session()
        self.privileges: Privileges = Privileges([])
        self._count: int = 0
        self._apitoken: list[str] = []
        self._apitoken_index: int = -1

    def get_request_count(self):
        """
        Get the number of API requests sent by the script

        RETURN
        -----------
        str
            number of API calls sent
        """
        return self._count

    def _url(self, uri) -> str:
        """
        Generate the url with the host (in the object) and the uri

        PARAMS
        -----------
        uri : str
            URI where to send the request to (e.g. "/api/v1/...")

        RETURN
        -----------
        str
            Full URL where to send the request to (e.g. "https://api.mist.com/api/v1/...")
        """
        logger.debug("apirequest:_url:https://%s%s", self._cloud_uri, uri)
        return f"https://{self._cloud_uri}{uri}"

    def _log_proxy(self) -> None:
        pwd_regex = r":([^:@]*)@"  # nosec bandit B105
        if self._session.proxies.get("https"):
            logger.info(
                "apirequest:sending request to proxy server %s",
                re.sub(pwd_regex, ":*********@", self._session.proxies["https"]),
            )
            print(
                f"apirequest:sending request to proxy server {re.sub(pwd_regex, ':*********@', self._session.proxies['https'])}"
            )

    def _next_apitoken(self) -> None:
        logger.info("apirequest:_next_apitoken:rotating API Token")
        logger.debug(
            f"apirequest:_next_apitoken:current API Token is "
            f"{self._apitoken[self._apitoken_index][:4]}..."
            f"{self._apitoken[self._apitoken_index][-4:]}"
        )
        new_index = self._apitoken_index + 1
        if new_index >= len(self._apitoken):
            new_index = 0
        if self._apitoken_index != new_index:
            self._apitoken_index = new_index
            self._session.headers.update(
                {"Authorization": "Token " + self._apitoken[self._apitoken_index]}
            )
            logger.debug(
                f"apirequest:_next_apitoken:new API Token is "
                f"{self._apitoken[self._apitoken_index][:4]}..."
                f"{self._apitoken[self._apitoken_index][-4:]}"
            )
        else:
            logger.critical(" /!\\ API TOKEN CRITICAL ERROR /!\\")
            logger.critical(
                " There is no other API Token to use and the API"
                " Request limit has been reached for the current one"
            )
            logger.critical(
                " For large organization, it is recommended to configure"
                " multiple API Tokens (comma separated list) to avoid this issue"
            )
            raise RuntimeError(
                "API rate limit reached and no other API Token available. "
                "For large organizations, configure multiple API Tokens "
                "(comma separated list) to avoid this issue."
            )

    def _gen_query(self, query: dict[str, str] | None) -> str:
        if not query:
            return ""
        return "?" + urllib.parse.urlencode(query)

    def _remove_auth_from_headers(self, resp: requests.Response):
        headers = resp.request.headers
        if "Authorization" in headers:
            headers["Authorization"] = "***hidden***"
        if "X-CSRFToken" in headers:
            headers["X-CSRFToken"] = "***hidden***"
        if "Cookie" in headers:
            headers["Cookie"] = "***hidden***"
        return headers

    def remove_file_from_body(self, resp: requests.Response):
        """
        function used to remove the file from the body response. Used to log the response
        """
        keepit = True
        werein = False
        request_body = ""
        if isinstance(resp.request.body, bytes):
            for i in resp.request.body.decode("utf-8", errors="ignore").split("\r\n"):
                if i.startswith(
                    'Content-Disposition: form-data; name="file";'
                ) or i.startswith('Content-Disposition: form-data; name="csv";'):
                    werein = True
                elif i == "" and werein:
                    keepit = False
                elif i.startswith("--") and not keepit:
                    request_body += "\r\n"
                    werein = False
                    keepit = True
                if keepit:
                    request_body += f"\r\n{i}"
        return request_body

    def _handle_rate_limit(self, resp: requests.Response, attempt: int) -> None:
        retry_after = resp.headers.get("Retry-After")
        if retry_after:
            try:
                wait = int(retry_after)
            except ValueError:
                wait = self._DEFAULT_RETRY_AFTER * (2**attempt)
        else:
            wait = self._DEFAULT_RETRY_AFTER * (2**attempt)
        logger.info(
            "apirequest:rate_limited:sleeping %ss (attempt %s/%s)",
            wait,
            attempt + 1,
            self._MAX_429_RETRIES,
        )
        time.sleep(wait)

    def _request_with_retry(
        self, method_name: str, request_fn: Callable, url: str
    ) -> APIResponse:
        """Shared retry wrapper for all HTTP methods."""
        resp = None
        proxy_failed = False
        for attempt in range(self._MAX_429_RETRIES + 1):
            try:
                logger.info(f"apirequest:{method_name}:sending request to {url}")
                self._log_proxy()
                resp = request_fn()
                logger.debug(
                    f"apirequest:{method_name}:request headers:{self._remove_auth_from_headers(resp)}"
                )
                resp.raise_for_status()
                break
            except requests.exceptions.ProxyError as e:
                logger.error(f"apirequest:{method_name}:Proxy Error: {e}")
                proxy_failed = True
                break
            except requests.exceptions.ConnectionError as e:
                logger.error(f"apirequest:{method_name}:Connection Error: {e}")
                break
            except HTTPError as e:
                if e.response.status_code == 429 and attempt < self._MAX_429_RETRIES:
                    logger.warning(
                        f"apirequest:{method_name}:HTTP 429 (attempt {attempt + 1}/{self._MAX_429_RETRIES})"
                    )
                    try:
                        self._next_apitoken()
                    except RuntimeError:
                        pass  # single token — still retry with backoff
                    self._handle_rate_limit(e.response, attempt)
                    continue
                logger.error(f"apirequest:{method_name}:HTTP error: {e}")
                if resp:
                    logger.error(
                        f"apirequest:{method_name}:HTTP error description: {resp.json()}"
                    )
                break
            except Exception as e:
                logger.error(f"apirequest:{method_name}:error: {e}")
                logger.error(
                    f"apirequest:{method_name}:Exception occurred", exc_info=True
                )
                break
        self._count += 1
        return APIResponse(url=url, response=resp, proxy_error=proxy_failed)

    def mist_get(self, uri: str, query: dict[str, str] | None = None) -> APIResponse:
        """
        GET HTTP Request

        PARAMS
        -----------
        uri : str
            HTTP URI (e.g. "/api/v1/self")
        query : dict
            dict of HTTP Queries (e.g. {"page": 1, "limit":100})

        RETURN
        -----------
        mistapi.APIResponse
            response from the API call
        """
        url = self._url(uri) + self._gen_query(query)
        return self._request_with_retry("mist_get", lambda: self._session.get(url), url)

    def mist_post(self, uri: str, body: dict | list | None = None) -> APIResponse:
        """
        POST HTTP Request

        PARAMS
        -----------
        uri : str
            HTTP URI (e.g. "/api/v1/self")
        body : dict

        RETURN
        -----------
        mistapi.APIResponse
            response from the API call
        """
        url = self._url(uri)
        headers = {"Content-Type": "application/json"}
        logger.debug(f"apirequest:mist_post:Request body:{body}")
        if isinstance(body, str):
            fn = lambda: self._session.post(url, data=body, headers=headers)
        else:
            fn = lambda: self._session.post(url, json=body, headers=headers)
        return self._request_with_retry("mist_post", fn, url)

    def mist_put(self, uri: str, body: dict | None = None) -> APIResponse:
        """
        PUT HTTP Request

        PARAMS
        -----------
        uri : str
            HTTP URI (e.g. "/api/v1/self")
        body : dict

        RETURN
        -----------
        mistapi.APIResponse
            response from the API call
        """
        url = self._url(uri)
        headers = {"Content-Type": "application/json"}
        logger.debug(f"apirequest:mist_put:Request body:{body}")
        if isinstance(body, str):
            fn = lambda: self._session.put(url, data=body, headers=headers)
        else:
            fn = lambda: self._session.put(url, json=body, headers=headers)
        return self._request_with_retry("mist_put", fn, url)

    def mist_delete(self, uri: str, query: dict | None = None) -> APIResponse:
        """
        DELETE HTTP Request

        PARAMS
        -----------
        uri : str
            HTTP URI (e.g. "/api/v1/self")

        RETURN
        -----------
        mistapi.APIResponse
            response from the API call
        """
        url = self._url(uri) + self._gen_query(query)
        return self._request_with_retry(
            "mist_delete", lambda: self._session.delete(url), url
        )

    def mist_post_file(
        self, uri: str, multipart_form_data: dict | None = None
    ) -> APIResponse:
        """
        POST HTTP Request

        PARAMS
        -----------
        uri : str uri
            HTTP URI (e.g. "/api/v1/self")
        multipart_form_data : dict
            dict of key/values to add include in the multipart form

        RETURN
        -----------
        mistapi.APIResponse
            response from the API call
        """
        if multipart_form_data is None:
            multipart_form_data = {}
        url = self._url(uri)
        logger.debug(
            f"apirequest:mist_post_file:initial multipart_form_data:{multipart_form_data}"
        )
        generated_multipart_form_data: dict[str, Any] = {}
        for key in multipart_form_data:
            logger.debug(
                f"apirequest:mist_post_file:"
                f"multipart_form_data:{key} = {multipart_form_data[key]}"
            )
            if multipart_form_data[key]:
                try:
                    if key in ["csv", "file"]:
                        logger.debug(
                            f"apirequest:mist_post_file:reading file:{multipart_form_data[key]}"
                        )
                        f = open(multipart_form_data[key], "rb")
                        generated_multipart_form_data[key] = (
                            os.path.basename(multipart_form_data[key]),
                            f,
                            "application/octet-stream",
                        )
                    else:
                        generated_multipart_form_data[key] = (
                            None,
                            json.dumps(multipart_form_data[key]),
                        )
                except (OSError, json.JSONDecodeError):
                    logger.error(
                        f"apirequest:mist_post_file:multipart_form_data:"
                        f"Unable to parse JSON object {key} "
                        f"with value {multipart_form_data[key]}"
                    )
                    logger.error(
                        "apirequest:mist_post_file: Exception occurred",
                        exc_info=True,
                    )
        logger.debug(
            f"apirequest:mist_post_file:"
            f"final multipart_form_data:{generated_multipart_form_data}"
        )

        def _do_post_file():
            resp = self._session.post(url, files=generated_multipart_form_data)
            logger.debug(
                f"apirequest:mist_post_file:request body:{self.remove_file_from_body(resp)}"
            )
            return resp

        return self._request_with_retry("mist_post_file", _do_post_file, url)
