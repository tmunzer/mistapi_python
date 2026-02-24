"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
WebSocket channel for Location events.
"""

from mistapi import APISession
from mistapi.websockets.__ws_client import _MistWebsocket


class LocationBleAssetsEvents(_MistWebsocket):
    """WebSocket stream for location BLE assets events.

    Subscribes to the ``/sites/{site_id}/stats/maps/{map_id}/assets`` channel and delivers
    real-time BLE assets events for the given location.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    site_id : str
        UUID of the site to stream events from.
    map_id : str
        UUID of the map to stream events from.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = LocationBleAssetsEvents(session, site_id="abc123", map_id="def456")
        ws.on_message(lambda data: print(data))
        ws.connect()
        input("Press Enter to stop")
        ws.disconnect()

    Generator style (background thread)::

        ws = LocationBleAssetsEvents(session, site_id="abc123", map_id="def456")
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with LocationBleAssetsEvents(session, site_id="abc123", map_id="def456") as ws:
            ws.on_message(my_handler)
            time.sleep(60)
    """

    def __init__(self, mist_session: APISession, site_id: str, map_id: str) -> None:
        super().__init__(
            mist_session, channel=f"/sites/{site_id}/stats/maps/{map_id}/assets"
        )


class LocationConnectedClientsEvents(_MistWebsocket):
    """WebSocket stream for location connected clients events.

    Subscribes to the ``/sites/{site_id}/stats/maps/{map_id}/clients`` channel and delivers
    real-time connected clients events for the given location.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    site_id : str
        UUID of the site to stream events from.
    map_id : str
        UUID of the map to stream events from.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = LocationConnectedClientsEvents(session, site_id="abc123", map_id="def456")
        ws.on_message(lambda data: print(data))
        ws.connect()
        input("Press Enter to stop")
        ws.disconnect()

    Generator style (background thread)::

        ws = LocationConnectedClientsEvents(session, site_id="abc123", map_id="def456")
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with LocationConnectedClientsEvents(session, site_id="abc123", map_id="def456") as ws:
            ws.on_message(my_handler)
            time.sleep(60)
    """

    def __init__(self, mist_session: APISession, site_id: str, map_id: str) -> None:
        super().__init__(
            mist_session,
            channel=f"/sites/{site_id}/stats/maps/{map_id}/clients",
        )


class LocationSdkClientsEvents(_MistWebsocket):
    """WebSocket stream for location SDK clients events.

    Subscribes to the ``/sites/{site_id}/stats/maps/{map_id}/sdkclients`` channel and delivers
    real-time SDK clients events for the given location.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    site_id : str
        UUID of the site to stream events from.
    map_id : str
        UUID of the map to stream events from.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = LocationSdkClientsEvents(session, site_id="abc123", map_id="def456")
        ws.on_message(lambda data: print(data))
        ws.connect()
        input("Press Enter to stop")
        ws.disconnect()

    Generator style (background thread)::

        ws = LocationSdkClientsEvents(session, site_id="abc123", map_id="def456")
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with LocationSdkClientsEvents(session, site_id="abc123", map_id="def456") as ws:
            ws.on_message(my_handler)
            time.sleep(60)
    """

    def __init__(self, mist_session: APISession, site_id: str, map_id: str) -> None:
        super().__init__(
            mist_session,
            channel=f"/sites/{site_id}/stats/maps/{map_id}/sdkclients",
        )


class LocationUnconnectedClientsEvents(_MistWebsocket):
    """WebSocket stream for location unconnected clients events.

    Subscribes to the ``/sites/{site_id}/stats/maps/{map_id}/unconnected_clients`` channel and delivers
    real-time unconnected clients events for the given location.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    site_id : str
        UUID of the site to stream events from.
    map_id : str
        UUID of the map to stream events from.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = LocationUnconnectedClientsEvents(session, site_id="abc123", map_id="def456")
        ws.on_message(lambda data: print(data))
        ws.connect()
        input("Press Enter to stop")
        ws.disconnect()

    Generator style (background thread)::

        ws = LocationUnconnectedClientsEvents(session, site_id="abc123", map_id="def456")
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with LocationUnconnectedClientsEvents(session, site_id="abc123", map_id="def456") as ws:
            ws.on_message(my_handler)
            time.sleep(60)
    """

    def __init__(self, mist_session: APISession, site_id: str, map_id: str) -> None:
        super().__init__(
            mist_session,
            channel=f"/sites/{site_id}/stats/maps/{map_id}/unconnected_clients",
        )


class LocationDiscoveredBleAssetsEvents(_MistWebsocket):
    """WebSocket stream for location discovered BLE assets events.

    Subscribes to the ``/sites/{site_id}/stats/maps/{map_id}/discovered_assets`` channel and delivers
    real-time discovered BLE assets events for the given location.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    site_id : str
        UUID of the site to stream events from.
    map_id : str
        UUID of the map to stream events from.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = LocationDiscoveredBleAssetsEvents(session, site_id="abc123", map_id="def456")
        ws.on_message(lambda data: print(data))
        ws.connect()
        input("Press Enter to stop")
        ws.disconnect()

    Generator style (background thread)::

        ws = LocationDiscoveredBleAssetsEvents(session, site_id="abc123", map_id="def456")
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with LocationDiscoveredBleAssetsEvents(session, site_id="abc123", map_id="def456") as ws:
            ws.on_message(my_handler)
            time.sleep(60)
    """

    def __init__(self, mist_session: APISession, site_id: str, map_id: str) -> None:
        super().__init__(
            mist_session,
            channel=f"/sites/{site_id}/stats/maps/{map_id}/discovered_assets",
        )
