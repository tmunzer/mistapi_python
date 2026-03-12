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
from mistapi.utils.arp import Node

# ARP functions
from mistapi.utils.arp import retrieve_ssr_arp_table as retrieve_arp_table

# BGP functions
from mistapi.utils.bgp import show_summary as show_bgp_summary

# DHCP functions
from mistapi.utils.dhcp import release_dhcp_leases, retrieve_dhcp_leases

# DNS functions
from mistapi.utils.dns import test_resolution as test_dns_resolution

# Policy functions
from mistapi.utils.policy import clear_hit_count

# Port functions
from mistapi.utils.port import bounce as bounce_port

# Service Path functions
from mistapi.utils.service_path import show_service_path

# Tools (ping only - no monitor_traffic for SSR)
from mistapi.utils.tools import ping

__all__ = [
    # Classes/Enums
    "Node",
    # ARP
    "retrieve_arp_table",
    # BGP
    "show_bgp_summary",
    # DHCP
    "release_dhcp_leases",
    "retrieve_dhcp_leases",
    # DNS
    "test_dns_resolution",
    # Port
    "bounce_port",
    # Policy
    "clear_hit_count",
    # Service Path
    "show_service_path",
    # Tools
    "ping",
]
