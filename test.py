import asyncio

import src.mistapi as mistapi

# APISESSION = mistapi.APISession(env_file="~/.mist_env_ld_ro", show_cli_notif=False)
# ORG_ID = "9777c1a0-6ef6-11e6-8bbf-02e208b2d34f"
# SITE_ID = "a925ea04-8393-4e0f-ab6b-209f11382cee"
# AP_ID = "00000000-0000-0000-1000-04a92439fb75"
# SWITCH_ID = "00000000-0000-0000-1000-2093390b3580"
# GATEWAY_ID = "00000000-0000-0000-1000-409ea4e60b00"

APISESSION = mistapi.APISession(env_file="~/.mist_env_gc1", show_cli_notif=False)
ORG_ID = "8aa21779-1178-4357-b3e0-42c02b93b870"
SITE_ID = "d6fb4f96-3ba4-4cf5-8af2-a8d7b85087ac"
AP_ID = "00000000-0000-0000-1000-04a92439fb75"
SWITCH_ID = "00000000-0000-0000-1000-2093390b3580"
GATEWAY_ID = "00000000-0000-0000-1000-0200010edbca"

APISESSION.login()

# data = asyncio.run(
#     mistapi.websockets.utils.common.bounce_ports(
#         apissession=APISESSION,
#         site_id=SITE_ID,
#         device_id=GATEWAY_ID,
#         port_ids=["ge-0/0/3"],
#     )
# )


data = asyncio.run(
    mistapi.websockets.utils.junos.monitor_traffic(
        apissession=APISESSION,
        site_id=SITE_ID,
        device_id=SWITCH_ID,
    )
)
print(data.trigger_api_response.data)
print("".center(50, "-"))
if data.ws_required:
    if isinstance(data.ws_data, list):
        print("".join(data.ws_data))
    else:
        print(data.ws_data)
else:
    print("No WebSocket data available.")
