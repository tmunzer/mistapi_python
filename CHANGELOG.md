# CHANGELOG
## Version 0.60.1 (February 2026)

**Pending Release**: February 21, 2026

This release includes function updates and bug fixes in the self/logs.py and sites/sle.py modules.

---

### 1. CHANGES

##### **API Function Updates**
- Updated `listSelfAuditLogs()` and related functions in `self/logs.py`.
- Updated deprecated and new SLE classifier functions in `sites/sle.py`.

---

### 2. BUG FIXES

- Minor bug fixes and improvements in API modules.

---

### Breaking Changes

No breaking changes in this release.

---

## Version 0.60.0 (February 2026)

**Released**: February 19, 2026

This release updates the OpenAPI submodule, adds new org/site endpoints, fixes a couple of API paths, and updates the API definitions to match the latest OpenAPI specification (2602.1.1).

---

### 1. NEW FEATURES

##### **Org AOS Registration**
- Added `getOrgAosRegisterCmd()` for AOS registration command retrieval

##### **JSI PBN/SIRT Endpoints**
- Added `countOrgJsiPbn()` and `searchOrgJsiPbn()`
- Added `countOrgJsiSirt()` and `searchOrgJsiSirt()`

##### **Site Assets Image Management**
- Added `deleteSiteAssetImage()`
- Added `attachSiteAssetImageFile()` for multipart image uploads

##### **Site Maps Auto-Geofence**
- Added `startSiteMapsAutoGeofence()` (site-level)
- Added `startSiteMapAutoGeofence()` (map-level)

##### **MxEdge VM Parameters**
- Added `getOrgMxEdgeVmParams()`

---

### 2. API UPDATES

##### **MxEdge Image Upload and Version Info**
- `addOrgMxEdgeImage()` replaced with `addOrgMxEdgeImageFile()` using multipart upload
- Updated MxEdge versions endpoint to `/mxedges/versions`

##### **NAC Client Search Enhancements**
- Added `cert_expiry_duration` to `searchOrgNacClients()`

##### **Ports Search Filters**
- Updated org/site ports search filters to align with OpenAPI parameters
- Added LTE identifiers and device-type filters where applicable
- Removed unsupported stats-only filters from search endpoints

---

### 3. BUG FIXES

##### **Sites Device Image Paths**
- Fixed image API paths to include `/image/{image_number}`

---

### Breaking Changes

**Potential Breaking Change**: `addOrgMxEdgeImage()` replaced by `addOrgMxEdgeImageFile()` and now uses multipart uploads. Update any callers to pass `file`/`json` parameters instead of a JSON body.

---

## Version 0.59.5 (January 2026)

**Released**: January 29, 2026

This release improves error handling by replacing `sys.exit()` calls with proper exceptions, fixes pagination issues, and updates the API definitions to match the latest OpenAPI specification (2511.1.14).

---

### 1. BUG FIXES

##### **Pagination Fix**
- Fixed pagination issue when `page` parameter is not already present in the URL
- Added logic to properly append `page` parameter with correct separator (`?` or `&`)
- Improved `APIResponse._check_next()` to handle URLs without existing pagination parameters

##### **Error Handling Improvements**
- Replaced `sys.exit()` calls with proper exception raising in API validation and authentication methods
- `_get_api_token_data()`: Now raises `ConnectionError` instead of calling `sys.exit()` for proxy and connection errors
- `_get_api_token_data()`: Now raises `ValueError` instead of calling `sys.exit(2)` for invalid API tokens (401 status)
- `_process_login()`: Now raises `ConnectionError` instead of calling `sys.exit()` for proxy and connection errors
- `_getself()`: Now raises `ConnectionError` for proxy errors and `ValueError` when authentication fails and user declines to retry

---

### 2. API UPDATES

##### **OpenAPI Specification Update**
- Updated to latest Mist OpenAPI specification
- Enhanced alarm search endpoints with additional filtering parameters:
  - `searchOrgAlarms()`: Added `group`, `severity`, `ack_admin_name`, and `acked` parameters
  - `searchSiteAlarms()`: Enhanced parameter support
- Updated parameter types and documentation across multiple endpoints

---

### Breaking Changes

**Potential Breaking Change**: Code that previously relied on `sys.exit()` behavior during authentication failures will now receive exceptions instead. This is a more correct behavior for library code.

- `ConnectionError` is raised for proxy and connection errors
- `ValueError` is raised for invalid API tokens or failed authentication

---

## Version 0.59.4 (January 2026)

**Released**: January 28, 2026

This release removes default values from optional parameters across all API functions, improving code clarity and consistency.

---

### 1. CHANGES

##### **API Parameter Defaults Removed**
- Removed default values from optional parameters across all API endpoint functions
- All optional parameters now default to `None` instead of using OpenAPI-specified defaults
- Default values are handled directly by the Mist Cloud API when parameters are omitted
- Eliminates redundancy and potential inconsistencies between client and server defaults
- Improves consistency and makes it clearer which parameters are explicitly set by the caller
- Affects 116 files across the codebase

---

### Breaking Changes

**Breaking Change**: Functions that previously had default values specified from the OpenAPI spec now default to `None`. However, this should not affect behavior as the Mist Cloud API applies the same default values server-side when parameters are omitted.

If you were explicitly relying on seeing the default values in the Python function signature, you will now need to refer to the Mist API documentation for default values.

Example:
```python
# Before 0.59.4 (if API spec had duration="1d" as default)
searchOrgAlarms(session, org_id)  # duration defaulted to "1d" in Python

# After 0.59.4
searchOrgAlarms(session, org_id)  # duration=None sent, Mist Cloud applies "1d" default
searchOrgAlarms(session, org_id, duration="1d")  # Explicit is also fine
```

**Note**: The actual API behavior remains unchanged - the Mist Cloud handles default values consistently.

---

## Version 0.59.3 (December 2024)

**Released**: December 26, 2024

This release adds security enhancements for log sanitization and includes dependency updates.

---

### 1. NEW FEATURES

##### **Log Sanitization**
- Added `LogSanitizer` filter to automatically redact sensitive fields from log messages
- Supports filtering of passwords, API tokens, keys, secrets, and other sensitive data
- Can be applied to both standard Python logging and the custom Console logger

##### **Usage Example**
```python
import logging
from mistapi.__logger import LogSanitizer

LOG_FILE = "./log.txt"
logging.basicConfig(filename=LOG_FILE, filemode="w")
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
LOGGER.addFilter(LogSanitizer())

LOGGER.debug(var_with_sensitive_data)
```

---

### 2. DEPENDENCIES

##### **Added**
- `keyring` - Secure system keyring access for password storage
  - macOS Keychain support
  - Windows Credential Locker support
  - Freedesktop Secret Service support (GNOME, KDE)

##### **Updated**
- Various dependency updates for security and compatibility

---

### Breaking Changes

None. This is a backwards-compatible release.

---

### Security Improvements

This release significantly improves security by automatically sanitizing sensitive information in logs, including:
- API tokens and keys
- Passwords and passphrases
- OAuth secrets
- PSK/mesh keys
- Authentication credentials
- And 20+ other sensitive field types

---

### Version 0.59.2 (December 2024)

**Released**: December 2024 

This is a maintenance release that adds support for deprecated SLE endpoints and reorganizes project structure.

---

### 1. FUNCTIONS ADDED

##### **src/mistapi/api/v1/sites/sle.py**
- `getSiteSleSummary(mist_session, site_id, scope, scope_id, metric, start, end, duration)` - Get SLE metric summary (marked as deprecated in Mist API, replaced by `getSiteSleSummaryTrend`)
- `getSiteSleSummaryTrend(mist_session, site_id, scope, scope_id, metric, start, end, duration)` - Get SLE metric summary trend (replacement for deprecated endpoint)
- `getSiteSleClassifierDetails(mist_session, site_id, scope, scope_id, metric, classifier, start, end, duration)` - Get SLE classifier details (marked as deprecated in Mist API, replaced by `getSiteSleClassifierSummaryTrend`)
- `getSiteSleClassifierSummaryTrend(mist_session, site_id, scope, scope_id, metric, classifier, start, end, duration)` - Get SLE classifier summary trend (replacement for deprecated endpoint)

---

### 2. FUNCTIONS DEPRECATED

##### **src/mistapi/api/v1/sites/sle.py**
- `getSiteSleSummary` - Deprecated in version 0.59.2, will be removed in 0.65.0 (replaced by `getSiteSleSummaryTrend`)
- `getSiteSleClassifierDetails` - Deprecated in version 0.59.2, will be removed in 0.65.0 (replaced by `getSiteSleClassifierSummaryTrend`)

**Note**: These functions are marked with `@deprecation.deprecated` decorator and will show deprecation warnings when used.

---

### Breaking Changes

None. All deprecated functions remain available with deprecation warnings.

---

### Migration Guide

If you're using the deprecated SLE functions:

**Before (deprecated):**
```python
# This will show deprecation warning
response = mistapi.api.v1.sites.sle.getSiteSleSummary(
    mist_session, site_id, scope, scope_id, metric
)
```

**After (recommended):**
```python
# Use the new trend endpoint
response = mistapi.api.v1.sites.sle.getSiteSleSummaryTrend(
    mist_session, site_id, scope, scope_id, metric
)
```

Both functions will continue to work until version 0.65.0.

---

### Resources

- **Full API Documentation**: [Mist API Documentation](https://doc.mist-lab.fr)
- **GitHub Repository**: [mistapi_python](https://github.com/tmunzer/mistapi_python)
- **PyPI Package**: [mistapi](https://pypi.org/project/mistapi/)
- **Issue Tracker**: [GitHub Issues](https://github.com/tmunzer/mistapi_python/issues)

---

## Version 0.59.1 (December 2024)

**Released**: December 2024

This release introduces significant enhancements to the Mist API Python SDK, including new endpoints, improved pagination support, and updated API specifications.

---

### 1. FUNCTIONS ADDED

##### **src/mistapi/api/v1/orgs/ssr.py**
- `exportOrgSsrIdTokens(mist_session, org_id, body)` - Export SSR identity tokens

##### **src/mistapi/api/v1/orgs/stats.py**
- `countOrgOspfStats(mist_session, org_id, distinct, start, end, limit, sort, search_after)` - Count OSPF stats at org level
- `searchOrgOspfStats(mist_session, org_id, site_id, mac, peer_ip, port_id, state, vrf_name, start, end, duration, limit, sort, search_after)` - Search OSPF peer stats

##### **src/mistapi/api/v1/sites/devices.py**
- `setSiteDevicesGbpTag(mist_session, site_id, body)` - Set Group-Based Policy tags for devices

##### **src/mistapi/api/v1/sites/insights.py**
- `getSiteInsightMetricsForGateway(mist_session, site_id, metric, device_id, start, end, duration, interval, limit, page)` - Get insight metrics for gateways
- `getSiteInsightMetricsForMxEdge(mist_session, site_id, metric, mxedge_id, start, end, duration, interval, limit, page)` - Get insight metrics for MxEdges
- `getSiteInsightMetricsForSwitch(mist_session, site_id, metric, device_id, start, end, duration, interval, limit, page)` - Get insight metrics for switches

##### **src/mistapi/api/v1/sites/stats.py**
- `countSiteOspfStats(mist_session, site_id, distinct, start, end, limit, sort, search_after)` - Count OSPF stats at site level
- `searchSiteOspfStats(mist_session, site_id, mac, peer_ip, port_id, state, vrf_name, start, end, duration, limit, sort, search_after)` - Search OSPF peer stats for site

---

### 3. FUNCTIONS DEPRECATED

- `getOrg128TRegistrationCommands` in **src/mistapi/api/v1/orgs/ssr.py** (replaced by `getOrgSsrRegistrationCommands`)

---

### 4. PARAMETER CHANGES

##### **A. Added `search_after` parameter (for improved pagination)**

**MSPs Module:**
- **src/mistapi/api/v1/msps/orgs.py**
  - `searchMspOrgs`: Added `start`, `end`, `search_after`

**Orgs Module - Alarms:**
- **src/mistapi/api/v1/orgs/alarms.py**
  - `searchOrgAlarms`: Added `search_after`

**Orgs Module - Clients:**
- **src/mistapi/api/v1/orgs/clients.py**
  - `searchOrgWirelessClientEvents`: Added `search_after`
  - `searchOrgWirelessClients`: Added `search_after`
  - `searchOrgWirelessClientSessions`: Added `search_after`

**Orgs Module - Devices:**
- **src/mistapi/api/v1/orgs/devices.py**
  - `searchOrgDeviceEvents`: Added `search_after`
  - `searchOrgDevices`: Added `search_after`

**Orgs Module - Events:**
- **src/mistapi/api/v1/orgs/events.py**
  - `searchOrgEvents`: Added `search_after`
  - `searchOrgSystemEvents`: Added `search_after`

**Orgs Module - MxEdges:**
- **src/mistapi/api/v1/orgs/mxedges.py**
  - `searchOrgMistEdgeEvents`: Added `search_after`

**Orgs Module - NAC Clients:**
- **src/mistapi/api/v1/orgs/nac_clients.py**
  - `searchOrgNacClientEvents`: Added `search_after`

**Orgs Module - Other Devices:**
- **src/mistapi/api/v1/orgs/otherdevices.py**
  - `searchOrgOtherDeviceEvents`: Added `search_after`

**Orgs Module - Sites:**
- **src/mistapi/api/v1/orgs/sites.py**
  - `searchOrgSites`: Added `search_after`

**Orgs Module - Stats:**
- **src/mistapi/api/v1/orgs/stats.py**
  - `searchOrgAssets`: Added `search_after`
  - `searchOrgBgpStats`: Added `search_after`
  - `searchOrgSwOrGwPorts`: Added `search_after`
  - `searchOrgTunnelsStats`: Added `search_after`
  - `searchOrgPeerPathStats`: Added `search_after`

**Orgs Module - WAN Clients:**
- **src/mistapi/api/v1/orgs/wan_clients.py**
  - `searchOrgWanClientEvents`: Added `search_after`

**Orgs Module - Webhooks:**
- **src/mistapi/api/v1/orgs/webhooks.py**
  - `searchOrgWebhooksDeliveries`: Added `search_after`

**Orgs Module - Wired Clients:**
- **src/mistapi/api/v1/orgs/wired_clients.py**
  - `searchOrgWiredClients`: Added `search_after`

**Sites Module - Alarms:**
- **src/mistapi/api/v1/sites/alarms.py**
  - `searchSiteAlarms`: Added `search_after`

**Sites Module - Clients:**
- **src/mistapi/api/v1/sites/clients.py**
  - `searchSiteWirelessClientEvents`: Added `search_after`
  - `searchSiteWirelessClients`: Added `search_after`
  - `searchSiteWirelessClientSessions`: Added `search_after`

**Sites Module - Devices:**
- **src/mistapi/api/v1/sites/devices.py**
  - `searchSiteDeviceConfigHistory`: Added `search_after`
  - `searchSiteDeviceEvents`: Added `search_after`
  - `searchSiteDeviceLastConfigs`: Added `search_after`
  - `searchSiteDevices`: Added `search_after`

**Sites Module - Events:**
- **src/mistapi/api/v1/sites/events.py**
  - `searchSiteSystemEvents`: Added `search_after`

**Sites Module - Guests:**
- **src/mistapi/api/v1/sites/guests.py**
  - `searchSiteGuestAuthorization`: Added `search_after`

**Sites Module - Insights:**
- **src/mistapi/api/v1/sites/insights.py**
  - `searchOrgClientFingerprints`: Added `search_after`

**Sites Module - Stats:**
- **src/mistapi/api/v1/sites/stats.py**
  - `searchSiteAssets`: Added `search_after`
  - `searchSiteBgpStats`: Added `search_after`
  - `searchSiteCalls`: Added `search_after`
  - `searchSiteDiscoveredSwitchesMetrics`: Added `search_after`

##### **B. Other Parameter Updates**

**Sites Module - Insights:**
- **src/mistapi/api/v1/sites/insights.py**
  - `searchOrgClientFingerprints`: Parameter `client_type` now accepts `'vty'` in addition to `'wireless'` and `'wired'`

---

### Resources

- **Full API Documentation**: [Mist API Documentation](https://doc.mist-lab.fr)
- **GitHub Repository**: [mistapi_python](https://github.com/tmunzer/mistapi_python)
- **PyPI Package**: [mistapi](https://pypi.org/project/mistapi/)
- **Issue Tracker**: [GitHub Issues](https://github.com/tmunzer/mistapi_python/issues)

---

### Previous Releases

##### Version 0.58.0
Previous stable release. See commit history for details.

---

**Author**: Thomas Munzer <tmunzer@juniper.net>  
**License**: MIT License  
**Python Compatibility**: Python 3.8+
