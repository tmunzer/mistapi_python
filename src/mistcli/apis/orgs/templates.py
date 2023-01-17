from mistcli import Session

def get(mist_session:Session, org_id, page=1, limit=100):
    uri = f"/api/v1/orgs/{org_id}/templates" 
    resp = mist_session.mist_get(uri, page=page, limit=limit)
    return resp

def get_details(mist_session:Session, org_id, template_id):
    uri = f"/api/v1/orgs/{org_id}/templates/{template_id}" 
    resp = mist_session.mist_get(uri)
    return resp

def create(mist_session:Session, org_id, template_settings):
    uri = f"/api/v1/orgs/{org_id}/templates" 
    resp = mist_session.mist_post(uri, body=template_settings)
    return resp

def delete(mist_session:Session, org_id, template_id):
    uri = f"/api/v1/orgs/{org_id}/templates/{template_id}" 
    resp = mist_session.mist_delete(uri)
    return resp

def get_by_id(mist_session:Session, org_id, template_id):
    uri = f"/api/v1/orgs/{org_id}/templates/{template_id}" 
    resp = mist_session.mist_get(uri)
    return resp
