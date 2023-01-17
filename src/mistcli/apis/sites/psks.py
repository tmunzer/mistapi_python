from mistcli import Session

def create(mist_session:Session, site_id, psk):
    uri = f"/api/v1/sites/{site_id}/psks"
    resp = mist_session.mist_post(uri, body=psk)
    return resp


def get(mist_session:Session, site_id, psk_id="", name="", ssid="", page=1, limit=100):
    uri = f"/api/v1/sites/{site_id}/psks"
    query={}
    if psk_id != "":
        uri +=f"/{psk_id}"
    if name != "":
        query["name"] = name
    if  ssid != "":
        query["ssid"] = ssid
    resp = mist_session.mist_get(uri, query=query, page=page, limit=limit)
    return resp 

def delete(mist_session:Session, site_id, psk_id:str, name:str, ssid:str):
    uri = f"/api/v1/sites/{site_id}/psks"
    query={}
    if psk_id != "":
        uri +=f"/{psk_id}"
    if name != "":
        query["name"] = name
    if  ssid != "":
        query["ssid"] = ssid
    resp = mist_session.mist_delete(uri, query=query)
    return resp 
