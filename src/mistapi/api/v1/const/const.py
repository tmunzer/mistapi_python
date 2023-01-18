
from mistapi.api.v1.const.alarm_defs import getAlarmDefinitions
import requests

class Const():

    def __init__(self):
        self.const = const.Const()
        self._cloud_uri = ""
        self._session = requests.session()
        self.privileges = ""