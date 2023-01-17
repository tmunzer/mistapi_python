from mistcli import Session

def get(mist_session:Session, site_id, page=1, limit=100):
    uri = f"/api/v1/sites/{site_id}/maps"
    resp = mist_session.mist_get(uri, page=page, limit=limit)
    return resp

def delete(mist_session:Session, site_id, map_id):
    uri = f"/api/v1/sites/{site_id}/maps/{map_id}"
    resp = mist_session.mist_delete(uri)
    return resp

def create(mist_session:Session, site_id, map_settings):
    uri = f"/api/v1/sites/{site_id}/maps"
    body = map_settings
    resp = mist_session.mist_post(uri, body=body)
    return resp


def add_image(mist_session:Session, site_id, map_id, image_path):
    uri = f"/api/v1/sites/{site_id}/maps/{map_id}/image"
    f= open(image_path, 'rb')
    files = {'file': f.read()}
    resp = mist_session.mist_post_file(uri, files=files)
    f.close()
    return resp

def delete_image(mist_session:Session, site_id, map_id):
    uri = f"/api/v1/sites/{site_id}/maps/{map_id}/image"
    resp = mist_session.mist_delete(uri)
    return resp