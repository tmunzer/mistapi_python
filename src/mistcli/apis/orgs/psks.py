from mistcli import Session

def create(mist_session:Session, org_id, psk):
    uri = f"/api/v1/orgs/{org_id}/psks" 
    resp = mist_session.mist_post(uri, body=psk)
    return resp


def get(mist_session:Session, org_id, psk_id="", name="", ssid="", page=1, limit=100):
    uri = f"/api/v1/orgs/{org_id}/psks" 
    query={}
    if psk_id != "":
        uri +=f"/{psk_id}" 
    if name != "":
        query["name"] = name
    if  ssid != "":
        query["ssid"] = ssid
    resp = mist_session.mist_get(uri, query=query, page=page, limit=limit)
    return resp 

def delete(mist_session:Session, org_id, psk_id="", name="", ssid=""):
    uri = f"/api/v1/orgs/{org_id}/psks" 
    if psk_id != "":
        uri +=f"/{psk_id}" 
    elif name != "" and ssid != "":
        uri += f"?name={name}&ssid={ssid}" 
    elif name != "":
        uri += f"?name={name}" 
    elif  ssid != "":
        uri += f"?ssid={ssid}" 
    resp = mist_session.mist_delete(uri)
    return resp 


def get_by_id(mist_session:Session, org_id, psk_id):
    uri = f"/api/v1/orgs/{org_id}/psks/{psk_id}" 
    resp = mist_session.mist_get(uri)
    return resp