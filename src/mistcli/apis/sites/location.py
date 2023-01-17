from mistcli import Session

def reset(mist_session:Session, site_id, map_id):
    uri = f"/api/v1/sites/{site_id}/location/ml/reset/map/{map_id}"
    resp = mist_session.mist_post(uri)
    return resp

