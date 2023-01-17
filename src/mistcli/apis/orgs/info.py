from mistcli import Session

def get(mist_session:Session, org_id):
    uri = f"/api/v1/orgs/{org_id}" 
    resp = mist_session.mist_get(uri)
    return resp

def create(mist_session:Session, org_id, org_settings):
    uri = f"/api/v1/orgs/{org_id}" 
    body = org_settings
    resp = mist_session.mist_post(uri, body=body)
    return resp

def update(mist_session:Session, org_id, org_settings):
    uri = f"/api/v1/orgs/{org_id}" 
    body = org_settings
    resp = mist_session.mist_put(uri, body=body)
    return resp