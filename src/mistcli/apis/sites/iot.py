from mistcli import Session

def get(mist_session:Session, site_id, device_id):
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/iot"
    resp = mist_session.mist_get(uri)
    return resp


def set(mist_session:Session, site_id, device_id):
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/iot"
    resp = mist_session.mist_put(uri)
    return resp
