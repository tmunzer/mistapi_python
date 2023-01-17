from mistcli import Session

def get_traffic_types(mist_session:Session):
    uri = "/api/v1/const/traffic_types"
    resp = mist_session.mist_get(uri)
    return resp

