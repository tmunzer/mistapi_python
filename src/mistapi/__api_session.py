'''
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
This module provide the APISession class, which is used to manage authentication
and HTTP session (if login/password is used) with Mist Cloud.
'''

import os
import sys
import requests
from dotenv import load_dotenv
from pathlib import Path
from getpass import getpass

from mistapi.__logger import console
from mistapi.__logger import logger
from mistapi.__api_request import APIRequest
from mistapi.__models.privilege import Privileges


###### GLOBALS ######
clouds = [
    {"short": "Europe 01", "host": "api.eu.mist.com", "cookies_ext": ".eu"},
    {"short": "Global 01", "host": "api.mist.com", "cookies_ext": ""},
    {"short": "Global 02", "host": "api.gc1.mist.com", "cookies_ext": ".gc1"},
    {"short": "Global 03", "host": "api.ac2.mist.com", "cookies_ext": ".ac2"},
    {"short": "Global 04", "host": "api.gc2.mist.com", "cookies_ext": ".gc2"}
]


def _header():
    print("""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------    
    """)


#### PARAMETERS #####

class APISession(APIRequest):
    """Class managing REST API Session"""

    def __init__(self, email: str = None, password: str = None, apitoken: str = None, host: str = None, env_file: str = None, console_log_level: str = 20, logging_log_level: int = 10):
        """
        :param str email        used if login/password is used. Can be defined later
        :param str password     used if login/password is used. Can be defined later
        :param str apitoken     used if API Token is used. Can de defined later
        :param str host         Mist Cloud to reach (e.g. "api.mist.com"). Can de defined later
        :param str env_file     path to the env file to load. See README.md for allowed variables
        :param int console_log_level
        :param int logging_log_level
        """        
        self._cloud_uri = None
        self.email = None
        self._password = None
        self._apitoken = None
        self._csrftoken = None
        self._authenticated = False
        self._session = requests.session()
        self._console_log_level = console_log_level
        self._logging_log_level = logging_log_level

        console._set_log_level(console_log_level, logging_log_level)

        self._load_env(env_file)

        if host:
            self._cloud_uri = host
        if email:
            self.email = email
        if password:
            self._password = password
        if apitoken:
            self._apitoken = apitoken
        self.first_name = ""
        self.last_name = ""
        self.via_sso = False
        self.tags = []

        self.privileges = Privileges([])
        self.session_expiry = ""

        logger.debug('API Session initialized')

    def __str__(self):
        fields = ["email", "first_name", "last_name", "phone", "via_sso",
                  "privileges", "session_expiry", "tags", "authenticated"]
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


    def _load_env(self, env_file=None):
        if env_file:
            if env_file.startswith("~/"):
                env_file = os.path.join(os.path.expanduser('~'), env_file.replace("~/",""))
            env_file = os.path.abspath(env_file)
            console.debug(f"Loading settings from {env_file}")
            logger.debug(f"apisession:Loading settings from {env_file}")
            dotenv_path = Path(env_file)
            load_dotenv(dotenv_path=dotenv_path)
        else:
            console.debug("Loading settings from env file")
            logger.debug(f"apisession:Loading settings from env file")
            load_dotenv()

        if os.getenv('MIST_HOST'):
            self.set_cloud(os.getenv('MIST_HOST'))
        if os.getenv('MIST_APITOKEN'):
            self.set_api_token(os.getenv('MIST_APITOKEN'))
        if os.getenv('MIST_USER'):
            self.set_email(os.getenv('MIST_USER'))
        if os.getenv('MIST_PASSWORD'):
            self.set_password(os.getenv('MIST_PASSWORD'))
        if os.getenv('CONSOLE_LOG_LEVEL'):
            self._console_log_level = os.getenv('CONSOLE_LOG_LEVEL')
        if os.getenv('LOGGING_LOG_LEVEL'):
            self._logging_log_level = os.getenv('LOGGING_LOG_LEVEL')

####################################
# CLOUD FUNCTIONS
    def set_cloud(self, cloud_uri: str) -> None:
        """
        Set Mist Cloud to reach.

        PARAMS
        -----------
        :param str cloud_uri - Mist FQDN to reach ("api.mist.com", "api.eu.mist.com", ...)
        """
        logger.debug(f"apisession:in  > set_cloud")
        self._cloud_uri = None
        for cloud in clouds:
            if cloud["host"] == cloud_uri:
                self._cloud_uri = cloud_uri
                logger.debug(
                    f"apisession:Mist Cloud configured to {self._cloud_uri}")
                console.debug(
                    f"Mist Cloud configured to {self._cloud_uri}")
        if not self._cloud_uri:
            logger.error(f"apisession:{cloud_uri} is not valid")
            console.error(f"{cloud_uri} is not valid")

    def get_cloud(self):
        """
        Return the Mist Cloud currently configured
        """
        logger.debug(f"apisession:in  > get_cloud")
        return self._cloud_uri

    def select_cloud(self) -> None:
        """
        Display a menu to select the Mist Cloud
        """
        logger.debug(f"apisession:in  > select_cloud")
        resp = "x"
        i = 0
        print()
        print(" Mist Cloud Selection ".center(80, "-"))
        print()
        for cloud in clouds:
            print(f"{i}) {cloud['short']} (host: {cloud['host']})")
            i += 1

        print()
        resp = input(f"Select a Cloud (0 to {i}, or q to exit): ")
        if resp == "q":
            sys.exit(0)
        elif resp == "i":
            self._cloud_uri = "api.mistsys.com"
        else:
            try:
                resp_num = int(resp)
                if resp_num >= 0 and resp_num <= i:
                    self.set_cloud(clouds[resp_num]["host"])
                else:
                    print(f"Please enter a number between 0 and {i}.")
                    self.select_cloud()
            except:
                print("\r\nPlease enter a number.")
                self.select_cloud()

####################################
# AUTH FUNCTIONS

    def set_email(self, email: str = None) -> None:
        """
        Set the user email

        PARAMS
        -----------
        :param str email    If no email provided, an interactive input will ask for it
        """
        logger.debug(f"apisession:in  > set_email")
        if email:
            self.email = email
        else:
            self.email = input("Login: ")
        logger.debug(f"apisession:Email configured to {self.email}")
        console.debug(f"Email configured to {self.email}")

    def set_password(self, password: str = None) -> None:
        """
        Set the user password

        PARAMS
        -----------
        :param str password    If no password provided, an interactive input will ask for it
        """
        logger.debug(f"apisession:in  > set_password")
        if password:
            self._password = password
        else:
            self._password = getpass("Password: ")
        logger.debug(f"apisession:Password configured")
        console.debug(f"Password configured")

    def set_api_token(self, apitoken: str):
        """
        Set Mist API Token

        PARAMS
        -----------
        :param str apitoken
        """
        logger.debug(f"apisession:in  > set_api_token")
        self._apitoken = apitoken
        self._session.headers.update(
            {'Authorization': "Token " + self._apitoken})
        logger.debug(f"apisession:API Token configured")
        console.debug(f"API Token configured")

    def _process_login(self):
        """
        Function to authenticate a user with login/password. 
        Will create and store a session used by other requests.
        """

        logger.debug(f"apisession:in  > _process_login")
        print()
        print(" Login/Pwd authentication ".center(80, "-"))
        print()

        self._session = requests.session()
        if not self.email:
            self.set_email()
        if not self._password:
            self.set_password()

        logger.debug(f"apisession:Email/Password configured")
        uri = "/api/v1/login"
        body = {
            "email": self.email,
            "password": self._password
        }
        resp = self._session.post(self._url(uri), json=body)
        if resp.status_code == 200:
            logger.info(f"apisession:Authentication successful!")
            console.info("Authentication successful!")
            self._set_authenticated(True)
        else:
            logger.error(
                f"apisession:Authentication failed: {resp.json().get('detail')}")
            console.error(f"Authentication failed: {resp.json().get('detail')}\r\n")
            self.email = None
            self._password = None
            logger.debug(
                f"apisession:Email/Password cleaned up. Restarting authentication function")
            self._process_login()

    def login(self):
        """
        Log in on the Mist Cloud.
        If information are missing to get connected, they will be requested
        during the process.
        If login/password is used, 2FA may be requests. Once authenticated, 
        the HTTP session and CSRF Token will be stored and used during the 
        future API requests.
        """
        logger.debug(f"apisession:in  > login")
        if self._authenticated:
            logger.info(f"apisession:Already logged in...")
            console.info("Already logged in...")
        else:
            logger.debug(f"apisession:Not authenticated yet")
            if not self._cloud_uri:
                self.select_cloud()
            if self._apitoken:
                self._set_authenticated(True)
            if not self._authenticated:
                self._process_login()
            # if successfuly authenticated
            if self.get_authentication_status():
                logger.info(f"apisession:Authenticated")
                self._getself()

    def logout(self):
        """
        Log out from the Mist Cloud.
        If login/password is used, the HTTP session is destroyed.
        """
        logger.debug(f"apisession:in  > logout")
        if not self._authenticated:
            logger.error(f"apisession:Not logged in...")
            console.error("Not logged in...")
        else:
            uri = "/api/v1/logout"
            resp = self.mist_post(uri)
            if resp.status_code == 200:
                logger.info(f"apisession:Mist Session closed")
                console.info("Logged out")
                self._set_authenticated(False)
            else:
                try:
                    console.error(resp.json()["detail"])
                except:
                    console.error(resp.text)

    def _set_authenticated(self, authentication_status: bool) -> None:
        """
        Set the authentication status.
        If True and Login/password is used, extract the HTTP session and 
        CSRF Token from the cookies and store them in memory to be used 
        during the future API requests.
        If False, clear the CSRF Token and delete the HTTP session.

        PARAMS
        -----------
        :param bool authentication_status
        """
        logger.debug(f"apisession:in  > _set_authenticated")
        logger.debug(
            f"apisession:authentication_status is {authentication_status}")
        if authentication_status == True:
            self._authenticated = True
            logger.info(f"apisession:Session is now Authenticated")
            if not self._apitoken:
                logger.debug(f"apisession:Processing HTTP cookies")
                try:
                    cookies_ext = next(
                        item["cookies_ext"] for item in clouds if item["host"] == self._cloud_uri)
                    logger.info(f"apisession:HTTP session cookies extracted")
                except:
                    cookies_ext = ""
                    logger.error(
                        f"apisession:Unable to extract HTTP session cookies")
                self._csrftoken = self._session.cookies['csrftoken' + cookies_ext]
                self._session.headers.update({'X-CSRFToken': self._csrftoken})
                logger.info(f"apisession:CSRF Token stored")
        elif authentication_status == False:
            self._authenticated = False
            logger.info(f"apisession:Session is now Unauthenticated")
            self._csrftoken = ""
            del self._session
            logger.info(
                f"apisession:CSRFT Token is cleaned up and HTTP Session deleted")

    def get_authentication_status(self) -> bool:
        """
        RETURN
        -----------
        Return the authentication status.
        """
        logger.debug(f"apisession:in  > get_authentication_status")
        return self._authenticated or self._apitoken

    def get_api_token(self):
        """
        Retrieve and display the User/Org API Tokens
        """
        logger.debug(f"apisession:in  > list_api_token")
        logger.info(
            f"apisession:Sending GET request to \"/api/v1/self/apitokens\"")
        resp = self.mist_get("/api/v1/self/apitokens")
        return resp

    def create_api_token(self, token_name: str = None):
        """
        Create a new API Token with the current account (user/org)

        PARAMS
        -----------
        :param str API token name (optional)
        """
        logger.debug(f"apisession:in  > create_api_token")
        if token_name:
            body = {"name": token_name}
        logger.info(
            f"apisession:Sending POST request to \"/api/v1/self/apitokens\" with name \"{token_name}\"")
        resp = self.mist_post("/api/v1/self/apitokens", body=body)
        return resp

    def delete_api_token(self, token_id: str):
        """
        Delete an API Token based on its token_id

        PARAMS
        -----------
        :param str api token_id
        """
        logger.debug(f"apisession:in  > delete_api_token")
        logger.info(
            f"apisession:Sending DELETE request to \"/api/v1/self/apitokens\" with token_id \"{token_id}\"")
        uri = f"https://{self._cloud_uri}/api/v1/self/apitokens/{token_id}"
        resp = self._session.delete(uri)
        return resp

    def _two_factor_authentication(self, two_factor: str) -> bool:
        """
        Function called when 2FA is requested by Mist Cloud to authenticate
        with 2FA enabled

        PARAMS
        -----------
        :param str two_factor - 2FA code to send to the Mist Cloud

        RETURN
        -----------
        :return bool - True if authentication succeed, False otherwise
        """
        logger.debug(f"apisession:in  > two_factor_authentication")
        uri = "/api/v1/login"
        body = {
            "email": self.email,
            "password": self._password,
            "two_factor": two_factor
        }
        resp = self._session.post(self._url(uri), json=body)
        if resp.status_code == 200:
            logger.info(f"apisession:2FA authentication successed")
            console.info("2FA authentication successed")
            self._set_authenticated(True)
            return True
        else:
            logger.error(
                f"apisession:2FA authentication failed with error code: {resp.status_code}")
            console.error(f"2FA authentication failed with error code: {resp.status_code}\r\n")
            return False

    def _getself(self) -> None:
        """
        Retrieve information about the current user and store them in the current object.
        """
        logger.debug(f"apisession:in  > getself")
        uri = "/api/v1/self"
        logger.info(f"apisession:Sending GET request to \"{uri}\"")
        resp = self.mist_get(uri)
        if resp.data:
            # Deal with 2FA if needed
            if (
                resp.data.get('two_factor_required') is True
                and resp.data.get('two_factor_passed') is False
            ):
                logger.info(f"apisession:2FA request by Mist Cloud")
                two_factor_ok = False
                while not two_factor_ok:
                    two_factor = input(
                        "Two Factor Authentication code required: ")
                    two_factor_ok = self._two_factor_authentication(two_factor)
                self._getself()
            # Get details of the account
            else:
                logger.info(
                    f"apisession:Authentication Ok. Processing account privileges")
                for key, val in resp.data.items():
                    if key == "privileges":
                        self.privileges = Privileges(resp.data["privileges"])
                    if key == "tags":
                        for tag in resp.data["tags"]:
                            self.tags.append(tag)
                    else:
                        setattr(self, key, val)
                print()
                print(" Authenticated ".center(80, "-"))
                print(f"\r\nWelcome {self.first_name} {self.last_name}!\r\n")
                logger.info(
                    f"apisession:Account used: {self.first_name} {self.last_name}")
                return True
        else:
            logger.error(f"apisession:Authentication not valid...")
            console.error("Authentication not valid...\r\n")
            resp = input(
                f"Do you want to try with new credentials for {self._cloud_uri} (y/N)? " % ())
            if resp.lower() == "y":
                self._process_login()
                return self._getself()
            else:
                sys.exit(0)

