
import json

try:
    from config import log_level
except:
    log_level = 6
finally:
    from mistapi.__logger import Console
    console = Console(log_level)


class Invite:

    def __init__(self):
        self.email = ""
        self.first_name = ""
        self.last_name = ""
        self.hours = 24
        self.privileges = []        

    def __str__(self):
        string = ""
        string += f"Email: {self.email}\r\n"
        string += f"First Name: {self.first_name}\r\n"
        string += f"Last Name: {self.last_name}\r\n"
        string += f"Hours: {self.hours}\r\n"
        string += f"Privileges: {self.privileges}\r\n" 
        return string
        
    def toJSON(self):
        invite = {
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "hours": self.hours,
            "privileges": self.privileges
        }
        return invite

    def define(self, email = "", first_name="", last_name="", hours=24, privileges=[]):
        self.set_email(email)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_hours(hours)
        self.set_privileges(privileges)
        