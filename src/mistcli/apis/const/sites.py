from mistcli import Session

def get_site_available_insight_metrics(mist_session:Session):
    uri = "/api/v1/const/insight_metrics"
    resp = mist_session.mist_get(uri)
    return resp

def get_site_languages(mist_session:Session):
    uri = "/api/v1/const/languages"
    resp = mist_session.mist_get(uri)
    return resp


