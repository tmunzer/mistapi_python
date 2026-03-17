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


class BleAssetsEvents(_MistWebsocket):
    """WebSocket stream for location BLE assets events.

    Subscribes to the ``/sites/{site_id}/stats/maps/{map_id}/assets`` channel and delivers
    real-time BLE assets events for the given location.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    site_id : str
        UUID of the site to stream events from.
    map_id : list[str]
        UUIDs of the maps to stream events from.
    ping_interval : int, default 30
        Interval in seconds to send WebSocket ping frames (keep-alive).
    ping_timeout : int, default 10
        Time in seconds to wait for a ping response before considering the connection dead.
    auto_reconnect : bool, default False
        Automatically reconnect on transient failures using exponential backoff.
    max_reconnect_attempts : int, default 5
        Maximum number of reconnect attempts before giving up.
    reconnect_backoff : float, default 2.0
        Base backoff delay in seconds. Doubles after each failed attempt.


    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = LocationBleAssetsEvents(session, site_id="abc123", map_id="def456")
        ws.on_message(lambda data: print(data))
        ws.connect()  # non-blocking, runs in background thread
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
            ws.connect()  # non-blocking, runs in background thread
            time.sleep(60)
    """

    def __init__(
        self,
        mist_session: APISession,
        site_id: str,
        map_id: list[str],
        ping_interval: int = 30,
        ping_timeout: int = 10,
        auto_reconnect: bool = False,
        max_reconnect_attempts: int = 5,
        reconnect_backoff: float = 2.0,
    ) -> None:
        channels = [f"/sites/{site_id}/stats/maps/{mid}/assets" for mid in map_id]
        super().__init__(
            mist_session,
            channels=channels,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            auto_reconnect=auto_reconnect,
            max_reconnect_attempts=max_reconnect_attempts,
            reconnect_backoff=reconnect_backoff,
        )


class ConnectedClientsEvents(_MistWebsocket):
    """WebSocket stream for location connected clients events.

    Subscribes to the ``/sites/{site_id}/stats/maps/{map_id}/clients`` channel and delivers
    real-time connected clients events for the given location.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    site_id : str
        UUID of the site to stream events from.
    map_id : list[str]
        UUIDs of the maps to stream events from.
    ping_interval : int, default 30
        Interval in seconds to send WebSocket ping frames (keep-alive).
    ping_timeout : int, default 10
        Time in seconds to wait for a ping response before considering the connection dead.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = LocationConnectedClientsEvents(session, site_id="abc123", map_id="def456")
        ws.on_message(lambda data: print(data))
        ws.connect()  # non-blocking, runs in background thread
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
            ws.connect()  # non-blocking, runs in background thread
            time.sleep(60)
    """

    def __init__(
        self,
        mist_session: APISession,
        site_id: str,
        map_id: list[str],
        ping_interval: int = 30,
        ping_timeout: int = 10,
        auto_reconnect: bool = False,
        max_reconnect_attempts: int = 5,
        reconnect_backoff: float = 2.0,
    ) -> None:
        channels = [f"/sites/{site_id}/stats/maps/{mid}/clients" for mid in map_id]
        super().__init__(
            mist_session,
            channels=channels,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            auto_reconnect=auto_reconnect,
            max_reconnect_attempts=max_reconnect_attempts,
            reconnect_backoff=reconnect_backoff,
        )


class SdkClientsEvents(_MistWebsocket):
    """WebSocket stream for location SDK clients events.

    Subscribes to the ``/sites/{site_id}/stats/maps/{map_id}/sdkclients`` channel and delivers
    real-time SDK clients events for the given location.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    site_id : str
        UUID of the site to stream events from.
    map_id : list[str]
        UUIDs of the maps to stream events from.
    ping_interval : int, default 30
        Interval in seconds to send WebSocket ping frames (keep-alive).
    ping_timeout : int, default 10
        Time in seconds to wait for a ping response before considering the connection dead.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = LocationSdkClientsEvents(session, site_id="abc123", map_id="def456")
        ws.on_message(lambda data: print(data))
        ws.connect()  # non-blocking, runs in background thread
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
            ws.connect()  # non-blocking, runs in background thread
            time.sleep(60)
    """

    def __init__(
        self,
        mist_session: APISession,
        site_id: str,
        map_id: list[str],
        ping_interval: int = 30,
        ping_timeout: int = 10,
        auto_reconnect: bool = False,
        max_reconnect_attempts: int = 5,
        reconnect_backoff: float = 2.0,
    ) -> None:
        channels = [f"/sites/{site_id}/stats/maps/{mid}/sdkclients" for mid in map_id]
        super().__init__(
            mist_session,
            channels=channels,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            auto_reconnect=auto_reconnect,
            max_reconnect_attempts=max_reconnect_attempts,
            reconnect_backoff=reconnect_backoff,
        )


class UnconnectedClientsEvents(_MistWebsocket):
    """WebSocket stream for location unconnected clients events.

    Subscribes to the ``/sites/{site_id}/stats/maps/{map_id}/unconnected_clients`` channel and delivers
    real-time unconnected clients events for the given location.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    site_id : str
        UUID of the site to stream events from.
    map_id : list[str]
        UUIDs of the maps to stream events from.
    ping_interval : int, default 30
        Interval in seconds to send WebSocket ping frames (keep-alive).
    ping_timeout : int, default 10
        Time in seconds to wait for a ping response before considering the connection dead.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = LocationUnconnectedClientsEvents(session, site_id="abc123", map_id="def456")
        ws.on_message(lambda data: print(data))
        ws.connect()  # non-blocking, runs in background thread
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
            ws.connect()  # non-blocking, runs in background thread
            time.sleep(60)
    """

    def __init__(
        self,
        mist_session: APISession,
        site_id: str,
        map_id: list[str],
        ping_interval: int = 30,
        ping_timeout: int = 10,
        auto_reconnect: bool = False,
        max_reconnect_attempts: int = 5,
        reconnect_backoff: float = 2.0,
    ) -> None:
        channels = [
            f"/sites/{site_id}/stats/maps/{mid}/unconnected_clients" for mid in map_id
        ]
        super().__init__(
            mist_session,
            channels=channels,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            auto_reconnect=auto_reconnect,
            max_reconnect_attempts=max_reconnect_attempts,
            reconnect_backoff=reconnect_backoff,
        )


class DiscoveredBleAssetsEvents(_MistWebsocket):
    """WebSocket stream for location discovered BLE assets events.

    Subscribes to the ``/sites/{site_id}/stats/maps/{map_id}/discovered_assets`` channel and delivers
    real-time discovered BLE assets events for the given location.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    site_id : str
        UUID of the site to stream events from.
    map_id : list[str]
        UUIDs of the maps to stream events from.
    ping_interval : int, default 30
        Interval in seconds to send WebSocket ping frames (keep-alive).
    ping_timeout : int, default 10
        Time in seconds to wait for a ping response before considering the connection dead.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = LocationDiscoveredBleAssetsEvents(session, site_id="abc123", map_id="def456")
        ws.on_message(lambda data: print(data))
        ws.connect()  # non-blocking, runs in background thread
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
            ws.connect()  # non-blocking, runs in background thread
            time.sleep(60)
    """

    def __init__(
        self,
        mist_session: APISession,
        site_id: str,
        map_id: list[str],
        ping_interval: int = 30,
        ping_timeout: int = 10,
        auto_reconnect: bool = False,
        max_reconnect_attempts: int = 5,
        reconnect_backoff: float = 2.0,
    ) -> None:
        channels = [
            f"/sites/{site_id}/stats/maps/{mid}/discovered_assets" for mid in map_id
        ]
        super().__init__(
            mist_session,
            channels=channels,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            auto_reconnect=auto_reconnect,
            max_reconnect_attempts=max_reconnect_attempts,
            reconnect_backoff=reconnect_backoff,
        )
