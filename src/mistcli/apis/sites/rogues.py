from mistcli import Session

def set_rogue(mist_session:Session, site_id, rogue_param):
    uri = f"/api/v1/sites/{site_id}/setting"
    resp = mist_session.mist_post(uri, body=rogue_param)
    return resp


def get(mist_session:Session, site_id, duration="1d", r_type="others", page=1, limit=100):
    uri = f"/api/v1/sites/{site_id}/insights/rogues"
    query = {"duration": duration, "type": r_type}
    resp = mist_session.mist_get(uri, query=query, page=page, limit=limit)
    return resp


def report(mist_session:Session, site_id, r_type, fields):
    rogues = get(mist_session, site_id)
    result = []
    for rogue in rogues['result']["results"]:
        temp= []
        for field in fields:
            if field not in rogue:
                temp.append("")            
            else:
                temp.append(f"{rogue[field]}")
        result.append(temp)
    return result