"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
"""

from mistapi.api.v1.msps import (
    msps,
    admins,
    claim,
    insights,
    inventory,
    invites,
    licenses,
    logo,
    logs,
    orggroups,
    orgs,
    search,
    ssoroles,
    ssos,
    stats,
    suggestion,
    tickets,
)

__all__ = [
    "msps",
    "admins",
    "claim",
    "insights",
    "inventory",
    "invites",
    "licenses",
    "logo",
    "logs",
    "orggroups",
    "orgs",
    "search",
    "ssoroles",
    "ssos",
    "stats",
    "suggestion",
    "tickets",
]
