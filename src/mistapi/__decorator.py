"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
"""

import asyncio
import functools

def sync_async_compatible(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # Check if we're in an async context
            loop = asyncio.get_running_loop()
            # Run the sync function in a thread pool
            return loop.run_in_executor(None, func, *args, **kwargs)
        except RuntimeError:
            # No event loop, run synchronously
            return func(*args, **kwargs)
    return wrapper