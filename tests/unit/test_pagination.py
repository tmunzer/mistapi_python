"""
Unit tests for mistapi.__pagination module.

Tests the get_next() and get_all() pagination helper functions using
mocked APISession and APIResponse objects.
"""

from unittest.mock import Mock

from mistapi.__pagination import get_all, get_next


def _make_response(data, next_url=None):
    """Create a mock APIResponse with the given data and next link."""
    response = Mock()
    response.data = data
    response.next = next_url
    return response


class TestGetNext:
    """Tests for get_next()."""

    def test_calls_mist_get_when_next_exists(self):
        """get_next() should call mist_session.mist_get with response.next."""
        session = Mock()
        next_url = "/api/v1/sites?page=2"
        response = _make_response(data=[], next_url=next_url)
        expected = _make_response(data=[{"id": "second"}])
        session.mist_get.return_value = expected

        result = get_next(session, response)

        session.mist_get.assert_called_once_with(next_url)
        assert result is expected

    def test_returns_none_when_next_is_none(self):
        """get_next() should return None when response.next is None."""
        session = Mock()
        response = _make_response(data=[], next_url=None)

        result = get_next(session, response)

        assert result is None
        session.mist_get.assert_not_called()

    def test_returns_none_when_next_is_empty_string(self):
        """get_next() should return None when response.next is an empty string."""
        session = Mock()
        response = _make_response(data=[], next_url="")

        result = get_next(session, response)

        assert result is None
        session.mist_get.assert_not_called()


class TestGetAllList:
    """Tests for get_all() when response.data is a list."""

    def test_single_page_returns_data(self):
        """get_all() should return the list data as-is when there is no next page."""
        session = Mock()
        items = [{"id": "a"}, {"id": "b"}]
        response = _make_response(data=items, next_url=None)

        result = get_all(session, response)

        assert result == items
        session.mist_get.assert_not_called()

    def test_single_page_returns_copy(self):
        """get_all() should return a new list, not the original reference."""
        session = Mock()
        items = [{"id": "a"}]
        response = _make_response(data=items, next_url=None)

        result = get_all(session, response)

        assert result == items
        assert result is not items

    def test_multi_page_concatenates(self):
        """get_all() should follow next links and concatenate all pages."""
        session = Mock()

        page1 = _make_response(
            data=[{"id": "1"}, {"id": "2"}],
            next_url="/api/v1/items?page=2",
        )
        page2 = _make_response(
            data=[{"id": "3"}, {"id": "4"}],
            next_url="/api/v1/items?page=3",
        )
        page3 = _make_response(
            data=[{"id": "5"}],
            next_url=None,
        )

        session.mist_get.side_effect = [page2, page3]

        result = get_all(session, page1)

        assert result == [
            {"id": "1"},
            {"id": "2"},
            {"id": "3"},
            {"id": "4"},
            {"id": "5"},
        ]
        assert session.mist_get.call_count == 2

    def test_empty_list_returns_empty(self):
        """get_all() should return an empty list for an empty first page."""
        session = Mock()
        response = _make_response(data=[], next_url=None)

        result = get_all(session, response)

        assert result == []

    def test_empty_list_with_next_follows_links(self):
        """get_all() should still follow next even when the first page is empty."""
        session = Mock()

        page1 = _make_response(data=[], next_url="/api/v1/items?page=2")
        page2 = _make_response(data=[{"id": "1"}], next_url=None)
        session.mist_get.return_value = page2

        result = get_all(session, page1)

        assert result == [{"id": "1"}]


class TestGetAllDict:
    """Tests for get_all() when response.data is a dict with 'results' key."""

    def test_single_page_extracts_results(self):
        """get_all() should extract and return the 'results' list from a dict response."""
        session = Mock()
        items = [{"id": "a"}, {"id": "b"}]
        response = _make_response(
            data={"results": items, "total": 2, "limit": 100},
            next_url=None,
        )

        result = get_all(session, response)

        assert result == items
        session.mist_get.assert_not_called()

    def test_single_page_returns_copy(self):
        """get_all() should return a copy of results, not the original."""
        session = Mock()
        items = [{"id": "a"}]
        response = _make_response(
            data={"results": items},
            next_url=None,
        )

        result = get_all(session, response)

        assert result == items
        assert result is not items

    def test_multi_page_concatenates_results(self):
        """get_all() should follow next links and concatenate results from dict responses."""
        session = Mock()

        page1 = _make_response(
            data={"results": [{"id": "1"}], "total": 3, "limit": 1},
            next_url="/api/v1/items?page=2",
        )
        page2 = _make_response(
            data={"results": [{"id": "2"}], "total": 3, "limit": 1},
            next_url="/api/v1/items?page=3",
        )
        page3 = _make_response(
            data={"results": [{"id": "3"}], "total": 3, "limit": 1},
            next_url=None,
        )

        session.mist_get.side_effect = [page2, page3]

        result = get_all(session, page1)

        assert result == [{"id": "1"}, {"id": "2"}, {"id": "3"}]
        assert session.mist_get.call_count == 2

    def test_empty_results_returns_empty(self):
        """get_all() should return an empty list when results is empty."""
        session = Mock()
        response = _make_response(
            data={"results": [], "total": 0},
            next_url=None,
        )

        result = get_all(session, response)

        assert result == []

    def test_empty_results_with_next_follows_links(self):
        """get_all() should follow next even when the first page results are empty."""
        session = Mock()

        page1 = _make_response(
            data={"results": []},
            next_url="/api/v1/items?page=2",
        )
        page2 = _make_response(
            data={"results": [{"id": "1"}]},
            next_url=None,
        )
        session.mist_get.return_value = page2

        result = get_all(session, page1)

        assert result == [{"id": "1"}]


class TestGetAllEdgeCases:
    """Tests for get_all() edge cases and unsupported data types."""

    def test_dict_without_results_key_returns_empty(self):
        """get_all() should return empty list when data is a dict without 'results'."""
        session = Mock()
        response = _make_response(
            data={"items": [1, 2, 3]},
            next_url=None,
        )

        result = get_all(session, response)

        assert result == []

    def test_non_list_non_dict_returns_empty(self):
        """get_all() should return empty list for unsupported data types."""
        session = Mock()
        response = _make_response(data="some string", next_url=None)

        result = get_all(session, response)

        assert result == []

    def test_none_data_returns_empty(self):
        """get_all() should return empty list when data is None."""
        session = Mock()
        response = _make_response(data=None, next_url=None)

        result = get_all(session, response)

        assert result == []

    def test_get_next_returns_none_on_last_page(self):
        """get_all() should stop when get_next returns None (no more pages)."""
        session = Mock()

        # Simulate: page1 has next, page2 does not.
        page1 = _make_response(
            data=[{"id": "1"}],
            next_url="/api/v1/items?page=2",
        )
        page2 = _make_response(
            data=[{"id": "2"}],
            next_url=None,
        )
        session.mist_get.return_value = page2

        result = get_all(session, page1)

        assert result == [{"id": "1"}, {"id": "2"}]
        session.mist_get.assert_called_once_with("/api/v1/items?page=2")

    def test_does_not_mutate_original_response(self):
        """get_all() should not modify the original response object's data."""
        session = Mock()
        original_items = [{"id": "1"}, {"id": "2"}]
        response = _make_response(data=original_items, next_url=None)

        get_all(session, response)

        assert response.data == [{"id": "1"}, {"id": "2"}]

    def test_dict_does_not_mutate_original_results(self):
        """get_all() should not mutate the original results list in a dict response."""
        session = Mock()
        original_results = [{"id": "1"}]
        response = _make_response(
            data={"results": original_results},
            next_url=None,
        )

        result = get_all(session, response)

        assert original_results == [{"id": "1"}]
        assert result is not original_results
