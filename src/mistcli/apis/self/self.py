from mistcli import Session

def get(mist_session:Session):
    uri = "/api/v1/self"
    resp = mist_session.mist_get(uri)
    return resp

def update(mist_session:Session, enable_two_factor:bool, first_name:str, last_name:str, password:str, phone:str, phone2:str):
    body={}
    if type(enable_two_factor) is bool:
        body["enable_two_factor"] = enable_two_factor
    if (first_name):
        body["first_name"] = first_name
    if (last_name):
        body["last_name"] = last_name
    if (password):
        body["password"] = password
    if (phone):
        body["phone"] = phone
    if (phone2):
        body["phone2"] = phone2
    uri = "/api/v1/self"
    resp = mist_session.mist_post(uri, body=body)
    return resp
