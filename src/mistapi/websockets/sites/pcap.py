"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
WebSocket channel for site PCAP events.
"""

from mistapi import APISession
from mistapi.websockets.__ws_client import _MistWebsocket


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

    def __init__(self, mist_session: APISession, site_id: str) -> None:
        super().__init__(mist_session, channel=f"/sites/{site_id}/pcap")
