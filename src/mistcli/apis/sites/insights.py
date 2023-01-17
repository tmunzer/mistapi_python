from mistcli import Session

def stats(mist_session:Session, site_id, start, end, metrics, page=1, limit=100):
    uri = f"/api/v1/sites/{site_id}/insights/stats"
    query = {"start": start, "end": end, "metrics": metrics}
    resp = mist_session.mist_get(uri, query=query, page=page, limit=limit)
    return resp


def client(mist_session:Session, site_id, client_mac, start, end, interval, metrics, page=1, limit=100):
    uri = f"/api/v1/sites/{site_id}/insights/client/{client_mac}/stats"
    query = {"start": start, "end": end, "interval": interval, "metrics": metrics}
    resp = mist_session.mist_get(uri, query=query, page=page, limit=limit)
    return resp
