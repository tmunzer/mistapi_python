from mistcli import Session

def get_applications(mist_session:Session):
    uri = "/api/v1/const/applications"
    resp = mist_session.mist_get(uri)
    return resp


