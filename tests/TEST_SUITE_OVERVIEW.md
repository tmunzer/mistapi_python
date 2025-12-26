# Test Suite Overview - APISession Tests

## Purpose
Comprehensive unit tests for the `APISession` class focusing on authentication mechanisms and session management without requiring real HTTP calls or external dependencies.

## Test Coverage

### 1. Login/Password Authentication (`TestLoginPasswordAuthentication`)
Tests traditional username/password authentication flows:

- ✅ **test_valid_credentials_success**: Successful login with valid username and password
- ✅ **test_invalid_credentials_failure**: Login failure with invalid credentials (returns 401)
- ✅ **test_login_with_2fa_required**: Login flow with Two-Factor Authentication
- ✅ **test_login_without_credentials**: Login fails when no credentials are provided

### 2. API Token Authentication (`TestAPITokenAuthentication`)
Tests API token-based authentication:

- ✅ **test_single_valid_token_success**: Authentication with a single valid API token
- ✅ **test_single_invalid_token_failure**: Authentication failure with an invalid API token
- ✅ **test_multiple_valid_tokens_success**: Authentication with multiple valid API tokens
- ✅ **test_mixed_tokens_partial_success**: Authentication with mixed valid and invalid tokens (filters out invalid)
- ✅ **test_all_invalid_tokens_failure**: Authentication failure when all tokens are invalid
- ✅ **test_empty_token_string**: Handling of empty token string
- ✅ **test_whitespace_in_tokens**: Whitespace in token strings is properly stripped

### 3. Keyring Authentication (`TestKeyringAuthentication`)
Tests system keyring integration for secure credential storage:

- ✅ **test_valid_keyring_service_success**: Successful authentication using keyring
- ✅ **test_invalid_keyring_service_failure**: Authentication failure with invalid/empty keyring
- ✅ **test_keyring_with_username_password**: Keyring with username/password instead of token

### 4. HashiCorp Vault Integration (`TestVaultIntegration`)
Tests Vault integration for enterprise secret management:

- ✅ **test_valid_vault_configuration**: Successful authentication using HashiCorp Vault
- ✅ **test_vault_connection_failure**: Handling of Vault connection failures
- ✅ **test_vault_empty_credentials**: Handling of empty credentials from Vault

### 5. Environment File Configuration (`TestEnvironmentFileConfiguration`)
Tests environment variable and .env file loading:

- ✅ **test_load_from_env_file**: Loading credentials from environment file
- ✅ **test_env_variables_override**: Environment variables are properly loaded
- ✅ **test_env_variable_type_conversion**: Environment variables converted from strings to proper types

### 6. Session Initialization (`TestSessionInitialization`)
Tests basic session creation and configuration:

- ✅ **test_default_initialization**: Session with default parameters
- ✅ **test_initialization_with_parameters**: Session with explicit parameters
- ✅ **test_proxy_configuration**: Session with proxy configuration
- ✅ **test_log_levels**: Different log level configurations (parametrized)

### 7. Cloud Configuration (`TestCloudConfiguration`)
Tests cloud selection and configuration:

- ✅ **test_set_valid_cloud**: Setting valid cloud URIs (parametrized)
- ✅ **test_set_invalid_cloud**: Setting invalid cloud URI
- ✅ **test_get_cloud**: Getting current cloud configuration
- ✅ **test_select_cloud_interactive**: Interactive cloud selection
- ✅ **test_select_cloud_quit**: Quitting cloud selection

### 8. Authentication Helpers (`TestAuthenticationHelpers`)
Tests helper methods for authentication setup:

- ✅ **test_set_email_direct**: Setting email directly
- ✅ **test_set_email_interactive**: Setting email interactively
- ✅ **test_set_password_direct**: Setting password directly
- ✅ **test_set_password_interactive**: Setting password interactively
- ✅ **test_get_authentication_status_false**: Authentication status when not authenticated
- ✅ **test_get_authentication_status_true**: Authentication status when authenticated

### 9. Privilege Management (`TestPrivilegeManagement`)
Tests user privilege handling:

- ✅ **test_get_privilege_by_org_id_found**: Getting privilege when org ID exists
- ✅ **test_get_privilege_by_org_id_not_found**: Getting privilege when org ID doesn't exist
- ✅ **test_privileges_object_creation**: Privileges object creation and iteration

### 10. Session State (`TestSessionState`)
Tests session state management and representation:

- ✅ **test_str_representation_authenticated**: String representation when authenticated
- ✅ **test_str_representation_unauthenticated**: String representation when not authenticated
- ✅ **test_session_headers_with_token**: Session headers contain authorization token

### 11. Error Handling (`TestErrorHandling`)
Tests error handling and edge cases:

- ✅ **test_login_without_cloud_configured**: Login fails without cloud configured
- ✅ **test_proxy_configurations**: Various proxy configurations (parametrized)
- ✅ **test_invalid_log_level_accepted**: Out-of-range log levels are accepted

### 12. Regression Bugs (`TestRegressionBugs`)
Tests fixes for specific bugs:

- ✅ **test_api_token_is_list_not_boolean**: Ensure _apitoken is always a list
- ✅ **test_privileges_supports_iteration**: Ensure Privileges object supports iteration
- ✅ **test_environment_variables_as_strings**: Environment variables converted from strings properly

## Test Architecture

### Mocking Strategy
- **HTTP Requests**: Using `@responses.activate` decorator to mock HTTP calls
- **System Services**: Mocking keyring and Vault clients
- **User Input**: Mocking `input()` and `getpass()` for interactive prompts
- **Environment**: Using `patch.dict(os.environ)` for clean test isolation

### Fixtures Used
- `isolated_session`: Clean APISession instance with no external dependencies
- `authenticated_session`: Pre-authenticated session with sample data
- `test_host`, `org_id`, `site_id`: Standard test identifiers
- `username`, `password`: Test credentials
- `valid_api_token`, `invalid_api_token`: Test tokens
- `valid_api_tokens`, `mixed_api_tokens`: Multiple token scenarios
- `sample_user_data`, `sample_privileges`: Mock API responses

### Benefits
1. **No Network Calls**: All HTTP requests are mocked
2. **Fast Execution**: Tests run quickly without external dependencies
3. **Isolated**: Each test is independent and doesn't affect others
4. **Comprehensive**: Covers all authentication methods and edge cases
5. **Maintainable**: Clear test organization and naming conventions

## Running Tests

```bash
# Run all tests
pytest tests/unit/test_api_session.py -v

# Run specific test class
pytest tests/unit/test_api_session.py::TestAPITokenAuthentication -v

# Run with coverage
pytest tests/unit/test_api_session.py --cov=src/mistapi --cov-report=html

# Run specific test
pytest tests/unit/test_api_session.py::TestAPITokenAuthentication::test_single_valid_token_success -v
```

## Total Tests: 58

All tests are designed to be:
- **Fast**: No network calls or external dependencies
- **Reliable**: Deterministic results
- **Isolated**: No side effects between tests
- **Comprehensive**: Cover all authentication scenarios
- **Maintainable**: Clear structure and documentation
