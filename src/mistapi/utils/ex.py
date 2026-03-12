"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------

Utility functions for Juniper EX Switches.

This module provides a device-specific namespace for EX switch utilities.
All functions are imported from their respective functional modules.
"""

# Re-export shared classes and types
from mistapi.utils.arp import Node

# ARP functions
from mistapi.utils.arp import retrieve_junos_arp_table as retrieve_arp_table

# BGP functions
from mistapi.utils.bgp import show_summary as show_bgp_summary

# BPDU functions
from mistapi.utils.bpdu import clear_error as clear_bpdu_error

# DHCP functions
from mistapi.utils.dhcp import release_dhcp_leases

# Dot1x functions
from mistapi.utils.dot1x import clear_sessions as clear_dot1x_sessions

# MAC table functions
from mistapi.utils.mac import (
    clear_learned_mac,
    clear_mac_table,
    retrieve_mac_table,
)

# Policy functions
from mistapi.utils.policy import clear_hit_count

# Port functions
from mistapi.utils.port import bounce as bounce_port
from mistapi.utils.port import cable_test

# Tools (ping, monitor traffic)
from mistapi.utils.tools import monitor_traffic, ping

__all__ = [
    # Classes/Enums
    "Node",
    # ARP
    "retrieve_arp_table",
    # BGP
    "show_bgp_summary",
    # BPDU
    "clear_bpdu_error",
    # DHCP
    "release_dhcp_leases",
    # Dot1x
    "clear_dot1x_sessions",
    # MAC
    "clear_learned_mac",
    "clear_mac_table",
    "retrieve_mac_table",
    # Port
    "bounce_port",
    "cable_test",
    # Policy
    "clear_hit_count",
    # Tools
    "monitor_traffic",
    "ping",
]
