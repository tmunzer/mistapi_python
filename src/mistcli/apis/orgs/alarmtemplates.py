from mistcli import Session

def create(mist_session:Session, org_id, alarmtemplate_settings):
    uri = f"/api/v1/orgs/{org_id}/alarmtemplates" 
    body = alarmtemplate_settings
    resp = mist_session.mist_post(uri, body=body)
    return resp

def update(mist_session:Session, org_id, alarmtemplate_settings, body={}):
    uri = f"/api/v1/orgs/{org_id}/alarmtemplates/{alarmtemplate_settings}" 
    resp = mist_session.mist_put(uri, body=body)
    return resp
    
def delete(mist_session:Session, org_id, alarmtemplate_settings):
    uri = f"/api/v1/orgs/{org_id}/alarmtemplates/{alarmtemplate_settings}" 
    resp = mist_session.mist_delete(uri)
    return resp

def get(mist_session:Session, org_id, page=1, limit=100):
    uri = f"/api/v1/orgs/{org_id}/alarmtemplates" 
    resp = mist_session.mist_get(uri, page=page, limit=limit)
    return resp

def get_by_id(mist_session:Session, org_id, alarmtemplate_id):
    uri = f"/api/v1/orgs/{org_id}/alarmtemplates/{alarmtemplate_id}" 
    resp = mist_session.mist_get(uri)
    return resp

def get_by_id(mist_session:Session, org_id, alarmtemplate_id):
    uri = f"/api/v1/orgs/{org_id}/alarmtemplates/{alarmtemplate_id}" 
    resp = mist_session.mist_get(uri)
    return resp

