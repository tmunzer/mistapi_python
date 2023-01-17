from mistcli import Session

def get_languages(mist_session:Session):
    uri = "/api/v1/const/languages"
    resp = mist_session.mist_get(uri)
    return resp


