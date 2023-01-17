from mistcli import Session

def get(mist_session:Session, site_id, name=None, device_type=None, page=1, limit=100):
    uri = f"/api/v1/sites/{site_id}/devices"
    query={}
    if name:
        query[name] = name
    if device_type in ["ap", "switch", "gateway", "all"]:
        query["type"] = device_type
    resp = mist_session.mist_get(uri, query=query, page=page, limit=limit)
    return resp

def get_details(mist_session:Session, site_id, device_id):
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}"
    resp = mist_session.mist_get(uri)
    return resp

def get_stats_devices(mist_session:Session, site_id, device_id=None, device_type=None, page=1, limit=100):
    uri = f"/api/v1/sites/{site_id}/stats/devices"
    query={}
    if device_id:
        uri += f"/{device_id}"
    if device_type:
        query["type"] = device_type
    resp = mist_session.mist_get(uri, query=query, page=page, limit=limit)
    return resp

def create(mist_session:Session, site_id, devices):
    uri = f"/api/v1/sites/{site_id}/devices"
    resp = mist_session.mist_post(uri, body=devices)
    return resp


def update(mist_session:Session, site_id, device_id, device_settings):
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}"
    resp = mist_session.mist_put(uri, body=device_settings)
    return resp


def delete(mist_session:Session, site_id, device_id):
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}"
    resp = mist_session.mist_delete(uri)
    return resp

def add_image(mist_session:Session, site_id, device_id, image_num, image_path):
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}/image{image_num}"
    f= open(image_path, 'rb')
    files = {'file': f.read()}
    resp = mist_session.mist_post_file(uri, files=files)
    f.close()
    return resp

def set_device_conf(mist_session:Session, site_id, device_id, conf):
    uri = f"/api/v1/sites/{site_id}/devices/{device_id}"
    body = conf
    resp = mist_session.mist_put(uri, body=body)
    return resp


