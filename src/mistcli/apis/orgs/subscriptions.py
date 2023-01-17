from mistcli import Session

def get(mist_session:Session, org_id, page=1, limit=100):
    uri = "/api/v1/self/subscriptions" 
    resp = mist_session.mist_get(uri, page=page, limit=limit)
    return resp

def subscribe(mist_session:Session, org_id, subscription):
    uri = f"/api/v1/orgs/{org_id}/subscriptions" 
    body = subscription
    resp = mist_session.mist_post(uri, body=body)
    return resp

def ussubscribe(mist_session:Session, org_id, subscription_id):
    uri = f"/api/v1/orgs/{org_id}/subscriptions/{subscription_id}" 
    resp = mist_session.mist_delete(uri)
    return resp

