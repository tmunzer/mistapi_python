# tests/unit/test_models.py
"""
Unit tests for privilege model classes.

These tests cover _Privilege and Privileges from mistapi.__models.privilege,
verifying construction, string representation, iteration, and field access.
"""

import pytest

from mistapi.__models.privilege import Privileges, _Privilege


# ---------------------------------------------------------------------------
# Constants re-declared locally so tests are self-contained within the file,
# but the sample_privileges fixture from conftest is reused for consistency.
# ---------------------------------------------------------------------------
TEST_ORG_ID = "203d3d02-dbc0-4c1b-9f41-76896a3330f4"
TEST_SITE_ID = "f5fcbee5-fbca-45b3-8bf1-1619ede87879"


# ===================================================================
# _Privilege tests
# ===================================================================
class TestPrivilegeCreation:
    """Test _Privilege initialisation and field population"""

    def test_all_fields_populated_from_dict(self) -> None:
        """All dict keys should become attributes on the _Privilege object"""
        # Arrange
        data = {
            "scope": "org",
            "role": "admin",
            "org_id": TEST_ORG_ID,
            "org_name": "Acme Corp",
            "msp_id": "msp-id-1",
            "msp_name": "MSP One",
            "orggroup_ids": ["grp-1", "grp-2"],
            "name": "Test Privilege",
            "site_id": TEST_SITE_ID,
            "sitegroup_ids": ["sg-1"],
            "views": ["monitoring", "location"],
        }

        # Act
        priv = _Privilege(data)

        # Assert
        assert priv.scope == "org"
        assert priv.role == "admin"
        assert priv.org_id == TEST_ORG_ID
        assert priv.org_name == "Acme Corp"
        assert priv.msp_id == "msp-id-1"
        assert priv.msp_name == "MSP One"
        assert priv.orggroup_ids == ["grp-1", "grp-2"]
        assert priv.name == "Test Privilege"
        assert priv.site_id == TEST_SITE_ID
        assert priv.sitegroup_ids == ["sg-1"]
        assert priv.views == ["monitoring", "location"]

    def test_partial_dict_sets_defaults_for_missing_fields(self) -> None:
        """Fields not present in the dict should retain their defaults"""
        # Arrange
        data = {"scope": "org", "role": "read"}

        # Act
        priv = _Privilege(data)

        # Assert — supplied values
        assert priv.scope == "org"
        assert priv.role == "read"

        # Assert — default values
        assert priv.org_id == ""
        assert priv.org_name == ""
        assert priv.msp_id == ""
        assert priv.msp_name == ""
        assert priv.orggroup_ids == []
        assert priv.name == ""
        assert priv.site_id == ""
        assert priv.sitegroup_ids == []
        assert priv.views == []

    def test_empty_dict_uses_all_defaults(self) -> None:
        """An empty dict should produce a _Privilege with all default values"""
        # Act
        priv = _Privilege({})

        # Assert
        assert priv.scope == ""
        assert priv.role == ""
        assert priv.org_id == ""
        assert priv.name == ""

    def test_extra_keys_become_attributes(self) -> None:
        """Keys not in the predefined set should still be set as attributes"""
        # Arrange
        data = {"scope": "org", "custom_field": "custom_value"}

        # Act
        priv = _Privilege(data)

        # Assert
        assert priv.scope == "org"
        assert priv.custom_field == "custom_value"

    def test_creation_from_sample_fixture(self, sample_privileges) -> None:
        """Verify creation using the sample_privileges fixture data"""
        # Act
        priv_org = _Privilege(sample_privileges[0])
        priv_site = _Privilege(sample_privileges[1])

        # Assert
        assert priv_org.scope == "org"
        assert priv_org.role == "admin"
        assert priv_org.org_id == TEST_ORG_ID
        assert priv_org.name == "Test Organisation"

        assert priv_site.scope == "site"
        assert priv_site.role == "write"
        assert priv_site.site_id == TEST_SITE_ID
        assert priv_site.org_id == TEST_ORG_ID
        assert priv_site.name == "Test Site"


class TestPrivilegeStr:
    """Test _Privilege.__str__() output"""

    def test_str_includes_non_empty_fields(self) -> None:
        """Non-empty string fields should appear in the output"""
        # Arrange
        data = {
            "scope": "org",
            "role": "admin",
            "org_id": TEST_ORG_ID,
            "name": "My Org",
        }

        # Act
        priv = _Privilege(data)
        result = str(priv)

        # Assert
        assert "scope: org" in result
        assert "role: admin" in result
        assert f"org_id: {TEST_ORG_ID}" in result
        assert "name: My Org" in result

    def test_str_excludes_empty_string_fields(self) -> None:
        """Empty string fields should not appear in the output"""
        # Arrange
        data = {"scope": "org", "role": "admin"}

        # Act
        priv = _Privilege(data)
        result = str(priv)

        # Assert — these fields are empty strings and should be absent
        assert "org_id:" not in result
        assert "org_name:" not in result
        assert "msp_id:" not in result
        assert "msp_name:" not in result
        assert "site_id:" not in result

    def test_str_includes_non_empty_list_fields(self) -> None:
        """Non-empty list fields (orggroup_ids, sitegroup_ids) should appear"""
        # Arrange
        data = {
            "scope": "org",
            "role": "admin",
            "orggroup_ids": ["grp-1"],
            "sitegroup_ids": ["sg-1"],
        }

        # Act
        priv = _Privilege(data)
        result = str(priv)

        # Assert
        assert "orggroup_ids:" in result
        assert "sitegroup_ids:" in result

    def test_str_uses_crlf_separator(self) -> None:
        """Each field line should end with ' \\r\\n'"""
        # Arrange
        data = {"scope": "org", "role": "admin"}

        # Act
        priv = _Privilege(data)
        result = str(priv)

        # Assert
        assert "scope: org \r\n" in result
        assert "role: admin \r\n" in result

    def test_str_empty_privilege(self) -> None:
        """A privilege with all defaults should only contain list fields"""
        # Act
        priv = _Privilege({})
        result = str(priv)

        # Assert - empty strings are excluded but empty lists [] are not ""
        # so orggroup_ids and sitegroup_ids will still appear
        assert "scope:" not in result
        assert "role:" not in result
        assert "org_id:" not in result


class TestPrivilegeGet:
    """Test _Privilege.get() method"""

    def test_get_returns_value_when_present(self) -> None:
        """get() should return the attribute value when it exists and is truthy"""
        # Arrange
        data = {"scope": "org", "role": "admin", "org_id": TEST_ORG_ID}
        priv = _Privilege(data)

        # Act & Assert
        assert priv.get("scope") == "org"
        assert priv.get("role") == "admin"
        assert priv.get("org_id") == TEST_ORG_ID

    def test_get_returns_default_when_key_missing(self) -> None:
        """get() should return the default when the attribute does not exist"""
        # Arrange
        priv = _Privilege({"scope": "org"})

        # Act & Assert
        assert priv.get("nonexistent") is None
        assert priv.get("nonexistent", "fallback") == "fallback"

    def test_get_returns_default_when_value_is_empty_string(self) -> None:
        """get() should return the default when the attribute is an empty string (falsy)"""
        # Arrange
        priv = _Privilege({})  # org_id defaults to ""

        # Act & Assert
        assert priv.get("org_id") is None
        assert priv.get("org_id", "default_org") == "default_org"

    def test_get_returns_default_when_value_is_empty_list(self) -> None:
        """get() should return the default when the attribute is an empty list (falsy)"""
        # Arrange
        priv = _Privilege({})  # views defaults to []

        # Act & Assert
        assert priv.get("views") is None
        assert priv.get("views", ["default_view"]) == ["default_view"]

    def test_get_returns_list_when_non_empty(self) -> None:
        """get() should return the list value when it is non-empty"""
        # Arrange
        data = {"views": ["monitoring", "location"]}
        priv = _Privilege(data)

        # Act & Assert
        assert priv.get("views") == ["monitoring", "location"]

    def test_get_default_parameter_defaults_to_none(self) -> None:
        """get() default parameter should be None when not specified"""
        # Arrange
        priv = _Privilege({})

        # Act & Assert
        assert priv.get("nonexistent") is None


# ===================================================================
# Privileges tests
# ===================================================================
class TestPrivilegesCreation:
    """Test Privileges initialisation"""

    def test_creates_privilege_objects_from_list_of_dicts(self, sample_privileges) -> None:
        """Privileges should wrap each dict into a _Privilege object"""
        # Act
        privs = Privileges(sample_privileges)

        # Assert
        assert len(privs.privileges) == 2
        assert all(isinstance(p, _Privilege) for p in privs.privileges)

    def test_first_entry_matches_source_data(self, sample_privileges) -> None:
        """First _Privilege should carry the values from the first dict"""
        # Act
        privs = Privileges(sample_privileges)

        # Assert
        first = privs.privileges[0]
        assert first.scope == "org"
        assert first.role == "admin"
        assert first.org_id == TEST_ORG_ID
        assert first.name == "Test Organisation"

    def test_second_entry_matches_source_data(self, sample_privileges) -> None:
        """Second _Privilege should carry the values from the second dict"""
        # Act
        privs = Privileges(sample_privileges)

        # Assert
        second = privs.privileges[1]
        assert second.scope == "site"
        assert second.role == "write"
        assert second.site_id == TEST_SITE_ID
        assert second.org_id == TEST_ORG_ID
        assert second.name == "Test Site"

    def test_empty_list_produces_empty_privileges(self) -> None:
        """An empty list should result in an empty privileges list"""
        # Act
        privs = Privileges([])

        # Assert
        assert privs.privileges == []

    def test_single_privilege(self) -> None:
        """A single-element list should produce exactly one _Privilege"""
        # Arrange
        data = [{"scope": "msp", "role": "admin", "msp_id": "msp-1"}]

        # Act
        privs = Privileges(data)

        # Assert
        assert len(privs.privileges) == 1
        assert privs.privileges[0].scope == "msp"
        assert privs.privileges[0].msp_id == "msp-1"


class TestPrivilegesIter:
    """Test Privileges.__iter__()"""

    def test_iter_yields_all_privileges(self, sample_privileges) -> None:
        """Iterating should yield every _Privilege in order"""
        # Arrange
        privs = Privileges(sample_privileges)

        # Act
        result = list(privs)

        # Assert
        assert len(result) == 2
        assert result[0].scope == "org"
        assert result[1].scope == "site"

    def test_iter_returns_privilege_instances(self, sample_privileges) -> None:
        """Each iterated element should be a _Privilege instance"""
        # Arrange
        privs = Privileges(sample_privileges)

        # Act & Assert
        for priv in privs:
            assert isinstance(priv, _Privilege)

    def test_iter_empty_privileges_returns_empty_iterator(self) -> None:
        """Iterating over empty Privileges should produce no elements"""
        # Arrange
        privs = Privileges([])

        # Act
        result = list(privs)

        # Assert
        assert result == []

    def test_iter_can_be_used_in_for_loop(self, sample_privileges) -> None:
        """Privileges should work naturally in a for loop"""
        # Arrange
        privs = Privileges(sample_privileges)
        scopes = []

        # Act
        for priv in privs:
            scopes.append(priv.scope)

        # Assert
        assert scopes == ["org", "site"]

    def test_iter_supports_next(self, sample_privileges) -> None:
        """The iterator returned by __iter__ should support next()"""
        # Arrange
        privs = Privileges(sample_privileges)

        # Act
        it = iter(privs)
        first = next(it)
        second = next(it)

        # Assert
        assert first.scope == "org"
        assert second.scope == "site"

        with pytest.raises(StopIteration):
            next(it)

    def test_iter_supports_generator_expression(self, sample_privileges) -> None:
        """Privileges should work with generator expressions (e.g. next(...))"""
        # Arrange
        privs = Privileges(sample_privileges)

        # Act
        found = next((p for p in privs if p.org_id == TEST_ORG_ID), None)

        # Assert
        assert found is not None
        assert found.org_id == TEST_ORG_ID


class TestPrivilegesStr:
    """Test Privileges.__str__() output"""

    def test_str_produces_tabulate_table(self, sample_privileges) -> None:
        """String output should be a tabulate-formatted table"""
        # Arrange
        privs = Privileges(sample_privileges)

        # Act
        result = str(privs)

        # Assert — column headers should be present
        assert "scope" in result
        assert "role" in result
        assert "name" in result
        assert "site_id" in result
        assert "org_name" in result
        assert "org_id" in result
        assert "msp_name" in result
        assert "msp_id" in result
        assert "views" in result

    def test_str_contains_privilege_data(self, sample_privileges) -> None:
        """The table should contain actual privilege field values"""
        # Arrange
        privs = Privileges(sample_privileges)

        # Act
        result = str(privs)

        # Assert
        assert "org" in result
        assert "admin" in result
        assert "Test Organisation" in result
        assert TEST_ORG_ID in result
        assert "site" in result
        assert "write" in result
        assert "Test Site" in result
        assert TEST_SITE_ID in result

    def test_str_empty_privileges(self) -> None:
        """An empty Privileges should produce just headers (or an empty table)"""
        # Arrange
        privs = Privileges([])

        # Act
        result = str(privs)

        # Assert — tabulate with an empty table and headers produces header row(s)
        # At minimum it should not raise and should be a string
        assert isinstance(result, str)

    def test_str_is_consistent(self, sample_privileges) -> None:
        """Calling str() multiple times should produce the same result"""
        # Arrange
        privs = Privileges(sample_privileges)

        # Act
        result1 = str(privs)
        result2 = str(privs)

        # Assert
        assert result1 == result2


class TestPrivilegesDisplay:
    """Test Privileges.display() method"""

    def test_display_returns_same_as_str(self, sample_privileges) -> None:
        """display() should return exactly the same string as __str__()"""
        # Arrange
        privs = Privileges(sample_privileges)

        # Act
        display_result = privs.display()
        str_result = str(privs)

        # Assert
        assert display_result == str_result

    def test_display_returns_string_type(self, sample_privileges) -> None:
        """display() should return a str"""
        # Arrange
        privs = Privileges(sample_privileges)

        # Act
        result = privs.display()

        # Assert
        assert isinstance(result, str)

    def test_display_empty_privileges(self) -> None:
        """display() on empty Privileges should match str() on empty Privileges"""
        # Arrange
        privs = Privileges([])

        # Act & Assert
        assert privs.display() == str(privs)
