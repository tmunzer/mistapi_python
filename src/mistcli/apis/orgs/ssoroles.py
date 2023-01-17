from mistcli import Session

def get(mist_session:Session, org_id, page=1, limit=100):
    uri = f"/api/v1/orgs/{org_id}/ssoroles" 
    resp = mist_session.mist_get(uri, page=page, limit=limit)
    return resp

def create(mist_session:Session, org_id, ssorole):
    uri = f"/api/v1/orgs/{org_id}/ssoroles" 
    body = ssorole
    resp = mist_session.mist_post(uri, body=body)
    return resp

def update(mist_session:Session, org_id, ssorole_id, ssorole):
    uri = f"/api/v1/orgs/{org_id}/ssoroles/{ssorole_id}" 
    body = ssorole 
    resp = mist_session.mist_put(uri, body=body)
    return resp

def delete(mist_session:Session, org_id, ssorole_id):
    uri = f"/api/v1/orgs/{org_id}/ssoroles/{ssorole_id}" 
    resp = mist_session.mist_delete(uri)
    return resp

def get__saml_metadata(mist_session:Session, org_id, sso_id):
    uri = f"/api/v1/orgs/{org_id}/ssos/{sso_id}/metadata" 
    resp = mist_session.mist_get(uri)
    return resp

def download_saml_metadata(mist_session:Session, org_id, sso_id):
    uri = f"/api/v1/orgs/{org_id}/ssos/{sso_id}/metadata.xml" 
    resp = mist_session.mist_get(uri)
    return resp

def get_sso_failures(mist_session:Session, org_id, sso_id, page=1, limit=100):
    uri = f"/api/v1/orgs/{org_id}/ssos/{sso_id}/failures" 
    resp = mist_session.mist_get(uri, page=page, limit=limit)
    return resp