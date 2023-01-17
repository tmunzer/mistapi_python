"""
A site represents a project, a deployment. For MSP, it can be 
as small as a coffee shop or a five-star 600-room hotel. A 
site contains a set of Maps, Wlans, Policies, Zones.
"""

from mistcli.apis.sites import assetfilters
from mistcli.apis.sites import assets
from mistcli.apis.sites import beacons
from mistcli.apis.sites import devices
from mistcli.apis.sites import info
from mistcli.apis.sites import insights
from mistcli.apis.sites import iot
from mistcli.apis.sites import location
from mistcli.apis.sites import maps
from mistcli.apis.sites import psks
from mistcli.apis.sites import rogues
from mistcli.apis.sites import rrm
from mistcli.apis.sites import rssizones
from mistcli.apis.sites import settings
from mistcli.apis.sites import stats
from mistcli.apis.sites import vbeacons
from mistcli.apis.sites import webhooks
from mistcli.apis.sites import wlans
from mistcli.apis.sites import wxrules
from mistcli.apis.sites import wxtags
from mistcli.apis.sites import wxtunnels
from mistcli.apis.sites import zones