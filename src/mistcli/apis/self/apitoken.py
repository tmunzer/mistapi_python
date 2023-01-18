from mistcli import Session

def get(mist_session:Session):
    uri = "/api/v1/self/apitokens"
    resp = mist_session.mist_get(uri)
    return resp


def create(mist_session:Session, token_name:str=None):
    body = {}
    if token_name: body["name"]=token_name
    uri = "/api/v1/self/apitokens"
    resp = mist_session.mist_post(uri, body=body)
    return resp


def delet(mist_session:Session, token_id:str):
    uri = "/api/v1/self/apitokens/{token_id}"
    resp = mist_session.mist_delete(uri)
    return resp