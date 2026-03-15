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

# ARP functions
from mistapi.device_utils.__tools.arp import (
    retrieve_junos_arp_table as retrieveArpTable,
)

# BGP functions
from mistapi.device_utils.__tools.bgp import summary as retrieveBgpSummary

# BPDU functions
from mistapi.device_utils.__tools.bpdu import clear_error as clearBpduError

# DHCP functions
from mistapi.device_utils.__tools.dhcp import release_dhcp_leases as releaseDhcpLeases
from mistapi.device_utils.__tools.dhcp import retrieve_dhcp_leases as retrieveDhcpLeases

# Dot1x functions
from mistapi.device_utils.__tools.dot1x import clear_sessions as clearDot1xSessions

# MAC table functions
from mistapi.device_utils.__tools.mac import clear_learned_mac as clearLearnedMac
from mistapi.device_utils.__tools.mac import clear_mac_table as clearMacTable
from mistapi.device_utils.__tools.mac import retrieve_mac_table as retrieveMacTable

# Shell (interactive SSH)
from mistapi.device_utils.__tools.shell import ShellSession
from mistapi.device_utils.__tools.shell import create_shell_session as createShellSession
from mistapi.device_utils.__tools.shell import interactive_shell as interactiveShell

# Tools (ping, monitor traffic)
from mistapi.device_utils.__tools.miscellaneous import monitor_traffic as monitorTraffic
from mistapi.device_utils.__tools.miscellaneous import ping
from mistapi.device_utils.__tools.miscellaneous import top_command as topCommand

# Policy functions
from mistapi.device_utils.__tools.policy import clear_hit_count as clearHitCount

# Port functions
from mistapi.device_utils.__tools.port import bounce as bouncePort
from mistapi.device_utils.__tools.port import cable_test as cableTest

__all__ = [
    # ARP
    "retrieveArpTable",
    # BGP
    "retrieveBgpSummary",
    # BPDU
    "clearBpduError",
    # DHCP
    "retrieveDhcpLeases",
    "releaseDhcpLeases",
    # Dot1x
    "clearDot1xSessions",
    # MAC
    "clearLearnedMac",
    "clearMacTable",
    "retrieveMacTable",
    # Policy
    "clearHitCount",
    # Port
    "bouncePort",
    "cableTest",
    # Shell
    "ShellSession",
    "createShellSession",
    "interactiveShell",
    # Tools
    "monitorTraffic",
    "ping",
    "topCommand",
]
