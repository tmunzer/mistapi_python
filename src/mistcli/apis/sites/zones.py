from mistcli import Session

def create(mist_session:Session, site_id:str, zone_settings):
    uri = f"/api/v1/sites/{site_id}/zones"
    body = zone_settings
    resp = mist_session.mist_post(uri, body=body)
    return resp

def update(mist_session:Session, site_id:str, zone_id:str, body={}):
    uri = f"/api/v1/sites/{site_id}/zones/{zone_id}"
    resp = mist_session.mist_put(uri, body=body)
    return resp
    
def delete(mist_session:Session, site_id:str, zone_id:str):
    uri = f"/api/v1/sites/{site_id}/zones/{zone_id}"
    resp = mist_session.mist_delete(uri)
    return resp

def get(mist_session:Session, site_id:str, zone_id:str=None, page=1, limit=100):
    uri = f"/api/v1/sites/{site_id}/zones"
    if zone_id: uri += f"{zone_id}"
    resp = mist_session.mist_get(uri, page=page, limit=limit)
    return resp


