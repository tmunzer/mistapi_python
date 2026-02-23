"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
WebSocket channel classes for real-time Mist API streaming.

Usage example::

    import mistapi
    session = mistapi.APISession(...)
    session.login()

    ws = mistapi.websockets.sites.SiteDeviceStatsEvents(session, site_id="<site_id>")
    ws.on_message(lambda data: print(data))
    ws.connect()
"""

from mistapi.websockets import location, orgs, sites
