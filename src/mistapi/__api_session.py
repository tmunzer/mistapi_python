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

import os
import sys
from getpass import getpass
from pathlib import Path

import hvac
import keyring
import requests
from dotenv import load_dotenv
from requests import Response, Session

from mistapi.__api_request import APIRequest
from mistapi.__api_response import APIResponse
from mistapi.__logger import console as CONSOLE
from mistapi.__logger import logger as LOGGER
from mistapi.__models.privilege import Privileges
from mistapi.__version import __version__

###### GLOBALS ######
CLOUDS = [
    {"short": "APAC 01", "host": "api.ac5.mist.com", "cookies_ext": ".ac5"},
    {"short": "APAC 02", "host": "api.gc5.mist.com", "cookies_ext": ".gc5"},
    {"short": "APAC 03", "host": "api.gc7.mist.com", "cookies_ext": ".gc7"},
    {"short": "EMEA 01", "host": "api.eu.mist.com", "cookies_ext": ".eu"},
    {"short": "EMEA 02", "host": "api.gc3.mist.com", "cookies_ext": ".gc3"},
    {"short": "EMEA 03", "host": "api.ac6.mist.com", "cookies_ext": ".ac6"},
    {"short": "EMEA 04", "host": "api.gc6.mist.com", "cookies_ext": ".gc6"},
    {"short": "Global 01", "host": "api.mist.com", "cookies_ext": ""},
    {"short": "Global 02", "host": "api.gc1.mist.com", "cookies_ext": ".gc1"},
    {"short": "Global 03", "host": "api.ac2.mist.com", "cookies_ext": ".ac2"},
    {"short": "Global 04", "host": "api.gc2.mist.com", "cookies_ext": ".gc2"},
    {"short": "Global 05", "host": "api.gc4.mist.com", "cookies_ext": ".gc4"},
]

#### PARAMETERS #####


class APISession(APIRequest):
    """Class managing REST API Session"""

    def __init__(
        self,
        email: str | None = None,
        password: str | None = None,
        apitoken: str | None = None,
        host: str | None = None,
        env_file: str | None = None,
        vault_url: str | None = None,
        vault_token: str | None = None,
        vault_mount_point: str | None = None,
        vault_path: str | None = None,
        keyring_service: str | None = None,
        console_log_level: int = 20,
        logging_log_level: int = 10,
        show_cli_notif: bool = True,
        https_proxy: str | None = None,
    ) -> None:
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
        vault_url : str
            URL of the HashiCorp Vault instance
        vault_mount_point : str
            Mount point for the secrets engine
        vault_path : str
            Path to the secret in Vault
        vault_token : str
            Token for authenticating with Vault
        keyring_service : str
            keyring service name to load Mist API settings from system keyring
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
        super().__init__()
        LOGGER.info("mistapi:init:package version %s", __version__)
        self._cloud_uri: str = ""
        self.email: str | None = None
        self._password: str | None = None
        self._apitoken: list[str] = []
        self._apitoken_index: int = -1
        self._csrftoken: str | None = None
        self._authenticated: bool = False
        self._count: int = 0
        self._session: Session = requests.session()
        self._session.headers["Accept"] = "application/json, application/vnd.api+json"
        self._console_log_level = console_log_level
        self._logging_log_level = logging_log_level
        self._show_cli_notif = show_cli_notif
        self._proxies = {"https": https_proxy}
        self.vault_url = vault_url
        self.vault_path = vault_path
        self.vault_mount_point = vault_mount_point
        self.vault_token = vault_token

        CONSOLE._set_log_level(console_log_level, logging_log_level)
        self._load_env(env_file)
        if keyring_service:
            self._load_keyring(keyring_service)
        if self.vault_path:
            self._load_vault()
        # Filter out None values before updating proxies
        filtered_proxies = {k: v for k, v in self._proxies.items() if v is not None}
        self._session.proxies.update(filtered_proxies)

        if host:
            self.set_cloud(host)
        if email:
            self.set_email(email)
        if password:
            self.set_password(password)
        if apitoken:
            self.set_api_token(apitoken)
        self.first_name: str = ""
        self.last_name: str = ""
        self.via_sso: bool = False
        self.tags: list[str] = []

        self.privileges: Privileges = Privileges([])
        self.session_expiry: int = -1

        LOGGER.debug("apisession:__init__: API Session initialized")

    def __str__(self) -> str:
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
                    if isinstance(self.privileges, Privileges):
                        string += self.privileges.display()
                    else:
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
    def _load_vault(
        self,
    ) -> None:
        """
        Load Vault settings from env file
        """
        LOGGER.info("apisession:_load_vault: Loading Vault settings")
        client = hvac.Client(url=self.vault_url, token=self.vault_token, verify=False)
        if not client.is_authenticated():
            LOGGER.error("apisession:_load_vault: Vault authentication failed")
            CONSOLE.error("Vault authentication failed")
            return
        LOGGER.debug(
            "apisession:_load_vault: Vault authentication successful. Retrieving secret"
        )
        try:
            read_response = client.secrets.kv.v2.read_secret(
                path=self.vault_path, mount_point=self.vault_mount_point
            )
            LOGGER.info("apisession:_load_vault: Secret retrieved successfully")

            mist_host = read_response["data"]["data"].get("MIST_HOST", None)
            LOGGER.info("apisession:_load_vault: MIST_HOST=%s", mist_host)
            if mist_host:
                self.set_cloud(mist_host)

            mist_apitoken = read_response["data"]["data"].get("MIST_APITOKEN", None)
            if mist_apitoken:
                self.set_api_token(mist_apitoken)
        except (KeyError, TypeError, AttributeError):
            LOGGER.error("apisession:_load_vault: Failed to retrieve secret")
            CONSOLE.error("Failed to retrieve secret")
        finally:
            del self.vault_url
            del self.vault_path
            del self.vault_mount_point
            del self.vault_token

    def _load_keyring(self, keyring_service) -> None:
        """
        Load Mist API settings from keyring
        """
        LOGGER.info(
            "apisession:_load_keyring: Loading settings from keyring with keyring service %s",
            keyring_service,
        )
        if keyring_service:
            try:
                mist_host = keyring.get_password(keyring_service, "MIST_HOST")
                if mist_host:
                    LOGGER.info("apisession:_load_keyring: MIST_HOST=%s", mist_host)
                    self.set_cloud(mist_host)
                mist_apitoken = keyring.get_password(keyring_service, "MIST_APITOKEN")
                if mist_apitoken:
                    if isinstance(mist_apitoken, str):
                        for token in mist_apitoken.split(","):
                            token = token.strip()
                            LOGGER.info(
                                "apisession:_load_keyring: Found MIST_APITOKEN=%s...%s",
                                token[:4],
                                token[-4:],
                            )
                    self.set_api_token(mist_apitoken)
                mist_user = keyring.get_password(keyring_service, "MIST_USER")
                if mist_user:
                    LOGGER.info("apisession:_load_keyring: MIST_USER=%s", mist_user)
                    self.set_email(mist_user)
                mist_password = keyring.get_password(keyring_service, "MIST_PASSWORD")
                if mist_password:
                    LOGGER.info("apisession:_load_keyring: MIST_PASSWORD retrieved")
                    self.set_password(mist_password)
            except Exception as e:
                LOGGER.error(
                    "apisession:_load_keyring: Failed to retrieve settings from keyring: %s",
                    e,
                )
                CONSOLE.error("Failed to retrieve settings from keyring")

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
            CONSOLE.debug(f"Loading settings from {env_file}")
            LOGGER.debug("apisession:_load_env:loading settings from %s", env_file)
            dotenv_path = Path(env_file)
            load_dotenv(dotenv_path=dotenv_path, override=True)
        # else:
        #     CONSOLE.debug("Loading settings from env file")
        #     LOGGER.debug(f"apisession:_load_env:loading settings from env file")
        #     load_dotenv()

        if os.getenv("MIST_HOST"):
            self.set_cloud(os.getenv("MIST_HOST", ""))

        if os.getenv("MIST_APITOKEN"):
            self.set_api_token(os.getenv("MIST_APITOKEN", ""))

        if os.getenv("MIST_USER"):
            self.set_email(os.getenv("MIST_USER"))

        if os.getenv("MIST_PASSWORD"):
            self.set_password(os.getenv("MIST_PASSWORD"))

        console_log_level_env = os.getenv("CONSOLE_LOG_LEVEL")
        if console_log_level_env:
            try:
                self._console_log_level = int(console_log_level_env)
            except ValueError:
                self._console_log_level = 20  # Default fallback

        logging_log_level_env = os.getenv("LOGGING_LOG_LEVEL")
        if logging_log_level_env:
            try:
                self._logging_log_level = int(logging_log_level_env)
            except ValueError:
                self._logging_log_level = 10  # Default fallback

        if os.getenv("MIST_VAULT_URL") and not self.vault_url:
            self.vault_url = os.getenv("MIST_VAULT_URL")

        if os.getenv("MIST_VAULT_PATH") and not self.vault_path:
            self.vault_path = os.getenv("MIST_VAULT_PATH")

        if os.getenv("MIST_VAULT_MOUNT_POINT") and not self.vault_mount_point:
            self.vault_mount_point = os.getenv("MIST_VAULT_MOUNT_POINT")

        if os.getenv("MIST_VAULT_TOKEN") and not self.vault_token:
            self.vault_token = os.getenv("MIST_VAULT_TOKEN")

        if os.getenv("MIST_KEYRING_SERVICE"):
            self.keyring_service = os.getenv("MIST_KEYRING_SERVICE")

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
        LOGGER.debug("apisession:set_cloud")
        self._cloud_uri = ""
        if cloud_uri in [
            "api.mistsys.com",
            "api.ac99.mist.com",
            "api.gc1.mistsys.com",
            "api.us.mist-federal.com",
        ]:
            self._cloud_uri = cloud_uri
        else:
            for cloud in CLOUDS:
                if cloud["host"] == cloud_uri:
                    self._cloud_uri = cloud_uri
        if self._cloud_uri:
            LOGGER.debug(
                "apisession:set_cloud:Mist Cloud configured to %s", self._cloud_uri
            )
            CONSOLE.debug(f"Mist Cloud configured to {self._cloud_uri}")
        else:
            LOGGER.error("apisession:set_cloud: %s is not valid", cloud_uri)
            CONSOLE.error(f"{cloud_uri} is not valid")

    def get_cloud(self):
        """
        Return the Mist Cloud currently configured
        """
        LOGGER.debug("apisession:get_cloud:return %s", self._cloud_uri)
        return self._cloud_uri

    def select_cloud(self) -> None:
        """
        Display a menu to select the Mist Cloud
        """
        LOGGER.debug("apisession:select_cloud")
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
        resp = input(f"Select a Cloud (0 to {i - 1}, or q to quit): ")
        LOGGER.info("apisession:select_cloud:input is %s", resp)
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
                    LOGGER.info(
                        "apisession:select_cloud:Mist Cloud is %s",
                        CLOUDS[resp_num]["host"],
                    )
                    self.set_cloud(CLOUDS[resp_num]["host"])
                else:
                    print(f"Please enter a number between 0 and {i}.")
                    LOGGER.error(
                        "apisession:select_cloud:%s is not a valid input", resp
                    )
                    self.select_cloud()
            except ValueError:
                print("\r\nPlease enter a number.")
                LOGGER.error("apisession:select_cloud:%s is not a valid input", resp)
                self.select_cloud()

    ####################################
    # AUTH FUNCTIONS
    def set_email(self, email: str | None = None) -> None:
        """
        Set the user email

        PARAMS
        -----------
        email : str
            If no email provided, an interactive input will ask for it
        """
        LOGGER.debug("apisession:set_email")
        if email:
            self.email = email
        else:
            self.email = input("Login: ")
        LOGGER.info("apisession:set_email:email configured to %s", self.email)
        CONSOLE.debug(f"Email configured to {self.email}")

    def set_password(self, password: str | None = None) -> None:
        """
        Set the user password

        PARAMS
        -----------
        password : str
            If no password provided, an interactive input will ask for it
        """
        LOGGER.debug("apisession:set_password")
        if password:
            self._password = password
        else:
            self._password = getpass("Password: ")
        LOGGER.info("apisession:set_password:password configured")
        CONSOLE.debug("Password configured")

    def set_api_token(self, apitoken: str) -> None:
        """
        Set Mist API Token

        PARAMS
        -----------
        apitoken : str
            API Token to add in the requests headers for authentication and authorization
        """
        LOGGER.debug("apisession:set_api_token")
        apitokens_in = apitoken.split(",")
        apitokens_out: list[str] = []
        for token in apitokens_in:
            token = token.strip()
            if token and token not in apitokens_out:
                apitokens_out.append(token)
        LOGGER.info("apisession:set_api_token:found %s API Tokens", len(apitokens_out))

        valid_api_tokens = self._check_api_tokens(apitokens_out)
        if valid_api_tokens:
            self._apitoken = valid_api_tokens
            self._apitoken_index = 0
            self._session.headers.update(
                {"Authorization": "Token " + self._apitoken[self._apitoken_index]}
            )
            LOGGER.info("apisession:set_api_token:API Token configured")
            CONSOLE.debug("API Token configured")
        else:
            LOGGER.error("apisession:set_api_token:No valid API Token provided")
            CONSOLE.error("No valid API Token provided")

    def _get_api_token_data(self, apitoken) -> tuple[str | None, list | None]:
        token_privileges = []
        token_type = "org"  # nosec bandit B105
        try:
            url = f"https://{self._cloud_uri}/api/v1/self"
            headers = {"Authorization": "Token " + apitoken}
            # Filter out None values from proxies
            filtered_proxies = {k: v for k, v in self._proxies.items() if v is not None}
            data = requests.get(
                url, headers=headers, proxies=filtered_proxies or None, timeout=30
            )
            data_json = data.json()
            LOGGER.debug(
                "apisession:_get_api_token_data:info retrieved for token %s...%s",
                apitoken[:4],
                apitoken[-4:],
            )
        except requests.exceptions.ProxyError as proxy_error:
            LOGGER.critical("apisession:_get_api_token_data:proxy not valid...")
            CONSOLE.critical("Proxy not valid...\r\n")
            raise ConnectionError("Proxy not valid") from proxy_error
        except requests.exceptions.ConnectionError as connexion_error:
            LOGGER.critical(
                "apirequest:mist_post:Connection Error: %s", connexion_error
            )
            CONSOLE.critical("Connexion error...\r\n")
            raise ConnectionError(f"Connection error: {connexion_error}") from connexion_error
        except Exception:
            LOGGER.error(
                "apisession:_get_api_token_data:"
                "unable to retrieve info for token %s...%s",
                apitoken[:4],
                apitoken[-4:],
            )
            LOGGER.error(
                "apirequest:_get_api_token_data: Exception occurred", exc_info=True
            )
            return (None, None)

        if data.status_code == 401:
            LOGGER.critical(
                "apisession:_get_api_token_data:"
                "invalid API Token %s...%s: status code %s",
                apitoken[:4],
                apitoken[-4:],
                data.status_code,
            )
            CONSOLE.critical(
                f"Invalid API Token {apitoken[:4]}...{apitoken[-4:]}: status code {data.status_code}\r\n"
            )
            raise ValueError(f"Invalid API Token {apitoken[:4]}...{apitoken[-4:]}: status code {data.status_code}")

        if data_json.get("email"):
            token_type = "user"  # nosec bandit B105

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
                LOGGER.error(
                    "apisession:_check_api_tokens:"
                    "unable to process privileges %s for the %s "
                    "token %s...%s",
                    priv,
                    token_type,
                    apitoken[:4],
                    apitoken[-4:],
                )
        return (token_type, token_privileges)

    def _check_api_tokens(self, apitokens) -> list[str]:
        """
        Function used when multiple API tokens are provided, to validate they
        have same privileges
        """
        LOGGER.debug("apisession:_check_api_tokens")
        valid_api_tokens: list[str] = []
        if len(apitokens) == 0:
            LOGGER.error("apisession:_check_api_tokens:there is not API token to check")
        else:
            primary_token_privileges: list[str] = []
            primary_token_type: str | None = ""
            primary_token_value: str = ""
            for token in apitokens:
                token_value = f"{token[:4]}...{token[-4:]}"
                if token in valid_api_tokens:
                    LOGGER.info(
                        "apisession:_check_api_tokens:API Token %s is already valid",
                        token_value,
                    )
                    continue
                (token_type, token_privileges) = self._get_api_token_data(token)
                if token_type is None or token_privileges is None:
                    LOGGER.error(
                        "apisession:_check_api_tokens:API Token %s is not valid",
                        token_value,
                    )
                    LOGGER.error(
                        "API Token %s is not valid and will not be used", token_value
                    )
                elif len(primary_token_privileges) == 0 and token_privileges:
                    primary_token_privileges = token_privileges
                    primary_token_type = token_type
                    primary_token_value = token_value
                    valid_api_tokens.append(token)
                    LOGGER.info(
                        "apisession:_check_api_tokens:"
                        "API Token %s set as primary for comparison",
                        token_value,
                    )
                elif primary_token_privileges == token_privileges:
                    valid_api_tokens.append(token)
                    LOGGER.info(
                        "apisession:_check_api_tokens:"
                        "%s API Token %s has same privileges as "
                        "the %s API Token %s",
                        token_type,
                        token_value,
                        primary_token_type,
                        primary_token_value,
                    )
                else:
                    LOGGER.error(
                        "apisession:_check_api_tokens:"
                        "%s API Token %s has different privileges "
                        "than the %s API Token %s",
                        token_type,
                        token_value,
                        primary_token_type,
                        primary_token_value,
                    )
                    LOGGER.error(
                        "API Token %s has different privileges and will not be used",
                        token_value,
                    )
        return valid_api_tokens

    def _process_login(self, retry: bool = True) -> str | None:
        """
        Function to authenticate a user with login/password.
        Will create and store a session used by other requests.

        PARAMS
        -----------
        retry : bool, default True
            if `retry`==True, ask for login/password when authentication is failing
        """
        LOGGER.debug("apisession:_process_login")
        error: str | None = None
        if self._show_cli_notif:
            print()
            print(" Login/Pwd authentication ".center(80, "-"))
            print()

        self._session = requests.session()
        if not self.email:
            self.set_email()
        if not self._password:
            self.set_password()

        try:
            LOGGER.debug("apisession:_process_login:email/password configured")
            uri = "/api/v1/login"
            body = {"email": self.email, "password": self._password}
            resp = self._session.post(self._url(uri), json=body)
            if resp.status_code == 200:
                LOGGER.info("apisession:_process_login:authentication successful!")
                CONSOLE.info("Authentication successful!")
                self._set_authenticated(True)
            else:
                error = resp.json().get("detail")
                LOGGER.error(
                    "apisession:_process_login:authentication failed:%s", error
                )
                CONSOLE.error(f"Authentication failed: {error}\r\n")
                self.email = None
                self._password = None
                LOGGER.info(
                    "apisession:_process_login:"
                    "email/password cleaned up. Restarting authentication function"
                )
                if retry:
                    return self._process_login(retry)
        except requests.exceptions.ProxyError as proxy_error:
            LOGGER.critical("apisession:_process_login:proxy not valid...")
            CONSOLE.critical("Proxy not valid...\r\n")
            raise ConnectionError("Proxy not valid") from proxy_error
        except requests.exceptions.ConnectionError as connexion_error:
            LOGGER.critical(
                "apirequest:mist_post:Connection Error: %s", connexion_error
            )
            CONSOLE.critical("Connexion error...\r\n")
            raise ConnectionError(f"Connection error: {connexion_error}") from connexion_error
        except Exception:
            LOGGER.error("apisession:_process_login:Exception occurred", exc_info=True)
            error = "Exception occurred during authentication"

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
        LOGGER.debug("apisession:login")
        if self._authenticated:
            LOGGER.warning("apisession:login:already logged in...")
            CONSOLE.info("Already logged in...")
        else:
            LOGGER.debug("apisession:login:not authenticated yet")
            if not self._cloud_uri:
                self.select_cloud()
            if self._apitoken:
                self._set_authenticated(True)
            if not self._authenticated:
                self._process_login()
            # if successfully authenticated
            if self.get_authentication_status():
                LOGGER.info("apisession:login:authenticated")
                self._getself()

    def login_with_return(
        self,
        apitoken: str | None = None,
        email: str | None = None,
        password: str | None = None,
        two_factor: str | None = None,
    ) -> dict:
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
        LOGGER.debug("apisession:login_with_return")
        self._session = requests.session()
        if apitoken:
            self.set_api_token(apitoken)
        if email:
            self.set_email(email)
        if password:
            self.set_password(password)

        if self._apitoken:
            LOGGER.debug("apisession:login_with_return:apitoken provided")
            self._set_authenticated(True)
            LOGGER.info("apisession:login_with_return:get self")
            uri = "/api/v1/self"
            LOGGER.info(
                'apisession:login_with_return: sending GET request to "%s"', uri
            )
            resp = self.mist_get(uri)

        elif self.email and self._password:
            if two_factor:
                LOGGER.debug("apisession:login_with_return:login/pwd provided with 2FA")
                if self._two_factor_authentication(two_factor):
                    LOGGER.error(
                        "apisession:login_with_return:login/pwd auth failed: 2FA authentication failed"
                    )
                    return {
                        "authenticated": False,
                        "error": "2FA authentication failed",
                    }
            else:
                LOGGER.debug("apisession:login_with_return:login/pwd provided w/o 2FA")
                error_login = self._process_login(retry=False)
                if error_login:
                    LOGGER.error(
                        "apisession:login_with_return:login/pwd auth failed: %s",
                        error_login,
                    )
                    return {"authenticated": False, "error": error_login}
            LOGGER.info("apisession:login_with_return:get self")
            uri = "/api/v1/self"
            LOGGER.info(
                'apisession:login_with_return: sending GET request to "%s"', uri
            )
            resp = self.mist_get(uri)

        else:
            LOGGER.error("apisession:login_with_return:credentials are missing")
            return {"authenticated": False, "error": "credentials are missing"}

        if resp.status_code == 200 and not resp.data.get("two_factor_required", False):
            LOGGER.info("apisession:login_with_return:access authorized")
            return {"authenticated": True, "error": ""}
        else:
            LOGGER.error("apisession:login_with_return:access denied: %s", resp.data)
            return {"authenticated": False, "error": resp.data}

    def logout(self) -> None:
        """
        Log out from the Mist Cloud.
        If login/password is used, the HTTP session is destroyed.
        """
        LOGGER.debug("apisession:logout")
        if not self._authenticated:
            LOGGER.error("apisession:logout:not logged in...")
            CONSOLE.error("Not logged in...")
        else:
            uri = "/api/v1/logout"
            resp = self.mist_post(uri)
            if resp.status_code == 200:
                LOGGER.info("apisession:logout:Mist Session closed and cleaned up")
                CONSOLE.info("Logged out")
                self._set_authenticated(False)
            else:
                try:
                    CONSOLE.error(resp.data["detail"])
                except (KeyError, TypeError, AttributeError):
                    if isinstance(resp.raw_data, bytes):
                        CONSOLE.error(resp.raw_data.decode("utf-8", errors="replace"))
                    else:
                        CONSOLE.error(str(resp.raw_data))

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
        LOGGER.debug("apisession:_set_authenticated")
        LOGGER.debug(
            "apisession:_set_authenticated:authentication_status is %s",
            authentication_status,
        )
        if authentication_status:
            self._authenticated = True
            LOGGER.info('apisession:_set_authenticated: session is now "Authenticated"')
            if not self._apitoken:
                LOGGER.info("apisession:_set_authenticated:processing HTTP cookies")
                try:
                    if self._cloud_uri == "api.mistsys.com":
                        cookies_ext = ""
                    elif self._cloud_uri == "api.ac99.mist.com":
                        cookies_ext = ".ac99"
                    elif self._cloud_uri == "api.gc1.mistsys.com":
                        cookies_ext = ".gc1"
                    elif self._cloud_uri == "api.us.mist-federal.com":
                        cookies_ext = ".us"
                    else:
                        cookies_ext = next(
                            item["cookies_ext"]
                            for item in CLOUDS
                            if item["host"] == self._cloud_uri
                        )
                    LOGGER.info(
                        "apisession:_set_authenticated:HTTP session cookies extracted. Cookies extension is %s",
                        cookies_ext,
                    )
                except (StopIteration, KeyError, AttributeError):
                    cookies_ext = ""
                    LOGGER.error(
                        "apisession:_set_authenticated:unable to extract HTTP session cookies"
                    )
                    LOGGER.error(
                        "apirequest:mist_post_file: Exception occurred", exc_info=True
                    )
                self._csrftoken = self._session.cookies["csrftoken" + cookies_ext]
                self._session.headers.update({"X-CSRFToken": self._csrftoken})
                LOGGER.info("apisession:_set_authenticated:CSRF Token stored")
        elif authentication_status is False:
            self._authenticated = False
            LOGGER.info(
                'apisession:_set_authenticated: session is now "Unauthenticated"'
            )
            self._csrftoken = ""
            del self._session
            LOGGER.info(
                "apisession:_set_authenticated:CSRF Token is cleaned up and HTTP Session deleted"
            )

    def get_authentication_status(self) -> bool:
        """
        RETURN
        -----------
        bool
            Return the authentication status.
        """
        LOGGER.debug(
            "apisession:get_authentication_status:return %s", self._authenticated
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
        LOGGER.info(
            'apisession:get_api_token: Sending GET request to "/api/v1/self/apitokens"'
        )
        resp = self.mist_get("/api/v1/self/apitokens")
        return resp

    def create_api_token(self, token_name: str | None = None) -> APIResponse:
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
        LOGGER.debug("apisession:create_api_token")
        body = {}
        if token_name:
            body = {"name": token_name}
        LOGGER.info(
            "apisession:create_api_token:"
            'sending POST request to "/api/v1/self/apitokens" with name "%s"',
            token_name,
        )
        resp = self.mist_post("/api/v1/self/apitokens", body=body)
        return resp

    def delete_api_token(self, apitoken_id: str) -> Response:
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
        LOGGER.debug("apisession:delete_api_token")
        LOGGER.info(
            "apisession:delete_api_token:"
            'sending DELETE request to "/api/v1/self/apitokens" with token_id "%s"',
            apitoken_id,
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
        LOGGER.debug("apisession:_two_factor_authentication")
        uri = "/api/v1/login"
        body = {
            "email": self.email,
            "password": self._password,
            "two_factor": two_factor,
        }
        resp = self._session.post(self._url(uri), json=body)
        if resp.status_code == 200:
            LOGGER.info(
                "apisession:_two_factor_authentication:2FA authentication succeed"
            )
            CONSOLE.info("2FA authentication succeeded")
            self._set_authenticated(True)
            return True
        else:
            LOGGER.error(
                "apisession:_two_factor_authentication:"
                "2FA authentication failed with error code: %s",
                resp.status_code,
            )
            CONSOLE.error(
                f"2FA authentication failed with error code: {resp.status_code}\r\n"
            )
            return False

    def _getself(self) -> bool:
        """
        Retrieve information about the current user and store them in the current object.
        """
        LOGGER.debug("apisession:_getself")
        uri = "/api/v1/self"
        LOGGER.info('apisession:_getself: sending GET request to "%s"', uri)
        resp = self.mist_get(uri)
        if resp.status_code == 200 and resp.data:
            # Deal with 2FA if needed
            if (
                resp.data.get("two_factor_required") is True
                and resp.data.get("two_factor_passed") is False
            ):
                LOGGER.info("apisession:_getself:2FA request by Mist Cloud")
                two_factor_ok = False
                while not two_factor_ok:
                    two_factor = input("Two Factor Authentication code required: ")
                    two_factor_ok = self._two_factor_authentication(two_factor)
                self._getself()
            # Get details of the account
            else:
                LOGGER.info(
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
                LOGGER.info(
                    "apisession:_getself:account used: %s %s",
                    self.first_name,
                    self.last_name,
                )
                return True
        elif resp.proxy_error:
            LOGGER.critical("apisession:_getself:proxy not valid...")
            CONSOLE.critical("Proxy not valid...\r\n")
            raise ConnectionError("Proxy not valid")
        else:
            LOGGER.error("apisession:_getself:authentication not valid...")
            CONSOLE.error("Authentication not valid...\r\n")
            user_resp = input(
                f"Do you want to try with new credentials for {self._cloud_uri} (y/N)? "
            )
            if user_resp.lower() == "y":
                self._process_login()
                return self._getself()
            else:
                raise ValueError("Authentication not valid and user declined to retry")
        return False

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
        LOGGER.debug("apisession:get_privilege_by_org_id")
        org_priv = next(
            (priv for priv in self.privileges if priv.get("org_id") == org_id),
            None,
        )
        if org_priv:
            LOGGER.info(
                "apisession:get_privilege_by_org_id:"
                "org %s privileges found in user info",
                org_id,
            )
            LOGGER.debug("apisession:get_privilege_by_org_id: %s", org_priv)
            return org_priv
        else:
            LOGGER.warning(
                "apisession:get_privilege_by_org_id:"
                "unable of find org %s privileges in user data",
                org_id,
            )
            LOGGER.info(
                "apisession:get_privilege_by_org_id:"
                "trying to request org %s info from the Cloud",
                org_id,
            )
            uri = f"/api/v1/orgs/{org_id}"
            msp_id = None
            try:
                resp = self.mist_get(uri)
                if resp.data and resp.data.get("msp_id"):
                    LOGGER.info(
                        "apisession:get_privilege_by_org_id:org %s belong to msp_id %s",
                        {org_id},
                        resp.data["msp_id"],
                    )
                    msp_id = resp.data.get("msp_id")
                else:
                    LOGGER.warning(
                        "apisession:get_privilege_by_org_id:"
                        "not able to find msp_id information in the org info"
                    )
            except Exception:
                LOGGER.error(
                    "apisession:get_privilege_by_org_id: error when retrieving org info"
                )
                LOGGER.error(
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
                    LOGGER.warning(
                        "apisession:get_privilege_by_org_id:"
                        "unable of find msp %s privileges in user data",
                        msp_id,
                    )
                else:
                    return {
                        "scope": "org",
                        "org_id": org_id,
                        "name": resp.data.get("name"),
                        "role": msp_priv.get("role"),
                        "msp_id": msp_id,
                        "msp_name": msp_priv.get("name"),
                        "orggroup_ids": resp.data.get("orggroup_ids"),
                        "msp_logo_url": resp.data.get("logo_url"),
                    }
            return {}
