"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------

Utility functions for Juniper SRX Firewalls.

This module provides a device-specific namespace for SRX firewall utilities.
All functions are imported from their respective functional modules.
"""

# Re-export shared classes and types
from mistapi.device_utils.__tools.__common import Node

# ARP functions
from mistapi.device_utils.__tools.arp import (
    retrieve_junos_arp_table as retrieveArpTable,
)

# BGP functions
from mistapi.device_utils.__tools.bgp import summary as retrieveBgpSummary

# DHCP functions
from mistapi.device_utils.__tools.dhcp import release_dhcp_leases as releaseDhcpLeases
from mistapi.device_utils.__tools.dhcp import retrieve_dhcp_leases as retrieveDhcpLeases

# Shell (interactive SSH)
from mistapi.device_utils.__tools.shell import ShellSession
from mistapi.device_utils.__tools.shell import (
    create_shell_session as createShellSession,
)
from mistapi.device_utils.__tools.shell import interactive_shell as interactiveShell

# Tools (ping, monitor traffic)
from mistapi.device_utils.__tools.miscellaneous import monitor_traffic as monitorTraffic
from mistapi.device_utils.__tools.miscellaneous import ping
from mistapi.device_utils.__tools.miscellaneous import top_command as topCommand

# OSPF functions
from mistapi.device_utils.__tools.ospf import show_database as retrieveOspfDatabase
from mistapi.device_utils.__tools.ospf import show_interfaces as retrieveOspfInterfaces
from mistapi.device_utils.__tools.ospf import show_neighbors as retrieveOspfNeighbors
from mistapi.device_utils.__tools.ospf import show_summary as retrieveOspfSummary

# Port functions
from mistapi.device_utils.__tools.port import bounce as bouncePort

# Route functions
from mistapi.device_utils.__tools.routes import show as retrieveRoutes

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
    # OSPF
    "retrieveOspfDatabase",
    "retrieveOspfNeighbors",
    "retrieveOspfInterfaces",
    "retrieveOspfSummary",
    # Port
    "bouncePort",
    # Routes
    "retrieveRoutes",
    # Sessions
    "retrieveSessions",
    "clearSessions",
    # Shell
    "ShellSession",
    "createShellSession",
    "interactiveShell",
    # Tools
    "monitorTraffic",
    "ping",
    "topCommand",
]
