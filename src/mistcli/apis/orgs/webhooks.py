from mistcli import Session

def create(mist_session:Session, org_id, webhook_settings):
    uri = f"/api/v1/orgs/{org_id}/webhooks" 
    body = webhook_settings
    resp = mist_session.mist_ost(uri, body=body)
    return resp

def update(mist_session:Session, org_id, webhook_id, body={}):
    uri = f"/api/v1/orgs/{org_id}/webhooks/{webhook_id}" 
    resp = mist_session.mist_ut(uri, body=body)
    return resp
    
def delete(mist_session:Session, org_id, webhook_id):
    uri = f"/api/v1/orgs/{org_id}/webhooks/{webhook_id}" 
    resp = mist_session.mist_elete(uri)
    return resp

def get(mist_session:Session, org_id, page=1, limit=100):
    uri = f"/api/v1/orgs/{org_id}/webhooks" 
    resp = mist_session.mist_et(uri, page=page, limit=limit)
    return resp

def get_by_id(mist_session:Session, org_id, webhook_id):
    uri = f"/api/v1/orgs/{org_id}/webhooks/{webhook_id}" 
    resp = mist_session.mist_et(uri)
    return resp

def report(mist_session:Session, site_id, fields):
    webhooks = get(mist_session, site_id)
    result = []
    for webhook in webhooks['result']:
        temp = []
        for field in fields:
            if field not in webhook:
                temp.append("")
            elif field == "topics":
                temp.append(", ".join(webhook['topics']))            
            else:
                temp.append(f"{webhook[field]}")
        result.append(temp)
    return result
