import json
import os
import shutil
import re
import sys

openapi_file = "./mist_openapi/Mist.openapi.json"
openapi_json = None
root_folder = "./src/mistapi/"
root_api_folder = "api"

var_translation = {
    "integer": "int",
    "number": "float",
    "string": "str",
    "array": "list",
    "boolean": "bool"
}

file_header="""'''
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
'''
"""

def fprint(message: str):
    print(f"{message}".ljust(80))


def get_ref(ref_name: str):
    data = openapi_refs.get(ref_name)
    tmp = {}
    if data:
        tmp = {
            "name": data["name"].replace(" ", "_").replace("-", "_"),
            "required": data.get("required", False),
            "enum": data["schema"].get("enum", None),
            "type": data["schema"].get("type"),
            "default": data["schema"].get("default"),
            "minimum": data["schema"].get("minimum"),
            "maximum": data["schema"].get("maximum"),
        }
    return tmp

##################################
# Manage folders and files


def _create_or_append_file(file_path: str, data: str, create_only: bool = False):
    if not os.path.exists(file_path):
        with open(file_path, "w+") as f:
            f.write(f"{file_header}\r\n{data}")
            return True
    elif not create_only:
        with open(file_path, "a+") as f:
            f.write(f"{data}")
            return False


def _init_api_file(file_path: str, file_name: str, import_path: list = []):
    api_file = os.path.join(file_path, file_name)
    init_file = os.path.join(file_path, "__init__.py")
    file_created = _create_or_append_file(
        f"{api_file}.py", 
        f"""from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse
""", create_only=True)
    if file_created:
        import_from = f"mistapi.{'.'.join(import_path)}"
        if import_from.endswith("."):
            import_from = import_from[:-1]
        _create_or_append_file(
            init_file, f"from {import_from} import {file_name}\r\n")


def _init_folder(folder_path: str, folder_name: str, import_path: list = []):
    path = os.path.join(folder_path, folder_name)
    init_file = os.path.join(folder_path, "__init__.py")
    if not os.path.exists(path):
        os.makedirs(path)
        import_from = f"mistapi.{'.'.join(import_path)}"
        if import_from.endswith("."):
            import_from = import_from[:-1]
        if folder_path != root_folder:
            _create_or_append_file(
                init_file, f"from {import_from} import {folder_name}\r\n")


def _gen_folder_and_file_paths(endpoint: str):
    endpoint_path = endpoint.split("/")
    # remove vars from endpoint path
    tmp = []
    installer = False
    for part in endpoint_path:
        if part == "installer":
            installer = True
        if part != "" and not part.startswith("{"):
            tmp.append(part)
    endpoint_path = tmp

    if installer and len(endpoint_path) > 4:
        folder_path_parts = endpoint_path[0:4]
        file_name = endpoint_path[4:5][0]
    elif len(endpoint_path) > 3:
        folder_path_parts = endpoint_path[0:3]
        file_name = endpoint_path[3:4][0]
    else:
        folder_path_parts = endpoint_path[0:3]
        file_name = endpoint_path[2:3][0]
    
    if file_name=="128routers": file_name="ssr"
    return folder_path_parts, file_name


def _init_endpoint(endpoint: str):
    full_folder_path = root_folder
    full_import_path = []
    folder_path_parts, file_name = _gen_folder_and_file_paths(endpoint)
    for folder_path_part in folder_path_parts:
        _init_folder(full_folder_path, folder_path_part, full_import_path)
        full_folder_path = os.path.join(full_folder_path, folder_path_part)
        full_import_path.append(folder_path_part)
    _init_api_file(full_folder_path, file_name, full_import_path)
    return full_folder_path, file_name


##################################
# Generate functions
def _gen_code_params_default_value(param: object):
    code_default = ""
    if not param["required"]:
        if param.get("default"):
            if param["type"] == "string":
                code_default = f"=\"{param['default']}\""
            elif param["type"] == "boolean":
                if param['default'] == "true":
                    code_default = "=True"
                else:
                    code_default = "=False"
            else:
                code_default = f"={param['default']}"
        else:
            code_default = "=None"
    return code_default


def _gen_code_params(endpoint_params: list, operation_id: str):
    code_params = ""
    code_params_desc = ""
    for param in endpoint_params:
        ptype_src = param["type"]
        ptype = var_translation.get(ptype_src, "any")
        if ptype == "any":
            fprint(
                f"Unable to convert var type {ptype_src} (opid: {operation_id}, param {param['name']})")

        code_params += f", {param['name']}:{ptype}"

        code_params_desc += f"\r\n    :param {ptype} {param['name']}"
        if param.get("enum"):
            code_params_desc += f"({', '.join(param['enum'])})"
        if param.get("description"):
            code_params_desc += f" - {param['description']}"
        code_params += _gen_code_params_default_value(param)
    return code_params, code_params_desc


def _gen_description(operation_id: str, desc_path_params: str, desc_query_params: str = "", with_file:bool=False):
    description = f"""    \"\"\"
    API doc: https://doc.mist-lab.fr/#operation/{operation_id}
    
    PARAMS
    -----------
    :param APISession mist_session - mistapi session including authentication and Mist host information
    """
    if desc_path_params:
        description += f"""
    PATH PARAMS
    -----------{desc_path_params}        
    """
    if desc_query_params:
        description += f"""
    QUERY PARAMS
    ------------{desc_query_params}        
    """
    if with_file:
        description += f"""
    FILE PARAMS
    -----------
    :param str file_path - path to the file to upload
    """
    description += """
    RETURN
    -----------
    :return APIResponse - response from the API call
    \"\"\""""
    return description


def _gen_query_code(query_params: list):
    code = "\r\n    query_params={}"
    if query_params:
        for param in query_params:
            code += f"\r\n    if {param['name']}: query_params[\"{param['name']}\"]={param['name']}"
    return code

########
# CRUDS
def _create_get(operation_id: str, endpoint_path: str, path_params: list, query_params: list, folder_path: str, file_name: str):
    code_path_params, desc_path_params = _gen_code_params(
        path_params, operation_id)
    code_query_params, desc_query_params = _gen_code_params(
        query_params, operation_id)
    code_query = _gen_query_code(query_params)
    code_desc = _gen_description(
        operation_id, desc_path_params, desc_query_params)

    code = f"""
def {operation_id}(mist_session:_APISession{code_path_params}{code_query_params}) -> _APIResponse:
{code_desc}
    uri = f"{endpoint_path}"{code_query}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    """

    file = os.path.join(folder_path, file_name)
    with open(file, "a+") as f:
        f.write(code)


def _create_delete(operation_id: str, endpoint_path: str, path_params: list, query_params: list, folder_path: str, file_name: str):
    code_path_params, desc_path_params = _gen_code_params(
        path_params, operation_id)
    code_query_params, desc_query_params = _gen_code_params(
        query_params, operation_id)
    code_query = _gen_query_code(query_params)
    code_desc = _gen_description(
        operation_id, desc_path_params, desc_query_params)

    code = f"""
def {operation_id}(mist_session:_APISession{code_path_params}{code_query_params}) -> _APIResponse:
{code_desc}
    uri = f"{endpoint_path}"{code_query}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    """

    file = os.path.join(folder_path, file_name)
    with open(file, "a+") as f:
        f.write(code)


def _create_post_empty(operation_id: str, endpoint_path: str, path_params: list, folder_path: str, file_name: str):
    code_path_params, desc_path_params = _gen_code_params(
        path_params, operation_id)
    code_desc = _gen_description(operation_id, desc_path_params)

    code = f"""
def {operation_id}(mist_session:_APISession{code_path_params}) -> _APIResponse:
{code_desc}
    uri = f"{endpoint_path}"
    resp = mist_session.mist_post(uri=uri)
    return resp
    """

    file = os.path.join(folder_path, file_name)
    with open(file, "a+") as f:
        f.write(code)


def _create_post(operation_id: str, endpoint_path: str, path_params: list, folder_path: str, file_name: str):
    code_path_params, desc_path_params = _gen_code_params(
        path_params, operation_id)
    code_desc = _gen_description(operation_id, desc_path_params)

    code = f"""
def {operation_id}(mist_session:_APISession{code_path_params}, body:object) -> _APIResponse:
{code_desc}
    uri = f"{endpoint_path}"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    """

    file = os.path.join(folder_path, file_name)
    with open(file, "a+") as f:
        f.write(code)


def _create_post_file(operation_id: str, endpoint_path: str, path_params: list, folder_path: str, file_name: str):
    code_path_params, desc_path_params = _gen_code_params(
        path_params, operation_id)
    code_desc = _gen_description(operation_id, desc_path_params, with_file=True)
    code = f"""
def {operation_id}File(mist_session:_APISession{code_path_params}, file_path:str) -> _APIResponse:
{code_desc}
    uri = f"{endpoint_path}"
    with open(file_path, "rb") as f:    
        files = {{"file": f.read()}}
        resp = mist_session.mist_post_file(uri=uri, files=files)
        return resp
    """

    file = os.path.join(folder_path, file_name)
    with open(file, "a+") as f:
        f.write(code)


def _create_put(operation_id: str, endpoint_path: str, path_params: list, folder_path: str, file_name: str):
    code_path_params, desc_path_params = _gen_code_params(
        path_params, operation_id)
    code_desc = _gen_description(operation_id, desc_path_params)

    code = f"""
def {operation_id}(mist_session:_APISession{code_path_params}, body:object) -> _APIResponse:
{code_desc}
    uri = f"{endpoint_path}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    """

    file = os.path.join(folder_path, file_name)
    with open(file, "a+") as f:
        f.write(code)


########
# PARAMS
def _process_path_params(endpoint_params: object):
    params = []
    for parameter in endpoint_params:
        if parameter.get("$ref"):
            tmp_param = get_ref(parameter["$ref"].split("/")[-1:][0])
        else:
            tmp_param = {
                "name": parameter["name"].replace(" ", "_").replace("-", "_"),
                "required": parameter.get("required", False),
                "enum": parameter.get("enum", None),
                "type": parameter.get("schema", {}).get("type"),
                "description": parameter.get("description"),
            }
        if tmp_param not in params:
            params.append(tmp_param)
    return params


def _process_query_params(endpoint_params: object):
    params = []
    for parameter in endpoint_params:
        if parameter.get("$ref"):
            tmp_param = get_ref(parameter["$ref"].split("/")[-1:][0])
        else:
            tmp_param = {
                "name": parameter["name"].replace(" ", "_").replace("-", "_"),
                "required": parameter.get("required", False),
                "enum": parameter.get("schema", {}).get("enum", None),
                "type": parameter.get("schema", {}).get("type"),
                "description": parameter.get("description"),
                "default": parameter["schema"].get("default"),
                "minimum": parameter["schema"].get("minimum"),
                "maximum": parameter["schema"].get("maximum")
            }
        if tmp_param not in params:
            params.append(tmp_param)
    return params


def _process_endpoint(endpoint_data: object, endpoint_path: str, folder_path: str, file_name: str):
    count = 0
    path_params = []
    query_params = []
    operation_id = ""
    path_params = _process_path_params(endpoint_data.get("parameters", []))
    if endpoint_data.get("get"):
        query_params = _process_query_params(
            endpoint_data["get"].get("parameters", []))
        operation_id = endpoint_data["get"]['operationId']
        _create_get(
            operation_id,
            endpoint_path,
            path_params,
            query_params,
            folder_path,
            f"{file_name}.py"
        )
    if endpoint_data.get("delete"):
        query_params = _process_query_params(
            endpoint_data["delete"].get("parameters", []))
        operation_id = endpoint_data["delete"]['operationId']
        _create_delete(
            operation_id,
            endpoint_path,
            path_params,
            query_params,
            folder_path,
            f"{file_name}.py"
        )
    if endpoint_data.get("post"):
        operation_id = endpoint_data["post"]['operationId']
        request_body = endpoint_data["post"].get("requestBody")
        if request_body:
            if "multipart/form-data" in request_body.get("content"):
                _create_post_file(
                    operation_id,
                    endpoint_path,
                    path_params,
                    folder_path,
                    f"{file_name}.py"
                )
            if "application/json" in request_body.get("content"):
                _create_post(
                    operation_id,
                    endpoint_path,
                    path_params,
                    folder_path,
                    f"{file_name}.py"
                )
        else:
            _create_post_empty(
                operation_id,
                endpoint_path,
                path_params,
                folder_path,
                f"{file_name}.py"
            )

    if endpoint_data.get("put"):
        operation_id = endpoint_data["put"]['operationId']
        _create_put(
            operation_id,
            endpoint_path,
            path_params,
            folder_path,
            f"{file_name}.py"
        )

        count += 1
    return count

##################################
# start


def start():
    endpoint_count = 0
    api_count = 0

    out = sys.stdout
    count = len(openapi_paths)
    size = 60
    i = 0

    def show(j):
        x = int(size*j/count)
        out.write(f"".ljust(0))
        out.write(f"[{'█'*x}{'.'*(size-x)}]")
        out.write(f"{j}/{count}\r".rjust(9))
        out.flush()

    for endpoint_path in openapi_paths:
        if endpoint_path.startswith("/api"):
            endpoint_data = openapi_paths[endpoint_path]
            folder_path, file_name = _init_endpoint(endpoint_path)
            api_count += _process_endpoint(endpoint_data,
                                           endpoint_path, folder_path, file_name)
            endpoint_count += 1
        show(i+1)
        i += 1
    out.write("\n")
    out.flush()

    #_create_get_next()
    return endpoint_count, api_count
############################################################################################################ 
############################################################################################################ 


if os.path.exists(f"{root_folder}/{root_api_folder}"):
    shutil.rmtree(f"{root_folder}/{root_api_folder}")
# if os.path.exists("./__init__.py"):
#     os.remove("./__init__.py")

with open(openapi_file, "r") as f:
    openapi_json = json.loads(f.read())

openapi_paths = openapi_json.get("paths")
openapi_refs = openapi_json.get("components", {}).get("parameters")
endpoint_count, api_count = start()

print(f"Endpoint: {endpoint_count}")
print(f"API     : {api_count}")
