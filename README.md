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
    - [Connection Parameters](#connection-parameters)
    - [Methods](#methods)
    - [Available Channels](#available-channels)
    - [Usage Patterns](#usage-patterns)
- [Async Usage](#async-usage)
    - [Running API Calls Asynchronously](#running-api-calls-asynchronously)
    - [Concurrent API Calls](#concurrent-api-calls)
    - [Combining with Device Utilities](#combining-with-device-utilities)
- [Device Utilities](#device-utilities)
    - [Supported Devices](#supported-devices)
    - [Usage](#device-utilities-usage)
    - [UtilResponse Object](#utilresponse-object)
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
- **Async Support**: Run any API call asynchronously with `mistapi.arun()` — no changes to existing code
- **Automatic Pagination**: Built-in support for paginated responses
- **WebSocket Streaming**: Real-time event streaming for devices, clients, and location data
- **Device Diagnostics**: High-level, non-blocking utilities for ping, traceroute, ARP, BGP, OSPF, and more
- **Error Handling**: Detailed error responses and logging
- **Proxy Support**: HTTP/HTTPS proxy configuration
- **Log Sanitization**: Automatic redaction of sensitive data in logs


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

### Installation with uv

[uv](https://docs.astral.sh/uv/) is a fast Python package manager:

```bash
# Install in current project
uv add mistapi

# Or run directly without installing
uv run --with mistapi python my_script.py
```

### Development Installation

```bash
# With pip
pip install -e ".[dev]"

# With uv
uv sync
```

### Requirements
- Python 3.10 or higher
- Dependencies: `requests`, `python-dotenv`, `tabulate`, `deprecation`, `hvac`, `keyring`, `websocket-client`

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
| `MIST_VAULT_URL` | `vault_url` | string | None | HashiCorp Vault URL |
| `MIST_VAULT_PATH` | `vault_path` | string | None | Path to secret in Vault |
| `MIST_VAULT_MOUNT_POINT` | `vault_mount_point` | string | None | Vault mount point |
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
    client_mac="aabbccddeeff"
)
```

---

## Async Usage

All API functions in `mistapi.api.v1` are synchronous by default. To use them in an `asyncio` context (e.g., FastAPI, aiohttp, or any async application) without blocking the event loop, use `mistapi.arun()`.

`arun()` wraps any sync mistapi function in `asyncio.to_thread()`, running the blocking HTTP request in a thread pool while the event loop continues. No changes are needed to the existing API functions.

### Running API Calls Asynchronously

```python
import asyncio
import mistapi
from mistapi.api.v1.sites import devices

apisession = mistapi.APISession(env_file="~/.mist_env")
apisession.login()

async def main():
    # Wrap any sync API call with mistapi.arun()
    response = await mistapi.arun(
        devices.listSiteDevices, apisession, site_id
    )
    print(response.data)

asyncio.run(main())
```

### Concurrent API Calls

Use `asyncio.gather()` to run multiple API calls concurrently:

```python
import asyncio
import mistapi
from mistapi.api.v1.orgs import orgs
from mistapi.api.v1.sites import devices

async def main():
    org_info, site_devices = await asyncio.gather(
        mistapi.arun(orgs.getOrg, apisession, org_id),
        mistapi.arun(devices.listSiteDevices, apisession, site_id),
    )
    print(f"Org: {org_info.data['name']}")
    print(f"Devices: {len(site_devices.data)}")

asyncio.run(main())
```

### Combining with Device Utilities

Device utility functions are already non-blocking and return a `UtilResponse` that supports `await`. You can mix `arun()` for API calls and `await` for device utilities:

```python
import asyncio
import mistapi
from mistapi.api.v1.sites import devices
from mistapi.device_utils import ex

async def main():
    # Start device utility — returns immediately, collects data in a background thread
    response = ex.retrieveArpTable(apisession, site_id, device_id)

    # Meanwhile, run an API call via arun() — both execute concurrently
    device_info = await mistapi.arun(
        devices.getSiteDevice, apisession, site_id, device_id
    )
    print(f"Device: {device_info.data['name']}")

    # Wait for the device utility background thread to finish
    await response
    print(f"ARP entries: {len(response.ws_data)}")

asyncio.run(main())
```

---

## WebSocket Streaming

The package provides a WebSocket client for real-time event streaming from the Mist API (`wss://{host}/api-ws/v1/stream`). Authentication is handled automatically using the same session credentials (API token or login/password).

### Connection Parameters

All channel classes accept the following optional keyword arguments:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `ping_interval` | `int` | `30` | Seconds between automatic ping frames. Set to `0` to disable pings. |
| `ping_timeout` | `int` | `10` | Seconds to wait for a pong response before treating the connection as dead. |
| `auto_reconnect` | `bool` | `False` | Automatically reconnect on transient failures using exponential backoff. |
| `max_reconnect_attempts` | `int` | `5` | Maximum number of reconnect attempts before giving up. |
| `reconnect_backoff` | `float` | `2.0` | Base backoff delay in seconds. Doubles after each failed attempt (2s, 4s, 8s, ...). Resets on successful reconnection. |
| `queue_maxsize` | `int` | `0` | Maximum messages buffered in the internal queue for `receive()`. `0` means unbounded. When set, the receive thread blocks if the queue is full, providing backpressure for high-frequency streams. |

```python
ws = mistapi.websockets.sites.DeviceStatsEvents(
    apisession,
    site_ids=["<site_id>"],
    ping_interval=60,       # ping every 60 s
    ping_timeout=20,        # wait up to 20 s for pong
    auto_reconnect=True,    # reconnect on transient failures
)
ws.connect()
```

### Methods

| Method | Signature | Description |
|--------|-----------|-------------|
| `ws.on_open(cb)` | `cb()` | Register callback for connection established |
| `ws.on_message(cb)` | `cb(data: dict)` | Register callback for incoming messages. Mutually exclusive with `receive()`. |
| `ws.on_error(cb)` | `cb(error: Exception)` | Register callback for WebSocket errors |
| `ws.on_close(cb)` | `cb(code: int, msg: str)` | Register callback for connection close. Safe to call `connect()` from within. |
| `ws.connect(run_in_background)` | | Open the connection. `True` (default) runs in a daemon thread; `False` blocks. |
| `ws.disconnect(wait, timeout)` | | Close the connection. `wait=True` blocks until the background thread finishes. |
| `ws.receive()` | `-> Generator[dict]` | Blocking generator yielding messages. Mutually exclusive with `on_message`. |
| `ws.ready()` | `-> bool` | Returns `True` if the connection is open and ready |

### Available Channels

#### Organization Channels

| Class | Channel | Description |
|-------|---------|-------------|
| `mistapi.websockets.orgs.InsightsEvents` | `/orgs/{org_id}/insights/summary` | Real-time insights events for an organization |
| `mistapi.websockets.orgs.MxEdgesStatsEvents` | `/orgs/{org_id}/stats/mxedges` | Real-time MX edges stats for an organization |
| `mistapi.websockets.orgs.MxEdgesEvents` | `/orgs/{org_id}/mxedges` | Real-time MX edges events for an organization |

#### Site Channels

| Class | Channel | Description |
|-------|---------|-------------|
| `mistapi.websockets.sites.ClientsStatsEvents` | `/sites/{site_id}/stats/clients` | Real-time clients stats for a site |
| `mistapi.websockets.sites.DeviceCmdEvents` | `/sites/{site_id}/devices/{device_id}/cmd` | Real-time device command events for a site |
| `mistapi.websockets.sites.DeviceStatsEvents` | `/sites/{site_id}/stats/devices` | Real-time device stats for a site |
| `mistapi.websockets.sites.DeviceEvents` | `/sites/{site_id}/devices` | Real-time device events for a site |
| `mistapi.websockets.sites.MxEdgesStatsEvents` | `/sites/{site_id}/stats/mxedges` | Real-time MX edges stats for a site |
| `mistapi.websockets.sites.PcapEvents` | `/sites/{site_id}/pcap` | Real-time PCAP events for a site |

#### Location Channels

| Class | Channel | Description |
|-------|---------|-------------|
| `mistapi.websockets.location.BleAssetsEvents` | `/sites/{site_id}/stats/maps/{map_id}/assets` | Real-time BLE assets location events |
| `mistapi.websockets.location.ConnectedClientsEvents` | `/sites/{site_id}/stats/maps/{map_id}/clients` | Real-time connected clients location events |
| `mistapi.websockets.location.SdkClientsEvents` | `/sites/{site_id}/stats/maps/{map_id}/sdkclients` | Real-time SDK clients location events |
| `mistapi.websockets.location.UnconnectedClientsEvents` | `/sites/{site_id}/stats/maps/{map_id}/unconnected_clients` | Real-time unconnected clients location events |
| `mistapi.websockets.location.DiscoveredBleAssetsEvents` | `/sites/{site_id}/stats/maps/{map_id}/discovered_assets` | Real-time discovered BLE assets location events |

#### Session Channels

| Class | Channel | Description |
|-------|---------|-------------|
| `mistapi.websockets.session.SessionWithUrl` | Custom URL | Connect to a custom WebSocket channel URL |

### Usage Patterns

#### Callback style (recommended)

`connect()` defaults to `run_in_background=True` and returns immediately. The WebSocket runs in a daemon thread, so your program must stay alive (e.g., with `input()` or an event loop). Messages are delivered to the registered callback in the background thread.

```python
import mistapi

apisession = mistapi.APISession(env_file="~/.mist_env")
apisession.login()

ws = mistapi.websockets.sites.DeviceStatsEvents(apisession, site_ids=["<site_id>"])
ws.on_message(lambda data: print(data))
ws.connect()                    # non-blocking

input("Press Enter to stop")
ws.disconnect()
```

#### Generator style

Iterate over incoming messages as a blocking generator. Useful when you want to process messages sequentially in a loop.

```python
ws = mistapi.websockets.sites.DeviceStatsEvents(apisession, site_ids=["<site_id>"])
ws.connect(run_in_background=True)

for msg in ws.receive():        # blocks, yields each message as a dict
    print(msg)
    if some_condition:
        ws.disconnect()         # stops the generator cleanly
```

#### Blocking style

`connect(run_in_background=False)` blocks the calling thread until the connection closes. Useful for simple scripts.

```python
ws = mistapi.websockets.sites.DeviceStatsEvents(apisession, site_ids=["<site_id>"])
ws.on_message(lambda data: print(data))
ws.connect(run_in_background=False)  # blocks until disconnected
```

#### Context manager

`disconnect()` is called automatically on exit, even if an exception is raised.

```python
import time

with mistapi.websockets.sites.DeviceStatsEvents(apisession, site_ids=["<site_id>"]) as ws:
    ws.on_message(lambda data: print(data))
    ws.connect()
    time.sleep(60)
# ws.disconnect() called automatically here
```

---

## Device Utilities

`mistapi.device_utils` provides high-level utilities for running diagnostic commands on Mist-managed devices. Each function triggers a REST API call and streams the results back via WebSocket. The library handles the connection plumbing — you just call the function and get back a `UtilResponse` object.

### Supported Devices

| Module | Device Type | Functions |
|--------|-------------|-----------|
| `device_utils.ap` | Mist Access Points | `ping`, `traceroute`, `retrieveArpTable` |
| `device_utils.ex` | Juniper EX Switches | `ping`, `monitorTraffic`, `topCommand`, `interactiveShell`, `createShellSession`, `retrieveArpTable`, `retrieveBgpSummary`, `retrieveDhcpLeases`, `releaseDhcpLeases`, `retrieveMacTable`, `clearMacTable`, `clearLearnedMac`, `clearBpduError`, `clearDot1xSessions`, `clearHitCount`, `bouncePort`, `cableTest` |
| `device_utils.srx` | Juniper SRX Firewalls | `ping`, `monitorTraffic`, `topCommand`, `interactiveShell`, `createShellSession`, `retrieveArpTable`, `retrieveBgpSummary`, `retrieveDhcpLeases`, `releaseDhcpLeases`, `retrieveOspfDatabase`, `retrieveOspfNeighbors`, `retrieveOspfInterfaces`, `retrieveOspfSummary`, `retrieveSessions`, `clearSessions`, `bouncePort`, `retrieveRoutes` |
| `device_utils.ssr` | Juniper SSR Routers | `ping`, `retrieveArpTable`, `retrieveBgpSummary`, `retrieveDhcpLeases`, `releaseDhcpLeases`, `retrieveOspfDatabase`, `retrieveOspfNeighbors`, `retrieveOspfInterfaces`, `retrieveOspfSummary`, `retrieveSessions`, `clearSessions`, `bouncePort`, `retrieveRoutes`, `showServicePath` |

### Device Utilities Usage

All device utility functions are **non-blocking**: they trigger the REST API call, start a WebSocket stream in the background, and return a `UtilResponse` immediately. Your script can continue processing while data streams in.

#### Callback style

Pass an `on_message` callback to process each result as it arrives:

```python
from mistapi.device_utils import ex

def handle(msg):
    print("Live:", msg)

response = ex.retrieveArpTable(apisession, site_id, device_id, on_message=handle)
# returns immediately — on_message fires for each message in the background

do_other_work()

response.wait()              # block until streaming is complete
print(response.ws_data)      # all collected data
```

#### Generator style

Iterate over processed messages as they arrive, similar to `_MistWebsocket.receive()`:

```python
response = ex.retrieveMacTable(apisession, site_id, device_id)
for msg in response.receive():    # blocking generator, yields each message
    print(msg, end="", flush=True)
# loop ends when the WebSocket closes
print(response.ws_data)
```

#### Context manager

`disconnect()` is called automatically when the context exits:

```python
with ex.cableTest(apisession, site_id, device_id, port_id="ge-0/0/0") as response:
    for msg in response.receive():
        print(msg, end="", flush=True)
# WebSocket disconnected, data ready
print(response.ws_data)
```

#### Polling

Check `response.done` to avoid blocking:

```python
response = ex.retrieveBgpSummary(apisession, site_id, device_id)
while not response.done:
    do_other_work()
print(response.ws_data)
```

#### Cancel early

Stop a long-running stream before it completes:

```python
response = ex.monitorTraffic(apisession, site_id, device_id, port_id="ge-0/0/0")
do_some_work()
response.disconnect()        # stop the WebSocket
print(response.ws_data)      # data collected so far
```

#### Async await

Works in `asyncio` contexts without blocking the event loop:

```python
import asyncio
from mistapi.device_utils import ex

async def main():
    response = ex.retrieveArpTable(apisession, site_id, device_id)
    await response               # non-blocking await
    print(response.ws_data)

asyncio.run(main())
```

### UtilResponse Object

All device utility functions return a `UtilResponse` object:

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `trigger_api_response` | `APIResponse` | The initial REST API response that triggered the device command. Contains `status_code`, `data`, and `headers` from the trigger request. |
| `ws_required` | `bool` | `True` if the command required a WebSocket connection to stream results (most diagnostic commands do). `False` if the REST response alone was sufficient. |
| `ws_data` | `list[str]` | Parsed result data extracted from the WebSocket stream. This list is **live** — it grows as messages arrive in the background, even before `wait()` is called. |
| `ws_raw_events` | `list[str]` | Raw, unprocessed WebSocket event payloads as received from the Mist API. Useful for debugging or custom parsing. |

#### Properties and Methods

| Method / Property | Returns | Description |
|-------------------|---------|-------------|
| `done` | `bool` | `True` if data collection is complete (or no WS was needed). |
| `wait(timeout=None)` | `UtilResponse` | Block until data collection is complete. Returns `self`. |
| `receive()` | `Generator` | Blocking generator that yields each processed message as it arrives. Exits when the WebSocket closes. |
| `disconnect()` | `None` | Stop the WebSocket connection early. |
| `await response` | `UtilResponse` | Non-blocking await for `asyncio` contexts. |

`UtilResponse` also supports the context manager protocol (`with` statement).

### Enums

- `ap.TracerouteProtocol` — `ICMP`, `UDP` (for `ap.traceroute()`)
- `srx.Node` / `ssr.Node` — `NODE0`, `NODE1` (for dual-node devices)

### Interactive Shell

`interactiveShell()` and `createShellSession()` provide SSH-over-WebSocket access to EX and SRX devices. Unlike the diagnostic utilities above, the shell is **bidirectional** — you send keystrokes and receive terminal output in real time.

#### Interactive mode (human at the keyboard)

Takes over the terminal. Blocks until the connection closes or you press Ctrl+C:

```python
from mistapi.device_utils import ex

ex.interactiveShell(apisession, site_id, device_id)
```

Requires the `sshkeyboard` package (installed automatically as a dependency).

#### Programmatic mode

Use `createShellSession()` to get a `ShellSession` object for scripting:

```python
from mistapi.device_utils import ex
import time

with ex.createShellSession(apisession, site_id, device_id) as session:
    session.send_text("show version\r\n")
    time.sleep(3)
    while True:
        data = session.recv(timeout=0.5)
        if data is None:
            break
        print(data.decode("utf-8", errors="replace"), end="")
```

#### ShellSession API

| Method / Property | Returns | Description |
|-------------------|---------|-------------|
| `connect()` | `None` | Open the WebSocket connection. Called automatically by `createShellSession()`. |
| `disconnect()` | `None` | Close the WebSocket connection. |
| `connected` | `bool` | `True` if the WebSocket is currently connected. |
| `send(data)` | `None` | Send raw bytes (keystrokes) to the device. |
| `send_text(text)` | `None` | Send a text string to the device (auto-prefixed with `\x00`). |
| `recv(timeout=0.1)` | `bytes \| None` | Receive output from the device. Returns `None` on timeout or if disconnected. |
| `resize(rows, cols)` | `None` | Send a terminal resize message. |

`ShellSession` also supports the context manager protocol (`with` statement).

---

## Development and Testing

### Development Setup

```bash
# Clone the repository
git clone https://github.com/tmunzer/mistapi_python.git
cd mistapi_python

# With pip
pip install -e ".[dev]"

# With uv
uv sync
```

### Running Tests

```bash
# Run all tests
pytest
# or with uv
uv run pytest

# Run with coverage report
pytest --cov=src/mistapi --cov-report=html

# Run specific test file
pytest tests/unit/test_api_session.py

# Run linting
ruff check src/
# or with uv
uv run ruff check src/
```

### Package Structure

```
src/mistapi/
├── __init__.py           # Main package exports (lazy-loads api, cli, utils, websockets)
├── __api_session.py      # Session management and authentication
├── __api_request.py      # HTTP request handling
├── __api_response.py     # Response parsing and pagination
├── __logger.py           # Logging and sanitization
├── __pagination.py       # Pagination utilities
├── cli.py                # Interactive CLI functions
├── __models/             # Data models
│   ├── __init__.py
│   └── privilege.py
├── api/v1/               # Auto-generated API endpoints
│   ├── const/            # Constants and enums
│   ├── orgs/             # Organization-level APIs
│   ├── sites/            # Site-level APIs
│   ├── login/            # Authentication APIs
│   └── utils/            # Utility functions
├── device_utils/         # Device utility implementations
│   ├── ap.py             # Access Point utilities
│   ├── ex.py             # EX Switch utilities
│   ├── srx.py            # SRX Firewall utilities
│   ├── ssr.py            # Session Smart Router utilities
│   └── ...               # Function-based modules (arp, bgp, dhcp, etc.)
└── websockets/           # Real-time WebSocket streaming
    ├── __ws_client.py    # Base WebSocket client
    ├── orgs.py           # Organization-level channels
    ├── sites.py          # Site-level channels
    ├── location.py       # Location/map channels
    └── session.py        # Custom URL session channel
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
