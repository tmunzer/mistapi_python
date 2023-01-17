from mistcli import Session

def get(mist_session:Session, org_id):
    uri = f"/api/v1/orgs/{org_id}/vpns" 
    resp = mist_session.mist_et(uri)
    return resp

def create(mist_session:Session, org_id, settings):
    uri = f"/api/v1/orgs/{org_id}/vpns" 
    body = settings
    resp = mist_session.mist_ost(uri, body=body)
    return resp

def get_by_id(mist_session:Session, org_id, vpn_id):
    uri = f"/api/v1/orgs/{org_id}/vpns/{vpn_id}" 
    resp = mist_session.mist_et(uri)
    return resp

def update(mist_session:Session, org_id, vpn_id, settings):
    uri = f"/api/v1/orgs/{org_id}/vpns/{vpn_id}" 
    body = settings
    resp = mist_session.mist_ut(uri, body=body)
    return resp

def delete(mist_session:Session, org_id, vpn_id):
    uri = f"/api/v1/orgs/{org_id}/vpns/{vpn_id}" 
    resp = mist_session.mist_elete(uri)
    return resp



