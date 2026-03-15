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

    from mistapi.device_utils import ap, ex, srx, ssr

    # Use device-specific utilities
    ap.ping(session, site_id, device_id, host)
    ex.cableTest(session, site_id, device_id, port_id)
    ssr.showServicePath(session, site_id, device_id)

Supported Devices:
- ap:  Mist Access Points
- ex:  Juniper EX Switches
- srx: Juniper SRX Firewalls
- ssr: Juniper Session Smart Routers
"""

# Device-specific modules (recommended)
# Function-based modules (legacy, still supported)
# Internal modules
from mistapi.device_utils import (
    ap,
    ex,
    srx,
    ssr,
)

__all__ = [
    # Device-specific modules (recommended)
    "ap",
    "ex",
    "srx",
    "ssr",
]
