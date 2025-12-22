# CHANGELOG

## Version 0.59.1 (December 2024)

**Released**: December 2024  
**Previous Version**: 0.58.0

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
