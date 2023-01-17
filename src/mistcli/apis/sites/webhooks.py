from mistcli import Session

def get(mist_session:Session, site_id, page=1, limit=100):
    uri = f"/api/v1/sites/{site_id}/webhooks"
    resp = mist_session.mist_get(uri, page=page, limit=limit)
    return resp

def get_details(mist_session:Session, site_id, webhook_id):
    uri = f"/api/v1/sites/{site_id}/webhooks/{webhook_id}"
    resp = mist_session.mist_get(uri)
    return resp

def create(mist_session:Session, site_id, webhook):
    uri = f"/api/v1/sites/{site_id}/webhooks"
    resp = mist_session.mist_post(uri, body=webhook)
    return resp


def update(mist_session:Session, site_id, webhook_id, webhook_settings):
    uri = f"/api/v1/sites/{site_id}/webhooks/{webhook_id}"
    resp = mist_session.mist_put(uri, body=webhook_settings)
    return resp


def delete(mist_session:Session, site_id, webhook_id):
    uri = f"/api/v1/sites/{site_id}/webhooks/{webhook_id}"
    resp = mist_session.mist_delete(uri)
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
