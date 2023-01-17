from mistcli import Session

def get(mist_session:Session,page=1, limit=100):
    uri = "/api/v1/self/subscriptions"
    resp = mist_session.mist_get(uri, page=page, limit=limit)
    return resp


