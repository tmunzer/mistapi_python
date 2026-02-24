"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
WebSocket channel for Site events.
"""

from mistapi import APISession
from mistapi.websockets.__ws_client import _MistWebsocket


class SiteClientsStatsEvents(_MistWebsocket):
    """WebSocket stream for site clients stats events.

    Subscribes to the ``sites/{site_id}/stats/clients`` channel and delivers
    real-time clients stats events for the given site.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    site_id : str
        UUID of the site to stream events from.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = SiteClientsStatsEvents(session, site_id="abc123")
        ws.on_message(lambda data: print(data))
        ws.connect()
        input("Press Enter to stop")
        ws.disconnect()

    Generator style::

        ws = SiteClientsStatsEvents(session, site_id="abc123")
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with SiteClientsStatsEvents(session, site_id="abc123") as ws:
            ws.on_message(my_handler)
            time.sleep(60)
    """

    def __init__(self, mist_session: APISession, site_id: str, **kwargs) -> None:
        super().__init__(mist_session, channel=f"/sites/{site_id}/stats/clients", **kwargs)


class SiteDeviceCmdEvents(_MistWebsocket):
    """WebSocket stream for site device command events.

    Subscribes to the ``sites/{site_id}/devices/{device_id}/cmd`` channel and delivers
    real-time device command events for the given site and device.

    Device commands functions:
    mistapi.api.v1.sites.devices.arpFromDevice
    mistapi.api.v1.sites.devices.bounceDevicePort
    mistapi.api.v1.sites.devices.cableTestFromSwitch
    mistapi.api.v1.sites.devices.clearSiteDeviceMacTable

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    site_id : str
        UUID of the site to stream events from.
    device_id : str
        UUID of the device to stream events from.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = SiteDeviceCmdEvents(session, site_id="abc123", device_id="def456")
        ws.on_message(lambda data: print(data))
        ws.connect()
        input("Press Enter to stop")
        ws.disconnect()

    Generator style::

        ws = SiteDeviceCmdEvents(session, site_id="abc123", device_id="def456")
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with SiteDeviceCmdEvents(session, site_id="abc123", device_id="def456") as ws:
            ws.on_message(my_handler)
            time.sleep(60)
    """

    def __init__(self, mist_session: APISession, site_id: str, device_id: str, **kwargs) -> None:
        super().__init__(
            mist_session, channel=f"/sites/{site_id}/devices/{device_id}/cmd", **kwargs
        )


class SiteDeviceStatsEvents(_MistWebsocket):
    """WebSocket stream for site device stats events.

    Subscribes to the ``sites/{site_id}/stats/devices`` channel and delivers
    real-time device stats events for the given site.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    site_id : str
        UUID of the site to stream events from.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = SiteDeviceStatsEvents(session, site_id="abc123")
        ws.on_message(lambda data: print(data))
        ws.connect()
        input("Press Enter to stop")
        ws.disconnect()

    Generator style::

        ws = SiteDeviceStatsEvents(session, site_id="abc123")
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with SiteDeviceStatsEvents(session, site_id="abc123") as ws:
            ws.on_message(my_handler)
            time.sleep(60)
    """

    def __init__(self, mist_session: APISession, site_id: str, **kwargs) -> None:
        super().__init__(mist_session, channel=f"/sites/{site_id}/stats/devices", **kwargs)


class SiteDeviceUpgradesEvents(_MistWebsocket):
    """WebSocket stream for site device upgrades events.

    Subscribes to the ``sites/{site_id}/devices`` channel and delivers
    real-time device upgrades events for the given site.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    site_id : str
        UUID of the site to stream events from.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = SiteDeviceUpgradesEvents(session, site_id="abc123")
        ws.on_message(lambda data: print(data))
        ws.connect()
        input("Press Enter to stop")
        ws.disconnect()

    Generator style::

        ws = SiteDeviceUpgradesEvents(session, site_id="abc123")
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with SiteDeviceUpgradesEvents(session, site_id="abc123") as ws:
            ws.on_message(my_handler)
            time.sleep(60)
    """

    def __init__(self, mist_session: APISession, site_id: str, **kwargs) -> None:
        super().__init__(mist_session, channel=f"/sites/{site_id}/devices", **kwargs)


class SiteMxEdgesStatsEvents(_MistWebsocket):
    """WebSocket stream for site MX edges stats events.

    Subscribes to the ``sites/{site_id}/stats/mxedges`` channel and delivers
    real-time MX edges stats events for the given site.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    site_id : str
        UUID of the site to stream events from.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = SiteMxEdgesStatsEvents(session, site_id="abc123")
        ws.on_message(lambda data: print(data))
        ws.connect()
        input("Press Enter to stop")
        ws.disconnect()

    Generator style::

        ws = SiteMxEdgesStatsEvents(session, site_id="abc123")
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with SiteMxEdgesStatsEvents(session, site_id="abc123") as ws:
            ws.on_message(my_handler)
            time.sleep(60)
    """

    def __init__(self, mist_session: APISession, site_id: str, **kwargs) -> None:
        super().__init__(mist_session, channel=f"/sites/{site_id}/stats/mxedges", **kwargs)


class SitePcapEvents(_MistWebsocket):
    """WebSocket stream for site PCAP events.

    Subscribes to the ``sites/{site_id}/pcap`` channel and delivers
    real-time PCAP events for the given site.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    site_id : str
        UUID of the site to stream events from.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = SitePcapEvents(session, site_id="abc123")
        ws.on_message(lambda data: print(data))
        ws.connect()
        input("Press Enter to stop")
        ws.disconnect()

    Generator style::

        ws = SitePcapEvents(session, site_id="abc123")
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with SitePcapEvents(session, site_id="abc123") as ws:
            ws.on_message(my_handler)
            time.sleep(60)
    """

    def __init__(self, mist_session: APISession, site_id: str, **kwargs) -> None:
        super().__init__(mist_session, channel=f"/sites/{site_id}/pcap", **kwargs)
