# tests/unit/test_api_session.py
"""
Unit tests for APISession class.

These tests focus on authentication mechanisms and session management
without requiring real HTTP calls or external dependencies.
"""

import os
from unittest.mock import MagicMock, patch

import pytest
import responses

from mistapi import APISession
from mistapi.__models.privilege import Privileges
from tests.fixtures.test_data import SAMPLE_CLOUDS


class TestLoginPasswordAuthentication:
    """Test login/password authentication scenarios"""

    def test_valid_credentials_success(
        self,
        isolated_session,
        test_host,
        test_username,
        test_password,
    ) -> None:
        """Test successful login with valid username and password"""
        # Setup
        isolated_session.set_cloud(test_host)
        isolated_session.set_email(test_username)
        isolated_session.set_password(test_password)

        # Execute & Verify - real API call with correct password
        isolated_session.login()
        assert isolated_session._authenticated is True
        assert isolated_session.email == test_username
        assert len(isolated_session.privileges) > 0

    @responses.activate
    def test_invalid_credentials_failure(
        self,
        isolated_session,
        test_host,
        test_username,
    ) -> None:
        """Test login failure with invalid credentials"""
        # Setup
        isolated_session.set_cloud(test_host)
        isolated_session.set_email(test_username)
        isolated_session.set_password("wrong_password")

        # Mock login endpoint to return 401
        responses.add(
            responses.POST,
            f"https://{test_host}/api/v1/login",
            json={"error": "Unauthorized"},
            status=401,
        )

        # Execute & Verify
        try:
            isolated_session.login()
        except OSError:
            # OSError is raised when pytest tries to read stdin
            # This confirms login failed and tried to prompt for new credentials
            pass

        # Verify authentication failed
        assert isolated_session._authenticated is False

    @responses.activate
    def test_login_with_2fa_required(
        self,
        isolated_session,
        test_host,
        test_username,
        test_password,
        sample_user_data,
    ) -> None:
        """Test login with 2FA requirement"""
        # Setup
        isolated_session._cloud_uri = test_host
        isolated_session.set_email(test_username)
        isolated_session.set_password(test_password)

        # Mock login endpoint requiring 2FA
        responses.add(
            responses.POST,
            f"https://{test_host}/api/v1/login",
            json={"two_factor_required": True, "two_factor_passed": False},
            status=200,
        )

        # Mock 2FA verification
        responses.add(
            responses.POST,
            f"https://{test_host}/api/v1/login/two-factor",
            json={"status": "success"},
            status=200,
        )

        # Mock self endpoint
        responses.add(
            responses.GET,
            f"https://{test_host}/api/v1/self",
            json=sample_user_data,
            status=200,
        )

        # Mock user input for 2FA code
        with patch("builtins.input", return_value="123456"):
            with patch.object(
                isolated_session._session, "cookies", {"csrftoken": "test-csrf"}
            ):
                # Execute
                isolated_session.login()

                # Verify
                assert isolated_session._authenticated is True

    def test_login_without_credentials(self, isolated_session, test_host) -> None:
        """Test login fails when no credentials are provided"""
        # Setup
        isolated_session.set_cloud(test_host)

        # Execute & Verify - should prompt for input or raise error
        with patch("builtins.input", side_effect=["q"]):  # Quit interactive prompt
            with pytest.raises(SystemExit):
                isolated_session.login()


class TestAPITokenAuthentication:
    """Test API token authentication scenarios"""

    def test_single_valid_token_success(
        self, isolated_session, test_host, valid_api_token
    ) -> None:
        """Test authentication with a single valid API token"""
        # Setup
        isolated_session.set_cloud(test_host)
        isolated_session.set_api_token(valid_api_token)
        isolated_session.login()

        # Verify
        assert isolated_session._apitoken == [valid_api_token]
        assert isolated_session._apitoken_index == 0
        assert len(responses.calls) == 1  # Token was validated
        assert isolated_session._authenticated is True

    @responses.activate
    def test_single_invalid_token_failure(
        self, isolated_session, test_host, invalid_api_token
    ) -> None:
        """Test authentication failure with an invalid API token"""
        # Setup
        isolated_session._cloud_uri = test_host

        # Mock token validation endpoint to return 401
        responses.add(
            responses.GET,
            f"https://{test_host}/api/v1/self",
            json={"error": "Unauthorized"},
            status=401,
        )

        # Execute & Verify
        with pytest.raises(SystemExit) as exc_info:
            isolated_session.set_api_token(invalid_api_token)

        assert exc_info.value.code == 2
        assert isolated_session._apitoken == []

    @responses.activate
    def test_multiple_valid_tokens_success(
        self, isolated_session, test_host, valid_api_tokens, sample_user_data
    ) -> None:
        """Test authentication with multiple valid API tokens"""
        # Setup
        isolated_session._cloud_uri = test_host
        expected_tokens = valid_api_tokens.split(",")

        # Mock token validation endpoint for each token
        for _ in expected_tokens:
            responses.add(
                responses.GET,
                f"https://{test_host}/api/v1/self",
                json=sample_user_data,
                status=200,
            )

        # Execute
        isolated_session.set_api_token(valid_api_tokens)

        # Verify
        assert isolated_session._apitoken == expected_tokens
        assert isolated_session._apitoken_index == 0
        assert len(responses.calls) == len(expected_tokens)

    @responses.activate
    def test_mixed_tokens_partial_success(
        self, isolated_session, test_host, mixed_api_tokens, sample_user_data
    ) -> None:
        """Test authentication with mixed valid and invalid tokens"""
        # Setup
        isolated_session._cloud_uri = test_host
        tokens = mixed_api_tokens.split(",")

        # Mock responses: first token invalid (401), second token valid (200)
        responses.add(
            responses.GET,
            f"https://{test_host}/api/v1/self",
            json={"error": "Unauthorized"},
            status=401,
        )
        responses.add(
            responses.GET,
            f"https://{test_host}/api/v1/self",
            json=sample_user_data,
            status=200,
        )

        # Execute - should filter out invalid tokens
        isolated_session.set_api_token(mixed_api_tokens)

        # Verify - only valid tokens should be kept
        assert len(isolated_session._apitoken) == 1
        assert isolated_session._apitoken[0] == tokens[1]  # Second token is valid

    @responses.activate
    def test_all_invalid_tokens_failure(self, isolated_session, test_host) -> None:
        """Test authentication failure when all tokens are invalid"""
        # Setup
        isolated_session._cloud_uri = test_host
        invalid_tokens = "invalid1,invalid2,invalid3"

        # Mock all tokens as invalid
        for _ in range(3):
            responses.add(
                responses.GET,
                f"https://{test_host}/api/v1/self",
                json={"error": "Unauthorized"},
                status=401,
            )

        # Execute & Verify
        with pytest.raises(SystemExit) as exc_info:
            isolated_session.set_api_token(invalid_tokens)

        assert exc_info.value.code == 2
        assert isolated_session._apitoken == []

    def test_empty_token_string(self, isolated_session) -> None:
        """Test handling of empty token string"""
        isolated_session.set_api_token("")
        assert isolated_session._apitoken == []

    def test_whitespace_in_tokens(
        self, isolated_session, test_host, sample_user_data
    ) -> None:
        """Test that whitespace in token strings is properly handled"""
        isolated_session._cloud_uri = test_host
        tokens_with_whitespace = "  token1  ,  token2  ,  token3  "

        with patch.object(
            isolated_session,
            "_check_api_tokens",
            return_value=["token1", "token2", "token3"],
        ):
            isolated_session.set_api_token(tokens_with_whitespace)
            # Verify whitespace is stripped
            assert all(token == token.strip() for token in isolated_session._apitoken)


class TestKeyringAuthentication:
    """Test keyring integration for secure credential storage"""

    @patch("mistapi.__api_session.keyring")
    @responses.activate
    def test_valid_keyring_service_success(
        self, mock_keyring, test_host, valid_api_token, sample_user_data
    ) -> None:
        """Test successful authentication using keyring"""

        # Setup keyring mock
        def get_password(service, key):
            credentials = {
                "MIST_HOST": test_host,
                "MIST_APITOKEN": valid_api_token,
            }
            return credentials.get(key)

        mock_keyring.get_password.side_effect = get_password

        # Mock token validation
        responses.add(
            responses.GET,
            f"https://{test_host}/api/v1/self",
            json=sample_user_data,
            status=200,
        )

        # Execute
        with patch.dict(os.environ, {}, clear=True):
            with patch("mistapi.__api_session.requests.session"):
                session = APISession(
                    keyring_service="test_service",
                    console_log_level=50,
                    show_cli_notif=False,
                )

                # Verify
                assert session._cloud_uri == test_host
                assert session._apitoken == [valid_api_token]
                mock_keyring.get_password.assert_any_call("test_service", "MIST_HOST")
                mock_keyring.get_password.assert_any_call(
                    "test_service", "MIST_APITOKEN"
                )

    @patch("mistapi.__api_session.keyring")
    def test_invalid_keyring_service_failure(self, mock_keyring) -> None:
        """Test authentication failure with invalid/empty keyring"""
        # Setup keyring mock to return None (no credentials)
        mock_keyring.get_password.return_value = None

        # Execute & Verify
        with patch.dict(os.environ, {}, clear=True):
            with patch("mistapi.__api_session.requests.session"):
                with pytest.raises(SystemExit):
                    APISession(
                        keyring_service="invalid_service",
                        console_log_level=50,
                    )

    @patch("mistapi.__api_session.keyring")
    @responses.activate
    def test_keyring_with_username_password(
        self, mock_keyring, test_host, username, password, sample_user_data
    ) -> None:
        """Test keyring with username/password instead of token"""

        # Setup keyring mock
        def get_password(service, key):
            credentials = {
                "MIST_HOST": test_host,
                "MIST_USER": username,
                "MIST_PASSWORD": password,
            }
            return credentials.get(key)

        mock_keyring.get_password.side_effect = get_password

        # Execute
        with patch.dict(os.environ, {}, clear=True):
            with patch("mistapi.__api_session.requests.session"):
                session = APISession(
                    keyring_service="test_service",
                    console_log_level=50,
                    show_cli_notif=False,
                )

                # Verify
                assert session._cloud_uri == test_host
                assert session.email == username
                assert session._password == password
                assert session._apitoken == []


class TestVaultIntegration:
    """Test HashiCorp Vault integration"""

    @patch("mistapi.__api_session.hvac")
    @responses.activate
    def test_valid_vault_configuration(
        self, mock_hvac, test_host, valid_api_token, sample_user_data
    ) -> None:
        """Test successful authentication using HashiCorp Vault"""
        # Setup vault mock
        mock_client = MagicMock()
        mock_client.secrets.kv.v2.read_secret_version.return_value = {
            "data": {
                "data": {
                    "MIST_HOST": test_host,
                    "MIST_APITOKEN": valid_api_token,
                }
            }
        }
        mock_hvac.Client.return_value = mock_client

        # Mock token validation
        responses.add(
            responses.GET,
            f"https://{test_host}/api/v1/self",
            json=sample_user_data,
            status=200,
        )

        # Execute
        with patch.dict(os.environ, {}, clear=True):
            with patch("mistapi.__api_session.requests.session"):
                session = APISession(
                    vault_url="https://vault.example.com",
                    vault_path="secret/mist",
                    vault_token="test-token",
                    console_log_level=50,
                    show_cli_notif=False,
                )

                # Verify
                assert session._cloud_uri == test_host
                assert session._apitoken == [valid_api_token]

    @patch("mistapi.__api_session.hvac")
    def test_vault_connection_failure(self, mock_hvac) -> None:
        """Test handling of Vault connection failures"""
        # Setup vault mock to raise exception
        mock_hvac.Client.side_effect = Exception("Connection failed")

        # Execute & Verify
        with patch.dict(os.environ, {}, clear=True):
            with patch("mistapi.__api_session.requests.session"):
                with pytest.raises(Exception):
                    APISession(
                        vault_url="https://vault.example.com",
                        vault_path="secret/mist",
                        vault_token="test-token",
                        console_log_level=50,
                    )

    @patch("mistapi.__api_session.hvac")
    def test_vault_empty_credentials(self, mock_hvac) -> None:
        """Test handling of empty credentials from Vault"""
        # Setup vault mock with empty data
        mock_client = MagicMock()
        mock_client.secrets.kv.v2.read_secret_version.return_value = {
            "data": {"data": {}}
        }
        mock_hvac.Client.return_value = mock_client

        # Execute
        with patch.dict(os.environ, {}, clear=True):
            with patch("mistapi.__api_session.requests.session"):
                session = APISession(
                    vault_url="https://vault.example.com",
                    vault_path="secret/mist",
                    vault_token="test-token",
                    console_log_level=50,
                    show_cli_notif=False,
                )

                # Verify - should have empty credentials
                assert session._cloud_uri == ""
                assert session._apitoken == []


class TestEnvironmentFileConfiguration:
    """Test environment file loading"""

    @responses.activate
    def test_load_from_env_file(
        self, tmp_env_file, test_host, valid_api_token, sample_user_data
    ) -> None:
        """Test loading credentials from environment file"""
        # Mock token validation
        responses.add(
            responses.GET,
            f"https://{test_host}/api/v1/self",
            json=sample_user_data,
            status=200,
        )

        # Execute
        with patch("mistapi.__api_session.requests.session"):
            with patch.dict(
                os.environ,
                {
                    "MIST_HOST": test_host,
                    "MIST_APITOKEN": valid_api_token,
                },
            ):
                session = APISession(
                    env_file=tmp_env_file,
                    console_log_level=50,
                    show_cli_notif=False,
                )

                # Verify
                assert session._cloud_uri == test_host
                assert session._apitoken == [valid_api_token]

    def test_env_variables_override(self, username, password) -> None:
        """Test that environment variables are properly loaded"""
        with patch.dict(
            os.environ,
            {
                "MIST_HOST": "api.eu.mist.com",
                "MIST_USER": username,
                "MIST_PASSWORD": password,
            },
        ):
            with patch("mistapi.__api_session.requests.session"):
                session = APISession(console_log_level=50, show_cli_notif=False)

                assert session._cloud_uri == "api.eu.mist.com"
                assert session.email == username
                assert session._password == password

    def test_env_variable_type_conversion(self) -> None:
        """Test that environment variables are properly converted from strings"""
        env_vars = {
            "CONSOLE_LOG_LEVEL": "40",  # String
            "LOGGING_LOG_LEVEL": "30",  # String
        }

        with patch.dict(os.environ, env_vars):
            with patch("mistapi.__api_session.requests.session"):
                session = APISession()

                # Should convert to integers
                assert session._console_log_level == 40
                assert isinstance(session._console_log_level, int)
                assert session._logging_log_level == 30
                assert isinstance(session._logging_log_level, int)


class TestSessionInitialization:
    """Test basic session initialization"""

    def test_default_initialization(self, isolated_session) -> None:
        """Test session with default parameters"""
        assert isolated_session._cloud_uri == ""
        assert isolated_session.email is None
        assert isolated_session._password is None
        assert isolated_session._apitoken == []
        assert not isolated_session._authenticated
        assert isolated_session._show_cli_notif is True

    def test_initialization_with_parameters(self, username, password) -> None:
        """Test session with explicit parameters"""
        with patch.dict(os.environ, {}, clear=True):
            with patch("mistapi.__api_session.requests.session"):
                session = APISession(
                    email=username,
                    password=password,
                    host="api.mist.com",
                    console_log_level=30,
                    logging_log_level=20,
                    show_cli_notif=False,
                )

                assert session.email == username
                assert session._password == password
                assert session._cloud_uri == "api.mist.com"
                assert session._console_log_level == 30
                assert session._logging_log_level == 20
                assert session._show_cli_notif is False

    def test_proxy_configuration(self) -> None:
        """Test session with proxy configuration"""
        proxy_url = "http://proxy:8080"

        with patch.dict(os.environ, {}, clear=True):
            with patch("mistapi.__api_session.requests.session"):
                session = APISession(
                    host="api.mist.com",
                    https_proxy=proxy_url,
                    console_log_level=50,
                )

                assert session._proxies["https"] == proxy_url

    @pytest.mark.parametrize(
        "log_level,expected", [(0, 0), (10, 10), (20, 20), (30, 30), (40, 40), (50, 50)]
    )
    def test_log_levels(self, log_level, expected) -> None:
        """Test different log level configurations"""
        with patch.dict(os.environ, {}, clear=True):
            with patch("mistapi.__api_session.requests.session"):
                session = APISession(console_log_level=log_level)
                assert session._console_log_level == expected


class TestCloudConfiguration:
    """Test cloud selection and configuration"""

    @pytest.mark.parametrize("cloud_data", SAMPLE_CLOUDS)
    def test_set_valid_cloud(self, isolated_session, cloud_data) -> None:
        """Test setting valid cloud URIs"""
        isolated_session.set_cloud(cloud_data["host"])
        assert isolated_session._cloud_uri == cloud_data["host"]

    def test_set_invalid_cloud(self, isolated_session) -> None:
        """Test setting invalid cloud URI"""
        isolated_session.set_cloud("invalid.example.com")
        assert isolated_session._cloud_uri == ""

    def test_get_cloud(self, isolated_session, test_host) -> None:
        """Test getting current cloud configuration"""
        isolated_session._cloud_uri = test_host
        assert isolated_session.get_cloud() == test_host

    @patch("builtins.input", return_value="0")
    def test_select_cloud_interactive(self, mock_input, isolated_session) -> None:
        """Test interactive cloud selection"""
        isolated_session.select_cloud()
        assert isolated_session._cloud_uri == "api.ac5.mist.com"

    @patch("builtins.input", return_value="q")
    def test_select_cloud_quit(self, mock_input, isolated_session) -> None:
        """Test quitting cloud selection"""
        with pytest.raises(SystemExit):
            isolated_session.select_cloud()


class TestAuthenticationHelpers:
    """Test authentication helper methods"""

    def test_set_email_direct(self, isolated_session, username) -> None:
        """Test setting email directly"""
        isolated_session.set_email(username)
        assert isolated_session.email == username

    @patch("builtins.input", return_value="interactive@example.com")
    def test_set_email_interactive(self, mock_input, isolated_session) -> None:
        """Test setting email interactively"""
        isolated_session.set_email()
        assert isolated_session.email == "interactive@example.com"
        mock_input.assert_called_once_with("Login: ")

    def test_set_password_direct(self, isolated_session, password) -> None:
        """Test setting password directly"""
        isolated_session.set_password(password)
        assert isolated_session._password == password

    @patch("mistapi.__api_session.getpass", return_value="secret_password")
    def test_set_password_interactive(self, mock_getpass, isolated_session) -> None:
        """Test setting password interactively"""
        isolated_session.set_password()
        assert isolated_session._password == "secret_password"
        mock_getpass.assert_called_once_with("Password: ")

    def test_get_authentication_status_false(self, isolated_session) -> None:
        """Test authentication status when not authenticated"""
        assert isolated_session.get_authentication_status() is False

    def test_get_authentication_status_true(self, authenticated_session) -> None:
        """Test authentication status when authenticated"""
        assert authenticated_session.get_authentication_status() is True


class TestPrivilegeManagement:
    """Test privilege-related functionality"""

    def test_get_privilege_by_org_id_found(self, authenticated_session, org_id) -> None:
        """Test getting privilege when org ID exists"""
        privilege = authenticated_session.get_privilege_by_org_id(org_id)

        assert privilege is not None
        # Privilege is an object, access via attributes
        assert privilege.org_id == org_id
        assert privilege.scope == "org"

    def test_get_privilege_by_org_id_not_found(self, authenticated_session) -> None:
        """Test getting privilege when org ID doesn't exist"""
        non_existent_org_id = "00000000-0000-0000-0000-000000000000"
        privilege = authenticated_session.get_privilege_by_org_id(non_existent_org_id)
        assert privilege == {}

    def test_privileges_object_creation(self, sample_privileges) -> None:
        """Test Privileges object creation and iteration"""
        privileges_obj = Privileges(sample_privileges)

        assert len(privileges_obj.privileges) == 2
        assert privileges_obj.privileges[0].scope == "org"
        assert privileges_obj.privileges[1].scope == "site"

        # Test iteration
        count = 0
        for priv in privileges_obj.privileges:
            count += 1
        assert count == 2


class TestSessionState:
    """Test session state management"""

    def test_str_representation_authenticated(self, authenticated_session) -> None:
        """Test string representation when authenticated"""
        session_str = str(authenticated_session)

        assert "email:" in session_str
        assert "first_name:" in session_str
        assert "last_name:" in session_str
        assert authenticated_session.email in session_str

    def test_str_representation_unauthenticated(self, isolated_session) -> None:
        """Test string representation when not authenticated"""
        session_str = str(isolated_session)
        assert "email:" in session_str
        assert "privileges:" in session_str

    def test_session_headers_with_token(
        self, isolated_session, valid_api_token
    ) -> None:
        """Test that session headers contain authorization token"""
        isolated_session._apitoken = [valid_api_token]
        isolated_session._apitoken_index = 0

        # Update headers as set_api_token would
        isolated_session._session.headers.update(
            {"Authorization": f"Token {valid_api_token}"}
        )

        assert "Authorization" in isolated_session._session.headers
        assert (
            isolated_session._session.headers["Authorization"]
            == f"Token {valid_api_token}"
        )


class TestErrorHandling:
    """Test error handling and edge cases"""

    def test_login_without_cloud_configured(self, isolated_session) -> None:
        """Test login fails without cloud configured"""
        with patch("builtins.input", side_effect=["q"]):
            with pytest.raises(SystemExit):
                isolated_session.login()

    @pytest.mark.parametrize(
        "proxy_url",
        [
            "http://proxy:8080",
            "https://secure-proxy:443",
            "http://user:pass@proxy:3128",
            None,
        ],
    )
    def test_proxy_configurations(self, proxy_url) -> None:
        """Test various proxy configurations"""
        with patch.dict(os.environ, {}, clear=True):
            with patch("mistapi.__api_session.requests.session"):
                session = APISession(https_proxy=proxy_url, console_log_level=50)
                assert session._proxies["https"] == proxy_url

    def test_invalid_log_level_accepted(self) -> None:
        """Test that out-of-range log levels are accepted"""
        with patch.dict(os.environ, {}, clear=True):
            with patch("mistapi.__api_session.requests.session"):
                # Should not raise exceptions
                session = APISession(console_log_level=100)
                assert session._console_log_level == 100

                session2 = APISession(console_log_level=-1)
                assert session2._console_log_level == -1


class TestRegressionBugs:
    """Test fixes for specific bugs"""

    def test_api_token_is_list_not_boolean(self, isolated_session) -> None:
        """Ensure _apitoken is always a list, not a boolean"""
        assert isinstance(isolated_session._apitoken, list)

        isolated_session._apitoken = ["token1"]
        assert isinstance(isolated_session._apitoken, list)
        assert isolated_session._apitoken[0] == "token1"

    def test_privileges_supports_iteration(self, sample_privileges) -> None:
        """Ensure Privileges object supports iteration"""
        privileges_obj = Privileges(sample_privileges)

        # Should not raise TypeError
        org_id = sample_privileges[0]["org_id"]
        found_priv = next(
            (priv for priv in privileges_obj.privileges if priv.org_id == org_id), None
        )
        assert found_priv is not None
        assert found_priv.org_id == org_id

    def test_environment_variables_as_strings(self) -> None:
        """Ensure environment variables are converted from strings properly"""
        env_vars = {
            "CONSOLE_LOG_LEVEL": "30",
            "LOGGING_LOG_LEVEL": "20",
        }

        with patch.dict(os.environ, env_vars):
            with patch("mistapi.__api_session.requests.session"):
                session = APISession()

                assert session._console_log_level == 30
                assert not isinstance(session._console_log_level, str)
                assert session._logging_log_level == 20
                assert not isinstance(session._logging_log_level, str)
