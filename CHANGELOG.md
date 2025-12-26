# CHANGELOG

## Version 0.59.3 (December 2024)

**Released**: December 26, 2024

This release adds security enhancements for log sanitization and includes dependency updates.

---

## 1. NEW FEATURES

### **Log Sanitization**
- Added `LogSanitizer` filter to automatically redact sensitive fields from log messages
- Supports filtering of passwords, API tokens, keys, secrets, and other sensitive data
- Can be applied to both standard Python logging and the custom Console logger

### **Usage Example**
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

## 2. DEPENDENCIES

### **Added**
- `keyring` - Secure system keyring access for password storage
  - macOS Keychain support
  - Windows Credential Locker support
  - Freedesktop Secret Service support (GNOME, KDE)

### **Updated**
- Various dependency updates for security and compatibility

---

## 3. FILES MODIFIED

### **src/mistapi/__logger.py**
- Added `LogSanitizer` class for filtering sensitive data from logs
- Enhanced regex pattern for detecting sensitive fields
- Added support for case-insensitive matching of sensitive field names
- Improved sanitization to handle various JSON formats

### **pyproject.toml**
- Added keyring dependency
- Updated version to 0.59.3

---

## Summary Statistics

- **New Features**: 1 (Log Sanitization)
- **Dependencies Added**: 1 (keyring)
- **Total Files Modified**: 3
- **Lines Added**: 655
- **Lines Removed**: 407

---

## Breaking Changes

None. This is a backwards-compatible release.

---

## Security Improvements

This release significantly improves security by automatically sanitizing sensitive information in logs, including:
- API tokens and keys
- Passwords and passphrases
- OAuth secrets
- PSK/mesh keys
- Authentication credentials
- And 20+ other sensitive field types

---

## Version 0.59.2 (December 2024)

**Released**: December 2024 

This is a maintenance release that adds support for deprecated SLE endpoints and reorganizes project structure.

---

## 1. FUNCTIONS ADDED

### **src/mistapi/api/v1/sites/sle.py**
- `getSiteSleSummary(mist_session, site_id, scope, scope_id, metric, start, end, duration)` - Get SLE metric summary (marked as deprecated in Mist API, replaced by `getSiteSleSummaryTrend`)
- `getSiteSleSummaryTrend(mist_session, site_id, scope, scope_id, metric, start, end, duration)` - Get SLE metric summary trend (replacement for deprecated endpoint)
- `getSiteSleClassifierDetails(mist_session, site_id, scope, scope_id, metric, classifier, start, end, duration)` - Get SLE classifier details (marked as deprecated in Mist API, replaced by `getSiteSleClassifierSummaryTrend`)
- `getSiteSleClassifierSummaryTrend(mist_session, site_id, scope, scope_id, metric, classifier, start, end, duration)` - Get SLE classifier summary trend (replacement for deprecated endpoint)

---

## 2. FUNCTIONS DEPRECATED

### **src/mistapi/api/v1/sites/sle.py**
- `getSiteSleSummary` - Deprecated in version 0.59.2, will be removed in 0.65.0 (replaced by `getSiteSleSummaryTrend`)
- `getSiteSleClassifierDetails` - Deprecated in version 0.59.2, will be removed in 0.65.0 (replaced by `getSiteSleClassifierSummaryTrend`)

**Note**: These functions are marked with `@deprecation.deprecated` decorator and will show deprecation warnings when used.

---

## Summary Statistics

- **Functions Added**: 4 (2 deprecated, 2 replacement)
- **Functions Deprecated**: 2
- **Total Files Modified**: 7
- **Lines Added**: 296
- **Lines Removed**: 6

---

## Breaking Changes

None. All deprecated functions remain available with deprecation warnings.

---

## Migration Guide

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

## Resources

- **Full API Documentation**: [Mist API Documentation](https://doc.mist-lab.fr)
- **GitHub Repository**: [mistapi_python](https://github.com/tmunzer/mistapi_python)
- **PyPI Package**: [mistapi](https://pypi.org/project/mistapi/)
- **Issue Tracker**: [GitHub Issues](https://github.com/tmunzer/mistapi_python/issues)

---

## Version 0.59.1 (December 2024)

**Released**: December 2024

This release introduces significant enhancements to the Mist API Python SDK, including new endpoints, improved pagination support, and updated API specifications.

---

## 1. FUNCTIONS ADDED

### **src/mistapi/api/v1/orgs/ssr.py**
- `exportOrgSsrIdTokens(mist_session, org_id, body)` - Export SSR identity tokens

### **src/mistapi/api/v1/orgs/stats.py**
- `countOrgOspfStats(mist_session, org_id, distinct, start, end, limit, sort, search_after)` - Count OSPF stats at org level
- `searchOrgOspfStats(mist_session, org_id, site_id, mac, peer_ip, port_id, state, vrf_name, start, end, duration, limit, sort, search_after)` - Search OSPF peer stats

### **src/mistapi/api/v1/sites/devices.py**
- `setSiteDevicesGbpTag(mist_session, site_id, body)` - Set Group-Based Policy tags for devices

### **src/mistapi/api/v1/sites/insights.py**
- `getSiteInsightMetricsForGateway(mist_session, site_id, metric, device_id, start, end, duration, interval, limit, page)` - Get insight metrics for gateways
- `getSiteInsightMetricsForMxEdge(mist_session, site_id, metric, mxedge_id, start, end, duration, interval, limit, page)` - Get insight metrics for MxEdges
- `getSiteInsightMetricsForSwitch(mist_session, site_id, metric, device_id, start, end, duration, interval, limit, page)` - Get insight metrics for switches

### **src/mistapi/api/v1/sites/stats.py**
- `countSiteOspfStats(mist_session, site_id, distinct, start, end, limit, sort, search_after)` - Count OSPF stats at site level
- `searchSiteOspfStats(mist_session, site_id, mac, peer_ip, port_id, state, vrf_name, start, end, duration, limit, sort, search_after)` - Search OSPF peer stats for site


---

## 3. FUNCTIONS DEPRECATED

- `getOrg128TRegistrationCommands` in **src/mistapi/api/v1/orgs/ssr.py** (replaced by `getOrgSsrRegistrationCommands`)

---

## 4. PARAMETER CHANGES

### **A. Added `search_after` parameter (for improved pagination)**

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

### **B. Other Parameter Updates**

**Sites Module - Insights:**
- **src/mistapi/api/v1/sites/insights.py**
  - `searchOrgClientFingerprints`: Parameter `client_type` now accepts `'vty'` in addition to `'wireless'` and `'wired'`

---

## Summary Statistics

- **Functions Added**: 9
- **Functions Renamed**: 1
- **Functions Deprecated**: 1
- **Functions with Parameter Changes**: 40+ (primarily `search_after` additions)
- **Total Files Modified**: 40
- **Lines Added**: 812
- **Lines Removed**: 85

---

## Resources

- **Full API Documentation**: [Mist API Documentation](https://doc.mist-lab.fr)
- **GitHub Repository**: [mistapi_python](https://github.com/tmunzer/mistapi_python)
- **PyPI Package**: [mistapi](https://pypi.org/project/mistapi/)
- **Issue Tracker**: [GitHub Issues](https://github.com/tmunzer/mistapi_python/issues)

---

## Previous Releases

### Version 0.58.0
Previous stable release. See commit history for details.

---

**Author**: Thomas Munzer <tmunzer@juniper.net>  
**License**: MIT License  
**Python Compatibility**: Python 3.8+
