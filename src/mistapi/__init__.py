"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
"""

# isort: skip_file
from mistapi.__api_session import APISession as APISession
from mistapi import api as api
from mistapi import cli as cli
from mistapi import websockets as websockets
from mistapi import utils as utils
from mistapi.__pagination import get_all as get_all
from mistapi.__pagination import get_next as get_next
from mistapi.__version import __author__ as __author__
from mistapi.__version import __version__ as __version__

_LAZY_SUBPACKAGES = {
    "api": "mistapi.api",
    "cli": "mistapi.cli",
}


def __getattr__(name: str):
    if name in _LAZY_SUBPACKAGES:
        import importlib

        module = importlib.import_module(_LAZY_SUBPACKAGES[name])
        globals()[name] = module
        return module
    raise AttributeError(f"module 'mistapi' has no attribute {name!r}")
