from mistcli import Session

def get(mist_session:Session, org_id):
    uri = f"/api/v1/orgs/{org_id}/stats" 
    resp = mist_session.mist_get(uri)
    return resp

