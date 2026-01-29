# tests/unit/test_api_session.py
"""
Unit tests for APISession class.

These tests focus on individual methods and use minimal mocking.
They test the logic without requiring real HTTP calls.
"""

import os
from unittest.mock import Mock, patch

import pytest

from mistapi import APISession
from mistapi.__models.privilege import Privileges
from tests.fixtures.test_data import SAMPLE_CLOUDS


class TestAPISessionInitialisation:
    """Test APISession initialisation and basic configuration"""

    def test_default_initialisation(self, isolated_session) -> None:
        """Test APISession with default parameters"""
        # Act & Assert
        assert isolated_session._cloud_uri == ""
        assert isolated_session.email is None
        assert isolated_session._password is None
        assert isolated_session._apitoken == []
        assert not isolated_session._authenticated
        assert isolated_session._console_log_level == 50  # Set in fixture
        assert isolated_session._logging_log_level == 10
        assert isolated_session._show_cli_notif is True

    def test_initialisation_with_parameters(self, api_token, test_host) -> None:
        """Test APISession with all parameters provided"""
        # Arrange
        email = "test@example.com"
        password = "secure_password"

        # Mock environment to ensure clean state
        with patch.dict(os.environ, {}, clear=True):
            with patch("mistapi.__api_session.requests.session"):
                with patch("mistapi.__api_session.requests.get") as mock_get:
                    # Mock successful token validation
                    mock_response = Mock()
                    mock_response.status_code = 200
                    mock_response.json.return_value = {
                        "privileges": [
                            {"scope": "org", "org_id": "test-org", "role": "admin"}
                        ]
                    }
                    mock_get.return_value = mock_response

                    # Act
                    session = APISession(
                        email=email,
                        password=password,
                        apitoken=api_token,
                        host=test_host,
                        console_log_level=30,
                        logging_log_level=20,
                        show_cli_notif=False,
                        https_proxy="http://proxy:8080",
                    )

                    # Assert
                    assert session.email == email
                    assert session._password == password
                    assert session._apitoken == [
                        api_token
                    ]  # Should be converted to list
                    assert session._cloud_uri == test_host
                    assert session._console_log_level == 30
                    assert session._logging_log_level == 20
                    assert session._show_cli_notif is False
                    assert session._proxies["https"] == "http://proxy:8080"

    def test_initialisation_with_env_file(self, tmp_env_file) -> None:
        """Test APISession initialisation using environment file"""
        # Mock requests.session and ensure clean environment
        with patch("mistapi.__api_session.requests.session"):
            with patch("mistapi.__api_session.requests.get") as mock_get:
                # Mock successful token validation
                mock_response = Mock()
                mock_response.status_code = 200
                mock_response.json.return_value = {
                    "privileges": [
                        {"scope": "org", "org_id": "test-org", "role": "admin"}
                    ]
                }
                mock_get.return_value = mock_response

                with patch.dict(
                    os.environ,
                    {
                        "MIST_HOST": "api.mist.com",
                        "MIST_APITOKEN": "abcdef0123456789abcdef0123456789abcdef01",
                        "MIST_USER": "test@example.com",
                        "MIST_PASSWORD": "test_password",
                        "CONSOLE_LOG_LEVEL": "30",
                        "LOGGING_LOG_LEVEL": "20",
                        "HTTPS_PROXY": "http://proxy:8080",
                    },
                ):
                    # Act
                    session = APISession(env_file=tmp_env_file)

                    # Assert
                    assert session._cloud_uri == "api.mist.com"
                    assert session._apitoken == [
                        "abcdef0123456789abcdef0123456789abcdef01"
                    ]
                    assert session.email == "test@example.com"
                    assert session._password == "test_password"


class TestCloudConfiguration:
    """Test cloud configuration methods"""

    @pytest.mark.parametrize("cloud_data", SAMPLE_CLOUDS)
    def test_set_valid_cloud(self, isolated_session, cloud_data) -> None:
        """Test setting valid cloud URIs"""
        # Act
        isolated_session.set_cloud(cloud_data["host"])

        # Assert
        assert isolated_session._cloud_uri == cloud_data["host"]

    def test_set_invalid_cloud(self, isolated_session) -> None:
        """Test setting invalid cloud URI"""
        # Arrange
        invalid_host = "invalid.example.com"

        # Act
        isolated_session.set_cloud(invalid_host)

        # Assert
        assert isolated_session._cloud_uri == ""

    def test_get_cloud(self, isolated_session, test_host) -> None:
        """Test getting current cloud configuration"""
        # Arrange
        isolated_session._cloud_uri = test_host

        # Act
        result = isolated_session.get_cloud()

        # Assert
        assert result == test_host

    @patch("builtins.input", return_value="0")  # Select first cloud
    def test_select_cloud_first_option(self, mock_input, isolated_session) -> None:
        """Test selecting first cloud option interactively"""
        # Act
        isolated_session.select_cloud()

        # Assert
        assert isolated_session._cloud_uri == "api.ac5.mist.com"

    @patch("builtins.input", return_value="q")
    def test_select_cloud_quit(self, mock_input, isolated_session) -> None:
        """Test quitting cloud selection"""
        # Act & Assert
        with pytest.raises(SystemExit):
            isolated_session.select_cloud()


class TestAuthentication:
    """Test authentication-related methods"""

    def test_set_email_direct(self, isolated_session) -> None:
        """Test setting email directly"""
        # Arrange
        email = "direct@example.com"

        # Act
        isolated_session.set_email(email)

        # Assert
        assert isolated_session.email == email

    @patch("builtins.input", return_value="interactive@example.com")
    def test_set_email_interactive(self, mock_input, isolated_session) -> None:
        """Test setting email through interactive input"""
        # Act
        isolated_session.set_email()

        # Assert
        assert isolated_session.email == "interactive@example.com"
        mock_input.assert_called_once_with("Login: ")

    def test_set_password_direct(self, isolated_session) -> None:
        """Test setting password directly"""
        # Arrange
        password = "direct_password"

        # Act
        isolated_session.set_password(password)

        # Assert
        assert isolated_session._password == password

    @patch("mistapi.__api_session.getpass", return_value="secret_password")
    def test_set_password_interactive(self, mock_getpass, isolated_session) -> None:
        """Test setting password through interactive input"""
        # Act
        isolated_session.set_password()

        # Assert
        assert isolated_session._password == "secret_password"
        mock_getpass.assert_called_once_with("Password: ")

    def test_set_single_api_token(self, isolated_session, api_token) -> None:
        """Test setting a single API token"""
        # Arrange
        isolated_session.set_cloud("api.mist.com")  # Set cloud to enable validation
        with patch.object(
            isolated_session, "_check_api_tokens", return_value=[api_token]
        ):
            # Act
            isolated_session.set_api_token(api_token)

            # Assert
            assert isolated_session._apitoken == [api_token]
            assert isolated_session._apitoken_index == 0

    def test_set_multiple_api_tokens(self, isolated_session) -> None:
        """Test setting multiple API tokens"""
        # Arrange
        tokens = "token1, token2, token3"
        expected_tokens = ["token1", "token2", "token3"]

        isolated_session.set_cloud("api.mist.com")  # Set cloud to enable validation
        with patch.object(
            isolated_session, "_check_api_tokens", return_value=expected_tokens
        ):
            # Act
            isolated_session.set_api_token(tokens)

            # Assert
            assert isolated_session._apitoken == expected_tokens
            assert isolated_session._apitoken_index == 0

    def test_authentication_status_unauthenticated(self, isolated_session) -> None:
        """Test authentication status when not authenticated"""
        # Act & Assert
        assert not isolated_session.get_authentication_status()

    def test_authentication_status_authenticated(self, authenticated_session) -> None:
        """Test authentication status when authenticated"""
        # Act & Assert
        assert authenticated_session.get_authentication_status()


class TestPrivilegeManagement:
    """Test privilege-related functionality"""

    @pytest.mark.skip()
    def test_privilege_by_org_id_found(self, authenticated_session, org_id) -> None:
        """Test getting privilege when org ID exists in user privileges"""
        # Act
        privilege = authenticated_session.get_privilege_by_org_id(org_id)

        # Assert
        assert privilege is not None
        assert privilege["org_id"] == org_id
        assert privilege["scope"] == "org"

    @pytest.mark.skip()
    def test_privilege_by_org_id_not_found(self, authenticated_session) -> None:
        """Test getting privilege when org ID doesn't exist"""
        # Arrange
        non_existent_org_id = "00000000-0000-0000-0000-000000000000"

        # Mock the org info request that would normally happen
        with patch.object(authenticated_session, "mist_get") as mock_get:
            mock_get.return_value.data = None

            # Act
            privilege = authenticated_session.get_privilege_by_org_id(
                non_existent_org_id
            )

            # Assert
            assert privilege == {}

    def test_privileges_object_creation(self, sample_privileges) -> None:
        """Test that Privileges object can be created and iterated"""
        # Act
        privileges_obj = Privileges(sample_privileges)

        # Assert
        assert len(privileges_obj.privileges) == 2
        assert privileges_obj.privileges[0].scope == "org"
        assert privileges_obj.privileges[1].scope == "site"


class TestStringRepresentation:
    """Test string representation of APISession"""

    def test_str_representation(self, authenticated_session) -> None:
        """Test string representation includes key information"""
        # Act
        session_str = str(authenticated_session)

        # Assert
        assert "email:" in session_str
        assert "first_name:" in session_str
        assert "last_name:" in session_str
        assert "privileges:" in session_str
        assert authenticated_session.email in session_str

        # Check that the authentication status is correctly reflected
        # Looking at the actual __str__ implementation, it only shows "authenticated:"
        # field if the authentication status is available and not empty
        if (
            hasattr(authenticated_session, "_authenticated")
            and authenticated_session._authenticated
        ):
            # The string should contain key user info showing they're authenticated
            assert "Test" in session_str  # first_name
            assert "User" in session_str  # last_name
            assert "test@example.com" in session_str  # email


# Parametrised tests for testing multiple scenarios efficiently
class TestParametrisedScenarios:
    """Test various scenarios using parametrised tests"""

    @pytest.mark.parametrize(
        "log_level,expected", [(0, 0), (10, 10), (20, 20), (30, 30), (40, 40), (50, 50)]
    )
    def test_console_log_levels(self, log_level, expected) -> None:
        """Test different console log levels"""
        # Mock environment and requests to ensure clean state
        with patch.dict(os.environ, {}, clear=True):
            with patch("mistapi.__api_session.requests.session"):
                # Act
                session = APISession(console_log_level=log_level)

                # Assert
                assert session._console_log_level == expected

    @pytest.mark.parametrize(
        "proxy_url",
        [
            "http://proxy:8080",
            "https://secure-proxy:443",
            "http://user:pass@proxy:3128",
            None,
        ],
    )
    def test_proxy_configuration(self, proxy_url) -> None:
        """Test different proxy configurations"""
        # Mock environment and requests to ensure clean state
        with patch.dict(os.environ, {}, clear=True):
            with patch("mistapi.__api_session.requests.session"):
                # Act
                session = APISession(https_proxy=proxy_url)

                # Assert
                assert session._proxies["https"] == proxy_url


class TestBugFixes:
    """Test fixes for specific bugs found during testing"""

    def test_privileges_object_is_iterable(self, sample_privileges) -> None:
        """
        Bug fix: Privileges object should be iterable for get_privilege_by_org_id

        The original error was:
        TypeError: 'Privileges' object is not iterable
        """
        # Arrange
        privileges_obj = Privileges(sample_privileges)

        # Act & Assert - This should not raise TypeError
        org_id = sample_privileges[0]["org_id"]
        found_priv = next(
            (priv for priv in privileges_obj.privileges if priv.org_id == org_id), None
        )
        assert found_priv is not None
        assert found_priv.org_id == org_id

    def test_environment_variable_type_handling(self) -> None:
        """
        Bug fix: Environment variables are strings, need type conversion

        The original error was console_log_level being '30' instead of 30
        """
        # Arrange - Environment variables are always strings
        env_vars = {
            "CONSOLE_LOG_LEVEL": "30",  # String, not int
            "LOGGING_LOG_LEVEL": "20",  # String, not int
        }

        with patch.dict(os.environ, env_vars):
            with patch("mistapi.__api_session.requests.session"):
                # Act
                session = APISession()

                # Assert - Should convert string to int
                assert session._console_log_level == 30  # int, not '30'
                assert session._logging_log_level == 20  # int, not '20'
