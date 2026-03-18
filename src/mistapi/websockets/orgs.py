"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
WebSocket channel for Org events.
"""

from mistapi import APISession
from mistapi.websockets.__ws_client import _COMMON_WS_PARAMS_DOC, _MistWebsocket


class InsightsEvents(_MistWebsocket):
    f"""WebSocket stream for organization insights events.

    Subscribes to the ``orgs/{org_id}/insights/summary`` channel and delivers
    real-time insights events for the given organization.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    org_id : str
        UUID of the organization to stream events from.
{_COMMON_WS_PARAMS_DOC}

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = InsightsEvents(session, org_id="abc123")
        ws.on_message(lambda data: print(data))
        ws.connect()  # non-blocking, runs in background thread
        input("Press Enter to stop")
        ws.disconnect()

    Generator style::

        ws = InsightsEvents(session, org_id="abc123")
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with InsightsEvents(session, org_id="abc123") as ws:
            ws.on_message(my_handler)
            ws.connect()  # non-blocking, runs in background thread
            time.sleep(60)
    """

    def __init__(
        self,
        mist_session: APISession,
        org_id: str,
        ping_interval: int = 30,
        ping_timeout: int = 10,
        auto_reconnect: bool = False,
        max_reconnect_attempts: int = 5,
        reconnect_backoff: float = 2.0,
        queue_maxsize: int = 0,
    ) -> None:
        super().__init__(
            mist_session,
            channels=[f"/orgs/{org_id}/insights/summary"],
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            auto_reconnect=auto_reconnect,
            max_reconnect_attempts=max_reconnect_attempts,
            reconnect_backoff=reconnect_backoff,
            queue_maxsize=queue_maxsize,
        )


class MxEdgesStatsEvents(_MistWebsocket):
    f"""WebSocket stream for organization MX edges stats events.

    Subscribes to the ``orgs/{org_id}/stats/mxedges`` channel and delivers
    real-time MX edges stats events for the given organization.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    org_id : str
        UUID of the organization to stream events from.
{_COMMON_WS_PARAMS_DOC}

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = MxEdgesStatsEvents(session, org_id="abc123")
        ws.on_message(lambda data: print(data))
        ws.connect()  # non-blocking, runs in background thread
        input("Press Enter to stop")
        ws.disconnect()

    Generator style::

        ws = MxEdgesStatsEvents(session, org_id="abc123")
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with MxEdgesStatsEvents(session, org_id="abc123") as ws:
            ws.on_message(my_handler)
            ws.connect()  # non-blocking, runs in background thread
            time.sleep(60)
    """

    def __init__(
        self,
        mist_session: APISession,
        org_id: str,
        ping_interval: int = 30,
        ping_timeout: int = 10,
        auto_reconnect: bool = False,
        max_reconnect_attempts: int = 5,
        reconnect_backoff: float = 2.0,
        queue_maxsize: int = 0,
    ) -> None:
        super().__init__(
            mist_session,
            channels=[f"/orgs/{org_id}/stats/mxedges"],
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            auto_reconnect=auto_reconnect,
            max_reconnect_attempts=max_reconnect_attempts,
            reconnect_backoff=reconnect_backoff,
            queue_maxsize=queue_maxsize,
        )


class MxEdgesEvents(_MistWebsocket):
    f"""WebSocket stream for org MX edges events.

    Subscribes to the ``orgs/{org_id}/mxedges`` channel and delivers
    real-time MX edges events for the given org.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    org_id : str
        UUID of the org to stream events from.
{_COMMON_WS_PARAMS_DOC}

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = MxEdgesEvents(session, org_id="abc123")
        ws.on_message(lambda data: print(data))
        ws.connect()  # non-blocking, runs in background thread
        input("Press Enter to stop")
        ws.disconnect()

    Generator style::

        ws = MxEdgesEvents(session, org_id="abc123")
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with MxEdgesEvents(session, org_id="abc123") as ws:
            ws.on_message(my_handler)
            ws.connect()  # non-blocking, runs in background thread
            time.sleep(60)
    """

    def __init__(
        self,
        mist_session: APISession,
        org_id: str,
        ping_interval: int = 30,
        ping_timeout: int = 10,
        auto_reconnect: bool = False,
        max_reconnect_attempts: int = 5,
        reconnect_backoff: float = 2.0,
        queue_maxsize: int = 0,
    ) -> None:
        super().__init__(
            mist_session,
            channels=[f"/orgs/{org_id}/mxedges"],
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            auto_reconnect=auto_reconnect,
            max_reconnect_attempts=max_reconnect_attempts,
            reconnect_backoff=reconnect_backoff,
            queue_maxsize=queue_maxsize,
        )
