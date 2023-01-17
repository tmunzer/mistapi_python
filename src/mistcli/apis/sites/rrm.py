from mistcli import Session

def get_current_channel_planning(mist_session:Session, site_id):
    uri = f"/api/v1/sites/{site_id}/rrm/current"
    resp = mist_session.mist_get(uri)
    return resp

def get_device_rrm_info(mist_session:Session, site_id, device_id, band):
    uri = f"/api/v1/sites/{site_id}/rrm/current/devices/{device_id}/band/{band}"
    resp = mist_session.mist_get(uri)
    return resp

def optimize(mist_session:Session, site_id, band_24=False, band_5=False):
    bands = []
    if band_24:
        bands.append("24")
    if band_5:
        bands.append("5")
    body = { "bands": bands}
    uri = f"/api/v1/sites/{site_id}/rrm/optimize"
    resp = mist_session.mist_post(uri, body=body)
    return resp

def reset(mist_session:Session, site_id):
    uri = f"/api/v1/sites/{site_id}/devices/reset_radio_config"
    resp = mist_session.mist_post(uri)
    return resp

def get_events(mist_session:Session, site_id, band, duration="", page=1, limit=100):
    uri =f"/api/v1/sites/{site_id}/rrm/events?band={band}"
    query ={"band": band}
    if duration != "":
        query["duration"] = duration
    resp = mist_session.mist_get(uri, query=query, page=page, limit=limit)
    return resp

def get_interference_events(mist_session:Session, site_id, duration="", page=1, limit=100):
    uri = f"/api/v1/sites/{site_id}/events/interference"
    query ={}
    if duration != "":
        query["duration"] = duration
    resp = mist_session.mist_get(uri, query=query, page=page, limit=limit)
    return resp

def get_roaming_events(mist_session:Session, site_id, mtype, start="", end="", page=1, limit=100):
    uri = f"/api/v1/sites/{site_id}/events/fast_roam"
    query={"type": mtype}    
    if end != "":
        query["duration"]= end
    if limit != "":
        query["duration"]= limit
    resp = mist_session.mist_get(uri, query=query, page=page, limit=limit)
    return resp
