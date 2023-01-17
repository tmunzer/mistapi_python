from mistcli import Session

def create(mist_session:Session, data):
    uri = "/api/v1/orgs"
    resp = mist_session.mist_post(uri, org_id=None, body=data)
    return resp


def update(mist_session:Session, org_id, data):
    uri = f"/api/v1/orgs/{org_id}"
    resp = mist_session.mist_put(uri, body=data)
    return resp 

def delete(mist_session:Session, org_id):
    uri = f"/api/v1/orgs/{org_id}"
    resp = mist_session.mist_delete(uri)
    return resp 

def get_stats(mist_session:Session, org_id):
    uri = f"/api/v1/orgs/{org_id}/stats"
    resp = mist_session.mist_get(uri)
    return resp

def get_settings(mist_session:Session, org_id):
    uri = f"/api/v1/orgs/{org_id}/setting"
    resp = mist_session.mist_get(uri)
    return resp

def update_settings(mist_session:Session, org_id, data):
    uri = f"/api/v1/orgs/{org_id}/setting"
    resp = mist_session.mist_put(uri, body=data)
    return resp

def clone(mist_session:Session, org_id, new_name):
    uri = f"/api/v1/orgs/{org_id}/clone"
    resp = mist_session.mist_post(uri, body={"name": new_name})
    return resp