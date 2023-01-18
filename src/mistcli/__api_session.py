'''
Written by: Thomas Munzer (tmunzer@juniper.net)
Github repository: https://github.com/tmunzer/Mist_library/
'''

import requests
import sys
import json
from getpass import getpass

from mistcli.__api_request import APIRequest
#from mistcli import apis
from mistcli.__models.privilege import Privileges

import logging
log_file = "./org_migration.log"
logger = logging.getLogger(__name__)

from mistcli.__console import Console 
console = Console(7)

###### GLOBALS ######
clouds = []

def _header():
    print("".center(80, '-'))
    print(" Mist Python CLI Session ".center(80, "-"))
    print("")
    print(" Written by: Thomas Munzer (tmunzer@juniper.net)")
    print(" Github    : https://github.com/tmunzer/mist_library")
    print("")
    print(" This file is licensed under the MIT License.")
    print("")
    print("".center(80, '-'))
    print()


#### PARAMETERS #####

class APISession(APIRequest):
    """Class managing REST login and requests"""

    def __init__(self, load_settings:bool=True, email:str="", password:str="", apitoken:str=None, host:str=None):    
        if load_settings:
            _header()
        # user and https session parameters
        self._cloud_uri = host
        self.email= email
        self._password= password
        self._session = requests.session()
        self._csrftoken = ""
        self._apitoken = apitoken
        self.first_name= ""
        self.last_name= ""
        self.via_sso= False
        self.tags= []
        
        self.privileges= Privileges([])
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
### CLOUD FUNCTIONS
    def set_cloud(self, cloud_uri:str):
        """
        Set Mist Cloud to reach.
        must be something like "api.mist.com", "api.eu.mist.com", ...
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
        i=0
        print()
        print(" Mist Cloud Selection ".center(80, "-"))
        print()
        for cloud in clouds:
            print(f"{i}) {cloud['short']} (host: {cloud['host']})")
            i+=1

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
### AUTH FUNCTIONS
    def set_api_token(self, apitoken:str):
        """
        Set Mist API Token
        """
        self._apitoken = apitoken
        self._session.headers.update({'Authorization': "Token " + self._apitoken})
        self._set_authenticated(True)            

    def _process_login(self): 
        console.debug("in  > _process_login")
        """
        Function to authenticate a user. Will create and store a session used by other requests
        Params: email, password
        return: nothing
        """
        print()
        print(" Login/Pwd authentication ".center(80, "-"))
        print()

        self._session = requests.session()
        if not self.email: self.email = input("Login: ")
        if not self._password: self._password = getpass("Password: ")

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
            console.error(f"Authentication failed: {resp.json().get('detail')}")
            self.email = None
            self._password = None
            print()
            self._process_login()

    def login(self):
        console.debug("in > login")
        if self._authenticated:
            console.error("Already logged in...")
        else:
            if not self._cloud_uri: self._cloud_uri = self.select_cloud()
            if self._apitoken:
                self.set_api_token(self._apitoken)
            if not self._authenticated:
                self._process_login()
            # if successfuly authenticated
            if self.get_authentication_status(): 
                self._getself()


    def logout(self):  
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

    def _set_authenticated(self, value):  
        console.debug("in  > _set_authenticated")
        if value == True:
            self._authenticated = True
            if not self._apitoken:
                try: 
                    cookies_ext = next(item["cookies_ext"] for item in clouds if item["host"] == self._cloud_uri)
                except:
                    cookies_ext = ""
                self._csrftoken = self._session.cookies['csrftoken' + cookies_ext]
                self._session.headers.update({'X-CSRFToken': self._csrftoken})
        elif value == False:
            self._authenticated = False
            self._csrftoken = ""
            del self._session

    def get_authentication_status(self):  
        console.debug("in  > get_authentication_status")
        return self._authenticated or self._apitoken 

    def get_api_token(self):  
        console.debug("in  > list_api_token")
        #resp = apis.self.self.get
        #resp = self.mist_get("/api/v1/self/apitokens")        
        #return resp

    def create_api_token(self, token_name:str=None):  
        console.debug("in  > create_api_token")
        resp = self.mist_post("/api/v1/self/apitokens")
        uri = f"https://{self._cloud_uri}/api/v1/self/apitokens"
        resp = self._session.post(uri)
        return resp

    def delete_api_token(self, token_id):  
        console.debug("in  > delete_api_token")
        uri = f"https://{self._cloud_uri}/api/v1/self/apitokens/{token_id}"
        resp = self._session.delete(uri)
        return resp

    def _two_factor_authentication(self, two_factor):  
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
        """Retrieve information about the current user and store them in the current object.
        Params: password (optional. Only needed for 2FA processing)
        Return: none"""
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
                    two_factor = input("Two Factor Authentication code required: ")                    
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
            resp = input(f"Do you want to try with new credentials for {self._cloud_uri} (y/N)? " %())
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
import pkgutil
data = pkgutil.get_data(__name__, "static/clouds.json")
clouds = json.loads(data)

# with open("./clouds.json", "r") as f:
#     data = f.read()
#    clouds = json.loads(data)

if __name__ == "__main__":
    #### LOGS ####
    logging.basicConfig(filename=log_file, filemode='w')
    logger.setLevel(logging.DEBUG)

