from mistcli import Session

def get(mist_session:Session, site_id):
    uri = f"/api/v1/sites/{site_id}"
    resp = mist_session.mist_get(uri)
    return resp