"""Utility functions for site-level and organization-level Mist Edges."""

from mistapi.device_utils.__tools.remote_capture import (
    org_mxedge_remote_pcap as orgRemotePcap,
)
from mistapi.device_utils.__tools.remote_capture import (
    site_mxedge_remote_pcap as siteRemotePcap,
)

__all__ = ["orgRemotePcap", "siteRemotePcap"]
