"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
This module provide the APISession class, which is used to manage authentication
and HTTP session (if login/password is used) with Mist Cloud.
"""

from pathlib import Path
from getpass import getpass
import os
import sys
import requests
from dotenv import load_dotenv

from mistapi.__logger import logger, console
from mistapi.__api_request import APIRequest
from mistapi.__api_response import APIResponse
from mistapi.__models.privilege import Privileges
from mistapi.__version import __version__
###### GLOBALS ######
CLOUDS = [
    {"short": "APAC 01", "host": "api.ac5.mist.com", "cookies_ext": ".ac5"},
    {"short": "EMEA 01", "host": "api.eu.mist.com", "cookies_ext": ".eu"},
    {"short": "EMEA 02", "host": "api.gc3.mist.com", "cookies_ext": ".gc3"},
    {"short": "EMEA 03", "host": "api.ac6.mist.com", "cookies_ext": ".ac6"},
    {"short": "Global 01", "host": "api.mist.com", "cookies_ext": ""},
    {"short": "Global 02", "host": "api.gc1.mist.com", "cookies_ext": ".gc1"},
    {"short": "Global 03", "host": "api.ac2.mist.com", "cookies_ext": ".ac2"},
    {"short": "Global 04", "host": "api.gc2.mist.com", "cookies_ext": ".gc2"},
]

#### PARAMETERS #####


class APISession(APIRequest):
    """Class managing REST API Session"""

    def __init__(
        self,
        email: str = None,
        password: str = None,
        apitoken: str = None,
        host: str = None,
        env_file: str = None,
        console_log_level: str = 20,
        logging_log_level: int = 10,
        show_cli_notif: bool = True,
        https_proxy: str = None,
    ):
        """
        Initialise the APISession class. This class is used to manage Mist API authentication.

        PARAMS
        -----------
        email : str
            used if login/password is used. Can be defined later
        password : str
            used if login/password is used. Can be defined later
        apitoken : str
            used if API Token is used. Can de defined later
        host : str
            Mist Cloud to reach (e.g. "api.mist.com"). Can de defined later
        env_file : str
            path to the env file to load. See README.md for allowed variables
        console_log_level : int, default: 20
            Log level for the console output. Values are:
                50 -> CRITICAL
                40 -> ERROR
                30 -> WARNING
                20 -> INFO
                10 -> DEBUG
                0  -> DISABLED
        logging_log_level : int, default: 10
            Log level for the log file output. Values are:
                Values:
                50 -> CRITICAL
                40 -> ERROR
                30 -> WARNING
                20 -> INFO
                10 -> DEBUG
                0  -> DISABLED
        show_cli_notif : bool, default True
            show/hide package decorative text on the console output
        https_proxy : str, default None
            HTTPS Proxy to use to send the API Requests
        """
        logger.info(f"mistapi:init:package version {__version__}")
        self._cloud_uri = None
        self.email = None
        self._password = None
        self._apitoken = None
        self._apitoken_index = -1
        self._csrftoken = None
        self._authenticated = False
        self._count = 0
        self._session = requests.session()
        self._console_log_level = console_log_level
        self._logging_log_level = logging_log_level
        self._show_cli_notif = show_cli_notif
        self._proxies = {
            "https": https_proxy
        }

        console._set_log_level(console_log_level, logging_log_level)

        self._load_env(env_file)
        self._session.proxies.update(self._proxies)

        if host:
            self.set_cloud(host)
        if email:
            self.set_email(email)
        if password:
            self.set_password(password)
        if apitoken:
            self.set_api_token(apitoken)
        self.first_name = ""
        self.last_name = ""
        self.via_sso = False
        self.tags = []

        self.privileges = Privileges([])
        self.session_expiry = ""

        logger.debug("apisession:__init__: API Session initialized")

    def __str__(self):
        fields = [
            "email",
            "first_name",
            "last_name",
            "phone",
            "via_sso",
            "privileges",
            "session_expiry",
            "tags",
            "authenticated",
        ]
        string = ""
        for field in fields:
            if hasattr(self, field) and getattr(self, field) != "":
                string += f"{field}:\r\n"
                if field == "privileges":
                    string += Privileges(self.privileges).display()
                    string += "\r\n"
                elif field == "tags":
                    for tag in self.tags:
                        string += f"  -  {tag}\r\n"
                elif field == "authenticated":
                    string += f"{self.get_authentication_status()}\r\n"
                else:
                    string += f"{getattr(self, field)}\r\n"
                string += "\r\n"
        return string

    ####################################
    # LOAD FUNCTIONS
    def _load_env(self, env_file=None) -> None:
        """
        Load Mist API settings from env file
        """
        if env_file:
            if env_file.startswith("~/"):
                env_file = os.path.join(
                    os.path.expanduser("~"), env_file.replace("~/", "")
                )
            env_file = os.path.abspath(env_file)
            console.debug(f"Loading settings from {env_file}")
            logger.debug(f"apisession:_load_env:loading settings from {env_file}")
            dotenv_path = Path(env_file)
            load_dotenv(dotenv_path=dotenv_path, override=True)
        # else:
        #     console.debug("Loading settings from env file")
        #     logger.debug(f"apisession:_load_env:loading settings from env file")
        #     load_dotenv()

        if os.getenv("MIST_HOST"):
            self.set_cloud(os.getenv("MIST_HOST"))
        if os.getenv("MIST_APITOKEN"):
            self.set_api_token(os.getenv("MIST_APITOKEN"))
        if os.getenv("MIST_USER"):
            self.set_email(os.getenv("MIST_USER"))
        if os.getenv("MIST_PASSWORD"):
            self.set_password(os.getenv("MIST_PASSWORD"))
        if os.getenv("CONSOLE_LOG_LEVEL"):
            self._console_log_level = os.getenv("CONSOLE_LOG_LEVEL")
        if os.getenv("LOGGING_LOG_LEVEL"):
            self._logging_log_level = os.getenv("LOGGING_LOG_LEVEL")
        if os.getenv("HTTPS_PROXY"):
            self._proxies["https"] = os.getenv("HTTPS_PROXY")

    ####################################
    # CLOUD FUNCTIONS
    def set_cloud(self, cloud_uri: str) -> None:
        """
        Set Mist Cloud to reach.

        PARAMS
        -----------
        cloud_uri : str
            Mist FQDN to reach ("api.mist.com", "api.eu.mist.com", ...)
        """
        logger.debug("apisession:set_cloud")
        self._cloud_uri = None
        if cloud_uri in ["api.mistsys.com", "api.ac99.mist.com", "api.gc1.mistsys.com", "api.us.mist-federal.com"]:
            self._cloud_uri = cloud_uri
        else:
            for cloud in CLOUDS:
                if cloud["host"] == cloud_uri:
                    self._cloud_uri = cloud_uri
        if self._cloud_uri:
            logger.debug(
                f"apisession:set_cloud:Mist Cloud configured to {self._cloud_uri}"
            )
            console.debug(f"Mist Cloud configured to {self._cloud_uri}")
        else:
            logger.error(f"apisession:set_cloud: {cloud_uri} is not valid")
            console.error(f"{cloud_uri} is not valid")

    def get_cloud(self):
        """
        Return the Mist Cloud currently configured
        """
        logger.debug(f"apisession:get_cloud:return {self._cloud_uri}")
        return self._cloud_uri

    def select_cloud(self) -> None:
        """
        Display a menu to select the Mist Cloud
        """
        logger.debug("apisession:select_cloud")
        if self._show_cli_notif:
            print()
            print(" Mist Cloud Selection ".center(80, "-"))
            print()

        resp = "x"
        i = 0
        for cloud in CLOUDS:
            print(f"{i}) {cloud['short']} (host: {cloud['host']})")
            i += 1

        print()
        resp = input(f"Select a Cloud (0 to {i-1}, or q to quit): ")
        logger.info(f"apisession:select_cloud:input is {resp}")
        if resp == "q":
            sys.exit(0)
        elif resp == "i":
            self._cloud_uri = "api.mistsys.com"
        elif resp == "c":
            self._cloud_uri = "api.ac99.mist.com"
        elif resp == "g":
            self._cloud_uri = "api.gc1.mistsys.com"
        elif resp == "f":
            self._cloud_uri = "api.us.mist-federal.com"
        else:
            try:
                resp_num = int(resp)
                if resp_num >= 0 and resp_num < i:
                    logger.info(
                        f"apisession:select_cloud:Mist Cloud is {CLOUDS[resp_num]['host']}"
                    )
                    self.set_cloud(CLOUDS[resp_num]["host"])
                else:
                    print(f"Please enter a number between 0 and {i}.")
                    logger.error(
                        f"apisession:select_cloud:{resp} is not a valid input"
                    )
                    self.select_cloud()
            except:
                print("\r\nPlease enter a number.")
                logger.error(f"apisession:select_cloud:{resp} is not a valid input")
                self.select_cloud()

    ####################################
    # AUTH FUNCTIONS
    def set_email(self, email: str = None) -> None:
        """
        Set the user email

        PARAMS
        -----------
        email : str
            If no email provided, an interactive input will ask for it
        """
        logger.debug("apisession:set_email")
        if email:
            self.email = email
        else:
            self.email = input("Login: ")
        logger.info(f"apisession:set_email:email configured to {self.email}")
        console.debug(f"Email configured to {self.email}")

    def set_password(self, password: str = None) -> None:
        """
        Set the user password

        PARAMS
        -----------
        password : str
            If no password provided, an interactive input will ask for it
        """
        logger.debug("apisession:set_password")
        if password:
            self._password = password
        else:
            self._password = getpass("Password: ")
        logger.info("apisession:set_password:password configured")
        console.debug("Password configured")

    def set_api_token(self, apitoken: str) -> None:
        """
        Set Mist API Token

        PARAMS
        -----------
        apitoken : str
            API Token to add in the requests headers for authentication and authorization
        """
        logger.debug("apisession:set_api_token")
        apitokens_in = apitoken.split(",")
        apitokens_out = []
        for token in apitokens_in:
            token = token.strip()
            if token and not token in apitokens_out:
                apitokens_out.append(token)
        logger.info(f"apisession:set_api_token:found {len(apitokens_out)} API Tokens")
        if self._check_api_tokens(apitokens_out):
            self._apitoken = apitokens_out
            self._apitoken_index = 0
            self._session.headers.update({
                "Authorization": "Token " + self._apitoken[self._apitoken_index]
                })
            logger.info("apisession:set_api_token:API Token configured")
            console.debug("API Token configured")

    def _get_api_token_data(self, apitoken) -> (str, list):
        token_privileges = []
        token_type = "org"
        try:
            url = f"https://{self._cloud_uri}/api/v1/self"
            headers = {"Authorization": "Token " + apitoken}
            data = requests.get(url, headers=headers, proxies=self._proxies)
            data_json = data.json()
            logger.debug(
                f"apisession:_get_api_token_data:"
                f"info retrieved for token {apitoken[:4]}...{apitoken[-4:]}"
                )
        except requests.exceptions.ProxyError as proxy_error:
            logger.critical("apisession:_get_api_token_data:proxy not valid...")
            console.critical("Proxy not valid...\r\n")        
            sys.exit(0)
        except requests.exceptions.ConnectionError as connexion_error:
            logger.critical(f"apirequest:mist_post:Connection Error: {connexion_error}")
            console.critical("Connexion error...\r\n")        
            sys.exit(0)
        except:
            logger.error(
                f"apisession:_get_api_token_data:"
                f"unable to retrieve info for token {apitoken[:4]}...{apitoken[-4:]}"
            )
            logger.error("apirequest:_get_api_token_data: Exception occurred", exc_info=True)
            return (None, None)

        if data_json.get("email"):
            token_type = "user"

        for priv in data_json.get("privileges"):
            tmp = {
                "scope": priv.get("scope"),
                "role": priv.get("role"),
                "name": priv.get("name"),
            }
            if priv.get("scope") == "msp":
                tmp["id"] = priv.get("msp_id")
                token_privileges.append(tmp)
            elif priv.get("scope") == "org":
                tmp["id"] = priv.get("org_id")
                token_privileges.append(tmp)
            elif priv.get("scope") == "site":
                tmp["id"] = priv.get("site_id")
                token_privileges.append(tmp)
            else:
                logger.error(
                    f"apisession:_check_api_tokens:"
                    f"unable to process privileges {priv} for the {token_type} "
                    f"token {apitoken[:4]}...{apitoken[-4:]}"
                )
        return (token_type, token_privileges)

    def _check_api_tokens(self, apitokens) -> None:
        """
        Function used when multiple API tokens are provided, to validate they
        have same privileges
        """
        logger.debug("apisession:_check_api_tokens")
        if len(apitokens) == 0:
            logger.error("apisession:_check_api_tokens:there is not API token to check")
        elif (len(apitokens)) == 1:
            logger.info(
                "apisession:_check_api_tokens:there is only 1 API token. No check required"
            )
        else:
            primary_token_privileges = []
            primary_token_type = ""
            primary_token_value = ""
            for token in apitokens:
                token_value = f"{token[:4]}...{token[-4:]}"
                (token_type, token_privileges ) = self._get_api_token_data(token)
                if len(primary_token_privileges) == 0:
                    primary_token_privileges = token_privileges
                    primary_token_type = token_type
                    primary_token_value = token_value
                elif primary_token_privileges == token_privileges:
                    logger.info(
                        f"apisession:_check_api_tokens:"
                        f"{token_type} API Token {token_value} has same privileges as "
                        f"the {primary_token_type} API Token {primary_token_value}"
                        )
                else:
                    logger.critical(
                        f"apisession:_check_api_tokens:"
                        f"{token_type} API Token {token_value} has different privileges "
                        f"than the {primary_token_type} API Token {primary_token_value}"
                        )
                    logger.critical(" /!\\ API TOKEN CRITICAL ERROR /!\\")
                    logger.critical(
                        " When using multiple API Tokens, be sure they are all linked"
                        " to the same Org/User, and all have the same privileges"
                        )
                    logger.critical(" Exiting...")
                    sys.exit(255)
        return True

    def _process_login(self, retry: bool = True) -> None:
        """
        Function to authenticate a user with login/password.
        Will create and store a session used by other requests.

        PARAMS
        -----------
        retry : bool, default True
            if `retry`==True, ask for login/password when authentication is failing
        """
        logger.debug("apisession:_process_login")
        error = None
        if self._show_cli_notif:
            print()
            print(" Login/Pwd authentication ".center(80, "-"))
            print()

        self._session = requests.session()
        if not self.email:
            self.set_email()
        if not self._password:
            self.set_password()

        logger.debug("apisession:_process_login:email/password configured")
        uri = "/api/v1/login"
        body = {"email": self.email, "password": self._password}
        resp = self._session.post(self._url(uri), json=body)
        if resp.status_code == 200:
            logger.info("apisession:_process_login:authentication successful!")
            console.info("Authentication successful!")
            self._set_authenticated(True)
        else:
            error = resp.json().get("detail")
            logger.error(f"apisession:_process_login:authentication failed:{error}")
            console.error(f"Authentication failed: {error}\r\n")
            self.email = None
            self._password = None
            logger.info(
                "apisession:_process_login:"
                "email/password cleaned up. Restarting authentication function"
            )
            if retry:
                return self._process_login(retry)

        return error

    def login(self) -> None:
        """
        Log in on the Mist Cloud.
        If information are missing to get connected, they will be requested
        during the process.
        If login/password is used, 2FA may be requests. Once authenticated,
        the HTTP session and CSRF Token will be stored and used during the
        future API requests.
        """
        logger.debug("apisession:login")
        if self._authenticated:
            logger.warning("apisession:login:already logged in...")
            console.info("Already logged in...")
        else:
            logger.debug("apisession:login:not authenticated yet")
            if not self._cloud_uri:
                self.select_cloud()
            if self._apitoken:
                self._set_authenticated(True)
            if not self._authenticated:
                self._process_login()
            # if successfuly authenticated
            if self.get_authentication_status():
                logger.info("apisession:login:authenticated")
                self._getself()

    def login_with_return(
        self,
        apitoken: str = "",
        email: str = "",
        password: str = "",
        two_factor: str = None,
    ):
        """
        Log in on the Mist Cloud.
        This function will return the authentication result an object with the
        authentication result and the error message send by the Mist Cloud (if
        any).
        Credentials (apitoken or login/pwd) may be provided in the function
        parameters, otherwise the credentials provided during the class
        initialization will be reused.

        PARAMS
        -----------
        apitoken : str
            Optional, API Token to add in the requests headers for
            authentication and authorization
        email : str
            Optional, user email
        password : str
            Optional, user password
        two_factor : str
            Optional, 2FA code to send to the Mist Cloud

        RETURN
        -----------
        dict
            success : bool
                Authentication result
            message : str
                Error message from Mist (if any)
        """
        logger.debug("apisession:login_with_return")
        self._session = requests.session()
        if apitoken:
            self.set_api_token(apitoken)
        if email:
            self.set_email(email)
        if password:
            self.set_password(password)

        if self._apitoken:
            logger.debug("apisession:login_with_return:apitoken provided")
            self._set_authenticated(True)
            logger.info("apisession:login_with_return:get self")
            uri = "/api/v1/self"
            logger.info(f'apisession:login_with_return: sending GET request to "{uri}"')
            resp = self.mist_get(uri)

        elif self.email and self._password:
            if two_factor:
                logger.debug(
                    "apisession:login_with_return:login/pwd provided witht 2FA"
                )
                error = self._two_factor_authentication(two_factor)
            else:
                logger.debug(
                    "apisession:login_with_return:login/pwd provided w/o 2FA"
                )
                error = self._process_login(retry=False)
            if error:
                logger.error(
                    f"apisession:login_with_return:login/pwd auth faild: {error}"
                )
                return {"authenticated": False, "error": error}
            logger.info("apisession:login_with_return:get self")
            uri = "/api/v1/self"
            logger.info(f'apisession:login_with_return: sending GET request to "{uri}"')
            resp = self.mist_get(uri)

        else:
            logger.error("apisession:login_with_return:credentials are missing")
            return {"authenticated": False, "error": "credentials are missing"}

        if resp.status_code == 200 and not resp.data.get("two_factor_required", False):
            logger.info("apisession:login_with_return:access authorized")
            return {"authenticated": True, "error": ""}
        else:
            logger.error(f"apisession:login_with_return:access denied: {resp.data}")
            return {"authenticated": False, "error": resp.data}

    def logout(self) -> None:
        """
        Log out from the Mist Cloud.
        If login/password is used, the HTTP session is destroyed.
        """
        logger.debug("apisession:logout")
        if not self._authenticated:
            logger.error("apisession:logout:not logged in...")
            console.error("Not logged in...")
        else:
            uri = "/api/v1/logout"
            resp = self.mist_post(uri)
            if resp.status_code == 200:
                logger.info("apisession:logout:Mist Session closed and cleaned up")
                console.info("Logged out")
                self._set_authenticated(False)
            else:
                try:
                    console.error(resp.data["detail"])
                except:
                    console.error(resp.raw_data)

    def _set_authenticated(self, authentication_status: bool) -> None:
        """
        Set the authentication status.
        If True and Login/password is used, extract the HTTP session and
        CSRF Token from the cookies and store them in memory to be used
        during the future API requests.
        If False, clear the CSRF Token and delete the HTTP session.

        PARAMS
        -----------
        authentication_status : bool
        """
        logger.debug("apisession:_set_authenticated")
        logger.debug(
            f"apisession:_set_authenticated:authentication_status is {authentication_status}"
        )
        if authentication_status:
            self._authenticated = True
            logger.info(
                f'apisession:_set_authenticated: session is now "Authenticated"'
            )
            if not self._apitoken:
                logger.info("apisession:_set_authenticated:processing HTTP cookies")
                try:
                    if self._cloud_uri == "api.mistsys.com":
                        cookies_ext = ""
                    elif self._cloud_uri == "api.ac99.mist.com":
                        cookies_ext= ".ac99"
                    elif self._cloud_uri == "api.gc1.mistsys.com":
                        cookies_ext= ".gc1"
                    elif self._cloud_uri == "api.us.mist-federal.com":
                        cookies_ext= ".us"
                    else:
                        cookies_ext = next(
                            item["cookies_ext"]
                            for item in CLOUDS
                            if item["host"] == self._cloud_uri
                        )
                    logger.info(
                        f"apisession:_set_authenticated:HTTP session cookies extracted. Cookies extension is {cookies_ext}"
                    )
                except:
                    cookies_ext = ""
                    logger.error(
                        "apisession:_set_authenticated:unable to extract HTTP session cookies"
                    )
                    logger.error(
                        "apirequest:mist_post_file: Exception occurred", exc_info=True
                    )
                self._csrftoken = self._session.cookies["csrftoken" + cookies_ext]
                self._session.headers.update({"X-CSRFToken": self._csrftoken})
                logger.info("apisession:_set_authenticated:CSRF Token stored")
        elif authentication_status is False:
            self._authenticated = False
            logger.info(
                f'apisession:_set_authenticated: session is now "Unauthenticated"'
            )
            self._csrftoken = ""
            del self._session
            logger.info(
                "apisession:_set_authenticated:CSRF Token is cleaned up and HTTP Session deleted"
            )

    def get_authentication_status(self) -> bool:
        """
        RETURN
        -----------
        bool
            Return the authentication status.
        """
        logger.debug(
            f"apisession:get_authentication_status:return {self._authenticated}"
        )
        return self._authenticated

    def get_api_token(self) -> APIResponse:
        """
        Retrieve and display the User/Org API Tokens

        RETURN
        -----------
        mistapi.APIResponse
            api response for the GET /api/v1/self request
        """
        logger.info(
            f'apisession:get_api_token: Sending GET request to "/api/v1/self/apitokens"'
        )
        resp = self.mist_get("/api/v1/self/apitokens")
        return resp

    def create_api_token(self, token_name: str = None) -> APIResponse:
        """
        Create a new API Token with the current account (user/org)

        PARAMS
        -----------
        token_name : str
            API token name (optional)

        RETURN
        -----------
        mistapi.APIResponse
            api response for the POST /api/v1/self/apitokens request
        """
        logger.debug("apisession:create_api_token")
        if token_name:
            body = {"name": token_name}
        logger.info(
            f"apisession:create_api_token:"
            f"sending POST request to \"/api/v1/self/apitokens\" with name \"{token_name}\""
        )
        resp = self.mist_post("/api/v1/self/apitokens", body=body)
        return resp

    def delete_api_token(self, apitoken_id: str) -> APIResponse:
        """
        Delete an API Token based on its token_id

        PARAMS
        -----------
        apitoken_id : str
            API Token ID to delete

        RETURN
        -----------
        mistapi.APIResponse
            api response for the DELETE /api/v1/self/apitokens/{apitoken_id} request
        """
        logger.debug("apisession:delete_api_token")
        logger.info(
            f"apisession:delete_api_token:"
            f"sending DELETE request to \"/api/v1/self/apitokens\" with token_id \"{apitoken_id}\""
        )
        uri = f"https://{self._cloud_uri}/api/v1/self/apitokens/{apitoken_id}"
        resp = self._session.delete(uri)
        return resp

    def _two_factor_authentication(self, two_factor: str) -> bool:
        """
        Function called when 2FA is requested by Mist Cloud to authenticate
        with 2FA enabled

        PARAMS
        -----------
        two_factor : str
            2FA code to send to the Mist Cloud

        RETURN
        -----------
        bool
            True if authentication succeed, False otherwise
        """
        logger.debug("apisession:_two_factor_authentication")
        uri = "/api/v1/login"
        body = {
            "email": self.email,
            "password": self._password,
            "two_factor": two_factor,
        }
        resp = self._session.post(self._url(uri), json=body)
        if resp.status_code == 200:
            logger.info(
                "apisession:_two_factor_authentication:2FA authentication successed"
            )
            console.info("2FA authentication successed")
            self._set_authenticated(True)
            return True
        else:
            logger.error(
                f"apisession:_two_factor_authentication:"
                f"2FA authentication failed with error code: {resp.status_code}"
            )
            console.error(
                f"2FA authentication failed with error code: {resp.status_code}\r\n"
            )
            return False

    def _getself(self) -> None:
        """
        Retrieve information about the current user and store them in the current object.
        """
        logger.debug("apisession:_getself")
        uri = "/api/v1/self"
        logger.info(f'apisession:_getself: sending GET request to "{uri}"')
        resp = self.mist_get(uri)
        if resp.status_code == 200 and resp.data:
            # Deal with 2FA if needed
            if (
                resp.data.get("two_factor_required") is True
                and resp.data.get("two_factor_passed") is False
            ):
                logger.info("apisession:_getself:2FA request by Mist Cloud")
                two_factor_ok = False
                while not two_factor_ok:
                    two_factor = input("Two Factor Authentication code required: ")
                    two_factor_ok = self._two_factor_authentication(two_factor)
                self._getself()
            # Get details of the account
            else:
                logger.info(
                    "apisession:_getself:authentication Ok. Processing account privileges"
                )
                for key, val in resp.data.items():
                    if key == "privileges":
                        self.privileges = Privileges(resp.data["privileges"])
                    if key == "tags":
                        for tag in resp.data["tags"]:
                            self.tags.append(tag)
                    else:
                        setattr(self, key, val)
                if self._show_cli_notif:
                    print()
                    print(" Authenticated ".center(80, "-"))
                    print(f"\r\nWelcome {self.first_name} {self.last_name}!\r\n")
                logger.info(
                    f"apisession:_getself:account used: {self.first_name} {self.last_name}"
                )
                return True
        elif resp.proxy_error:
            logger.critical("apisession:_getself:proxy not valid...")
            console.critical("Proxy not valid...\r\n")        
            sys.exit(0)
        else:
            logger.error("apisession:_getself:authentication not valid...")
            console.error("Authentication not valid...\r\n")
            resp = input(
                f"Do you want to try with new credentials for {self._cloud_uri} (y/N)? "
            )
            if resp.lower() == "y":
                self._process_login()
                return self._getself()
            else:
                sys.exit(0)

    ####################################
    # PRIVILEGES

    def get_privilege_by_org_id(self, org_id: str):
        """
        return the User privileges for the specific org_id. The privileges are
        calculated based on the MSP and the Org privileges.

        PARAMS
        -----------
        :org_id : str
            org_id for which the function must return the user's privileges

        RETURN
        -----------
        dict
            user's privileges for the org_id
        """
        logger.debug("apisession:get_privilege_by_org_id")
        org_priv = next(
            (priv for priv in self.privileges if priv.get("org_id") == org_id), None
        )
        if org_priv:
            logger.info(
                f"apisession:get_privilege_by_org_id:"
                f"org {org_id} privileges found in user info"
            )
            logger.debug(f"apisession:get_privilege_by_org_id: {org_priv}")
            return org_priv
        else:
            logger.warn(
                f"apisession:get_privilege_by_org_id:"
                f"unable of find org {org_id} privileges in user data"
            )
            logger.info(
                f"apisession:get_privilege_by_org_id:"
                f"trying to request org {org_id} info from the Cloud"
            )
            uri = f"/api/v1/orgs/{org_id}"
            msp_id = None
            try:
                resp = self.mist_get(uri)
                if resp.data and resp.data.get("msp_id"):
                    logger.info(
                        f"apisession:get_privilege_by_org_id:"
                        f"org {org_id} belong to msp_id {resp.data['msp_id']}"
                    )
                    msp_id = resp.data.get("msp_id")
                else:
                    logger.warn(
                        "apisession:get_privilege_by_org_id:"
                        "not able to find msp_id information in the org info"
                    )
            except:
                logger.error(
                    "apisession:get_privilege_by_org_id: error when retrieving org info"
                )
                logger.error(
                    "apirequest:mist_post_file: Exception occurred", exc_info=True
                )
            if msp_id:
                msp_priv = next(
                    (
                        priv
                        for priv in self.privileges
                        if priv.get("scope") == "msp" and priv.get("msp_id") == msp_id
                    ),
                    None,
                )
                if not msp_priv:
                    logger.warning(
                        f"apisession:get_privilege_by_org_id:"
                        f"unable of find msp {msp_id} privileges in user data"
                    )
                else:
                    return {
                        "scope": "org",
                        "org_id": org_id,
                        "name": resp.data.get("name"),
                        "role": msp_priv["role"],
                        "msp_id": msp_id,
                        "msp_name": msp_priv["name"],
                        "orggroup_ids": resp.data.get("orggroup_ids"),
                        "msp_logo_url": resp.data.get("logo_url"),
                    }
            return {}
