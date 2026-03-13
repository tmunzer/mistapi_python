"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------

Mist API Utilities
==================

This package provides utility functions for interacting with Mist devices.

Device-Specific Modules (Recommended)
--------------------------------------
Import device-specific modules for a clean, organized API:

    from mistapi.utils import ap, ex, srx, ssr

    # Use device-specific utilities
    ap.ping(session, site_id, device_id, host)
    ex.cable_test(session, site_id, device_id, port_id)
    ssr.show_service_path(session, site_id, device_id)

Supported Devices:
- ap:  Mist Access Points
- ex:  Juniper EX Switches
- srx: Juniper SRX Firewalls
- ssr: Juniper Session Smart Routers

Function-Based Modules (Legacy)
---------------------------------
Original organization by function type (still available):

    from mistapi.utils import arp, bgp, dhcp, mac, port, routes, tools

Available modules: arp, bgp, bpdu, dhcp, dns, dot1x, mac, policy, port, routes,
                   service_path, tools
"""
