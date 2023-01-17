from mistcli import Session

def get_definition(mist_session:Session):
    uri = "/api/v1/const/system_events"
    resp = mist_session.mist_get(uri)
    return resp
def search(mist_session:Session, site_id, mtype, start, end):
    uri = f"/api/v1/sites/{site_id}/events/system/search"
    query = {"type": mtype, "start": start, "end": end}
    resp = mist_session.mist_get(uri, query=query)
    return resp
def count(mist_session:Session, site_id, mtype, start, end):
    uri = f"/api/v1/sites/{site_id}/events/system/coun"
    query = {"type": mtype, "start": start, "end": end}
    resp = mist_session.mist_get(uri, query=query)
    return resp
