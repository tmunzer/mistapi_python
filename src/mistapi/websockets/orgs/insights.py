"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
WebSocket channel for organization insights events.
"""

from mistapi import APISession
from mistapi.websockets.__ws_client import _MistWebsocket


class OrgInsightsEvents(_MistWebsocket):
    """WebSocket stream for organization insights events.

    Subscribes to the ``orgs/{org_id}/insights/summary`` channel and delivers
    real-time insights events for the given organization.

    PARAMS
    -----------
    mist_session : mistapi.APISession
        Authenticated API session.
    org_id : str
        UUID of the organization to stream events from.

    EXAMPLE
    -----------
    Callback style (background thread)::

        ws = OrgInsightsEvents(session, org_id="abc123")
        ws.on_message(lambda data: print(data))
        ws.connect()
        input("Press Enter to stop")
        ws.disconnect()

    Generator style::

        ws = OrgInsightsEvents(session, org_id="abc123")
        ws.connect(run_in_background=True)
        for msg in ws.receive():
            process(msg)

    Context manager::

        with OrgInsightsEvents(session, org_id="abc123") as ws:
            ws.on_message(my_handler)
            time.sleep(60)
    """

    def __init__(self, mist_session: APISession, org_id: str) -> None:
        super().__init__(mist_session, channel=f"/orgs/{org_id}/insights/summary")
