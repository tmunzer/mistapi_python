from mistcli import Session

def create(mist_session:Session, site_id, beacon_settings):
    uri = f"/api/v1/sites/{site_id}/beacons"
    body = beacon_settings
    resp = mist_session.mist_ost(uri, body=body)
    return resp

def update(mist_session:Session, site_id, beacon_id, body={}):
    uri = f"/api/v1/sites/{site_id}/beacons/{beacon_id}"
    resp = mist_session.mist_ut(uri, body=body)
    return resp
    
def delete(mist_session:Session, site_id, beacon_id):
    uri = f"/api/v1/sites/{site_id}/beacons/{beacon_id}"
    resp = mist_session.mist_elete(uri)
    return resp

def get(mist_session:Session, site_id, page=1, limit=100):
    uri = f"/api/v1/sites/{site_id}/beacons"
    resp = mist_session.mist_et(uri, page=page, limit=limit)
    return resp


