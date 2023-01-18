'''
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
'''

from dotenv import load_dotenv
import os
from pathlib import Path
import requests
import sys
from getpass import getpass

from mistapi.__console import Console
from mistapi.__api_request import APIRequest
from mistapi.__models.privilege import Privileges

import logging
log_file = "./org_migration.log"
logger = logging.getLogger(__name__)

console = Console(7)

###### GLOBALS ######
clouds = [
    {"short": "Europe 01","host": "api.eu.mist.com","cookies_ext": ".eu"},
    {"short": "Global 01","host": "api.mist.com","cookies_ext": ""},
    {"short": "Global 02","host": "api.gc1.mist.com","cookies_ext": ".gc1"},
    {"short": "Global 03","host": "api.ac2.mist.com","cookies_ext": ".ac2"},
    {"short": "Global 04","host": "api.gc2.mist.com","cookies_ext": ".gc2"}
]


def _header():
    print("""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mist_library

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------    
    """)


#### PARAMETERS #####

class APISession(APIRequest):
    """Class managing REST login and requests"""

    def __init__(self, email: str = None, password: str = None, apitoken: str = None, host: str = None, env_file: str = None):
        _header()
        self._cloud_uri = None
        self.email = None
        self._password = None
        self._apitoken = None

        self._load_env(env_file)
        
        if host: self._cloud_uri = host
        if email: self.email = email
        if password: self._password = password
        if apitoken: self._apitoken = apitoken
        self._csrftoken = ""
        self._session = requests.session()
        self.first_name = ""
        self.last_name = ""
        self.via_sso = False
        self.tags = []

        self.privileges = Privileges([])
        self.session_expiry = ""
        self._authenticated = False


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
            env_file = os.path.abspath(env_file)
            console.debug(f"Loading settings from {env_file}")
            logger.debug(f"Loading settings from {env_file}")
            dotenv_path = Path(env_file)
            load_dotenv(dotenv_path=dotenv_path)
        else:
            console.debug("Loading settings from env file")
            logger.debug("Loading settings from env file")
            load_dotenv()

        self._cloud_uri = os.getenv('MIST_HOST')
        self._apitoken = os.getenv('MIST_API_TOKEN')

####################################
# CLOUD FUNCTIONS
    def set_cloud(self, cloud_uri: str):
        """
        Set Mist Cloud to reach.
        
        :param str cloud_uri - Mist FQDN to reach ("api.mist.com", "api.eu.mist.com", ...)
        """
        console.debug("in  > set_cloud")
        self._cloud_uri = None
        for cloud in clouds:
            if cloud["host"] == cloud_uri:
                self._cloud_uri = cloud_uri
        if not self._cloud_uri:
            logger.error(f"{cloud_uri} is not valid")
            console.error(f"{cloud_uri} is not valid")

    def get_cloud(self):
        """
        Return the Mist Cloud currently configured
        """
        console.debug("in  > get_cloud")
        return self._cloud_uri

    def select_cloud(self):
        """
        Display a menu to select the Mist Cloud
        """
        console.debug("in  > select_cloud")
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
            return "api.mistsys.com"
        else:
            try:
                resp_num = int(resp)
                if resp_num >= 0 and resp_num <= i:
                    return clouds[resp_num]["host"]
                else:
                    print(f"Please enter a number between 0 and {i}.")
                    return self.select_cloud()
            except:
                print("\r\nPlease enter a number.")
                return self.select_cloud()

####################################
# AUTH FUNCTIONS
    def set_api_token(self, apitoken: str):
        """
        Set Mist API Token
        """
        self._apitoken = apitoken
        self._session.headers.update(
            {'Authorization': "Token " + self._apitoken})
        self._set_authenticated(True)

    def _process_login(self):
        console.debug("in  > _process_login")
        """
        Function to authenticate a user. Will create and store a session used by other requests
        """
        print()
        print(" Login/Pwd authentication ".center(80, "-"))
        print()

        self._session = requests.session()
        if not self.email:
            self.email = input("Login: ")
        if not self._password:
            self._password = getpass("Password: ")

        uri = "/api/v1/login"
        body = {
            "email": self.email,
            "password": self._password
        }
        resp = self._session.post(self._url(uri), json=body)
        if resp.status_code == 200:
            print()
            console.info("Authentication successful!")
            print()
            self._set_authenticated(True)
        else:
            print()
            console.error(
                f"Authentication failed: {resp.json().get('detail')}")
            self.email = None
            self._password = None
            print()
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
        console.debug("in  > login")
        if self._authenticated:
            console.error("Already logged in...")
        else:
            if not self._cloud_uri:
                self._cloud_uri = self.select_cloud()
            if self._apitoken:
                self.set_api_token(self._apitoken)
            if not self._authenticated:
                self._process_login()
            # if successfuly authenticated
            if self.get_authentication_status():
                self._getself()

    def logout(self):
        """
        Log out from the Mist Cloud.
        If login/password is used, the HTTP session is destroyed.
        """
        console.debug("in  > logout")
        if not self._authenticated:
            console.error("Not logged in...")
        else:
            uri = "/api/v1/logout"
            resp = self.mist_post(uri)
            if resp['status_code'] == 200:
                console.warning("Logged out")
                self._set_authenticated(False)
            else:
                try:
                    console.error(resp.json()["detail"])
                except:
                    console.error(resp.text)

    def _set_authenticated(self, value:bool):
        """
        Set the authentication status.
        If True and Login/password is used, extract the HTTP session and 
        CSRF Token from the cookies and store them in memory to be used 
        during the future API requests.
        If False, clear the CSRF Token and delete the HTTP session.
        """
        console.debug("in  > _set_authenticated")
        if value == True:
            self._authenticated = True
            if not self._apitoken:
                try:
                    cookies_ext = next(
                        item["cookies_ext"] for item in clouds if item["host"] == self._cloud_uri)
                except:
                    cookies_ext = ""
                self._csrftoken = self._session.cookies['csrftoken' + cookies_ext]
                self._session.headers.update({'X-CSRFToken': self._csrftoken})
        elif value == False:
            self._authenticated = False
            self._csrftoken = ""
            del self._session

    def get_authentication_status(self) -> bool:
        """
        Return the authentication status.
        """
        console.debug("in  > get_authentication_status")
        return self._authenticated or self._apitoken

    def get_api_token(self):
        """
        Retrieve and display the User/Org API Tokens
        """
        console.debug("in  > list_api_token")
        resp = self.mist_get("/api/v1/self/apitokens")
        return resp

    def create_api_token(self, token_name: str = None):
        """
        Create a new API Token with the current account (user/org)
        """
        console.debug("in  > create_api_token")
        resp = self.mist_post("/api/v1/self/apitokens")
        if token_name:
            body = {"name": token_name}
        uri = f"https://{self._cloud_uri}/api/v1/self/apitokens"
        resp = self._session.post(uri, json=body)
        return resp

    def delete_api_token(self, token_id:str):
        """
        Delete an API Token based on its token_id
        """
        console.debug("in  > delete_api_token")
        uri = f"https://{self._cloud_uri}/api/v1/self/apitokens/{token_id}"
        resp = self._session.delete(uri)
        return resp

    def _two_factor_authentication(self, two_factor:str) -> bool:
        """
        Function called when 2FA is requested by Mist Cloud to authenticate
        with 2FA enabled

        :param str two_factor - 2FA code to send to the Mist Cloud
        :return bool - True if authentication succeed, False otherwise
        """
        console.debug("in  > two_factor_authentication")
        uri = "/api/v1/login"
        body = {
            "email": self.email,
            "password": self._password,
            "two_factor": two_factor
        }
        resp = self._session.post(self._url(uri), json=body)
        if resp.status_code == 200:
            print()
            console.info("2FA authentication successed")
            self._set_authenticated(True)
            return True
        else:
            print()
            console.error("2FA authentication failed")
            console.error(f"Error code: {resp.status_code}")
            return False

    def _getself(self):
        """
        Retrieve information about the current user and store them in the current object.
        """
        console.debug("in  > getself")
        uri = "/api/v1/self"
        resp = self.mist_get(uri)
        if resp.data:
            # Deal with 2FA if needed
            if (
                resp.data.get('two_factor_required') is True
                and resp.data.get('two_factor_passed') is False
            ):
                print()
                two_factor_ok = False
                while not two_factor_ok:
                    two_factor = input(
                        "Two Factor Authentication code required: ")
                    two_factor_ok = self._two_factor_authentication(two_factor)
                self._getself()
            # Get details of the account
            else:
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
                print()
                print(f"Welcome {self.first_name} {self.last_name}!")
                print()
                return True
        else:
            console.error("Authentication not valid...")
            print()
            resp = input(
                f"Do you want to try with new credentials for {self._cloud_uri} (y/N)? " % ())
            if resp.lower() == "y":
                self._process_login()
                return self._getself()
            else:
                sys.exit(0)

    def set_log_level(self, log_level):
        """
        0: emergency
        1: alert
        2: critical
        3: error
        4: warning
        5: notice
        6: info
        7: debug
        """
        global console
        console = Console(log_level)


###### ENTRYPOINT ########

logging.basicConfig(filename=log_file, filemode='w')
logger.setLevel(logging.DEBUG)