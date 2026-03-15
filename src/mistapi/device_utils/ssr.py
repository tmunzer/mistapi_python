"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------

Utility functions for Juniper Session Smart Routers (SSR).

This module provides a device-specific namespace for SSR router utilities.
All functions are imported from their respective functional modules.
"""

# Re-export shared classes and types
from mistapi.device_utils.__tools.__common import Node

# ARP functions
from mistapi.device_utils.__tools.arp import (
    retrieve_ssr_arp_table as retrieveArpTable,
)

# BGP functions
from mistapi.device_utils.__tools.bgp import summary as retrieveBgpSummary

# DHCP functions
from mistapi.device_utils.__tools.dhcp import release_dhcp_leases as releaseDhcpLeases
from mistapi.device_utils.__tools.dhcp import retrieve_dhcp_leases as retrieveDhcpLeases

# Tools (ping only - no monitor_traffic for SSR)
from mistapi.device_utils.__tools.miscellaneous import ping

# DNS functions
# from mistapi.utils.dns import test_resolution as test_dns_resolution
# OSPF functions
from mistapi.device_utils.__tools.ospf import show_database as retrieveOspfDatabase
from mistapi.device_utils.__tools.ospf import show_interfaces as retrieveOspfInterfaces
from mistapi.device_utils.__tools.ospf import show_neighbors as retrieveOspfNeighbors
from mistapi.device_utils.__tools.ospf import show_summary as retrieveOspfSummary

# Port functions
from mistapi.device_utils.__tools.port import bounce as bouncePort

# Route functions
from mistapi.device_utils.__tools.routes import show as retrieveRoutes

# Service Path functions
from mistapi.device_utils.__tools.service_path import (
    show_service_path as showServicePath,
)

# Sessions functions
from mistapi.device_utils.__tools.sessions import clear as clearSessions
from mistapi.device_utils.__tools.sessions import show as retrieveSessions

__all__ = [
    # Classes/Enums
    "Node",
    # ARP
    "retrieveArpTable",
    # BGP
    "retrieveBgpSummary",
    # DHCP
    "releaseDhcpLeases",
    "retrieveDhcpLeases",
    # DNS
    # "test_dns_resolution",
    # OSPF
    "retrieveOspfDatabase",
    "retrieveOspfNeighbors",
    "retrieveOspfInterfaces",
    "retrieveOspfSummary",
    # Port
    "bouncePort",
    # Routes
    "retrieveRoutes",
    # Service Path
    "showServicePath",
    # Sessions
    "retrieveSessions",
    "clearSessions",
    # Tools
    "ping",
]
