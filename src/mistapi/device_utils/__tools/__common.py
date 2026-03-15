"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
"""

from enum import Enum


class Node(Enum):
    """Node enum for specifying which node to target on dual-node devices."""

    NODE0 = "node0"
    NODE1 = "node1"
