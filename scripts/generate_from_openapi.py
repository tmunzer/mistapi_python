import os
import re
import shutil
import sys

import yaml

# Configuration constants
OPENAPI_FILE = "./mist_openapi/mist.openapi.yaml"
OPENAPI_JSON = None
ROOT_FOLDER = "./src/mistapi/"
ROOT_API_FOLDER = "api"

# Type mapping from OpenAPI to Python types
var_translation = {
    "integer": "int",
    "number": "float",
    "string": "str",
    "array": "list",
    "boolean": "bool",
}

DEPRECATED_METHODS = {
    "getSiteSleSummary": {
        "new_operation_id": "getSiteSleSummaryTrend",
        "version_deprecated": "0.59.2",
        "version_final": "0.65.0",
    },
    "getSiteSleClassifierDetails": {
        "new_operation_id": "getSiteSleClassifierSummaryTrend",
        "version_deprecated": "0.59.2",
        "version_final": "0.65.0",
    },
}

# Template for __init__.py files in generated packages
INIT_TEMPLATE = """'''
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
'''

from {path_import} import (
{function_imports}
)

__all__ = [
{all_imports}
]
"""

# Template for individual Python API files
FILE_TEMPLATE = """'''
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
'''

{imports}
{functions}
"""

# Template for function docstrings
DESCRIPTION_TEMPLATE = """    \"\"\"
    API doc: https://www.juniper.net/documentation/us/en/software/mist/api/http/api/{tags_in_url}/{operation}

    PARAMS
    -----------
    mistapi.APISession : mist_session
        mistapi session including authentication and Mist host information
    {path_params_desc}{query_params_desc}{body_params_desc}
    RETURN
    -----------
    mistapi.APIResponse
        response from the API call
    \"\"\"
    """

# Template for deprecated GET functions (backward compatibility)
FUNCTION_GET_DEPRECATED_TEMPLATE = """
@deprecation.deprecated(deprecated_in="{version_deprecated}", removed_in="{version_final}", current_version="{version_current}", details="function replaced with {operation_id}")
def {old_operation_id}(mist_session: _APISession{code_path_params}{code_query_params}) -> _APIResponse:
{code_desc}
    uri = {uri}{query_code}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    """

# Template for GET method functions
FUNCTION_GET_TEMPLATE = """
def {operation_id}(mist_session: _APISession{code_path_params}{code_query_params}) -> _APIResponse:
{code_desc}
    uri = {uri}{query_code}
    resp = mist_session.mist_get(uri=uri, query=query_params)
    return resp
    """

# Template for DELETE method functions
FUNCTION_DELETE_TEMPLATE = """
def {operation_id}(mist_session: _APISession{code_path_params}{code_query_params}) -> _APIResponse:
{code_desc}
    uri = {uri}{query_code}
    resp = mist_session.mist_delete(uri=uri, query=query_params)
    return resp
    """

# Template for PUT method functions with JSON body
FUNCTION_PUT_TEMPLATE = """
def {operation_id}(mist_session: _APISession{code_path_params}, body:dict) -> _APIResponse:
{code_desc}
    uri = {uri}
    resp = mist_session.mist_put(uri=uri, body=body)
    return resp
    """

# Template for POST method functions without request body
FUNCTION_POST_EMPTY_TEMPLATE = """
def {operation_id}(mist_session: _APISession{code_path_params}) -> _APIResponse:
{code_desc}
    uri = {uri}
    resp = mist_session.mist_post(uri=uri)
    return resp
    """

# Template for POST method functions with JSON body
FUNCTION_POST_BODY_TEMPLATE = """
def {operation_id}(mist_session: _APISession{code_path_params}, body:dict|list) -> _APIResponse:
{code_desc}
    uri = {uri}
    resp = mist_session.mist_post(uri=uri, body=body)
    return resp
    """

# Template for POST method functions with file upload (multipart/form-data)
FUNCTION_POST_FILE_TEMPLATE = """
def {operation_id}(mist_session: _APISession{code_path_params}{multipart}) -> _APIResponse:
{code_desc}
    multipart_form_data = {{{multipart_form_data}
        }}
    uri = {uri}
    resp = mist_session.mist_post_file(uri=uri, multipart_form_data=multipart_form_data)
    return resp
    """


def keep_deprecated(max_deprecation_version: str, current_version: str) -> bool:
    """
    Determine if deprecated functions should be kept based on version comparison.
    """
    current = current_version.split(".")
    max_version = max_deprecation_version.split(".")

    for i, req in enumerate(max_version):
        if current[int(i)] < req:
            break
        if current[int(i)] > req:
            return False
    return True


def fprint(message: str) -> None:
    """Print a formatted message with left justification to 80 characters."""
    print(f"{message}".ljust(80))


def gen_param(data: dict, openapi_schemas: dict) -> dict:
    """
    Generate parameter dictionary from OpenAPI parameter definition.

    Args:
        data: OpenAPI parameter definition containing name, schema, etc.
        openapi_schemas: Dictionary of OpenAPI schema components for resolving references

    Returns:
        dict: Processed parameter with name, type, description, validation rules, etc.
    """
    tmp = {}
    if data:
        if data["schema"].get("$ref"):
            # Handle parameter with schema reference - resolve the reference
            ref_name = data["schema"]["$ref"].split("/")[-1:][0]
            ref = openapi_schemas.get(ref_name, {})
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
            # Handle inline parameter definition - extract directly from schema
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
# Folder and file management functions


def _gen_imports(has_deprecated: bool) -> str:
    """
    Generate import statements for API function files.

    Args:
        has_deprecated: Whether the file contains deprecated functions requiring deprecation module

    Returns:
        str: Import statements for the file
    """
    if has_deprecated:
        return """from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse
import deprecation
"""
    return """from mistapi import APISession as _APISession
from mistapi.__api_response import APIResponse as _APIResponse
"""


def _init_folder(folder_path: str, folder_name: str, import_path: list = []) -> None:
    """
    Initialize folder structure and create basic __init__.py file if needed.

    Args:
        folder_path: Parent directory path where folder should be created
        folder_name: Name of folder to create
        import_path: List of module path components for constructing import statements
    """
    path = os.path.join(folder_path, folder_name)
    init_file = os.path.join(folder_path, "__init__.py")

    if not os.path.exists(path):
        os.makedirs(path)
        import_from = f"mistapi.{'.'.join(import_path)}"
        if import_from.endswith("."):
            import_from = import_from[:-1]
        if folder_path != ROOT_FOLDER:
            # Create basic __init__.py in parent folder if it doesn't exist
            if not os.path.exists(init_file):
                with open(init_file, "w", encoding="utf-8") as f:
                    f.write(f"from {import_from} import *\r\n")


def _gen_folder_and_file_paths(endpoint: str) -> tuple[list[str], str]:
    """
    Generate folder structure and file name from API endpoint path.
    Maps API endpoints to organized Python module structure.

    Args:
        endpoint: API endpoint path (e.g., "/api/v1/orgs/{org_id}/sites")

    Returns:
        tuple: (folder_path_parts, file_name) - list of folder names and target file name
    """
    endpoint_path = endpoint.split("/")

    # Remove empty strings and path variables (e.g., {org_id}) from endpoint
    tmp = []
    installer = False
    for part in endpoint_path:
        if part == "installer":
            installer = True
        if part != "" and not part.startswith("{"):
            tmp.append(part)
    endpoint_path = tmp

    # Determine folder structure based on endpoint depth and special cases
    if installer and len(endpoint_path) > 4:
        # Special handling for installer endpoints with deeper nesting
        folder_path_parts = endpoint_path[0:4]
        file_name = endpoint_path[4:5][0]
    elif len(endpoint_path) > 3:
        # Standard case: use first 3 parts for folders, 4th for file
        folder_path_parts = endpoint_path[0:3]
        file_name = endpoint_path[3:4][0]
    else:
        # Shallow endpoints: use available parts for folders, last for file
        folder_path_parts = endpoint_path[0:3]
        file_name = endpoint_path[2:3][0]

    # Special case for 128routers endpoint (renamed for Python compatibility)
    if file_name == "128routers":
        file_name = "ssr"
    return folder_path_parts, file_name


def _init_endpoint(endpoint: str) -> tuple[str, str]:
    """
    Initialize complete folder structure and determine file path for an API endpoint.

    Args:
        endpoint: API endpoint path (e.g., "/api/v1/orgs/{org_id}/sites")

    Returns:
        tuple: (full_folder_path, file_name) - complete path to target folder and file name
    """
    full_folder_path = ROOT_FOLDER
    full_import_path: list[str] = []
    folder_path_parts, file_name = _gen_folder_and_file_paths(endpoint)

    # Create nested folder structure progressively
    for folder_path_part in folder_path_parts:
        _init_folder(full_folder_path, folder_path_part, full_import_path)
        full_folder_path = os.path.join(full_folder_path, folder_path_part)
        full_import_path.append(folder_path_part)

    return full_folder_path, file_name


##################################
# Function generation utilities


def _gen_code_params_default_value(param: dict) -> str:
    """
    Generate default value code for function parameters based on OpenAPI specification.

    Args:
        param: Parameter definition with type, required flag, and default info

    Returns:
        str: Code string for default value (e.g., '=None', '="default"', '=True')
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
            # TODO: Fix union type syntax for Python 3.9 compatibility
            code_default = "|None=None"
            # code_default = "=None"
    return code_default


def _gen_code_params(endpoint_params: list, operation_id: str) -> tuple[str, str]:
    """
    Generate function parameter code and corresponding documentation.

    Args:
        endpoint_params: List of parameter definitions from OpenAPI
        operation_id: OpenAPI operation ID for error reporting

    Returns:
        tuple: (code_params, code_params_desc) - parameter signature and documentation
    """
    code_params = ""
    code_params_desc = ""

    for param in endpoint_params:
        ptype_src = param["type"]
        ptype = var_translation.get(ptype_src, "any")

        # Log warning for unknown parameter types
        if ptype == "any":
            fprint(
                f"Unable to convert var type {ptype_src} (opid: {operation_id}, param {param['name']})"
            )

        # Build parameter signature with type annotations
        code_params += f", {param['name']}: {ptype}"

        # Build parameter documentation for docstring
        code_params_desc += f"\r\n    {param['name']} : {ptype}"
        if param.get("enum"):
            # Format enum values as set notation for documentation
            code_params_desc += str(param["enum"]).replace("[", "{").replace("]", "}")
        if param.get("default"):
            code_params_desc += f", default: {param['default']}"
        if param.get("description"):
            code_params_desc += f"\r\n      {param['description']}"

        # Add default value to parameter signature
        code_params += _gen_code_params_default_value(param)

    return code_params, code_params_desc


def _gen_description_property(property_data: dict) -> tuple[str, str]:
    """
    Generate property description for multipart form data documentation.

    Args:
        property_data: Property definition with type, enum, default, description keys

    Returns:
        tuple: (property_type, property_desc) - formatted type info and description
    """
    property_type = property_data["property_type"]
    property_desc = ""

    if property_data.get("property_enum"):
        # Format enum as set notation for documentation
        property_type = (
            str(property_data["property_enum"]).replace("[", "{").replace("]", "}")
        )
    if property_data.get("property_default"):
        property_type += f", default: {property_data['property_default']}"
    if property_data.get("property_desc"):
        property_desc = f"\r\n        {property_data['property_desc']}"

    return property_type, property_desc


def _process_tags(tags: list) -> str:
    """
    Process OpenAPI tags to generate URL path for API documentation links.

    Args:
        tags: List of OpenAPI tags (usually contains one tag with category info)

    Returns:
        str: Processed tag path for documentation URL (e.g., "orgs/sites")
    """
    result = []
    splitted_tag = tags[0].split(" ", 1)
    result.append(splitted_tag[0].strip().lower())

    if len(splitted_tag) > 1:
        # Process subcategories separated by " - "
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
) -> str:
    """
    Generate complete function docstring with API documentation link and parameter descriptions.

    Args:
        operation_id: OpenAPI operation ID for generating documentation URL
        tags: OpenAPI tags for categorizing API documentation
        desc_path_params: Path parameters documentation string
        desc_query_params: Query parameters documentation string
        with_body: Whether function accepts JSON body parameter
        multipart_form_data: Dictionary of multipart form data parameters

    Returns:
        str: Complete formatted docstring
    """
    # Convert camelCase operation ID to kebab-case URL format
    r = "(?<!^)(?=[A-Z])"
    operation = re.sub(r, "-", operation_id).lower()
    tags_in_url = _process_tags(tags)
    path_params_desc = ""
    query_params_desc = ""
    body_params_desc = ""

    # Add path parameters section if present
    if desc_path_params:
        path_params_desc = f"""
    PATH PARAMS
    -----------{desc_path_params}
    """

    # Add query parameters section if present
    if desc_query_params:
        query_params_desc = f"""
    QUERY PARAMS
    ------------{desc_query_params}
    """

    # Add body parameters section for JSON body or multipart data
    if with_body or multipart_form_data:
        body_params_desc = """
    BODY PARAMS
    -----------"""

        if with_body:
            body_params_desc += "\r\n    body : dict\r\n        JSON object to send to Mist Cloud (see API doc above for more details)"

        # Add multipart form data parameters documentation
        if multipart_form_data:
            for key in multipart_form_data:
                if key in ["csv", "file"]:
                    # Special handling for file upload parameters
                    body_params_desc += f"\r\n    {key} : {multipart_form_data[key]['property_type']}\r\n        path to the file to upload. {multipart_form_data[key]['property_desc']}"
                else:
                    property_type, property_desc = _gen_description_property(
                        multipart_form_data[key]
                    )
                    body_params_desc += (
                        f"\r\n    {key} : {property_type}{property_desc}"
                    )

                    # Add nested object properties documentation
                    if multipart_form_data[key]["property_child"]:
                        for child in multipart_form_data[key]["property_child"]:
                            property_type, property_desc = _gen_description_property(
                                multipart_form_data[key]["property_child"][child]
                            )
                            body_params_desc += (
                                f"\r\n        {child} : {property_type}{property_desc}"
                            )
        body_params_desc += """
    """

    # Generate complete docstring using template
    description = DESCRIPTION_TEMPLATE.format(
        tags_in_url=tags_in_url,
        operation=operation,
        path_params_desc=path_params_desc,
        query_params_desc=query_params_desc,
        body_params_desc=body_params_desc,
    )
    return description


def _gen_query_code(query_params: list) -> str:
    """
    Generate code for building query parameters dictionary from function arguments.

    Args:
        query_params: List of query parameter definitions

    Returns:
        str: Code block for constructing query_params dictionary
    """
    code = "\r\n    query_params:dict[str, str]={}"
    if query_params:
        for param in query_params:
            # Only add parameter to query dict if it has a value (truthy check)
            code += f'\r\n    if {param["name"]}:\r\n        query_params["{param["name"]}"]=str({param["name"]})'
    return code


def _gen_uri(endpoint_path: str) -> str:
    """
    Generate URI string for API request, handling path parameter substitution.

    Args:
        endpoint_path: API endpoint path with possible path variables (e.g., "/api/v1/orgs/{org_id}")

    Returns:
        str: Formatted URI string (f-string if variables present, regular string otherwise)
    """
    if "{" in endpoint_path:
        # Use f-string for path parameter substitution
        return f'f"{endpoint_path}"'
    # Use regular string for static paths
    return f'"{endpoint_path}"'


########
# HTTP method function generators (CRUD operations)


def _create_get_deprecated(
    operation_id: str,
    tags: list,
    new_operation_id: str,
    version_deprecated: str,
    version_final: str,
    endpoint_path: str,
    path_params: list,
    query_params: list,
) -> str:
    """
    Create deprecated version of GET functions for backward compatibility.

    Args:
        operation_id: Current OpenAPI operation ID (DeviceEvents*)
        endpoint_path: API endpoint path
        path_params: Path parameters list
        query_params: Query parameters list

    Returns:
        str: Generated deprecated function code
    """
    code = ""
    if not keep_deprecated(version_final, VERSION):
        print(f"Skipping deprecated function {operation_id} as per version settings.")
        return code
    code_path_params, desc_path_params = _gen_code_params(path_params, operation_id)
    code_query_params, desc_query_params = _gen_code_params(query_params, operation_id)
    code_query = _gen_query_code(query_params)
    code_desc = _gen_description(
        operation_id, tags, desc_path_params, desc_query_params
    )

    # Generate old operation ID for the deprecated function
    code += FUNCTION_GET_DEPRECATED_TEMPLATE.format(
        version_deprecated=version_deprecated,
        version_final=version_final,
        version_current=VERSION,
        operation_id=new_operation_id,
        old_operation_id=operation_id,
        code_path_params=code_path_params,
        code_query_params=code_query_params,
        code_desc=code_desc,
        uri=_gen_uri(endpoint_path),
        query_code=code_query,
    )
    return code


def _create_get(
    operation_id: str,
    tags: list,
    endpoint_path: str,
    path_params: list,
    query_params: list,
) -> tuple[str, bool]:
    """
    Generate GET method function with optional deprecated version for compatibility.

    Args:
        operation_id: OpenAPI operation ID
        tags: OpenAPI tags for documentation
        endpoint_path: API endpoint path
        path_params: Path parameters list
        query_params: Query parameters list

    Returns:
        tuple: (generated_code, has_deprecated_function)
    """
    code = ""
    has_deprecated = False
    if DEPRECATED_METHODS.get(operation_id):
        code += _create_get_deprecated(
            operation_id,
            tags,
            DEPRECATED_METHODS[operation_id]["new_operation_id"],
            DEPRECATED_METHODS[operation_id]["version_deprecated"],
            DEPRECATED_METHODS[operation_id]["version_final"],
            endpoint_path,
            path_params,
            query_params,
        )
        if code:
            has_deprecated = True

    # Generate main function parameters and documentation
    code_path_params, desc_path_params = _gen_code_params(path_params, operation_id)
    code_query_params, desc_query_params = _gen_code_params(query_params, operation_id)
    code_query = _gen_query_code(query_params)
    code_desc = _gen_description(
        operation_id, tags, desc_path_params, desc_query_params
    )

    # Generate main GET function code
    code += FUNCTION_GET_TEMPLATE.format(
        operation_id=operation_id,
        code_path_params=code_path_params,
        code_query_params=code_query_params,
        code_desc=code_desc,
        uri=_gen_uri(endpoint_path),
        query_code=code_query,
    )
    return code, has_deprecated


def _create_delete(
    operation_id: str,
    tags: list,
    endpoint_path: str,
    path_params: list,
    query_params: list,
) -> str:
    """
    Generate DELETE method function.

    Args:
        operation_id: OpenAPI operation ID
        tags: OpenAPI tags for documentation
        endpoint_path: API endpoint path
        path_params: Path parameters list
        query_params: Query parameters list

    Returns:
        str: Generated DELETE function code
    """
    code = ""
    code_path_params, desc_path_params = _gen_code_params(path_params, operation_id)
    code_query_params, desc_query_params = _gen_code_params(query_params, operation_id)
    code_query = _gen_query_code(query_params)
    code_desc = _gen_description(
        operation_id, tags, desc_path_params, desc_query_params
    )

    code += FUNCTION_DELETE_TEMPLATE.format(
        operation_id=operation_id,
        code_path_params=code_path_params,
        code_query_params=code_query_params,
        code_desc=code_desc,
        uri=_gen_uri(endpoint_path),
        query_code=code_query,
    )

    return code


def _create_post_empty(
    operation_id: str,
    tags: list,
    endpoint_path: str,
    path_params: list,
) -> str:
    """
    Generate POST method function without request body (empty POST).

    Args:
        operation_id: OpenAPI operation ID
        tags: OpenAPI tags for documentation
        endpoint_path: API endpoint path
        path_params: Path parameters list

    Returns:
        str: Generated POST function code
    """
    code = ""
    code_path_params, desc_path_params = _gen_code_params(path_params, operation_id)
    code_desc = _gen_description(operation_id, tags, desc_path_params)

    code += FUNCTION_POST_EMPTY_TEMPLATE.format(
        operation_id=operation_id,
        code_path_params=code_path_params,
        code_desc=code_desc,
        uri=_gen_uri(endpoint_path),
    )

    return code


def _create_post(
    operation_id: str,
    tags: list,
    endpoint_path: str,
    path_params: list,
) -> str:
    """
    Generate POST method function with JSON request body.

    Args:
        operation_id: OpenAPI operation ID
        tags: OpenAPI tags for documentation
        endpoint_path: API endpoint path
        path_params: Path parameters list

    Returns:
        str: Generated POST function code
    """
    code = ""
    code_path_params, desc_path_params = _gen_code_params(path_params, operation_id)
    code_desc = _gen_description(operation_id, tags, desc_path_params, with_body=True)

    code += FUNCTION_POST_BODY_TEMPLATE.format(
        operation_id=operation_id,
        code_path_params=code_path_params,
        code_desc=code_desc,
        uri=_gen_uri(endpoint_path),
    )

    return code


def _process_multipart_json(properties: dict) -> dict:
    """
    Process multipart form data properties into structured format for code generation.
    Recursively handles nested object properties.

    Args:
        properties: OpenAPI schema properties for multipart data

    Returns:
        dict: Processed multipart form data structure with type info and descriptions
    """
    multipart_form_data = {}
    for key in properties:
        property_type = "dict"  # Default type
        property_default = properties[key].get("default", None)
        property_enum = properties[key].get("enum", None)
        property_child = None

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
                property_type = "str"  # File paths are strings
            case "object":
                property_type = "dict"
                # Recursively process nested object properties
                if properties[key].get("properties"):
                    property_child = _process_multipart_json(
                        properties[key]["properties"]
                    )

        multipart_form_data[key] = {
            "property_type": property_type,
            "property_desc": properties[key].get("description", ""),
            "property_default": property_default,
            "property_enum": property_enum,
            "property_child": property_child,
        }
    return multipart_form_data


def _create_post_file(
    operation_id: str,
    tags: list,
    endpoint_path: str,
    path_params: list,
    properties: dict,
) -> str:
    """
    Generate POST method function for file uploads using multipart/form-data.

    Args:
        operation_id: OpenAPI operation ID
        tags: OpenAPI tags for documentation
        endpoint_path: API endpoint path
        path_params: Path parameters list
        properties: Multipart form properties from OpenAPI schema

    Returns:
        str: Generated POST file upload function code
    """
    code = ""
    code_path_params, desc_path_params = _gen_code_params(path_params, operation_id)
    multipart_form_data_parameters = _process_multipart_json(properties)
    code_desc = _gen_description(
        operation_id,
        tags,
        desc_path_params,
        multipart_form_data=multipart_form_data_parameters,
    )

    # Build function signature with multipart parameters
    multipart = ""
    for key, value in multipart_form_data_parameters.items():
        multipart += f", {key}:{value['property_type']}|None=None"

    # Build multipart form data dictionary for function body
    multipart_form_data = ""
    for key in multipart_form_data_parameters:
        multipart_form_data += f"""
        "{key}":{key},"""

    code += FUNCTION_POST_FILE_TEMPLATE.format(
        operation_id=f"{operation_id}File",  # Append "File" to distinguish from regular POST
        code_path_params=code_path_params,
        code_desc=code_desc,
        multipart=multipart,
        multipart_form_data=multipart_form_data,
        uri=_gen_uri(endpoint_path),
    )

    return code


def _create_put(
    operation_id: str,
    tags: list,
    endpoint_path: str,
    path_params: list,
) -> str:
    """
    Generate PUT method function with JSON request body.

    Args:
        operation_id: OpenAPI operation ID
        tags: OpenAPI tags for documentation
        endpoint_path: API endpoint path
        path_params: Path parameters list

    Returns:
        str: Generated PUT function code
    """
    code = ""
    code_path_params, desc_path_params = _gen_code_params(path_params, operation_id)
    code_desc = _gen_description(operation_id, tags, desc_path_params, with_body=True)

    code += FUNCTION_PUT_TEMPLATE.format(
        operation_id=operation_id,
        code_path_params=code_path_params,
        code_desc=code_desc,
        uri=_gen_uri(endpoint_path),
        query_code="",
    )

    return code


########
# Parameter processing functions


def _process_path_params(
    endpoint_params: dict, openapi_refs: dict, openapi_schemas: dict
) -> list:
    """
    Process path parameters from OpenAPI endpoint definition.
    Handles both direct parameter definitions and parameter references.

    Args:
        endpoint_params: List of OpenAPI parameter objects
        openapi_refs: Dictionary of reusable parameter components
        openapi_schemas: Dictionary of schema components for resolving references

    Returns:
        list: Processed path parameters with resolved types and validation rules
    """
    params = []
    for parameter in endpoint_params:
        if parameter.get("$ref"):
            # Handle parameter reference - resolve from components
            ref_name = parameter["$ref"].split("/")[-1:][0]
            data = openapi_refs.get(ref_name, {})
            tmp_param = gen_param(data, openapi_schemas)
        else:
            # Handle inline parameter definition
            tmp_param = gen_param(parameter, openapi_schemas)

        # Avoid duplicate parameters
        if tmp_param not in params:
            params.append(tmp_param)
    return params


def _process_query_params(
    endpoint_params: dict, openapi_refs: dict, openapi_schemas: dict
) -> list:
    """
    Process query parameters from OpenAPI endpoint definition.
    Handles both direct parameter definitions and parameter references.

    Args:
        endpoint_params: List of OpenAPI parameter objects
        openapi_refs: Dictionary of reusable parameter components
        openapi_schemas: Dictionary of schema components for resolving references

    Returns:
        list: Processed query parameters with resolved types and validation rules
    """
    params = []
    for parameter in endpoint_params:
        if parameter.get("$ref"):
            # Handle parameter reference - resolve from components
            ref_name = parameter["$ref"].split("/")[-1:][0]
            data = openapi_refs.get(ref_name, {})
            tmp_param = gen_param(data, openapi_schemas)
        else:
            # Handle inline parameter definition
            tmp_param = gen_param(parameter, openapi_schemas)

        # Avoid duplicate parameters
        if tmp_param not in params:
            params.append(tmp_param)
    return params


def _process_body_params(
    request_body: dict, openapi_schemas: dict, content_type: str = "application/json"
) -> dict:
    """
    Process request body parameters from OpenAPI requestBody definition.
    Extracts schema properties for the specified content type.

    Args:
        request_body: OpenAPI requestBody object
        openapi_schemas: Dictionary of schema components for resolving references
        content_type: MIME type of the request body (default: application/json)

    Returns:
        dict: Schema properties for the request body content type
    """
    schema = request_body["content"][content_type]["schema"]
    properties = {}

    if schema.get("$ref"):
        # Handle schema reference - resolve from components
        ref_name = schema["$ref"].split("/")[-1:][0]
        properties = openapi_schemas.get(ref_name, {}).get("properties", {})
    else:
        # Handle inline schema definition
        properties = schema.get("properties", {})
    return properties


def _process_endpoint(
    endpoint_data: dict, endpoint_path: str, openapi_schemas: dict, openapi_refs: dict
) -> tuple[str, bool, int]:
    """
    Process a single API endpoint and generate corresponding Python functions.
    Handles all HTTP methods (GET, POST, PUT, DELETE) defined for the endpoint.

    Args:
        endpoint_data: OpenAPI endpoint definition with HTTP methods
        endpoint_path: API endpoint path (e.g., "/api/v1/orgs/{org_id}")
        openapi_schemas: Dictionary of schema components
        openapi_refs: Dictionary of parameter components

    Returns:
        tuple: (generated_code, has_deprecated_functions, function_count)
    """
    count = 0
    path_params = []
    query_params = []
    operation_id = ""
    tags = []
    code = ""
    has_deprecated = False

    # Process path parameters (shared across all HTTP methods for this endpoint)
    path_params = _process_path_params(
        endpoint_data.get("parameters", []), openapi_refs, openapi_schemas
    )

    # Process GET method
    if endpoint_data.get(
        "get"
    ):  # and not endpoint_data.get("get", {}).get("deprecated"):
        query_params = _process_query_params(
            endpoint_data["get"].get("parameters", []), openapi_refs, openapi_schemas
        )
        operation_id = endpoint_data["get"]["operationId"]
        tags = endpoint_data["get"]["tags"]
        tmp_code, has_deprecated = _create_get(
            operation_id,
            tags,
            endpoint_path,
            path_params,
            query_params,
        )
        code += tmp_code
        count += 1

    # Process DELETE method
    if endpoint_data.get("delete") and not endpoint_data.get("delete", {}).get(
        "deprecated"
    ):
        query_params = _process_query_params(
            endpoint_data["delete"].get("parameters", []), openapi_refs, openapi_schemas
        )
        operation_id = endpoint_data["delete"]["operationId"]
        tags = endpoint_data["delete"]["tags"]
        code += _create_delete(
            operation_id,
            tags,
            endpoint_path,
            path_params,
            query_params,
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
                code += _create_post_file(
                    operation_id,
                    tags,
                    endpoint_path,
                    path_params,
                    _process_body_params(
                        request_body, openapi_schemas, "multipart/form-data"
                    ),
                )
            # Handle JSON request body
            if "application/json" in request_body.get("content"):
                code += _create_post(
                    operation_id,
                    tags,
                    endpoint_path,
                    path_params,
                )
        else:
            # Handle POST without request body (trigger/action endpoints)
            code += _create_post_empty(
                operation_id,
                tags,
                endpoint_path,
                path_params,
            )
        count += 1

    # Process PUT method
    if endpoint_data.get("put") and not endpoint_data.get("put", {}).get("deprecated"):
        operation_id = endpoint_data["put"]["operationId"]
        tags = endpoint_data["put"]["tags"]
        code += _create_put(
            operation_id,
            tags,
            endpoint_path,
            path_params,
        )
        count += 1

    return code, has_deprecated, count


def _is_totally_deprecated(endpoint_data: dict) -> bool:
    """
    Check if an endpoint is completely deprecated (all HTTP methods are deprecated).

    Args:
        endpoint_data: OpenAPI endpoint definition

    Returns:
        bool: True if all available methods are deprecated, False otherwise
    """
    for crud in ["get", "post", "put", "delete"]:
        if endpoint_data.get(crud, {}):
            operation_id = endpoint_data.get(crud, {}).get("operationId")
            if not endpoint_data[crud].get("deprecated"):
                return False
            elif operation_id and DEPRECATED_METHODS.get(operation_id):
                return False
    return True


def _process_oas(
    openapi_paths: dict,
    openapi_schemas: dict,
    openapi_refs: dict,
) -> tuple[int, int, dict[str, dict[str, str]], list[str]]:
    """
    Process OpenAPI specification paths and generate Python functions for each endpoint.

    Args:
        openapi_paths: Dictionary of OpenAPI paths from specification
        openapi_schemas: Dictionary of schema components
        openapi_refs: Dictionary of parameter components

    Returns:
        tuple: (endpoint_count, api_count, files_code, files_with_deprecated)
            - endpoint_count: Number of endpoints processed
            - api_count: Total number of API functions generated
            - files_code: Dictionary mapping folder paths to file contents
            - files_with_deprecated: List of files containing deprecated functions
    """
    ##############################################################################
    # Initialize counters and output structures
    ##############################################################################
    out = sys.stdout
    endpoint_count = 0
    api_count = 0
    count = len(openapi_paths)
    size = 60  # Progress bar width
    i = 0
    files_code: dict[str, dict[str, str]] = {}
    files_with_deprecated: list[str] = []

    def show(j) -> None:
        """Display progress bar for processing status."""
        x = int(size * j / count)
        out.write("".ljust(0))
        out.write(f"[{'█' * x}{'.' * (size - x)}]")
        out.write(f"{j}/{count}\r".rjust(9))
        out.flush()

    # Process each endpoint in the OpenAPI specification
    for endpoint_path in openapi_paths:
        if endpoint_path.startswith("/api"):  # Only process API endpoints
            endpoint_data = openapi_paths[endpoint_path]
            if not _is_totally_deprecated(endpoint_data):
                # Initialize folder structure and process endpoint
                folder_path, file_name = _init_endpoint(endpoint_path)
                code, has_deprecated, api_count_tmp = _process_endpoint(
                    endpoint_data, endpoint_path, openapi_schemas, openapi_refs
                )
                api_count += api_count_tmp
                if code:
                    # Store generated code for file creation
                    if folder_path not in files_code:
                        files_code[folder_path] = {}
                    if file_name not in files_code[folder_path]:
                        files_code[folder_path][file_name] = ""
                    files_code[folder_path][file_name] += code
                    if has_deprecated:
                        files_with_deprecated.append(file_name)
                endpoint_count += 1
        show(i + 1)
        i += 1
    return endpoint_count, api_count, files_code, files_with_deprecated


def _create_code_files(
    files_code: dict[str, dict[str, str]], files_with_deprecated: list[str]
) -> None:
    """
    Save generated code to Python files with appropriate imports and formatting.

    Args:
        files_code: Dictionary mapping folder paths to file contents
        files_with_deprecated: List of files containing deprecated functions (need deprecation import)
    """
    for folder_path, folder_data in files_code.items():
        for file_name, file_data in folder_data.items():
            file_path = os.path.join(folder_path, f"{file_name}.py")
            with open(file_path, "w", encoding="utf-8") as f:
                imports = _gen_imports(file_name in files_with_deprecated)
                f.write(
                    FILE_TEMPLATE.format(
                        imports=imports,
                        functions=file_data,
                    )
                )


def _ensure_module_in_imports(imports: dict, module: str) -> dict:
    """
    Initialize module entry in imports dictionary structure if not exists.
    Helper function for building nested import structures.

    Args:
        imports: Current imports dictionary
        module: Module name to initialize

    Returns:
        dict: Updated imports dictionary
    """
    if module not in imports["submodules"]:
        imports["submodules"][module] = {
            "submodules": {},
            "function_imports": [],
            "all_imports": [],
        }
    if f"    {module}" not in imports["function_imports"]:
        imports["function_imports"].append(f"    {module}")
    if f'    "{module}"' not in imports["all_imports"]:
        imports["all_imports"].append(f'    "{module}"')
    return imports


def _create_init_file(
    imports: dict, path_import_param: list = [], src_path: str = "./src/"
) -> None:
    """
    Recursively create __init__.py files for the generated module structure.

    Args:
        imports: Nested dictionary structure of imports
        path_import_param: Current import path being processed
        src_path: Source directory path for file creation
    """
    for module, module_data in imports.items():
        path_import = path_import_param.copy()
        path_import.append(module)

        # Recursively process submodules
        if module_data["submodules"]:
            _create_init_file(
                module_data["submodules"],
                path_import,
                os.path.join(src_path, module),
            )

        # Create __init__.py file (except for root mistapi module)
        init_file = os.path.join(src_path, module.replace(".", "/"), "__init__.py")
        if (
            module_data.get("function_imports")
            and init_file != "./src/mistapi/__init__.py"
        ):
            with open(init_file, "w", encoding="utf-8") as f:
                f.write(
                    INIT_TEMPLATE.format(
                        path_import=".".join(path_import),
                        function_imports=",\r\n".join(module_data["function_imports"]),
                        all_imports=",\r\n".join(module_data["all_imports"]),
                    )
                )


def _create_init_files(
    files_code: dict[str, dict[str, str]],
) -> None:
    """
    Create all __init__.py files for the generated package structure.
    Builds proper import statements for each module level.

    Args:
        files_code: Dictionary mapping folder paths to generated file contents
    """
    # Initialize base import structure
    imports: dict = {
        "mistapi": {
            "submodules": {
                "api": {
                    "submodules": {},
                    "function_imports": [],
                    "all_imports": [],
                }
            },
            "function_imports": ["api"],
            "all_imports": ['"api"'],
        }
    }

    # Build nested import structure from generated files
    for folder_path, folder_data in files_code.items():
        # Extract import path from folder structure (skip ./src/mistapi/)
        import_path = folder_path.split("/")[3:]
        tmp = imports["mistapi"]

        # Navigate/create nested structure
        for path in import_path:
            tmp = _ensure_module_in_imports(tmp, path)
            tmp = tmp["submodules"][path]

        # Add file imports to the deepest level
        for file_name in folder_data:
            tmp["function_imports"].append(f"    {file_name}")
            tmp["all_imports"].append(f'    "{file_name}"')

    # Create all __init__.py files
    _create_init_file(imports)


##################################
# Main execution functions


def start(
    openapi_paths: dict,
    openapi_schemas: dict,
    openapi_refs: dict,
) -> None:
    """
    Main function to process OpenAPI specification and generate complete Python API client.
    Orchestrates the entire code generation process.

    Args:
        openapi_paths: Dictionary of OpenAPI paths from specification
        openapi_schemas: Dictionary of schema components
        openapi_refs: Dictionary of parameter components
    """
    out = sys.stdout

    # Process OpenAPI specification and generate code
    endpoint_count, api_count, files_code, files_with_deprecated = _process_oas(
        openapi_paths, openapi_schemas, openapi_refs
    )

    # Write generated code to files
    _create_code_files(files_code, files_with_deprecated)

    # Create package structure with __init__.py files
    _create_init_files(files_code)

    # Clear progress bar and print summary
    out.write("\n")
    out.flush()
    print(f"Endpoint: {endpoint_count}")
    print(f"API     : {api_count}")


############################################################################################################
############################################################################################################
# Script entry point

# Get version from command line argument for deprecation warnings
VERSION = sys.argv[1]

# Clean up existing API folder to ensure fresh generation
if os.path.exists(f"{ROOT_FOLDER}/{ROOT_API_FOLDER}"):
    shutil.rmtree(f"{ROOT_FOLDER}/{ROOT_API_FOLDER}")

# Load OpenAPI specification from YAML file
with open(OPENAPI_FILE, "r") as f_oas:
    OPENAPI_JSON = yaml.load(f_oas, Loader=yaml.loader.SafeLoader)

# Extract OpenAPI components for processing
OPENAPI_PATHS = OPENAPI_JSON.get("paths")
OPENAPI_REFS = OPENAPI_JSON.get("components", {}).get("parameters")
OPENAPI_SCHEMAS = OPENAPI_JSON.get("components", {}).get("schemas")

# Generate complete API client code
start(OPENAPI_PATHS, OPENAPI_SCHEMAS, OPENAPI_REFS)
