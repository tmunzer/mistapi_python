from mistcli import Session

def get_device_models(mist_session:Session):
    uri = "/api/v1/const/device_models"
    resp = mist_session.mist_get(uri)
    return resp


