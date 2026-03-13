# tests/unit/test_init.py
"""
Unit tests for mistapi.__init__ module.

Tests verify:
- Direct imports (APISession, get_all, get_next, __version__, __author__)
- Lazy subpackage loading (api, utils, websockets, cli)
- AttributeError for unknown attributes
"""

import importlib
import types
from unittest.mock import patch

import pytest


class TestDirectImports:
    """Test that directly-imported names are available on the mistapi module."""

    def test_apisession_is_available(self):
        """APISession should be importable from mistapi."""
        from mistapi import APISession

        assert APISession is not None

    def test_apisession_is_the_real_class(self):
        """APISession should be the class from mistapi.__api_session."""
        from mistapi import APISession
        from mistapi.__api_session import APISession as RealAPISession

        assert APISession is RealAPISession

    def test_get_all_is_available(self):
        """get_all should be importable from mistapi."""
        from mistapi import get_all

        assert callable(get_all)

    def test_get_all_is_the_real_function(self):
        """get_all should be the function from mistapi.__pagination."""
        from mistapi import get_all
        from mistapi.__pagination import get_all as real_get_all

        assert get_all is real_get_all

    def test_get_next_is_available(self):
        """get_next should be importable from mistapi."""
        from mistapi import get_next

        assert callable(get_next)

    def test_get_next_is_the_real_function(self):
        """get_next should be the function from mistapi.__pagination."""
        from mistapi import get_next
        from mistapi.__pagination import get_next as real_get_next

        assert get_next is real_get_next

    def test_version_is_available(self):
        """__version__ should be importable from mistapi."""
        from mistapi import __version__

        assert isinstance(__version__, str)
        assert len(__version__) > 0

    def test_version_matches_version_module(self):
        """__version__ should match the value in mistapi.__version."""
        import mistapi
        from mistapi.__version import __version__ as real_version

        assert mistapi.__version__ == real_version

    def test_author_is_available(self):
        """__author__ should be importable from mistapi."""
        from mistapi import __author__

        assert isinstance(__author__, str)
        assert len(__author__) > 0

    def test_author_matches_version_module(self):
        """__author__ should match the value in mistapi.__version."""
        import mistapi
        from mistapi.__version import __author__ as real_author

        assert mistapi.__author__ == real_author


class TestLazyImportApi:
    """Test lazy loading of the mistapi.api subpackage."""

    def test_api_loads_on_access(self):
        """Accessing mistapi.api should trigger lazy import and return a module."""
        import mistapi

        # Remove cached attribute if present so __getattr__ fires
        mistapi.__dict__.pop("api", None)

        with patch("importlib.import_module", wraps=importlib.import_module) as spy:
            result = mistapi.api
            spy.assert_any_call("mistapi.api")

        assert isinstance(result, types.ModuleType)
        assert result.__name__ == "mistapi.api"

    def test_api_is_cached_after_first_access(self):
        """After first access, mistapi.api should be cached in globals."""
        import mistapi

        # Force a fresh lazy load
        mistapi.__dict__.pop("api", None)
        first = mistapi.api
        second = mistapi.api

        assert first is second
        assert "api" in mistapi.__dict__


class TestLazyImportUtils:
    """Test lazy loading of the mistapi.device_utils subpackage."""

    def test_utils_loads_on_access(self):
        """Accessing mistapi.device_utils should trigger lazy import and return a module."""
        import mistapi

        mistapi.__dict__.pop("device_utils", None)

        with patch("importlib.import_module", wraps=importlib.import_module) as spy:
            result = mistapi.device_utils
            spy.assert_any_call("mistapi.device_utils")

        assert isinstance(result, types.ModuleType)
        assert result.__name__ == "mistapi.device_utils"

    def test_utils_is_cached_after_first_access(self):
        """After first access, mistapi.device_utils should be cached in globals."""
        import mistapi

        mistapi.__dict__.pop("device_utils", None)
        first = mistapi.device_utils
        second = mistapi.device_utils

        assert first is second
        assert "device_utils" in mistapi.__dict__


class TestLazyImportWebsockets:
    """Test lazy loading of the mistapi.websockets subpackage."""

    def test_websockets_loads_on_access(self):
        """Accessing mistapi.websockets should trigger lazy import and return a module."""
        import mistapi

        mistapi.__dict__.pop("websockets", None)

        with patch("importlib.import_module", wraps=importlib.import_module) as spy:
            result = mistapi.websockets
            spy.assert_any_call("mistapi.websockets")

        assert isinstance(result, types.ModuleType)
        assert result.__name__ == "mistapi.websockets"

    def test_websockets_is_cached_after_first_access(self):
        """After first access, mistapi.websockets should be cached in globals."""
        import mistapi

        mistapi.__dict__.pop("websockets", None)
        first = mistapi.websockets
        second = mistapi.websockets

        assert first is second
        assert "websockets" in mistapi.__dict__


class TestLazyImportCli:
    """Test lazy loading of the mistapi.cli subpackage."""

    def test_cli_loads_on_access(self):
        """Accessing mistapi.cli should trigger lazy import and return a module."""
        import mistapi

        mistapi.__dict__.pop("cli", None)

        with patch("importlib.import_module", wraps=importlib.import_module) as spy:
            result = mistapi.cli
            spy.assert_any_call("mistapi.cli")

        assert isinstance(result, types.ModuleType)
        assert result.__name__ == "mistapi.cli"

    def test_cli_is_cached_after_first_access(self):
        """After first access, mistapi.cli should be cached in globals."""
        import mistapi

        mistapi.__dict__.pop("cli", None)
        first = mistapi.cli
        second = mistapi.cli

        assert first is second
        assert "cli" in mistapi.__dict__


class TestLazyImportMechanism:
    """Test the __getattr__ mechanism in general."""

    def test_lazy_subpackages_dict_has_expected_keys(self):
        """_LAZY_SUBPACKAGES should contain the expected subpackage mappings."""
        import mistapi

        expected = {"api", "cli", "websockets", "device_utils"}
        assert set(mistapi._LAZY_SUBPACKAGES.keys()) == expected

    def test_lazy_subpackages_values_are_dotted_paths(self):
        """Each value in _LAZY_SUBPACKAGES should be a fully-qualified module path."""
        import mistapi

        for key, value in mistapi._LAZY_SUBPACKAGES.items():
            assert value == f"mistapi.{key}"

    def test_getattr_delegates_to_importlib(self):
        """__getattr__ should call importlib.import_module for known subpackages."""
        import mistapi

        sentinel = types.ModuleType("mistapi.api")
        mistapi.__dict__.pop("api", None)

        with patch("importlib.import_module", return_value=sentinel) as mock_import:
            result = mistapi.__getattr__("api")

        mock_import.assert_called_once_with("mistapi.api")
        assert result is sentinel

    def test_getattr_caches_result_in_globals(self):
        """__getattr__ should store the imported module in the package globals."""
        import mistapi

        sentinel = types.ModuleType("mistapi.device_utils")
        mistapi.__dict__.pop("device_utils", None)

        with patch("importlib.import_module", return_value=sentinel):
            mistapi.__getattr__("device_utils")

        assert mistapi.__dict__["device_utils"] is sentinel


class TestInvalidAttribute:
    """Test that accessing undefined attributes raises AttributeError."""

    def test_unknown_attribute_raises_attribute_error(self):
        """Accessing a non-existent attribute should raise AttributeError."""
        import mistapi

        with pytest.raises(
            AttributeError, match=r"module 'mistapi' has no attribute 'nonexistent'"
        ):
            mistapi.__getattr__("nonexistent")

    def test_unknown_attribute_via_getattr_builtin(self):
        """getattr on an unknown name without default should raise AttributeError."""
        import mistapi

        with pytest.raises(AttributeError):
            getattr(mistapi, "totally_made_up_attribute_xyz")

    def test_unknown_attribute_with_default(self):
        """getattr with a default should return the default for unknown names."""
        import mistapi

        result = getattr(mistapi, "totally_made_up_attribute_xyz", "fallback")
        assert result == "fallback"

    def test_error_message_includes_attribute_name(self):
        """The AttributeError message should include the missing attribute name."""
        import mistapi

        with pytest.raises(AttributeError, match="'bogus_name'"):
            mistapi.__getattr__("bogus_name")

    @pytest.mark.parametrize(
        "name",
        ["foo", "bar", "API", "Websockets", "Api", "UTILS"],
    )
    def test_various_invalid_names(self, name):
        """Various invalid names should all raise AttributeError (case-sensitive)."""
        import mistapi

        with pytest.raises(AttributeError):
            mistapi.__getattr__(name)
