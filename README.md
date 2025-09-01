# MISTAPI - Python Package for Mist API

[![PyPI version](https://img.shields.io/pypi/v/mistapi.svg)](https://pypi.org/project/mistapi/)
[![Python versions](https://img.shields.io/pypi/pyversions/mistapi.svg)](https://pypi.org/project/mistapi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive Python package to interact with the Mist Cloud APIs, built from the official [Mist OpenAPI specifications](https://www.juniper.net/documentation/us/en/software/mist/api/http/getting-started/how-to-get-started).

## MIT LICENSE

Copyright (c) 2023 Thomas Munzer

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the  Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


## Links

- **Documentation**: [Mist API Documentation](https://doc.mist-lab.fr)
- **Source Code**: [GitHub Repository](https://github.com/tmunzer/mistapi_python)
- **PyPI Package**: [mistapi on PyPI](https://pypi.org/project/mistapi/)
- **Examples**: [Mist Library Examples](https://github.com/tmunzer/mist_library)
- **Bug Reports**: [GitHub Issues](https://github.com/tmunzer/mistapi_python/issues)


## Features

This package provides a complete Python interface to the Mist Cloud APIs:

### Core Features
* **Authentication Management**: Support for API tokens and login/password (with 2FA)
* **Interactive CLI**: Built-in functions for organization and site selection
* **Comprehensive API Coverage**: Auto-generated from OpenAPI specs covering all endpoints
* **HashiCorp Vault Integration**: Secure credential storage support
* **Pagination Support**: Automatic handling of paginated responses
* **Robust Error Handling**: Detailed error responses and logging
* **Proxy Support**: HTTP/HTTPS proxy configuration

### API Coverage
The package includes complete coverage of Mist APIs:

#### Organization Level APIs
* Organizations, Sites, Site Groups, Site Templates
* Devices (APs, Switches, Gateways), Device Profiles, Device Templates
* Network configurations (WLANs, VPNs, Networks, EVPN Topologies)
* User management (Admins, API Tokens, Guests, PSKs)
* Monitoring (Alarms, Events, Insights, Statistics, SLE)
* Assets, Licenses, Subscriptions, Webhooks
* Security (NAC, Policies, Certificates)
* MSP and Multi-tenant management

#### Site Level APIs  
* Site-specific device management and configuration
* RF diagnostics and optimization (RRM, Channel Planning)
* Location services (Maps, Zones, Beacons, Asset tracking)
* Client management and analytics
* Synthetic testing and performance monitoring
* Anomaly detection and troubleshooting

#### Constants and Utilities
* Device models, AP channels, Application categories
* Country codes, Alarm definitions, Event types
* Webhook topics, License types, and more

#### Additional Services
* Two-factor authentication, OAuth, Login/Logout
* Account recovery, Registration, Invitations
* Mobile device management, Installer workflows

## Requirements

* Python 3.10 or higher
* Dependencies: `requests`, `python-dotenv`, `tabulate`, `deprecation`, `hvac`

## Installation

Install the package using pip:

```bash
# Linux/macOS
python3 -m pip install mistapi

# Windows
py -m pip install mistapi

# Install with development dependencies (for contributors)
pip install mistapi[dev]
```

## Upgrade

```bash
# Linux/macOS
python3 -m pip install --upgrade mistapi

# Windows
py -m pip install --upgrade mistapi
```

## Configuration

Configuration is optional. All required information can be passed as `APISession` parameters.
However, you can set them in an `.env` file. The location of this file must be provided when calling the `APISession` class with the `env_file` parameter:

```python
import mistapi
apisession = mistapi.APISession(env_file="path/to/the/.env")
```

### Environment Variables
| Variable Name         | Type   | Default                | Comment                                                                                                                                                                                                                                                                   |
|-----------------------|--------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MIST_HOST             | string | None                   | The Mist Cloud to use. It must be the "api" one (e.g. `api.mist.com`, `api.eu.mist.com`, ...)                                                                                                                                                                             |
| MIST_APITOKEN         | string | None                   | The API Token to use.                                                                                                                                                                                                                                                     |
| MIST_USER             | string | None                   | The login to use if no API Token is provided (apitoken use is preferred)                                                                                                                                                                                                  |
| MIST_PASSWORD         | string | None                   | The password to use if no API Token is provided (apitoken use is preferred)                                                                                                                                                                                               |
| MIST_VAULT_URL        | string | https://127.0.0.1:8200 | If the Mist MIST_HOST, MIST_APITOKEN, MIST_USER, MIST_PASSWORD are stored in an HashiCorp Vault, URL of the Vault instance                                                                                                                                                |
| MIST_VAULT_PATH       | string | None                   | If the Mist MIST_HOST, MIST_APITOKEN, MIST_USER, MIST_PASSWORD are stored in an HashiCorp Vault, Path to the secret in Vault                                                                                                                                              |
| MIST_VAULT_MOUNT_POINT| string | secret                 | If the Mist MIST_HOST, MIST_APITOKEN, MIST_USER, MIST_PASSWORD are stored in an HashiCorp Vault, Mount point for the secrets engine                                                                                                                                       |
| MIST_VAULT_TOKEN      | string | None                   | If the Mist MIST_HOST, MIST_APITOKEN, MIST_USER, MIST_PASSWORD are stored in an HashiCorp Vault, Token for authenticating with Vault                                                                                                                                      |
| CONSOLE_LOG_LEVEL     | int    | 20                     | The minimum log level to display on the console, using `logging` schema (0 = Disabled, 10 = Debug, 20 = Info, 30 = Warning, 40 = Error, 50 = Critical)                                                                                                                    |
| LOGGING_LOG_LEVEL     | int    | 10                     | The minimum log level to log on the file, using `logging` schema (0 = Disabled, 10 = Debug, 20 = Info, 30 = Warning, 40 = Error, 50 = Critical). This is only used when the script calling `mistapi` is using Python `logging` package and is configured to log to a file |
| HTTPS_PROXY           | string | None                   | Configure the package to use an HTTP/HTTPS proxy (e.g. http://user:password@myproxy.com:3128)                                                                                                                                                                           |

Example `.env` file:
```bash
MIST_HOST=api.mist.com
MIST_APITOKEN=your_api_token_here
```

## Quick Start

```python
import mistapi

# Initialize session
apisession = mistapi.APISession()

# Authenticate
apisession.login()

# Use the API
device_models = mistapi.api.v1.const.device_models.getDeviceModels(apisession)
print(f"Found {len(device_models.data)} device models")

# Interactive org selection
org_id = mistapi.cli.select_org(apisession)[0]

# Get organization information  
org_info = mistapi.api.v1.orgs.orgs.getOrg(apisession, org_id)
print(f"Organization: {org_info.data['name']}")
```

## Usage

Detailed usage examples are available in the [mist_library repository](https://github.com/tmunzer/mist_library).

### 1. Initialize APISession

```python
import mistapi
apisession = mistapi.APISession()
```
This class accepts different parameters, all optionals:

| Parameter Name    | Type   | Default                | Comment                                                                                                                                                                                                                                                                   |
|-------------------|--------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| email             | str    | None                   | used if login/password is used. Can be defined later                                                                                                                                                                                                                      |
| password          | str    | None                   | used if login/password is used. Can be defined later                                                                                                                                                                                                                      |
| apitoken          | str    | None                   | used if API Token is used. Can be defined later                                                                                                                                                                                                                           |
| host              | str    | None                   | Mist Cloud to reach (e.g. "api.mist.com"). Can be defined later                                                                                                                                                                                                           |
| vault_url         | string | https://127.0.0.1:8200 | If the Mist MIST_HOST, MIST_APITOKEN, MIST_USER, MIST_PASSWORD are stored in an HashiCorp Vault, URL of the Vault instance                                                                                                                                                |
| vault_path        | string | None                   | If the Mist MIST_HOST, MIST_APITOKEN, MIST_USER, MIST_PASSWORD are stored in an HashiCorp Vault, Path to the secret in Vault                                                                                                                                              |
| vault_mount_point | string | secret                 | If the Mist MIST_HOST, MIST_APITOKEN, MIST_USER, MIST_PASSWORD are stored in an HashiCorp Vault, Mount point for the secrets engine                                                                                                                                       |
| vault_token       | string | None                   | If the Mist MIST_HOST, MIST_APITOKEN, MIST_USER, MIST_PASSWORD are stored in an HashiCorp Vault, Token for authenticating with Vault                                                                                                                                      |
| env_file          | str    | None                   | path to the env file to load. See README.md for allowed variables                                                                                                                                                                                                         |
| console_log_level | int    | 20                     | The minimum log level to display on the console, using `logging` schema (0 = Disabled, 10 = Debug, 20 = Info, 30 = Warning, 40 = Error, 50 = Critical)                                                                                                                    |
| logging_log_level | int    | 10                     | The minimum log level to log on the file, using `logging` schema (0 = Disabled, 10 = Debug, 20 = Info, 30 = Warning, 40 = Error, 50 = Critical). This is only used when the script calling `mistapi` is using Python `logging` package and is configured to log to a file |
| https_proxy       | string | None                   | Configure the package to use an HTTP/HTTPS proxy (e.g. http://user:password@myproxy.com:3128)                                                                                                                                                                           |

### 2. Authenticate

The `login()` function must be called to validate authentication:

#### 2.1. Automatic Authentication (with env file)

If the env file contains valid credentials, authentication is automatic:

```python
import mistapi
apisession = mistapi.APISession(env_file="~/.mist_env")
apisession.login()

# Output:
# -------------------------------- Authenticated ---------------------------------
# Welcome Thomas Munzer!

print(apisession.get_authentication_status())  # True
```

#### 2.2. Interactive Authentication

If credentials are missing, the package will prompt for them interactively:

**Cloud Selection:**
If no `host` is configured, you'll be prompted to select a Mist cloud:

```
----------------------------- Mist Cloud Selection -----------------------------

0) APAC 01 (host: api.ac5.mist.com)
1) APAC 03 (host: api.gc7.mist.com) 
2) EMEA 01 (host: api.eu.mist.com)
3) EMEA 02 (host: api.gc3.mist.com)
4) EMEA 03 (host: api.ac6.mist.com)
5) EMEA 04 (host: api.gc6.mist.com)
6) Global 01 (host: api.mist.com)
7) Global 02 (host: api.gc1.mist.com)
8) Global 03 (host: api.ac2.mist.com)
9) Global 04 (host: api.gc2.mist.com)
10) Global 05 (host: api.gc4.mist.com)

Select a Cloud (0 to 10, or q to exit):
```

**Authentication:**
If no authentication is configured, you'll be prompted for credentials:

```
--------------------------- Login/Pwd authentication ---------------------------

Login: user@example.com
Password: 
[  INFO   ] Authentication successful!

Two Factor Authentication code required: 123456
[  INFO   ] 2FA authentication succeeded

-------------------------------- Authenticated ---------------------------------

Welcome Thomas Munzer!
```

### 3. Using the APIs

Once authenticated, you can access all Mist API endpoints:

```python
# Get device models (constants)
device_models = mistapi.api.v1.const.device_models.getDeviceModels(apisession)
print(f"Status: {device_models.status_code}")
print(f"URL: {device_models.url}")
print(f"Data: {len(device_models.data)} models")

# Get organization statistics
org_stats = mistapi.api.v1.orgs.stats.getOrgStats(apisession, org_id)
print(f"Organization has {org_stats.data['num_sites']} sites")

# Search for devices
devices = mistapi.api.v1.orgs.devices.searchOrgDevices(apisession, org_id, type="ap")
print(f"Found {len(devices.data['results'])} access points")
```
```

## CLI Helper Functions

The package includes helpful CLI functions for interactive use:

### Organization Selection

```python
# Select single organization
org_ids = mistapi.cli.select_org(apisession)
print(f"Selected org: {org_ids[0]}")

# Select multiple organizations
org_ids = mistapi.cli.select_org(apisession, allow_many=True)
print(f"Selected {len(org_ids)} organizations")
```

Output:
```
Available organizations:
0) Acme Corp (id: 203d3d02-xxxx-xxxx-xxxx-76896a3330f4)
1) Demo Lab (id: 6374a757-xxxx-xxxx-xxxx-361e45b2d4ac)
...

Select an Org (0 to 2, or q to exit): 0
```

### Site Selection  

```python
# Select site within an organization
site_ids = mistapi.cli.select_site(apisession, org_id="203d3d02-xxxx-xxxx-xxxx-76896a3330f4")
print(f"Selected site: {site_ids[0]}")
```

Output:
```
Available sites:
0) Headquarters (id: f5fcbee5-xxxx-xxxx-xxxx-1619ede87879)
1) Branch Office (id: a8b2c3d4-xxxx-xxxx-xxxx-987654321abc)
...

Select a Site (0 to 1, or q to exit): 0
```

## Pagination Support

For APIs that return paginated results, the package provides convenient methods:

### Get Next Page

```python
# Get first page
response = mistapi.api.v1.orgs.clients.searchOrgClientsEvents(apisession, org_id, duration="1d")
print(f"First page: {len(response.data['results'])} results")
print(f"Next page URL: {response.next}")

# Get next page
response_2 = mistapi.get_next(apisession, response)
print(f"Second page: {len(response_2.data['results'])} results")
```

### Get All Pages

```python
# Get all pages automatically
response = mistapi.api.v1.orgs.clients.searchOrgClientsEvents(apisession, org_id, duration="1d")
print(f"First page: {len(response.data['results'])} results")

all_data = mistapi.get_all(apisession, response)
print(f"Total results across all pages: {len(all_data)}")
```

## API Help and Documentation

Get help on any API function:

```python
help(mistapi.api.v1.orgs.stats.getOrgStats)
```

This displays detailed information about parameters, return values, and usage examples.

## Error Handling

The package provides structured error handling:

```python
try:
    org_info = mistapi.api.v1.orgs.orgs.getOrg(apisession, "invalid-org-id")
except Exception as e:
    print(f"API Error: {e}")
    
# Check response status
response = mistapi.api.v1.orgs.orgs.listOrgs(apisession)
if response.status_code == 200:
    print(f"Success: {len(response.data)} organizations")
else:
    print(f"Error {response.status_code}: {response.data}")
```

## Supported Mist Clouds

The package supports all Mist cloud instances:

- **APAC 01**: api.ac5.mist.com
- **APAC 03**: api.gc7.mist.com  
- **EMEA 01**: api.eu.mist.com
- **EMEA 02**: api.gc3.mist.com
- **EMEA 03**: api.ac6.mist.com
- **EMEA 04**: api.gc6.mist.com
- **Global 01**: api.mist.com
- **Global 02**: api.gc1.mist.com
- **Global 03**: api.ac2.mist.com
- **Global 04**: api.gc2.mist.com
- **Global 05**: api.gc4.mist.com

## Examples and Use Cases

### Device Management

```python
# List all devices in an organization
devices = mistapi.api.v1.orgs.devices.listOrgDevices(apisession, org_id)

# Get specific device details
device = mistapi.api.v1.orgs.devices.getOrgDevice(apisession, org_id, device_id)

# Update device configuration
update_data = {"name": "New Device Name"}
result = mistapi.api.v1.orgs.devices.updateOrgDevice(apisession, org_id, device_id, body=update_data)
```

### Site Management

```python
# Create a new site
site_data = {
    "name": "New Branch Office",
    "country_code": "US",
    "timezone": "America/New_York"
}
new_site = mistapi.api.v1.orgs.sites.createOrgSite(apisession, org_id, body=site_data)

# Get site statistics
site_stats = mistapi.api.v1.sites.stats.getSiteStats(apisession, site_id)
```

### Client Analytics

```python
# Search for wireless clients
clients = mistapi.api.v1.orgs.clients.searchOrgWirelessClients(
    apisession, org_id, 
    duration="1d",
    limit=100
)

# Get client events
events = mistapi.api.v1.orgs.clients.searchOrgClientsEvents(
    apisession, org_id,
    duration="1h",
    client_mac="aa:bb:cc:dd:ee:ff"
)
```

## Development and Testing

For contributors and advanced users:

### Development Setup

```bash
# Clone the repository
git clone https://github.com/tmunzer/mistapi_python.git
cd mistapi_python

# Install with development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run tests with coverage
pytest --cov=src/mistapi --cov-report=html

# Run linting
ruff check src/
```

### Package Structure

```
src/mistapi/
├── __init__.py           # Main package exports
├── __api_session.py      # Session management and authentication  
├── __api_request.py      # HTTP request handling
├── __api_response.py     # Response parsing and pagination
├── __logger.py           # Logging configuration
├── __pagination.py       # Pagination utilities
├── cli.py               # Interactive CLI functions
├── __models/            # Data models (privileges, etc.)
└── api/v1/              # Auto-generated API endpoints
    ├── const/           # Constants and enums
    ├── orgs/            # Organization-level APIs
    ├── sites/           # Site-level APIs  
    ├── login/           # Authentication APIs
    └── utils/           # Utility functions
```


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Guidelines

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)  
5. Open a Pull Request
