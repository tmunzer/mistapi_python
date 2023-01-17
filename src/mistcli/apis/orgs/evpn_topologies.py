from mistcli import Session

def get(mist_session:Session, org_id):
    uri = f"/api/v1/orgs/{org_id}/evpn_topologies" 
    resp = mist_session.mist_get(uri)
    return resp

def create(mist_session:Session, org_id, settings):
    uri = f"/api/v1/orgs/{org_id}/evpn_topologies" 
    body = settings
    resp = mist_session.mist_post(uri, body=body)
    return resp

def get_by_id(mist_session:Session, org_id, evpn_topology_id):
    uri = f"/api/v1/orgs/{org_id}/evpn_topologies/{evpn_topology_id}" 
    resp = mist_session.mist_get(uri)
    return resp

def update(mist_session:Session, org_id, evpn_topology_id, settings):
    uri = f"/api/v1/orgs/{org_id}/evpn_topologies/{evpn_topology_id}" 
    body = settings
    resp = mist_session.mist_put(uri, body=body)
    return resp

def delete(mist_session:Session, org_id, evpn_topology_id):
    uri = f"/api/v1/orgs/{org_id}/evpn_topologies/{evpn_topology_id}" 
    resp = mist_session.mist_delete(uri)
    return resp



