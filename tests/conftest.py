# tests/conftest.py
"""
Pytest configuration and shared fixtures.

This file contains fixtures that are shared across all tests.
Using pytest-mock and responses libraries for better testing patterns.
"""

import json
import os
import sys
from unittest.mock import Mock, patch

import pytest
import responses

# Add src to path for testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from mistapi import APISession
from mistapi.__api_response import APIResponse
from mistapi.__models.privilege import Privileges

# Test data - prefer real-looking data over mocks where possible
TEST_ORG_ID = "203d3d02-dbc0-4c1b-9f41-76896a3330f4"
TEST_SITE_ID = "f5fcbee5-fbca-45b3-8bf1-1619ede87879"
TEST_DEVICE_ID = "5c5b350e0001"
TEST_API_TOKEN = "abcdef0123456789abcdef0123456789abcdef01"
TEST_HOST = "api.mist.com"


@pytest.fixture
def org_id():
    """Standard test organisation ID"""
    return TEST_ORG_ID


@pytest.fixture
def site_id():
    """Standard test site ID"""
    return TEST_SITE_ID


@pytest.fixture
def device_id():
    """Standard test device ID"""
    return TEST_DEVICE_ID


@pytest.fixture
def api_token():
    """Standard test API token"""
    return TEST_API_TOKEN


@pytest.fixture
def test_host():
    """Standard test host"""
    return TEST_HOST


@pytest.fixture
def sample_org_data():
    """Sample organisation data matching real API responses"""
    return {
        "id": TEST_ORG_ID,
        "name": "Test Organisation",
        "created_time": 1234567890,
        "modified_time": 1234567890,
        "orggroup_ids": [],
        "alarmtemplate_id": None,
        "allow_mist": True,
        "session_expiry": 1440,
    }


@pytest.fixture
def sample_device_data():
    """Sample device data matching real API responses"""
    return {
        "id": TEST_DEVICE_ID,
        "mac": "5c5b350e0001",
        "model": "AP41",
        "type": "ap",
        "name": "Test AP",
        "site_id": TEST_SITE_ID,
        "org_id": TEST_ORG_ID,
        "created_time": 1234567890,
        "modified_time": 1234567890,
        "serial": "TEST123456789",
    }


@pytest.fixture
def sample_privileges():
    """Sample user privileges as raw data (list of dicts)"""
    return [
        {
            "scope": "org",
            "role": "admin",
            "org_id": TEST_ORG_ID,
            "name": "Test Organisation",
        },
        {
            "scope": "site",
            "role": "write",
            "site_id": TEST_SITE_ID,
            "org_id": TEST_ORG_ID,
            "name": "Test Site",
        },
    ]


@pytest.fixture
def sample_user_data(sample_privileges):
    """Sample user data from /api/v1/self"""
    return {
        "id": "user-id-123",
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User",
        "privileges": sample_privileges,  # Raw list, not Privileges object
        "two_factor_required": False,
        "two_factor_passed": True,
        "via_sso": False,
        "tags": [],
    }


@pytest.fixture
def isolated_session():
    """
    Completely isolated APISession that doesn't inherit environment settings.
    This prevents test contamination from environment variables.
    """
    # Mock environment variables to ensure clean state
    with patch.dict(os.environ, {}, clear=True):
        # Mock requests.session to prevent actual HTTP calls
        with patch("mistapi.__api_session.requests.session") as mock_session_class:
            mock_session_instance = Mock()
            mock_session_instance.headers = {}
            mock_session_instance.proxies = {}
            mock_session_instance.cookies = {}
            mock_session_class.return_value = mock_session_instance

            # Create session with minimal setup
            session = APISession(console_log_level=50)  # Suppress output
            session._session = mock_session_instance
            return session


@pytest.fixture
def basic_session(isolated_session, test_host, api_token):
    """Basic APISession with host and token configured"""
    isolated_session.set_cloud(test_host)
    # Mock token validation to prevent HTTP calls
    with patch("mistapi.__api_session.requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "privileges": [{"scope": "org", "org_id": "test-org", "role": "admin"}]
        }
        mock_get.return_value = mock_response
        isolated_session.set_api_token(api_token)
    return isolated_session


@pytest.fixture
def authenticated_session(basic_session, sample_user_data):
    """Authenticated APISession with sample user data"""
    basic_session._authenticated = True
    basic_session._cloud_uri = TEST_HOST
    basic_session._apitoken = [TEST_API_TOKEN]
    basic_session._apitoken_index = 0

    # Set user data as it would be after successful login
    for key, value in sample_user_data.items():
        if key == "privileges":
            # Create Privileges object from raw list
            basic_session.privileges = Privileges(value)
        elif key == "tags":
            basic_session.tags = value.copy()
        else:
            setattr(basic_session, key, value)

    return basic_session


@pytest.fixture
def api_response_factory():
    """Factory for creating APIResponse objects for testing"""

    def _create_response(
        status_code=200, data=None, headers=None, url="https://api.mist.com/api/v1/test"
    ):
        # Create a mock response object that behaves like requests.Response
        mock_response = Mock()
        mock_response.status_code = status_code
        mock_response.headers = headers or {}
        mock_response.content = json.dumps(data or {}).encode()
        mock_response.json.return_value = data or {}

        return APIResponse(response=mock_response, url=url)

    return _create_response


# Responses fixtures for HTTP mocking
@pytest.fixture
def responses_mock():
    """
    Activate responses mock for HTTP requests.

    This is better than unittest.mock for HTTP testing as it:
    - Actually intercepts HTTP calls
    - Provides realistic request/response cycle
    - Easier to configure than complex mocks
    """
    with responses.RequestsMock() as rsps:
        yield rsps


@pytest.fixture
def mock_successful_login(responses_mock):
    """Mock successful login flow"""
    responses_mock.add(
        responses.POST,
        f"https://{TEST_HOST}/api/v1/login",
        json={"status": "success"},
        status=200,
    )
    return responses_mock


@pytest.fixture
def mock_self_endpoint(responses_mock, sample_user_data):
    """Mock /api/v1/self endpoint"""
    responses_mock.add(
        responses.GET,
        f"https://{TEST_HOST}/api/v1/self",
        json=sample_user_data,
        status=200,
    )
    return responses_mock


@pytest.fixture
def mock_org_devices(responses_mock, sample_device_data):
    """Mock org devices endpoint"""
    devices_response = {
        "results": [sample_device_data],
        "limit": 100,
        "page": 1,
        "total": 1,
    }

    responses_mock.add(
        responses.GET,
        f"https://{TEST_HOST}/api/v1/orgs/{TEST_ORG_ID}/devices",
        json=devices_response,
        status=200,
    )
    return responses_mock


# Parametrised fixtures for testing different scenarios
@pytest.fixture(params=[200, 400, 401, 403, 404, 500])
def http_status_codes(request):
    """Different HTTP status codes for testing error handling"""
    return request.param


@pytest.fixture(params=["api.mist.com", "api.eu.mist.com", "api.gc1.mist.com"])
def mist_hosts(request):
    """Different Mist cloud hosts"""
    return request.param


# Helper fixtures for file operations
@pytest.fixture
def tmp_env_file(tmp_path):
    """Create a temporary .env file for testing"""
    env_file = tmp_path / ".env"
    env_content = f"""
MIST_HOST={TEST_HOST}
MIST_APITOKEN={TEST_API_TOKEN}
MIST_USER=test@example.com
MIST_PASSWORD=test_password
CONSOLE_LOG_LEVEL=30
LOGGING_LOG_LEVEL=20
HTTPS_PROXY=http://proxy:8080
"""
    env_file.write_text(env_content)
    return str(env_file)


# Session configuration to prevent test interference
@pytest.fixture(autouse=True)
def isolate_env_vars():
    """Automatically isolate environment variables for each test"""
    # Store original environment
    original_env = os.environ.copy()

    # Clear mistapi-related environment variables
    mist_vars = [var for var in os.environ.keys() if var.startswith("MIST_")]
    for var in mist_vars:
        os.environ.pop(var, None)

    yield

    # Restore original environment
    os.environ.clear()
    os.environ.update(original_env)


# Markers for test categorisation
def pytest_configure(config) -> None:
    """Configure custom markers"""
    config.addinivalue_line("markers", "unit: Unit tests")
    config.addinivalue_line("markers", "integration: Integration tests")
    config.addinivalue_line("markers", "slow: Slow tests")
    config.addinivalue_line("markers", "auth: Authentication tests")
    config.addinivalue_line("markers", "api: API endpoint tests")
