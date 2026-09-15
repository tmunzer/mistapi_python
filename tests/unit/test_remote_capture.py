"""Unit tests for remote packet capture utilities."""

from unittest.mock import Mock, patch

from mistapi.device_utils.__tools.remote_capture import (
    _build_pcap_body,
    org_mxedge_remote_pcap,
    site_mxedge_remote_pcap,
)


def _run_trigger_and_build_websocket(*, trigger_fn, ws_factory_fn):
    trigger_response = trigger_fn()
    return ws_factory_fn(trigger_response)


@patch("mistapi.device_utils.__tools.remote_capture.SitePcapEvents")
@patch("mistapi.device_utils.__tools.remote_capture.site_pcaps.startSitePacketCapture")
@patch("mistapi.device_utils.__tools.remote_capture.WebSocketWrapper")
def test_site_mxedge_capture_uses_site_endpoint_and_stream(
    wrapper_class, start_capture, pcap_events
) -> None:
    session = Mock()
    wrapper_class.return_value.start_with_trigger.side_effect = (
        _run_trigger_and_build_websocket
    )

    site_mxedge_remote_pcap(
        session,
        site_id="site-id",
        device_interfaces={
            "mxedge-id": {
                "port1": "udp port 67 or udp port 68",
                "oobm": None,
            }
        },
        tcpdump_expression="host 192.0.2.1",
    )

    start_capture.assert_called_once_with(
        session,
        site_id="site-id",
        body={
            "duration": 600,
            "format": "stream",
            "max_pkt_len": 512,
            "mxedges": {
                "mxedge-id": {
                    "interfaces": {
                        "port1": {"tcpdump_expression": "udp port 67 or udp port 68"},
                        "oobm": {},
                    }
                }
            },
            "num_packets": 1024,
            "tcpdump_expression": "host 192.0.2.1",
            "type": "mxedge",
        },
    )
    pcap_events.assert_called_once_with(session, site_id="site-id")


@patch("mistapi.device_utils.__tools.remote_capture.OrgPcapEvents")
@patch("mistapi.device_utils.__tools.remote_capture.org_pcaps.startOrgPacketCapture")
@patch("mistapi.device_utils.__tools.remote_capture.WebSocketWrapper")
def test_org_mxedge_capture_uses_org_endpoint_and_stream(
    wrapper_class, start_capture, pcap_events
) -> None:
    session = Mock()
    wrapper_class.return_value.start_with_trigger.side_effect = (
        _run_trigger_and_build_websocket
    )

    org_mxedge_remote_pcap(
        session,
        org_id="org-id",
        device_interfaces={"mxedge-id": {"kni0": "tcp port 443", "oobm": None}},
    )

    start_capture.assert_called_once_with(
        session,
        org_id="org-id",
        body={
            "duration": 600,
            "format": "stream",
            "max_pkt_len": 512,
            "mxedges": {
                "mxedge-id": {
                    "interfaces": {
                        "kni0": {"tcpdump_expression": "tcp port 443"},
                        "oobm": {},
                    }
                }
            },
            "num_packets": 1024,
            "type": "mxedge",
        },
    )
    pcap_events.assert_called_once_with(session, org_id="org-id")


def test_gateway_capture_keeps_main_and_per_port_expressions_independent() -> None:
    body = _build_pcap_body(
        {
            "00000000-0000-0000-1000-001122334455": {
                "ge-0/0/0": "tcp",
                "ge-0/0/1": None,
            },
            "001122334466": {"ge-1/0/0": "port 443"},
        },
        "gateways",
        "gateway",
        "udp",
        600,
        1500,
        100,
    )

    assert body["tcpdump_expression"] == "udp"
    assert body["gateways"] == {
        "001122334455": {
            "ports": {
                "ge-0/0/0": {"tcpdump_expression": "tcp"},
                "ge-0/0/1": {},
            }
        },
        "001122334466": {"ports": {"ge-1/0/0": {"tcpdump_expression": "port 443"}}},
    }


def test_switch_capture_omits_unspecified_main_expression() -> None:
    body = _build_pcap_body(
        {"001122334455": {"ge-0/0/0": "arp"}},
        "switches",
        "switch",
        None,
        60,
        512,
        10,
    )

    assert "tcpdump_expression" not in body
    assert body["switches"]["001122334455"]["ports"]["ge-0/0/0"] == {
        "tcpdump_expression": "arp"
    }


def test_org_pcap_events_uses_org_channel() -> None:
    from mistapi.websockets.orgs import PcapEvents

    websocket = PcapEvents(Mock(), org_id="org-id")

    assert vars(websocket)["_channels"] == ["/orgs/org-id/pcaps"]
