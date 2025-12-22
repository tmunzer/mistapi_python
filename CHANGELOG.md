# Release Notes

## Version 0.59.1 (December 2024)

**Released**: December 2024  
**Previous Version**: 0.58.0

This release introduces significant enhancements to the Mist API Python SDK, including new endpoints, improved pagination support, and updated API specifications.

### New Features

#### New API Endpoints

**Organization Statistics:**
- `countOrgOspfStats`: Count OSPF statistics for organization
- `searchOrgOspfStats`: Search OSPF peer statistics across organization
- `countOrgOspfNeighbors`: Count OSPF neighbors for organization  
- `getOrgOspfNeighborStats`: Get OSPF neighbor statistics

**Site Statistics:**
- `countSiteOspfStats`: Count OSPF statistics for site
- `searchSiteOspfStats`: Search OSPF peer statistics for site
- `countSiteOspfNeighbors`: Count OSPF neighbors for site
- `getOspfNeighborStatsForSiteDevice`: Get OSPF neighbor statistics for site device

**Site Insights:**
- `getSiteInsightMetricsForGateway`: Get insight metrics for specific gateway devices
- `getSiteInsightMetricsForSwitch`: Get insight metrics for specific switch devices

**Organization SSR (Session Smart Router):**
- `exportOrgSsrIdTokens`: Export SSR identity tokens for bulk operations
- `getOrgSsrRegistrationCommands`: Get registration commands for SSR devices (replaces deprecated 128T endpoint)

**MSP Organizations:**
- `searchMspOrgs`: Search and filter organizations within an MSP

**Site Synthetic Testing:**
- New endpoints for synthetic test management and monitoring

### API Enhancements

#### Enhanced Pagination Support
Added `search_after` parameter to multiple search endpoints for improved pagination:

**Organization Level:**
- `searchOrgAssets`
- `searchOrgBgpStats`
- `searchOrgClients`
- `searchOrgDevices`
- `searchOrgEvents`

**Site Level:**
- `searchSiteAssets`
- `searchSiteBgpStats`
- `searchSiteCalls`
- `searchSiteDiscoveredSwitchesMetrics`
- `searchSiteDevices`

#### Updated Parameters
- **Client Fingerprint Search**: Added `vty` as valid `client_type` option (wireless, wired, vty)
- **PSK Portals**: Updated field types and improved request handling
- **SSR Registration**: Enhanced documentation for `asset_ids` parameter with HTTP body preference

### API Updates

#### Renamed Endpoints (Backwards Compatible)
- `getOrg128TRegistrationCommands` → `getOrgSsrRegistrationCommands` (128T branding to SSR)

#### Updated API Documentation
- Improved parameter descriptions across multiple endpoints
- Enhanced inline documentation for better developer experience
- Updated query parameter handling for consistency

### Additional Changes

**Inventory Management:**
- Enhanced inventory claim and release operations
- Improved device adoption workflows

**Device Statistics:**
- Extended device metrics collection
- Enhanced BGP, OSPF, and other routing protocol statistics

**Webhook Management:**
- Improved webhook configuration and testing
- Enhanced event subscription handling

### Bug Fixes

- Fixed parameter type inconsistencies in various endpoints
- Corrected query parameter serialization issues
- Improved error handling for edge cases

### Documentation

- Updated API endpoint references to latest Mist documentation
- Improved parameter descriptions and examples
- Enhanced inline code documentation

### Resources

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
