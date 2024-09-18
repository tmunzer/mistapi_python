# MISTAPI - Python Package to use MIST API
 

## MIT LICENSE
 
Copyright (c) 2023 Thomas Munzer

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the  Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


## Features
This package is build from the [Mist OpenAPI specifications](https://doc.mist-lab.fr) and is designed to simplify the use of the Mist APIs with Python scripts.

* Manage Mist Authentication with login/password (and 2FA if required) or API Token
* Provide interactive user inputs for login and org/site selections
* Provide easy access to Mist APIs endpoints and documentation

## Installation
This Python Package can be install with `pip`:
```python3
# Linux/macOS
python3 -m pip install mistapi

# Windows
py -m pip install mistapi
```

## Upgrade
```python3
# Linux/macOS
python3 -m pip install --upgrade mistapi

# Windows
py -m pip install --upgrade mistapi
```

## Configuration
Configuration is optional. All the required information can be passed as APISession parameter.
However, it is possible to set them in an `.env` file. The location of this file must be provided during when calling the APISession class with the `env_file` parameter:
```python3
> import mistapi
> apisession = mistapi.APISession(enf_file="path/to/the/.env")
```

### Environment Variables
| Variable Name | Type | Default | Comment |
| ------------- | ---- |  ------ | ------- |
MIST_HOST | string | None | The Mist Cloud to use. It must be the "api" one (e.g. `api.mist.com`, `api.eu.mist.com`, ...) |
MIST_APITOKEN | string | None | The API Token to use.  |
MIST_USER | string | None | The login to use if no API Token is provided (apitoken use is prefered) |
MIST_PASSWORD | string | None | The password to use if no API Token is provided (apitoken use is prefered) |
CONSOLE_LOG_LEVEL | int | 20 | The minimum log level to display on the console, using `logging` schema (0 = Disabled, 10 = Debug, 20 = Info, 30 = Warning, 40 = Error, 50 = Critical) |
LOGGING_LOG_LEVEL | int | 10 | The minimum log level to log on the file, using `logging` schema (0 = Disabled, 10 = Debug, 20 = Info, 30 = Warning, 40 = Error, 50 = Critical). This is only used when the script calling `mistapi` is using Python `logging` package and is configured to log to a file |
HTTPS_PROXY | string | None | configure the package to use an HTTP/HTTPS (e.g. http://user:passowrd@myproxy.com:3128)

An example of the environment file content is:
```
MIST_HOST = api.mist.com
MIST_APITOKEN = xxxxxx
```

## Usage
Usage examples are available in the [mist_library repository](https://github.com/tmunzer/mist_library).

To use it, 
### 1. `APISession` must be instanciated:
```python3
>>> import mistapi
>>> apisession = mistapi.APISession()
```
This class accepts different parameters, all optionals:

| Parameter Name | Type | Default | Comment |
| ------------- | ---- |  ------ | ------- |
email | str | None | used if login/password is used. Can be defined later |
password | str | None | used if login/password is used. Can be defined later |
apitoken | str | None | used if API Token is used. Can de defined later |
host | str | None | Mist Cloud to reach (e.g. "api.mist.com"). Can de defined later |
env_file | str | None | path to the env file to load. See README.md for allowed variables |
console_log_level | int | 20 | The minimum log level to display on the console, using `logging` schema (0 = Disabled, 10 = Debug, 20 = Info, 30 = Warning, 40 = Error, 50 = Critical) |
logging_log_level | int | 10 | The minimum log level to log on the file, using `logging` schema (0 = Disabled, 10 = Debug, 20 = Info, 30 = Warning, 40 = Error, 50 = Critical). This is only used when the script calling `mistapi` is using Python `logging` package and is configured to log to a file |
https_proxy | string | None | configure the package to use an HTTP/HTTPS (e.g. http://user:passowrd@myproxy.com:3128)

### 2. `login()` function must be called to validate the authentication. 

#### 2.1. If the env file is provided and all the required information are valid, the session is validated:
```python3
>>> import mistapi
>>> apisession = mistapi.APISession(env_file="~/.mist_env")
>>> apisession.login()

-------------------------------- Authenticated ---------------------------------

Welcome Thomas Munzer!

>>> apisession.get_authentication_status()
True
```

#### 2.2. If the env file is not provided or does not contain the required valid information, the missing information will be requested:

* If no `host` has been configured, an interactive input will ask for it.
```python3
>>> apisession.login()

----------------------------- Mist Cloud Selection -----------------------------

0) APAC 01 (host: api.ac5.mist.com)
1) Europe 01 (host: api.eu.mist.com)
2) Global 01 (host: api.mist.com)
3) Global 02 (host: api.gc1.mist.com)
4) Global 03 (host: api.ac2.mist.com)
5) Global 04 (host: api.gc2.mist.com)

Select a Cloud (0 to 5, or q to exit): 
```
* if not authentication (`apitoken` or `email`/`password`) has been configured, an interactive input will ask for it. If login/password authentication is used and 2FA is requested by the Mist Cloud, the 2FA code will be asked.
```python3
>>> apisession.login()

--------------------------- Login/Pwd authentication ---------------------------

Login: tmunzer@juniper.net
Password: 
[  INFO   ] Authentication successful!

Two Factor Authentication code required: 122749
[  INFO   ] 2FA authentication successed

-------------------------------- Authenticated ---------------------------------

Welcome Thomas Munzer!
```

### 3. It is now possible to request Mist APIs
```python3
>>> device_models = mistapi.api.v1.const.device_models.getDeviceModels(apisession)
>>> device_models.url
'https://api.mist.com/api/v1/const/device_models'
>>> device_models.status_code
200
>>> device_models.data
[{'model': 'AP41', 'type': 'ap', 'ap_type': 'aph', 'description': 'AP-41', 'display': 'AP41', 'has_wifi_band5': True, 'has_wifi_band24': True, 'has_scanning_radio': True, 'has_usb': True, 'has_vble': True, 'vble': {'power': 8, 'beacon_rate': 4, 'beams': 8}, 'band24': {'max_clients': 128, 'max_power': 19, 'min_power': 8}, 'fcc_dfs_ok': ...
```

## Usefull functions
* easily find an Org Id from the current account with `mistapi.cli.select_org(apisession)`
```python3
>>> mistapi.cli.select_org(apisession)

Available organizations:
0) 000_TM-LAB (id: 6374a757-xxxx-xxxx-xxxx-361e45b2d4ac)
...
41) TM-LAB (id: 203d3d02-xxxx-xxxx-xxxx-76896a3330f4)
...

Select an Org (0 to 44, or q to exit): 41
['203d3d02-xxxx-xxxx-xxxx-76896a3330f4']
```

* easily find a Site Id from an org  with `mistapi.cli.select_org(apisession)`
```python3
>>> mistapi.cli.select_site(apisession, org_id="203d3d02-xxxx-xxxx-xxxx-76896a3330f4")

Available sites:
0) HLAB (id: f5fcbee5-xxxx-xxxx-xxxx-1619ede87879)
...

Select a Site (0 to 6, or q to exit): 0
['f5fcbee5-xxxx-xxxx-xxxx-1619ede87879']
```

* get the next page or all the pages from a request
For some requests, the Mist Cloud is using pagination to limit the size of the response. The required information the find the next page can either in the HTTP header (headers `X-Page-Total`, `X-Page-Limit` and `X-Page-Page`) or with the `next` key in the json document. To make it easier to request the next page or all the pages, the `mistapi` package is prossessing the response to extract or generate the URI to retrieve the next page.
```python3
>>> response = mistapi.api.v1.orgs.clients.searchOrgClientsEvents(apisession, my_org_id, duration="1d")
>>> len(response.data["results"])
100
>>> response.next
'/api/v1/orgs/203d3d02-xxxx-xxxx-xxxx-76896a3330f4/clients/events/search?end=1676966894&limit=100&search_after=%5B1676966519626%5D&start=1676880494'
```
To get the next page, use the `mistapi.get_next()` function. The returned response will be the same format as the previous one:

```python3
>>> response_1 = mistapi.api.v1.orgs.clients.searchOrgClientsEvents(apisession, my_org_id, duration="1d")
>>> len(response_1.data["results"])
100
>>> response_1.next
'/api/v1/orgs/203d3d02-xxxx-xxxx-xxxx-76896a3330f4/clients/events/search?end=1676966894&limit=100&search_after=%5B1676966519626%5D&start=1676880494'
>>> response_2 = response.get_next(apisession, response_1)
>>> response_2.next
'/api/v1/orgs/203d3d02-xxxx-xxxx-xxxx-76896a3330f4/clients/events/search?end=1676966894&limit=100&search_after=%5B1676966204625%5D&start=1676880494'
>>> len(response_2.data["results"])
100
```
To retrieve all the pages, use the `mistapi.get_all()` function. The returned response will be a list with the concatained data from all the Mist responses:
```python3
>>> response = mistapi.api.v1.orgs.clients.searchOrgClientsEvents(apisession, my_org_id, duration="1d")
>>> len(response.data["results"])
100
>>> response.next
'/api/v1/orgs/203d3d02-xxxx-xxxx-xxxx-76896a3330f4/clients/events/search?end=1676966894&limit=100&search_after=%5B1676966519626%5D&start=1676880494'
>>> data = mistapi.get_all(apisession, response)
>>> len(data)
26027
```

* get help on a specific function
```python3
>>> help(mistapi.api.v1.orgs.stats.getOrgStats)
Help on function getOrgStats in module mistapi.api.v1.orgs.stats:

getOrgStats(mist_session: mistapi.__api_session.APISession, org_id: str, page: int = 1, limit: int = 100, start: int = None, end: int = None, duration: str = '1d') -> mistapi.__api_response.APIResponse
    API doc: https://doc.mist-lab.fr/#operation/getOrgStats
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    
    PATH PARAMS
    -----------
    :param str org_id        
    
    QUERY PARAMS
    ------------
    :param int page
    :param int limit
    :param int start
    :param int end
    :param str duration(1d, 1h, 10m)
    
    RETURN
    -----------
    :return APIResponse - response from the API call
```
