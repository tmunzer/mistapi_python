from mistcli import Session

def get(mist_session:Session, org_id, page=1, limit=100):
    uri = f"/api/v1/orgs/{org_id}/sitegroups" 
    resp = mist_session.mist_get(uri, page=page, limit=limit)
    return resp

def get_by_id(mist_session:Session, org_id, sitegroup_id):
    uri = f"/api/v1/orgs/{org_id}/sitegroups/{sitegroup_id}" 
    resp = mist_session.mist_get(uri)
    return resp

def create(mist_session:Session, org_id, group_name):
    uri = f"/api/v1/orgs/{org_id}/sitegroups" 
    body = group_name
    resp = mist_session.mist_post(uri, body=body)
    return resp

def update(mist_session:Session, org_id, sitegroup_id, body):
    uri = f"/api/v1/orgs/{org_id}/sitegroups/{sitegroup_id}" 
    resp = mist_session.mist_put(uri, body=body)
    return resp

def delete(mist_session:Session, org_id, sitegroup_id):
    uri = f"/api/v1/orgs/{org_id}/sitegroups/{sitegroup_id}" 
    resp = mist_session.mist_delete(uri)
    return resp
