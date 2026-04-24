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


class ClientsStatsEvents(_MistWebsocket):
    """WebSocket stream for site clients stats events.

    Subscribes to the ``sites/{site_id}/stats/clients`` channel and delivers
    real-time clients stats events for the given site.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    site_ids : list[str]
        UUIDs of the sites to stream events from.
    ping_interval : int, default 60
        Interval in seconds to send WebSocket ping frames (keep-alive).
    ping_timeout : int, default 45
        Time in seconds to wait for a ping response before considering the connection dead.
    auto_reconnect : bool, default False
        Automatically reconnect on unexpected disconnections using exponential backoff.
    max_reconnect_attempts : int, default 5
        Maximum number of reconnect attempts before giving up.
    reconnect_backoff : float, default 2.0
        Base backoff delay in seconds. Doubles after each failed attempt.
    max_reconnect_backoff : float | None, default None
        Maximum backoff delay in seconds. If None, backoff grows indefinitely.
    queue_maxsize : int, default 0
        Maximum number of messages buffered in the internal queue for the
        ``receive()`` generator. ``0`` means unbounded. When set,
        incoming messages are dropped with a warning when the queue is
        full, preventing memory growth on high-frequency streams.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = ClientsStatsEvents(session, site_ids=["abc123"])
        ws.on_message(lambda data: print(data))
        ws.connect()  # non-blocking, runs in background thread
        input("Press Enter to stop")
        ws.disconnect()

    Generator style::

        ws = ClientsStatsEvents(session, site_ids=["abc123"])
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with ClientsStatsEvents(session, site_ids=["abc123"]) as ws:
            ws.on_message(my_handler)
            ws.connect()  # non-blocking, runs in background thread
            time.sleep(60)
    """

    def __init__(
        self,
        mist_session: APISession,
        site_ids: list[str],
        ping_interval: int = 60,
        ping_timeout: int = 45,
        auto_reconnect: bool = False,
        max_reconnect_attempts: int = 5,
        reconnect_backoff: float = 2.0,
        max_reconnect_backoff: float | None = None,
        queue_maxsize: int = 0,
        subscription_watchdog_timeout: float = 10.0,
        rate_limit_backoff: float = 30.0,
        throughput_log_interval: int = 100,
    ) -> None:
        channels = [f"/sites/{site_id}/stats/clients" for site_id in site_ids]
        super().__init__(
            mist_session,
            channels=channels,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            auto_reconnect=auto_reconnect,
            max_reconnect_attempts=max_reconnect_attempts,
            reconnect_backoff=reconnect_backoff,
            max_reconnect_backoff=max_reconnect_backoff,
            queue_maxsize=queue_maxsize,
            subscription_watchdog_timeout=subscription_watchdog_timeout,
            rate_limit_backoff=rate_limit_backoff,
            throughput_log_interval=throughput_log_interval,
        )


class DeviceCmdEvents(_MistWebsocket):
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
    device_ids : list[str]
        UUIDs of the devices to stream events from.
    ping_interval : int, default 60
        Interval in seconds to send WebSocket ping frames (keep-alive).
    ping_timeout : int, default 45
        Time in seconds to wait for a ping response before considering the connection dead.
    auto_reconnect : bool, default False
        Automatically reconnect on unexpected disconnections using exponential backoff.
    max_reconnect_attempts : int, default 5
        Maximum number of reconnect attempts before giving up.
    reconnect_backoff : float, default 2.0
        Base backoff delay in seconds. Doubles after each failed attempt.
    max_reconnect_backoff : float | None, default None
        Maximum backoff delay in seconds. If None, backoff grows indefinitely.
    queue_maxsize : int, default 0
        Maximum number of messages buffered in the internal queue for the
        ``receive()`` generator. ``0`` means unbounded. When set,
        incoming messages are dropped with a warning when the queue is
        full, preventing memory growth on high-frequency streams.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = DeviceCmdEvents(session, site_id="abc123", device_ids=["def456"])
        ws.on_message(lambda data: print(data))
        ws.connect()  # non-blocking, runs in background thread
        input("Press Enter to stop")
        ws.disconnect()

    Generator style::

        ws = DeviceCmdEvents(session, site_id="abc123", device_ids=["def456"])
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with DeviceCmdEvents(session, site_id="abc123", device_ids=["def456"]) as ws:
            ws.on_message(my_handler)
            ws.connect()  # non-blocking, runs in background thread
            time.sleep(60)
    """

    def __init__(
        self,
        mist_session: APISession,
        site_id: str,
        device_ids: list[str],
        ping_interval: int = 60,
        ping_timeout: int = 45,
        auto_reconnect: bool = False,
        max_reconnect_attempts: int = 5,
        reconnect_backoff: float = 2.0,
        max_reconnect_backoff: float | None = None,
        queue_maxsize: int = 0,
        subscription_watchdog_timeout: float = 10.0,
        rate_limit_backoff: float = 30.0,
        throughput_log_interval: int = 100,
    ) -> None:
        channels = [
            f"/sites/{site_id}/devices/{device_id}/cmd" for device_id in device_ids
        ]
        super().__init__(
            mist_session,
            channels=channels,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            auto_reconnect=auto_reconnect,
            max_reconnect_attempts=max_reconnect_attempts,
            reconnect_backoff=reconnect_backoff,
            max_reconnect_backoff=max_reconnect_backoff,
            queue_maxsize=queue_maxsize,
            subscription_watchdog_timeout=subscription_watchdog_timeout,
            rate_limit_backoff=rate_limit_backoff,
            throughput_log_interval=throughput_log_interval,
        )


class DeviceStatsEvents(_MistWebsocket):
    """WebSocket stream for site device stats events.

    Subscribes to the ``sites/{site_id}/stats/devices`` channel and delivers
    real-time device stats events for the given site.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    site_ids : list[str]
        UUIDs of the sites to stream events from.
    ping_interval : int, default 60
        Interval in seconds to send WebSocket ping frames (keep-alive).
    ping_timeout : int, default 45
        Time in seconds to wait for a ping response before considering the connection dead.
    auto_reconnect : bool, default False
        Automatically reconnect on unexpected disconnections using exponential backoff.
    max_reconnect_attempts : int, default 5
        Maximum number of reconnect attempts before giving up.
    reconnect_backoff : float, default 2.0
        Base backoff delay in seconds. Doubles after each failed attempt.
    max_reconnect_backoff : float | None, default None
        Maximum backoff delay in seconds. If None, backoff grows indefinitely.
    queue_maxsize : int, default 0
        Maximum number of messages buffered in the internal queue for the
        ``receive()`` generator. ``0`` means unbounded. When set,
        incoming messages are dropped with a warning when the queue is
        full, preventing memory growth on high-frequency streams.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = DeviceStatsEvents(session, site_ids=["abc123"])
        ws.on_message(lambda data: print(data))
        ws.connect()  # non-blocking, runs in background thread
        input("Press Enter to stop")
        ws.disconnect()

    Generator style::

        ws = DeviceStatsEvents(session, site_ids=["abc123"])
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with DeviceStatsEvents(session, site_ids=["abc123"]) as ws:
            ws.on_message(my_handler)
            ws.connect()  # non-blocking, runs in background thread
            time.sleep(60)
    """

    def __init__(
        self,
        mist_session: APISession,
        site_ids: list[str],
        ping_interval: int = 60,
        ping_timeout: int = 45,
        auto_reconnect: bool = False,
        max_reconnect_attempts: int = 5,
        reconnect_backoff: float = 2.0,
        max_reconnect_backoff: float | None = None,
        queue_maxsize: int = 0,
        subscription_watchdog_timeout: float = 10.0,
        rate_limit_backoff: float = 30.0,
        throughput_log_interval: int = 100,
    ) -> None:
        channels = [f"/sites/{site_id}/stats/devices" for site_id in site_ids]
        super().__init__(
            mist_session,
            channels=channels,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            auto_reconnect=auto_reconnect,
            max_reconnect_attempts=max_reconnect_attempts,
            reconnect_backoff=reconnect_backoff,
            max_reconnect_backoff=max_reconnect_backoff,
            queue_maxsize=queue_maxsize,
            subscription_watchdog_timeout=subscription_watchdog_timeout,
            rate_limit_backoff=rate_limit_backoff,
            throughput_log_interval=throughput_log_interval,
        )


class DeviceEvents(_MistWebsocket):
    """WebSocket stream for site device events.

    Subscribes to the ``sites/{site_id}/devices`` channel and delivers
    real-time device events for the given site.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    site_ids : list[str]
        UUIDs of the sites to stream events from.
    ping_interval : int, default 60
        Interval in seconds to send WebSocket ping frames (keep-alive).
    ping_timeout : int, default 45
        Time in seconds to wait for a ping response before considering the connection dead.
    auto_reconnect : bool, default False
        Automatically reconnect on unexpected disconnections using exponential backoff.
    max_reconnect_attempts : int, default 5
        Maximum number of reconnect attempts before giving up.
    reconnect_backoff : float, default 2.0
        Base backoff delay in seconds. Doubles after each failed attempt.
    max_reconnect_backoff : float | None, default None
        Maximum backoff delay in seconds. If None, backoff grows indefinitely.
    queue_maxsize : int, default 0
        Maximum number of messages buffered in the internal queue for the
        ``receive()`` generator. ``0`` means unbounded. When set,
        incoming messages are dropped with a warning when the queue is
        full, preventing memory growth on high-frequency streams.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = DeviceEvents(session, site_ids=["abc123"])
        ws.on_message(lambda data: print(data))
        ws.connect()  # non-blocking, runs in background thread
        input("Press Enter to stop")
        ws.disconnect()

    Generator style::

        ws = DeviceEvents(session, site_ids=["abc123"])
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with DeviceEvents(session, site_ids=["abc123"]) as ws:
            ws.on_message(my_handler)
            ws.connect()  # non-blocking, runs in background thread
            time.sleep(60)
    """

    def __init__(
        self,
        mist_session: APISession,
        site_ids: list[str],
        ping_interval: int = 60,
        ping_timeout: int = 45,
        auto_reconnect: bool = False,
        max_reconnect_attempts: int = 5,
        reconnect_backoff: float = 2.0,
        max_reconnect_backoff: float | None = None,
        queue_maxsize: int = 0,
        subscription_watchdog_timeout: float = 10.0,
        rate_limit_backoff: float = 30.0,
        throughput_log_interval: int = 100,
    ) -> None:
        channels = [f"/sites/{site_id}/devices" for site_id in site_ids]
        super().__init__(
            mist_session,
            channels=channels,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            auto_reconnect=auto_reconnect,
            max_reconnect_attempts=max_reconnect_attempts,
            reconnect_backoff=reconnect_backoff,
            max_reconnect_backoff=max_reconnect_backoff,
            queue_maxsize=queue_maxsize,
            subscription_watchdog_timeout=subscription_watchdog_timeout,
            rate_limit_backoff=rate_limit_backoff,
            throughput_log_interval=throughput_log_interval,
        )


class MxEdgesStatsEvents(_MistWebsocket):
    """WebSocket stream for site MX edges stats events.

    Subscribes to the ``sites/{site_id}/stats/mxedges`` channel and delivers
    real-time MX edges stats events for the given site.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    site_ids : list[str]
        UUIDs of the sites to stream events from.
    ping_interval : int, default 60
        Interval in seconds to send WebSocket ping frames (keep-alive).
    ping_timeout : int, default 45
        Time in seconds to wait for a ping response before considering the connection dead.
    auto_reconnect : bool, default False
        Automatically reconnect on unexpected disconnections using exponential backoff.
    max_reconnect_attempts : int, default 5
        Maximum number of reconnect attempts before giving up.
    reconnect_backoff : float, default 2.0
        Base backoff delay in seconds. Doubles after each failed attempt.
    max_reconnect_backoff : float | None, default None
        Maximum backoff delay in seconds. If None, backoff grows indefinitely.
    queue_maxsize : int, default 0
        Maximum number of messages buffered in the internal queue for the
        ``receive()`` generator. ``0`` means unbounded. When set,
        incoming messages are dropped with a warning when the queue is
        full, preventing memory growth on high-frequency streams.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = MxEdgesStatsEvents(session, site_ids=["abc123"])
        ws.on_message(lambda data: print(data))
        ws.connect()  # non-blocking, runs in background thread
        input("Press Enter to stop")
        ws.disconnect()

    Generator style::

        ws = MxEdgesStatsEvents(session, site_ids=["abc123"])
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with MxEdgesStatsEvents(session, site_ids=["abc123"]) as ws:
            ws.on_message(my_handler)
            ws.connect()  # non-blocking, runs in background thread
            time.sleep(60)
    """

    def __init__(
        self,
        mist_session: APISession,
        site_ids: list[str],
        ping_interval: int = 60,
        ping_timeout: int = 45,
        auto_reconnect: bool = False,
        max_reconnect_attempts: int = 5,
        reconnect_backoff: float = 2.0,
        max_reconnect_backoff: float | None = None,
        queue_maxsize: int = 0,
        subscription_watchdog_timeout: float = 10.0,
        rate_limit_backoff: float = 30.0,
        throughput_log_interval: int = 100,
    ) -> None:
        channels = [f"/sites/{site_id}/stats/mxedges" for site_id in site_ids]
        super().__init__(
            mist_session,
            channels=channels,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            auto_reconnect=auto_reconnect,
            max_reconnect_attempts=max_reconnect_attempts,
            reconnect_backoff=reconnect_backoff,
            max_reconnect_backoff=max_reconnect_backoff,
            queue_maxsize=queue_maxsize,
            subscription_watchdog_timeout=subscription_watchdog_timeout,
            rate_limit_backoff=rate_limit_backoff,
            throughput_log_interval=throughput_log_interval,
        )


class MxEdgesEvents(_MistWebsocket):
    """WebSocket stream for site MX edges events.

    Subscribes to the ``sites/{site_id}/mxedges`` channel and delivers
    real-time MX edges events for the given site.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    site_ids : list[str]
        UUIDs of the sites to stream events from.
    ping_interval : int, default 60
        Interval in seconds to send WebSocket ping frames (keep-alive).
    ping_timeout : int, default 45
        Time in seconds to wait for a ping response before considering the connection dead.
    auto_reconnect : bool, default False
        Automatically reconnect on unexpected disconnections using exponential backoff.
    max_reconnect_attempts : int, default 5
        Maximum number of reconnect attempts before giving up.
    reconnect_backoff : float, default 2.0
        Base backoff delay in seconds. Doubles after each failed attempt.
    max_reconnect_backoff : float | None, default None
        Maximum backoff delay in seconds. If None, backoff grows indefinitely.
    queue_maxsize : int, default 0
        Maximum number of messages buffered in the internal queue for the
        ``receive()`` generator. ``0`` means unbounded. When set,
        incoming messages are dropped with a warning when the queue is
        full, preventing memory growth on high-frequency streams.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = MxEdgesEvents(session, site_ids=["abc123"])
        ws.on_message(lambda data: print(data))
        ws.connect()  # non-blocking, runs in background thread
        input("Press Enter to stop")
        ws.disconnect()

    Generator style::

        ws = MxEdgesEvents(session, site_ids=["abc123"])
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with MxEdgesEvents(session, site_ids=["abc123"]) as ws:
            ws.on_message(my_handler)
            ws.connect()  # non-blocking, runs in background thread
            time.sleep(60)
    """

    def __init__(
        self,
        mist_session: APISession,
        site_ids: list[str],
        ping_interval: int = 60,
        ping_timeout: int = 45,
        auto_reconnect: bool = False,
        max_reconnect_attempts: int = 5,
        reconnect_backoff: float = 2.0,
        max_reconnect_backoff: float | None = None,
        queue_maxsize: int = 0,
        subscription_watchdog_timeout: float = 10.0,
        rate_limit_backoff: float = 30.0,
        throughput_log_interval: int = 100,
    ) -> None:
        channels = [f"/sites/{site_id}/mxedges" for site_id in site_ids]
        super().__init__(
            mist_session,
            channels=channels,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            auto_reconnect=auto_reconnect,
            max_reconnect_attempts=max_reconnect_attempts,
            reconnect_backoff=reconnect_backoff,
            max_reconnect_backoff=max_reconnect_backoff,
            queue_maxsize=queue_maxsize,
            subscription_watchdog_timeout=subscription_watchdog_timeout,
            rate_limit_backoff=rate_limit_backoff,
            throughput_log_interval=throughput_log_interval,
        )


class PcapEvents(_MistWebsocket):
    """WebSocket stream for site PCAP events.

    Subscribes to the ``sites/{site_id}/pcaps`` channel and delivers
    real-time PCAP events for the given site.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    site_id : str
        UUID of the site to stream events from.
    ping_interval : int, default 60
        Interval in seconds to send WebSocket ping frames (keep-alive).
    ping_timeout : int, default 45
        Time in seconds to wait for a ping response before considering the connection dead.
    auto_reconnect : bool, default False
        Automatically reconnect on unexpected disconnections using exponential backoff.
    max_reconnect_attempts : int, default 5
        Maximum number of reconnect attempts before giving up.
    reconnect_backoff : float, default 2.0
        Base backoff delay in seconds. Doubles after each failed attempt.
    max_reconnect_backoff : float | None, default None
        Maximum backoff delay in seconds. If None, backoff grows indefinitely.
    queue_maxsize : int, default 0
        Maximum number of messages buffered in the internal queue for the
        ``receive()`` generator. ``0`` means unbounded. When set,
        incoming messages are dropped with a warning when the queue is
        full, preventing memory growth on high-frequency streams.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = PcapEvents(session, site_id="abc123")
        ws.on_message(lambda data: print(data))
        ws.connect()  # non-blocking, runs in background thread
        input("Press Enter to stop")
        ws.disconnect()

    Generator style::

        ws = PcapEvents(session, site_id="abc123")
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with PcapEvents(session, site_id="abc123") as ws:
            ws.on_message(my_handler)
            ws.connect()  # non-blocking, runs in background thread
            time.sleep(60)
    """

    def __init__(
        self,
        mist_session: APISession,
        site_id: str,
        ping_interval: int = 60,
        ping_timeout: int = 45,
        auto_reconnect: bool = False,
        max_reconnect_attempts: int = 5,
        reconnect_backoff: float = 2.0,
        max_reconnect_backoff: float | None = None,
        queue_maxsize: int = 0,
        subscription_watchdog_timeout: float = 10.0,
        rate_limit_backoff: float = 30.0,
        throughput_log_interval: int = 100,
    ) -> None:
        channels = [f"/sites/{site_id}/pcaps"]
        super().__init__(
            mist_session,
            channels=channels,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            auto_reconnect=auto_reconnect,
            max_reconnect_attempts=max_reconnect_attempts,
            reconnect_backoff=reconnect_backoff,
            max_reconnect_backoff=max_reconnect_backoff,
            queue_maxsize=queue_maxsize,
            subscription_watchdog_timeout=subscription_watchdog_timeout,
            rate_limit_backoff=rate_limit_backoff,
            throughput_log_interval=throughput_log_interval,
        )
