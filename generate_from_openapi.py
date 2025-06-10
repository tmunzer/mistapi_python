import os
import re
import shutil
import sys

import yaml

# Configuration constants
openapi_file = "./mist_openapi/mist.openapi.yaml"
openapi_json = None
root_folder = "./src/mistapi/"
root_api_folder = "api"

# Type mapping from OpenAPI to Python types
var_translation = {
    "integer": "int",
    "number": "float",
    "string": "str",
    "array": "list",
    "boolean": "bool",
}

# Standard header for generated Python files
file_header = """'''
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
'''
"""


def fprint(message: str) -> None:
    """Print a formatted message with left justification."""
    print(f"{message}".ljust(80))


def gen_param(data: dict):
    """
    Generate parameter dictionary from OpenAPI parameter definition.

    Args:
        data: OpenAPI parameter definition

    Returns:
        dict: Processed parameter with name, type, description, etc.
    """
    tmp = {}
    if data:
        if data["schema"].get("$ref"):
            # Handle parameter with schema reference
            ref_name = data["schema"]["$ref"].split("/")[-1:][0]
            ref = openapi_schemas.get(ref_name)
            tmp = {
                "name": data["name"].replace(" ", "_").replace("-", "_"),
                "required": data.get("required", False),
                "enum": ref.get("enum", None),
                "type": ref.get("type"),
                "description": data.get("description"),
                "default": ref.get("default"),
                "minimum": ref.get("minimum"),
                "maximum": ref.get("maximum"),
            }
        else:
            # Handle inline parameter definition
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


def _create_or_append_file(
    file_path: str, data: str, create_only: bool = False
) -> bool:
    """
    Create a new file or append to existing file.

    Args:
        file_path: Path to the file
        data: Content to write/append
        create_only: If True, only create new files (don't append to existing)

    Returns:
        bool: True if file was created, False if appended to existing
    """
    if not os.path.exists(file_path):
        with open(file_path, "w+") as f:
            f.write(f"{file_header}\r\n{data}")
            return True
    elif not create_only:
        with open(file_path, "a+") as f:
            f.write(f"{data}")
            return False
    return False


def _init_api_file(file_path: str, file_name: str, import_path: list = []) -> None:
    """
    Initialize API file with imports and update __init__.py.

    Args:
        file_path: Directory path for the file
        file_name: Name of the API file (without .py extension)
        import_path: List of module path components for imports
    """
    api_file = os.path.join(file_path, file_name)
    init_file = os.path.join(file_path, "__init__.py")

    # Create API file with standard imports
    file_created = _create_or_append_file(
        f"{api_file}.py",
        """from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse
import deprecation
""",
        create_only=True,
    )

    # Add import to __init__.py if file was newly created
    if file_created:
        import_from = f"mistapi.{'.'.join(import_path)}"
        if import_from.endswith("."):
            import_from = import_from[:-1]
        _create_or_append_file(init_file, f"from {import_from} import {file_name}\r\n")


def _init_folder(folder_path: str, folder_name: str, import_path: list = []) -> None:
    """
    Initialize folder structure and update parent __init__.py.

    Args:
        folder_path: Parent directory path
        folder_name: Name of folder to create
        import_path: List of module path components for imports
    """
    path = os.path.join(folder_path, folder_name)
    init_file = os.path.join(folder_path, "__init__.py")

    if not os.path.exists(path):
        os.makedirs(path)
        import_from = f"mistapi.{'.'.join(import_path)}"
        if import_from.endswith("."):
            import_from = import_from[:-1]
        if folder_path != root_folder:
            _create_or_append_file(
                init_file, f"from {import_from} import {folder_name}\r\n"
            )


def _gen_folder_and_file_paths(endpoint: str):
    """
    Generate folder structure and file name from API endpoint path.

    Args:
        endpoint: API endpoint path (e.g., "/api/v1/orgs/{org_id}/sites")

    Returns:
        tuple: (folder_path_parts, file_name)
    """
    endpoint_path = endpoint.split("/")

    # Remove empty strings and path variables from endpoint
    tmp = []
    installer = False
    for part in endpoint_path:
        if part == "installer":
            installer = True
        if part != "" and not part.startswith("{"):
            tmp.append(part)
    endpoint_path = tmp

    # Determine folder structure based on endpoint depth and installer flag
    if installer and len(endpoint_path) > 4:
        folder_path_parts = endpoint_path[0:4]
        file_name = endpoint_path[4:5][0]
    elif len(endpoint_path) > 3:
        folder_path_parts = endpoint_path[0:3]
        file_name = endpoint_path[3:4][0]
    else:
        folder_path_parts = endpoint_path[0:3]
        file_name = endpoint_path[2:3][0]

    # Special case for 128routers endpoint
    if file_name == "128routers":
        file_name = "ssr"
    return folder_path_parts, file_name


def _init_endpoint(endpoint: str):
    """
    Initialize complete folder structure and API file for an endpoint.

    Args:
        endpoint: API endpoint path

    Returns:
        tuple: (full_folder_path, file_name)
    """
    full_folder_path = root_folder
    full_import_path = []
    folder_path_parts, file_name = _gen_folder_and_file_paths(endpoint)

    # Create nested folder structure
    for folder_path_part in folder_path_parts:
        _init_folder(full_folder_path, folder_path_part, full_import_path)
        full_folder_path = os.path.join(full_folder_path, folder_path_part)
        full_import_path.append(folder_path_part)

    # Create API file in the deepest folder
    _init_api_file(full_folder_path, file_name, full_import_path)
    return full_folder_path, file_name


##################################
# Generate functions


def _gen_code_params_default_value(param: object):
    """
    Generate default value code for function parameters.

    Args:
        param: Parameter definition with type and default info

    Returns:
        str: Code string for default value (e.g., '=None', '="default"')
    """
    code_default = ""
    if not param["required"]:
        if param.get("default"):
            if param["type"] == "string":
                code_default = f'="{param["default"]}"'
            elif param["type"] == "boolean":
                if param["default"] == "true":
                    code_default = "=True"
                else:
                    code_default = "=False"
            else:
                code_default = f"={param['default']}"
        else:
            code_default = "|None=None"
            # TODO fix for python 3.9
            # code_default = "=None"
    return code_default


def _gen_code_params(endpoint_params: list, operation_id: str):
    """
    Generate function parameter code and documentation.

    Args:
        endpoint_params: List of parameter definitions
        operation_id: OpenAPI operation ID for error reporting

    Returns:
        tuple: (code_params, code_params_desc) - parameter code and documentation
    """
    code_params = ""
    code_params_desc = ""

    for param in endpoint_params:
        ptype_src = param["type"]
        ptype = var_translation.get(ptype_src, "any")

        # Log warning for unknown types
        if ptype == "any":
            fprint(
                f"Unable to convert var type {ptype_src} (opid: {operation_id}, param {param['name']})"
            )

        # Build parameter signature
        code_params += f", {param['name']}:{ptype}"

        # Build parameter documentation
        code_params_desc += f"\r\n    {param['name']} : {ptype}"
        if param.get("enum"):
            code_params_desc += str(param["enum"]).replace("[", "{").replace("]", "}")
        if param.get("default"):
            code_params_desc += f", default: {param['default']}"
        if param.get("description"):
            code_params_desc += f"\r\n      {param['description']}"

        # Add default value
        code_params += _gen_code_params_default_value(param)

    return code_params, code_params_desc


def _gen_description_property(property_data: dict):
    """
    Generate property description for documentation.

    Args:
        property_data: Property definition with type, enum, default, description

    Returns:
        tuple: (property_type, property_desc) - formatted type and description
    """
    property_type = property_data["property_type"]
    property_desc = ""

    if property_data.get("property_enum"):
        property_type = (
            str(property_data["property_enum"]).replace("[", "{").replace("]", "}")
        )
    if property_data.get("property_default"):
        property_type += f", default: {property_data['property_default']}"
    if property_data.get("property_desc"):
        property_desc = f"\r\n        {property_data['property_desc']}"

    return property_type, property_desc


def _process_tags(tags: list):
    """
    Process OpenAPI tags to generate URL path for documentation.

    Args:
        tags: List of OpenAPI tags

    Returns:
        str: Processed tag path for documentation URL
    """
    result = []
    splitted_tag = tags[0].split(" ", 1)
    result.append(splitted_tag[0].strip().lower())

    if len(splitted_tag) > 1:
        for subcat in splitted_tag[1].split(" - "):
            result.append(subcat.strip().replace(" ", "-").lower())

    return "/".join(result)


def _gen_description(
    operation_id: str,
    tags: list,
    desc_path_params: str,
    desc_query_params: str = "",
    with_body: bool = False,
    multipart_form_data: dict = {},
):
    """
    Generate complete function docstring.

    Args:
        operation_id: OpenAPI operation ID
        tags: OpenAPI tags for documentation URL
        desc_path_params: Path parameters documentation
        desc_query_params: Query parameters documentation
        with_body: Whether function accepts body parameter
        multipart_form_data: Multipart form data parameters

    Returns:
        str: Complete docstring
    """
    # Convert operation ID to URL format
    r = "(?<!^)(?=[A-Z])"
    operation = re.sub(r, "-", operation_id).lower()
    tags_in_url = _process_tags(tags)

    # Start building docstring
    description = f"""    \"\"\"
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/{tags_in_url}/{operation}

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    """

    # Add path parameters section
    if desc_path_params:
        description += f"""
    PATH PARAMS
    -----------{desc_path_params}
    """

    # Add query parameters section
    if desc_query_params:
        description += f"""
    QUERY PARAMS
    ------------{desc_query_params}
    """

    # Add body parameters section
    if with_body or multipart_form_data:
        description += """
    BODY PARAMS
    -----------"""

        if with_body:
            description += "\r\n    body : dict\r\n        JSON object to send to Mist Cloud (see API doc above for more details)"

        # Add multipart form data parameters
        if multipart_form_data:
            for key in multipart_form_data:
                if key in ["csv", "file"]:
                    description += f"\r\n    {key} : {multipart_form_data[key]['property_type']}\r\n        path to the file to upload. {multipart_form_data[key]['property_desc']}"
                else:
                    property_type, property_desc = _gen_description_property(
                        multipart_form_data[key]
                    )
                    description += f"\r\n    {key} : {property_type}{property_desc}"

                    # Add nested properties
                    if multipart_form_data[key]["property_childs"]:
                        for child in multipart_form_data[key]["property_childs"]:
                            property_type, property_desc = _gen_description_property(
                                multipart_form_data[key]["property_childs"][child]
                            )
                            description += (
                                f"\r\n        {child} : {property_type}{property_desc}"
                            )
        description += """
    """

    # Add return section
    description += """
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    \"\"\""""
    return description


def _gen_query_code(query_params: list):
    """
    Generate code for handling query parameters.

    Args:
        query_params: List of query parameter definitions

    Returns:
        str: Code for building query parameters dictionary
    """
    code = "\r\n    query_params:dict[str, str]={}"
    if query_params:
        for param in query_params:
            code += f'\r\n    if {param["name"]}:\r\n        query_params["{param["name"]}"]=str({param["name"]})'
    return code


########
# CRUDS - Create, Read, Update, Delete, Search function generators


def _create_get_deprecated_device_events(
    operation_id: str,
    endpoint_path: str,
    path_params: list,
    query_params: list,
    folder_path: str,
    file_name: str,
) -> None:
    """
    Create deprecated version of DeviceEvents GET functions for backward compatibility.

    Args:
        operation_id: OpenAPI operation ID
        endpoint_path: API endpoint path
        path_params: Path parameters
        query_params: Query parameters
        folder_path: Output folder path
        file_name: Output file name
    """
    code_path_params, desc_path_params = _gen_code_params(path_params, operation_id)
    code_query_params, desc_query_params = _gen_code_params(query_params, operation_id)
    code_query = _gen_query_code(query_params)
    code_desc = _gen_description(operation_id, desc_path_params, desc_query_params)

    # Generate old operation ID for deprecated function
    old_operation_id = operation_id.replace("DeviceEvents", "DevicesEvents", 1)

    code = f"""
@deprecation.deprecated(deprecated_in="0.45.0", removed_in="0.60.0", current_version="{version}", details="function replaced with {operation_id}")
def {old_operation_id}(mist_session:_APISession{code_path_params}{code_query_params}) -> _APIResponse:
{code_desc}
    uri = f"{endpoint_path}"{code_query}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    """

    # Append to file
    file = os.path.join(folder_path, file_name)
    with open(file, "a+") as f:
        f.write(code)


def _create_get(
    operation_id: str,
    tags: list,
    endpoint_path: str,
    path_params: list,
    query_params: list,
    folder_path: str,
    file_name: str,
) -> None:
    """
    Generate GET method function.

    Args:
        operation_id: OpenAPI operation ID
        tags: OpenAPI tags
        endpoint_path: API endpoint path
        path_params: Path parameters
        query_params: Query parameters
        folder_path: Output folder path
        file_name: Output file name
    """
    # Create deprecated version if needed
    if operation_id.startswith("DeviceEvents"):
        _create_get_deprecated_device_events(
            operation_id,
            endpoint_path,
            path_params,
            query_params,
            folder_path,
            file_name,
        )

    # Generate function parameters and documentation
    code_path_params, desc_path_params = _gen_code_params(path_params, operation_id)
    code_query_params, desc_query_params = _gen_code_params(query_params, operation_id)
    code_query = _gen_query_code(query_params)
    code_desc = _gen_description(
        operation_id, tags, desc_path_params, desc_query_params
    )

    # Generate function code
    code = f"""
def {operation_id}(mist_session:_APISession{code_path_params}{code_query_params}) -> _APIResponse:
{code_desc}
    uri = f"{endpoint_path}"{code_query}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    """

    # Append to file
    file = os.path.join(folder_path, file_name)
    with open(file, "a+") as f:
        f.write(code)


def _create_delete(
    operation_id: str,
    tags: list,
    endpoint_path: str,
    path_params: list,
    query_params: list,
    folder_path: str,
    file_name: str,
) -> None:
    """
    Generate DELETE method function.

    Args:
        operation_id: OpenAPI operation ID
        tags: OpenAPI tags
        endpoint_path: API endpoint path
        path_params: Path parameters
        query_params: Query parameters
        folder_path: Output folder path
        file_name: Output file name
    """
    code_path_params, desc_path_params = _gen_code_params(path_params, operation_id)
    code_query_params, desc_query_params = _gen_code_params(query_params, operation_id)
    code_query = _gen_query_code(query_params)
    code_desc = _gen_description(
        operation_id, tags, desc_path_params, desc_query_params
    )

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


def _create_post_empty(
    operation_id: str,
    tags: list,
    endpoint_path: str,
    path_params: list,
    folder_path: str,
    file_name: str,
) -> None:
    """
    Generate POST method function without request body.

    Args:
        operation_id: OpenAPI operation ID
        tags: OpenAPI tags
        endpoint_path: API endpoint path
        path_params: Path parameters
        folder_path: Output folder path
        file_name: Output file name
    """
    code_path_params, desc_path_params = _gen_code_params(path_params, operation_id)
    code_desc = _gen_description(operation_id, tags, desc_path_params)

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


def _create_post(
    operation_id: str,
    tags: list,
    endpoint_path: str,
    path_params: list,
    folder_path: str,
    file_name: str,
) -> None:
    """
    Generate POST method function with JSON request body.

    Args:
        operation_id: OpenAPI operation ID
        tags: OpenAPI tags
        endpoint_path: API endpoint path
        path_params: Path parameters
        folder_path: Output folder path
        file_name: Output file name
    """
    code_path_params, desc_path_params = _gen_code_params(path_params, operation_id)
    code_desc = _gen_description(operation_id, tags, desc_path_params, with_body=True)

    code = f"""
def {operation_id}(mist_session:_APISession{code_path_params}, body:dict) -> _APIResponse:
{code_desc}
    uri = f"{endpoint_path}"
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    """

    file = os.path.join(folder_path, file_name)
    with open(file, "a+") as f:
        f.write(code)


def _process_multipart_json(properties: dict) -> dict:
    """
    Process multipart form data properties into structured format.

    Args:
        properties: OpenAPI schema properties for multipart data

    Returns:
        dict: Processed multipart form data structure
    """
    multipart_form_data = {}
    for key in properties:
        property_type = "dict"
        property_default = properties[key].get("default", None)
        property_enum = properties[key].get("enum", None)
        property_childs = None

        # Map OpenAPI types to Python types
        match properties[key].get("type"):
            case "boolean":
                property_type = "bool"
            case "string":
                property_type = "str"
            case "integer":
                property_type = "int"
            case "number":
                property_type = "float"
            case "array":
                property_type = "list"
            case "binary":
                property_type = "str"
            case "object":
                property_type = "dict"
                # Recursively process nested objects
                if properties[key].get("properties"):
                    property_childs = _process_multipart_json(
                        properties[key]["properties"]
                    )

        multipart_form_data[key] = {
            "property_type": property_type,
            "property_desc": properties[key].get("description", ""),
            "property_default": property_default,
            "property_enum": property_enum,
            "property_childs": property_childs,
        }
    return multipart_form_data


def _create_post_file(
    operation_id: str,
    tags: list,
    endpoint_path: str,
    path_params: list,
    folder_path: str,
    properties: dict,
    file_name: str,
) -> None:
    """
    Generate POST method function for file uploads (multipart/form-data).

    Args:
        operation_id: OpenAPI operation ID
        tags: OpenAPI tags
        endpoint_path: API endpoint path
        path_params: Path parameters
        folder_path: Output folder path
        properties: Multipart form properties
        file_name: Output file name
    """
    code_path_params, desc_path_params = _gen_code_params(path_params, operation_id)
    multipart_form_data = _process_multipart_json(properties)
    code_desc = _gen_description(
        operation_id, tags, desc_path_params, multipart_form_data=multipart_form_data
    )

    # Build function signature with multipart parameters
    code = f"""
def {operation_id}File(mist_session:_APISession{code_path_params}"""
    for key, value in multipart_form_data.items():
        code += f", {key}:{value['property_type']}|None=None"
    code += ") -> _APIResponse:"

    # Build function body
    code += f"""
{code_desc}
    """
    code += "multipart_form_data = {"
    for key in multipart_form_data:
        code += f"""
        "{key}":{key},"""
    code += f"""
    }}
    uri = f"{endpoint_path}"
    resp = mist_session.mist_post_file(uri=uri, multipart_form_data=multipart_form_data)
    return resp
"""

    file = os.path.join(folder_path, file_name)
    with open(file, "a+") as f:
        f.write(code)


def _create_put(
    operation_id: str,
    tags: list,
    endpoint_path: str,
    path_params: list,
    folder_path: str,
    file_name: str,
) -> None:
    """
    Generate PUT method function.

    Args:
        operation_id: OpenAPI operation ID
        tags: OpenAPI tags
        endpoint_path: API endpoint path
        path_params: Path parameters
        folder_path: Output folder path
        file_name: Output file name
    """
    code_path_params, desc_path_params = _gen_code_params(path_params, operation_id)
    code_desc = _gen_description(operation_id, tags, desc_path_params, with_body=True)

    code = f"""
def {operation_id}(mist_session:_APISession{code_path_params}, body:dict) -> _APIResponse:
{code_desc}
    uri = f"{endpoint_path}"
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    """

    file = os.path.join(folder_path, file_name)
    with open(file, "a+") as f:
        f.write(code)


########
# PARAMS - Parameter processing functions


def _process_path_params(endpoint_params: object):
    """
    Process path parameters from OpenAPI endpoint definition.

    Args:
        endpoint_params: List of OpenAPI parameter objects

    Returns:
        list: Processed path parameters
    """
    params = []
    for parameter in endpoint_params:
        if parameter.get("$ref"):
            # Handle parameter reference
            ref_name = parameter["$ref"].split("/")[-1:][0]
            data = openapi_refs.get(ref_name)
            tmp_param = gen_param(data)
        else:
            # Handle inline parameter
            tmp_param = gen_param(parameter)

        if tmp_param not in params:
            params.append(tmp_param)
    return params


def _process_query_params(endpoint_params: object):
    """
    Process query parameters from OpenAPI endpoint definition.

    Args:
        endpoint_params: List of OpenAPI parameter objects

    Returns:
        list: Processed query parameters
    """
    params = []
    for parameter in endpoint_params:
        if parameter.get("$ref"):
            # Handle parameter reference
            ref_name = parameter["$ref"].split("/")[-1:][0]
            data = openapi_refs.get(ref_name)
            tmp_param = gen_param(data)
        else:
            # Handle inline parameter
            tmp_param = gen_param(parameter)

        if tmp_param not in params:
            params.append(tmp_param)
    return params


def _process_body_params(request_body: object, content_type: str = "application/json"):
    """
    Process request body parameters from OpenAPI definition.

    Args:
        request_body: OpenAPI request body object
        content_type: MIME type of the request body

    Returns:
        dict: Schema properties for the request body
    """
    schema = request_body["content"][content_type]["schema"]
    properties = {}

    if schema.get("$ref"):
        # Handle schema reference
        ref_name = schema["$ref"].split("/")[-1:][0]
        properties = openapi_schemas.get(ref_name).get("properties", {})
    else:
        # Handle inline schema
        properties = schema.get("properties", {})
    return properties


def _process_endpoint(
    endpoint_data: object, endpoint_path: str, folder_path: str, file_name: str
):
    """
    Process a single API endpoint and generate corresponding functions.

    Args:
        endpoint_data: OpenAPI endpoint definition
        endpoint_path: API endpoint path
        folder_path: Output folder path
        file_name: Output file name

    Returns:
        int: Number of functions generated
    """
    count = 0
    path_params = []
    query_params = []
    operation_id = ""
    tags = []

    # Process path parameters (shared across all HTTP methods)
    path_params = _process_path_params(endpoint_data.get("parameters", []))

    # Process GET method
    if endpoint_data.get("get") and not endpoint_data.get("get", {}).get("deprecated"):
        query_params = _process_query_params(endpoint_data["get"].get("parameters", []))
        operation_id = endpoint_data["get"]["operationId"]
        tags = endpoint_data["get"]["tags"]
        _create_get(
            operation_id,
            tags,
            endpoint_path,
            path_params,
            query_params,
            folder_path,
            f"{file_name}.py",
        )
        count += 1

    # Process DELETE method
    if endpoint_data.get("delete") and not endpoint_data.get("delete", {}).get(
        "deprecated"
    ):
        query_params = _process_query_params(
            endpoint_data["delete"].get("parameters", [])
        )
        operation_id = endpoint_data["delete"]["operationId"]
        tags = endpoint_data["delete"]["tags"]
        _create_delete(
            operation_id,
            tags,
            endpoint_path,
            path_params,
            query_params,
            folder_path,
            f"{file_name}.py",
        )
        count += 1

    # Process POST method
    if endpoint_data.get("post") and not endpoint_data.get("post", {}).get(
        "deprecated"
    ):
        operation_id = endpoint_data["post"]["operationId"]
        tags = endpoint_data["post"]["tags"]
        request_body = endpoint_data["post"].get("requestBody")

        if request_body:
            # Handle multipart form data (file uploads)
            if "multipart/form-data" in request_body.get("content"):
                _create_post_file(
                    operation_id,
                    tags,
                    endpoint_path,
                    path_params,
                    folder_path,
                    _process_body_params(request_body, "multipart/form-data"),
                    f"{file_name}.py",
                )
            # Handle JSON request body
            if "application/json" in request_body.get("content"):
                _create_post(
                    operation_id,
                    tags,
                    endpoint_path,
                    path_params,
                    folder_path,
                    f"{file_name}.py",
                )
        else:
            # Handle POST without request body
            _create_post_empty(
                operation_id,
                tags,
                endpoint_path,
                path_params,
                folder_path,
                f"{file_name}.py",
            )
        count += 1

    # Process PUT method
    if endpoint_data.get("put") and not endpoint_data.get("put", {}).get("deprecated"):
        operation_id = endpoint_data["put"]["operationId"]
        tags = endpoint_data["put"]["tags"]
        _create_put(
            operation_id,
            tags,
            endpoint_path,
            path_params,
            folder_path,
            f"{file_name}.py",
        )
        count += 1

    return count


def _is_totaly_deprecated(endpoint_data: object) -> bool:
    """
    Check if an endpoint is completely deprecated (all HTTP methods are deprecated).

    Args:
        endpoint_data: OpenAPI endpoint definition

    Returns:
        bool: True if all methods are deprecated, False otherwise
    """
    for crud in ["get", "post", "put", "delete"]:
        if endpoint_data.get(crud, {}):
            if not endpoint_data[crud].get("deprecated"):
                return False
    return True


##################################
# Main execution functions


def start():
    """
    Main function to process all API endpoints and generate Python functions.

    Returns:
        tuple: (endpoint_count, api_count) - number of endpoints and functions processed
    """
    endpoint_count = 0
    api_count = 0
    out = sys.stdout
    count = len(openapi_paths)
    size = 60
    i = 0

    def show(j) -> None:
        """Display progress bar."""
        x = int(size * j / count)
        out.write("".ljust(0))
        out.write(f"[{'█' * x}{'.' * (size - x)}]")
        out.write(f"{j}/{count}\r".rjust(9))
        out.flush()

    # Process each endpoint in the OpenAPI specification
    for endpoint_path in openapi_paths:
        if endpoint_path.startswith("/api"):
            endpoint_data = openapi_paths[endpoint_path]
            if not _is_totaly_deprecated(endpoint_data):
                # Initialize folder structure and process endpoint
                folder_path, file_name = _init_endpoint(endpoint_path)
                api_count += _process_endpoint(
                    endpoint_data, endpoint_path, folder_path, file_name
                )
                endpoint_count += 1
        show(i + 1)
        i += 1

    out.write("\n")
    out.flush()
    return endpoint_count, api_count


############################################################################################################
############################################################################################################
# Script entry point

# Get version from command line argument
version = sys.argv[1]

# Clean up existing API folder
if os.path.exists(f"{root_folder}/{root_api_folder}"):
    shutil.rmtree(f"{root_folder}/{root_api_folder}")

# Load OpenAPI specification
with open(openapi_file, "r") as f:
    openapi_json = yaml.load(f, Loader=yaml.loader.SafeLoader)

# Extract OpenAPI components
openapi_paths = openapi_json.get("paths")
openapi_refs = openapi_json.get("components", {}).get("parameters")
openapi_schemas = openapi_json.get("components", {}).get("schemas")

# Generate API functions
endpoint_count, api_count = start()

# Print summary
print(f"Endpoint: {endpoint_count}")
print(f"API     : {api_count}")
