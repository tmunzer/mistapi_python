from mistcli import Session

def get(mist_session:Session, org_id):
    uri = f"/api/v1/orgs/{org_id}/setting" 
    resp = mist_session.mist_get(uri)
    return resp

def update(mist_session:Session, org_id, settings):
    uri = f"/api/v1/orgs/{org_id}/setting" 
    body = settings
    resp = mist_session.mist_put(uri, body=body)
    return resp


