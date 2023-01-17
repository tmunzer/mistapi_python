from mistcli import Session

def clients(mist_session:Session, site_id):
    uri = f"/api/v1/sites/{site_id}/stats/clients"
    resp = mist_session.mist_get(uri)
    return resp

