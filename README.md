# MISTAPI - Python Package for Mist API

[![PyPI version](https://img.shields.io/pypi/v/mistapi.svg)](https://pypi.org/project/mistapi/)
[![Python versions](https://img.shields.io/pypi/pyversions/mistapi.svg)](https://pypi.org/project/mistapi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive Python package to interact with the Mist Cloud APIs, built from the official [Mist OpenAPI specifications](https://www.juniper.net/documentation/us/en/software/mist/api/http/getting-started/how-to-get-started).

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
    - [Using Environment File](#using-environment-file)
    - [Environment Variables](#environment-variables)
- [Authentication](#authentication)
    - [Interactive Authentication](#interactive-authentication)
    - [Environment File Authentication](#environment-file-authentication)
    - [HashiCorp Vault Authentication](#hashicorp-vault-authentication)
    - [System Keyring Authentication](#system-keyring-authentication)
    - [Direct Parameter Authentication](#direct-parameter-authentication)
- [API Requests Usage](#api-requests-usage)
    - [Basic API Calls](#basic-api-calls)
    - [Error Handling](#error-handling)
    - [Log Sanitization](#log-sanitization)
    - [Getting Help](#getting-help)
    - [CLI Helper Functions](#cli-helper-functions)
    - [Pagination](#pagination-support)
    - [Examples](#examples)
- [WebSocket Streaming](#websocket-streaming)
    - [Available Channels](#available-channels)
    - [Callbacks](#callbacks)
    - [Usage Patterns](#usage-patterns)
- [Development](#development-and-testing)
- [Contributing](#contributing)
- [License](#license)
- [Links](#links)

---

## Features

### Supported Mist Clouds
Support for all Mist cloud instances worldwide:
- **APAC**: api.ac5.mist.com, api.gc5.mist.com, api.gc7.mist.com
- **EMEA**: api.eu.mist.com, api.gc3.mist.com, api.ac6.mist.com, api.gc6.mist.com
- **Global**: api.mist.com, api.gc1.mist.com, api.ac2.mist.com, api.gc2.mist.com, api.gc4.mist.com

### Authentication
- API token and username/password authentication (with 2FA support)
- Environment variable configuration (`.env` file support)
- HashiCorp Vault integration for secure credential storage
- System keyring integration (macOS Keychain, Windows Credential Locker, etc.)
- Interactive CLI prompts for credentials when needed

### Core Features
- **Complete API Coverage**: Auto-generated from OpenAPI specs
- **Automatic Pagination**: Built-in support for paginated responses
- **Error Handling**: Detailed error responses and logging
- **Proxy Support**: HTTP/HTTPS proxy configuration
- **Log Sanitization**: Automatic redaction of sensitive data in logs

### API Coverage
**Organization Level**: Organizations, Sites, Devices (APs/Switches/Gateways), WLANs, VPNs, Networks, NAC, Users, Admins, Guests, Alarms, Events, Statistics, SLE, Assets, Licenses, Webhooks, Security Policies, MSP management

**Site Level**: Device management, RF optimization, Location services, Maps, Client analytics, Asset tracking, Synthetic testing, Anomaly detection

**Constants & Utilities**: Device models, AP channels, Applications, Country codes, Alarm definitions, Event types, Webhook topics

**Additional Services**: OAuth, Two-factor authentication, Account recovery, Invitations, MDM workflows

---

## Installation

### Basic Installation

```bash
# Linux/macOS
python3 -m pip install mistapi

# Windows
py -m pip install mistapi
```

### Upgrade to Latest Version

```bash
# Linux/macOS
python3 -m pip install --upgrade mistapi

# Windows
py -m pip install --upgrade mistapi
```

### Development Installation

```bash
# Install with development dependencies (for contributors)
pip install mistapi[dev]
```

### Requirements
- Python 3.10 or higher
- Dependencies: `requests`, `python-dotenv`, `tabulate`, `deprecation`, `hvac`, `keyring`

---

## Quick Start

```python
import mistapi

# Initialize session
apisession = mistapi.APISession()

# Authenticate (interactive prompt if credentials not configured)
apisession.login()

# Use the API - Get device models
device_models = mistapi.api.v1.const.device_models.listDeviceModels(apisession)
print(f"Found {len(device_models.data)} device models")

# Interactive organization selection
org_id = mistapi.cli.select_org(apisession)[0]

# Get organization information
org_info = mistapi.api.v1.orgs.orgs.getOrg(apisession, org_id)
print(f"Organization: {org_info.data['name']}")
```

---

## Configuration

Configuration is optional - you can pass all parameters directly to `APISession`. However, using an `.env` file simplifies credential management.

### Using Environment File

```python
import mistapi
apisession = mistapi.APISession(env_file="~/.mist_env")
```

### Environment Variables

Create a `.env` file with your credentials:

```bash
MIST_HOST=api.mist.com
MIST_APITOKEN=your_api_token_here

# Alternative to API token
# MIST_USER=your_email@example.com
# MIST_PASSWORD=your_password

# Proxy configuration
# HTTPS_PROXY=http://user:password@myproxy.com:3128

# Logging configuration
# CONSOLE_LOG_LEVEL=20  # 0=Disabled, 10=Debug, 20=Info, 30=Warning, 40=Error, 50=Critical
# LOGGING_LOG_LEVEL=10
```

### Configuration Options

| Environment Variable | APISession Parameter | Type | Default | Description |
|---|---|---|---|---|
| `MIST_HOST` | `host` | string | None | Mist Cloud API endpoint (e.g., `api.mist.com`) |
| `MIST_APITOKEN` | `apitoken` | string | None | API Token for authentication (recommended) |
| `MIST_USER` | `email` | string | None | Username/email for authentication |
| `MIST_PASSWORD` | `password` | string | None | Password for authentication |
| `MIST_KEYRING_SERVICE` | `keyring_service` | string | None | System keyring service name |
| `MIST_VAULT_URL` | `vault_url` | string | https://127.0.0.1:8200 | HashiCorp Vault URL |
| `MIST_VAULT_PATH` | `vault_path` | string | None | Path to secret in Vault |
| `MIST_VAULT_MOUNT_POINT` | `vault_mount_point` | string | secret | Vault mount point |
| `MIST_VAULT_TOKEN` | `vault_token` | string | None | Vault authentication token |
| `CONSOLE_LOG_LEVEL` | `console_log_level` | int | 20 | Console log level (0-50) |
| `LOGGING_LOG_LEVEL` | `logging_log_level` | int | 10 | File log level (0-50) |
| `HTTPS_PROXY` | `https_proxy` | string | None | HTTP/HTTPS proxy URL |
| | `env_file` | str | None | Path to `.env` file |


---

## Authentication

The `login()` function must be called to authenticate. The package supports multiple authentication methods.

### 1. Interactive Authentication

If credentials are not configured, you'll be prompted interactively:

**Cloud Selection:**
```
----------------------------- Mist Cloud Selection -----------------------------

0) APAC 01 (host: api.ac5.mist.com)
1) EMEA 01 (host: api.eu.mist.com)
2) Global 01 (host: api.mist.com)
...

Select a Cloud (0 to 10, or q to exit):
```

**Credential Prompt:**
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

### 2. Environment File Authentication

```python
import mistapi

apisession = mistapi.APISession(env_file="~/.mist_env")
apisession.login()

# Output:
# -------------------------------- Authenticated ---------------------------------
# Welcome Thomas Munzer!
```

### 3. HashiCorp Vault Authentication

```python
import mistapi

apisession = mistapi.APISession(
    vault_url="https://vault.mycompany.com:8200",
    vault_path="secret/data/mist/credentials",
    vault_token="s.xxxxxxx"
)
apisession.login()
```

### 4. System Keyring Authentication

```python
import mistapi

apisession = mistapi.APISession(keyring_service="my_mist_service")
apisession.login()
```

**Note:** The keyring must contain: `MIST_HOST`, `MIST_APITOKEN` (or `MIST_USER` and `MIST_PASSWORD`)

### 5. Direct Parameter Authentication

```python
import mistapi

apisession = mistapi.APISession(
    host="api.mist.com",
    apitoken="your_token_here"
)
apisession.login()
```


---

## API Requests Usage

### Basic API Calls

```python
# Get device models (constants)
response = mistapi.api.v1.const.device_models.listDeviceModels(apisession)
print(f"Status: {response.status_code}")
print(f"Data: {len(response.data)} models")

# Get organization information
org_info = mistapi.api.v1.orgs.orgs.getOrg(apisession, org_id)
print(f"Organization: {org_info.data['name']}")

# Get organization statistics
org_stats = mistapi.api.v1.orgs.stats.getOrgStats(apisession, org_id)
print(f"Organization has {org_stats.data['num_sites']} sites")

# Search for devices
devices = mistapi.api.v1.orgs.devices.searchOrgDevices(apisession, org_id, type="ap")
print(f"Found {len(devices.data['results'])} access points")
```

### Error Handling

```python
# Check response status
response = mistapi.api.v1.orgs.orgs.listOrgs(apisession)
if response.status_code == 200:
    print(f"Success: {len(response.data)} organizations")
else:
    print(f"Error {response.status_code}: {response.data}")

# Exception handling
try:
    org_info = mistapi.api.v1.orgs.orgs.getOrg(apisession, "invalid-org-id")
except Exception as e:
    print(f"API Error: {e}")
```


### Log Sanitization

The package automatically sanitizes sensitive data in logs:

```python
import logging
from mistapi.__logger import LogSanitizer

# Configure logging
LOG_FILE = "./app.log"
logging.basicConfig(filename=LOG_FILE, filemode="w")
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

# Add sanitization filter
LOGGER.addFilter(LogSanitizer())

# Sensitive data is automatically redacted
LOGGER.debug({"user": "john", "apitoken": "secret123", "password": "pass456"})
# Output: {"user": "john", "apitoken": "****", "password": "****"}
```

### Getting Help

```python
# Get detailed help on any API function
help(mistapi.api.v1.orgs.stats.getOrgStats)
```

---

### CLI Helper Functions

Interactive functions for selecting organizations and sites.

#### Organization Selection

```python
# Select single organization
org_id = mistapi.cli.select_org(apisession)[0]

# Select multiple organizations
org_ids = mistapi.cli.select_org(apisession, allow_many=True)
```

**Output:**
```
Available organizations:
0) Acme Corp (id: 203d3d02-xxxx-xxxx-xxxx-76896a3330f4)
1) Demo Lab (id: 6374a757-xxxx-xxxx-xxxx-361e45b2d4ac)

Select an Org (0 to 1, or q to exit): 0
```

#### Site Selection

```python
# Select site within an organization
site_id = mistapi.cli.select_site(apisession, org_id=org_id)[0]
```

**Output:**
```
Available sites:
0) Headquarters (id: f5fcbee5-xxxx-xxxx-xxxx-1619ede87879)
1) Branch Office (id: a8b2c3d4-xxxx-xxxx-xxxx-987654321abc)

Select a Site (0 to 1, or q to exit): 0
```

---

### Pagination Support

#### Get Next Page

```python
# Get first page
response = mistapi.api.v1.orgs.clients.searchOrgClientsEvents(
    apisession, org_id, duration="1d"
)
print(f"First page: {len(response.data['results'])} results")

# Get next page
if response.next:
    response_2 = mistapi.get_next(apisession, response)
    print(f"Second page: {len(response_2.data['results'])} results")
```

#### Get All Pages Automatically

```python
# Get all pages with a single call
response = mistapi.api.v1.orgs.clients.searchOrgClientsEvents(
    apisession, org_id, duration="1d"
)
print(f"First page: {len(response.data['results'])} results")

# Retrieve all remaining pages
all_data = mistapi.get_all(apisession, response)
print(f"Total results across all pages: {len(all_data)}")
```

---

### Examples

Comprehensive examples are available in the [Mist Library repository](https://github.com/tmunzer/mist_library).

#### Device Management

```python
# List all devices in an organization
devices = mistapi.api.v1.orgs.devices.listOrgDevices(apisession, org_id)

# Get specific device details
device = mistapi.api.v1.orgs.devices.getOrgDevice(
    apisession, org_id, device_id
)

# Update device configuration
update_data = {"name": "New Device Name"}
result = mistapi.api.v1.orgs.devices.updateOrgDevice(
    apisession, device.org_id, device.id, body=update_data
)
```

#### Site Management

```python
# Create a new site
site_data = {
    "name": "New Branch Office",
    "country_code": "US",
    "timezone": "America/New_York"
}
new_site = mistapi.api.v1.orgs.sites.createOrgSite(
    apisession, org_id, body=site_data
)

# Get site statistics
site_stats = mistapi.api.v1.sites.stats.getSiteStats(apisession, new_site.id)
```

#### Client Analytics

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

---

## WebSocket Streaming

The package provides a WebSocket client for real-time event streaming from the Mist API (`wss://{host}/api-ws/v1/stream`). Authentication is handled automatically using the same session credentials (API token or login/password).

### Available Channels

#### Organization Channels

| Class | Channel | Description |
|-------|---------|-------------|
| `mistapi.websockets.orgs.OrgInsightsEvents` | `/orgs/{org_id}/insights/summary` | Real-time insights events for an organization |
| `mistapi.websockets.orgs.OrgMxEdgesStatsEvents` | `/orgs/{org_id}/stats/mxedges` | Real-time MX edges stats for an organization |
| `mistapi.websockets.orgs.OrgMxEdgesUpgradesEvents` | `/orgs/{org_id}/mxedges` | Real-time MX edges upgrades events for an organization |

#### Site Channels

| Class | Channel | Description |
|-------|---------|-------------|
| `mistapi.websockets.sites.SiteClientsStatsEvents` | `/sites/{site_id}/stats/clients` | Real-time clients stats for a site |
| `mistapi.websockets.sites.SiteDeviceCmdEvents` | `/sites/{site_id}/devices/{device_id}/cmd` | Real-time device command events for a site |
| `mistapi.websockets.sites.SiteDeviceStatsEvents` | `/sites/{site_id}/stats/devices` | Real-time device stats for a site |
| `mistapi.websockets.sites.SiteDeviceUpgradesEvents` | `/sites/{site_id}/devices` | Real-time device upgrades events for a site |
| `mistapi.websockets.sites.SitePcapEvents` | `/sites/{site_id}/pcap` | Real-time PCAP events for a site |

#### Location Channels

| Class | Channel | Description |
|-------|---------|-------------|
| `mistapi.websockets.location.LocationBleAssetsEvents` | `/sites/{site_id}/stats/maps/{map_id}/assets` | Real-time BLE assets location events |
| `mistapi.websockets.location.LocationConnectedClientsEvents` | `/sites/{site_id}/stats/maps/{map_id}/clients` | Real-time connected clients location events |
| `mistapi.websockets.location.LocationSdkClientsEvents` | `/sites/{site_id}/stats/maps/{map_id}/sdkclients` | Real-time SDK clients location events |
| `mistapi.websockets.location.LocationUnconnectedClientsEvents` | `/sites/{site_id}/stats/maps/{map_id}/unconnected_clients` | Real-time unconnected clients location events |
| `mistapi.websockets.location.LocationDiscoveredBleAssetsEvents` | `/sites/{site_id}/stats/maps/{map_id}/discovered_assets` | Real-time discovered BLE assets location events |

### Callbacks

| Method | Signature | Description |
|--------|-----------|-------------|
| `ws.on_open(cb)` | `cb()` | Called when the connection is established |
| `ws.on_message(cb)` | `cb(data: dict)` | Called for every incoming message |
| `ws.on_error(cb)` | `cb(error: Exception)` | Called on WebSocket errors |
| `ws.on_close(cb)` | `cb(status_code: int, msg: str)` | Called when the connection closes |

### Usage Patterns

#### Callback style (recommended)

`connect()` returns immediately; messages are delivered to the registered callback in a background thread.

```python
import mistapi

apisession = mistapi.APISession(env_file="~/.mist_env")
apisession.login()

ws = mistapi.websockets.sites.SiteDeviceStatsEvents(apisession, site_id="<site_id>")
ws.on_message(lambda data: print(data))
ws.connect()                    # non-blocking

input("Press Enter to stop")
ws.disconnect()
```

#### Generator style

Iterate over incoming messages as a blocking generator. Useful when you want to process messages sequentially in a loop.

```python
ws = mistapi.websockets.sites.SiteDeviceStatsEvents(apisession, site_id="<site_id>")
ws.connect(run_in_background=True)

for msg in ws.receive():        # blocks, yields each message as a dict
    print(msg)
    if some_condition:
        ws.disconnect()         # stops the generator cleanly
```

#### Blocking style

`connect(run_in_background=False)` blocks the calling thread until the connection closes. Useful for simple scripts.

```python
ws = mistapi.websockets.sites.SiteDeviceStatsEvents(apisession, site_id="<site_id>")
ws.on_message(lambda data: print(data))
ws.connect(run_in_background=False)  # blocks until disconnected
```

#### Context manager

`disconnect()` is called automatically on exit, even if an exception is raised.

```python
import time

with mistapi.websockets.sites.SiteDeviceStatsEvents(apisession, site_id="<site_id>") as ws:
    ws.on_message(lambda data: print(data))
    ws.connect()
    time.sleep(60)
# ws.disconnect() called automatically here
```

---

## Development and Testing

### Development Setup

```bash
# Clone the repository
git clone https://github.com/tmunzer/mistapi_python.git
cd mistapi_python

# Install with development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src/mistapi --cov-report=html

# Run specific test file
pytest tests/unit/test_api_session.py

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
├── __logger.py           # Logging and sanitization
├── __pagination.py       # Pagination utilities
├── cli.py                # Interactive CLI functions
├── __models/             # Data models
│   ├── __init__.py
│   └── privilege.py
└── api/v1/               # Auto-generated API endpoints
    ├── const/            # Constants and enums
    ├── orgs/             # Organization-level APIs
    ├── sites/            # Site-level APIs
    ├── login/            # Authentication APIs
    └── utils/            # Utility functions
```

---

## Contributing

Contributions are welcome! Please follow these guidelines:

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit** your changes
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push** to the branch
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open** a Pull Request

### Development Guidelines

- Write tests for new features
- Ensure all tests pass before submitting PR
- Follow existing code style and conventions
- Update documentation as needed
- Add entries to CHANGELOG.md for significant changes

---

## License

**MIT License**

Copyright (c) 2023 Thomas Munzer

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

## Links

- **Mist API Specs**: [OpenAPI Documentation](https://www.juniper.net/documentation/us/en/software/mist/api/http/getting-started/how-to-get-started)
- **Source Code**: [GitHub Repository](https://github.com/tmunzer/mistapi_python)
- **PyPI Package**: [mistapi on PyPI](https://pypi.org/project/mistapi/)
- **Examples**: [Mist Library Examples](https://github.com/tmunzer/mist_library)
- **Bug Reports**: [GitHub Issues](https://github.com/tmunzer/mistapi_python/issues)
