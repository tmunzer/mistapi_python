'''
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
'''

import json
from tabulate import tabulate

def pretty_print(response, fields=None):
    if "result" in response:
        data = response["result"]
    else:
        data = response
    print("")
    if type(data) is list:  
        if fields is None:
            fields = "keys" 
        print(tabulate(data, headers=fields))
    elif type(data) == dict:
        print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
    else:
        print(data)    
    print("")