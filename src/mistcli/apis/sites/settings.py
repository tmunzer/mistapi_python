from mistcli import Session

def get(mist_session:Session, site_id):
    uri = f"/api/v1/sites/{site_id}/setting"
    resp = mist_session.mist_get(uri)
    return resp


def update(mist_session:Session, site_id, settings):
    uri = f"/api/v1/sites/{site_id}/setting"
    resp = mist_session.mist_put(uri, body=settings)
    return resp
