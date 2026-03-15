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
from mistapi.__pagination import get_all as get_all
from mistapi.__pagination import get_next as get_next
from mistapi.__version import __author__ as __author__
from mistapi.__version import __version__ as __version__

import asyncio as _asyncio
from collections.abc import Callable as _Callable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mistapi import api as api
    from mistapi import cli as cli
    from mistapi import device_utils as device_utils
    from mistapi import websockets as websockets

_LAZY_SUBPACKAGES = {
    "api": "mistapi.api",
    "cli": "mistapi.cli",
    "websockets": "mistapi.websockets",
    "device_utils": "mistapi.device_utils",
}


def __getattr__(name: str):
    if name in _LAZY_SUBPACKAGES:
        import importlib

        module = importlib.import_module(_LAZY_SUBPACKAGES[name])
        globals()[name] = module
        return module
    raise AttributeError(f"module 'mistapi' has no attribute {name!r}")


async def arun(func: _Callable, *args, **kwargs):
    """
    Run any sync mistapi function without blocking the event loop.

    Wraps the function call in ``asyncio.to_thread()`` so the blocking
    HTTP request runs in a thread pool while the event loop continues.

    EXAMPLE
    -----------
    ::

        import asyncio
        import mistapi
        from mistapi.api.v1.sites import devices

        async def main():
            session = mistapi.APISession(env_file="~/.mist_env")
            session.login()

            response = await mistapi.arun(
                devices.listSiteDevices, session, site_id
            )
            print(response.data)

        asyncio.run(main())

    PARAMS
    -----------
    func : callable
        Any sync mistapi API function.
    *args, **kwargs
        Arguments forwarded to *func*.

    RETURNS
    -----------
    The return value of *func* (typically ``APIResponse``).
    """
    return await _asyncio.to_thread(func, *args, **kwargs)
