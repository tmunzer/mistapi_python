from mistcli import Session

def create(mist_session:Session, org_id, site_settings):
    uri = f"/api/v1/orgs/{org_id}/sites" 
    body = site_settings
    resp = mist_session.mist_post(uri, body=body)
    return resp

def update(mist_session:Session, org_id, site_id, body={}):
    uri = f"/api/v1/sites/{site_id}" 
    resp = mist_session.mist_put(uri, body=body)
    return resp
    
def delete(mist_session:Session, org_id, site_id):
    uri = f"/api/v1/sites/{site_id}" 
    resp = mist_session.mist_delete(uri)
    return resp

def get(mist_session:Session, org_id, page=1, limit=100):
    uri = f"/api/v1/orgs/{org_id}/sites" 
    resp = mist_session.mist_get(uri, page=page, limit=limit)
    return resp

def stats(mist_session:Session, site_id, page=1, limit=100):
    uri = f"/api/v1/sites/{site_id}/stats" 
    resp = mist_session.mist_get(uri, page=page, limit=limit)
    return resp

