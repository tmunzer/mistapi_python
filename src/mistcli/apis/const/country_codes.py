from mistcli import Session

def get_country_codes(mist_session:Session):
    uri = "/api/v1/const/countries"
    resp = mist_session.mist_get(uri)
    return resp


