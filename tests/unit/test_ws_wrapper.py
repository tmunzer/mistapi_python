# tests/unit/test_ws_wrapper.py
"""
Unit tests for WebSocketWrapper._extract_raw() — ANSI stripping (stream mode)
and VT100 screen-buffer rendering (screen mode).
"""

from unittest.mock import Mock

from mistapi.device_utils.__tools.__ws_wrapper import (
    WebSocketWrapper,
    UtilResponse,
    _VT100Screen,
)


def _make_wrapper():
    """Create a minimal WebSocketWrapper for testing _extract_raw."""
    session = Mock()
    util_response = UtilResponse()
    return WebSocketWrapper(session, util_response)


# ------------------------------------------------------------------
# Stream-mode tests (no cursor positioning → ANSI strip)
# ------------------------------------------------------------------
class TestExtractRawStreamMode:
    """Messages without cursor positioning use simple ANSI stripping."""

    def test_preserves_plain_text(self) -> None:
        wrapper = _make_wrapper()
        msg = {"raw": "64 bytes from 8.8.8.8: icmp_seq=1 ttl=118 time=12.3 ms"}
        result = wrapper._extract_raw(msg)
        assert result == "64 bytes from 8.8.8.8: icmp_seq=1 ttl=118 time=12.3 ms"

    def test_strips_sgr_color_codes(self) -> None:
        wrapper = _make_wrapper()
        msg = {"raw": "text\x1b[0m here\x1b[1;32m green"}
        result = wrapper._extract_raw(msg)
        assert result == "text here green"

    def test_strips_character_set_designations(self) -> None:
        wrapper = _make_wrapper()
        msg = {"raw": "hello\x1b(Bworld"}
        result = wrapper._extract_raw(msg)
        assert result == "helloworld"

    def test_nested_data_event_stripped(self) -> None:
        wrapper = _make_wrapper()
        msg = {"event": "data", "data": {"raw": "text\x1b[0m here"}}
        result = wrapper._extract_raw(msg)
        assert result == "text here"

    def test_pcap_dict_unaffected(self) -> None:
        wrapper = _make_wrapper()
        msg = {"pcap_dict": {"packet": "data"}}
        result = wrapper._extract_raw(msg)
        assert result == {"packet": "data"}


# ------------------------------------------------------------------
# Screen-mode tests (cursor positioning detected → VT100 screen buffer)
# ------------------------------------------------------------------
class TestExtractRawScreenMode:
    """Messages with cursor positioning / clear-screen use the VT100 buffer."""

    def test_activates_on_cursor_home(self) -> None:
        wrapper = _make_wrapper()
        msg = {"raw": "\x1b[H\x1b[2JHello World"}
        wrapper._extract_raw(msg)
        assert wrapper._screen_mode is True
        assert wrapper._screen is not None

    def test_renders_clear_screen_then_text(self) -> None:
        wrapper = _make_wrapper()
        msg = {"raw": "\x1b[H\x1b[2JLine1\r\nLine2"}
        result = wrapper._extract_raw(msg)
        assert "Line1" in result
        assert "Line2" in result

    def test_cursor_positioning_places_text(self) -> None:
        wrapper = _make_wrapper()
        # Row 1 col 1: "A", then row 2 col 5: "B"
        msg = {"raw": "\x1b[1;1HA\x1b[2;5HB"}
        result = wrapper._extract_raw(msg)
        lines = result.split("\n")
        assert lines[0] == "A"
        assert lines[1] == "    B"

    def test_in_place_update_overwrites(self) -> None:
        """Subsequent messages update the screen buffer in place."""
        wrapper = _make_wrapper()
        # First message: draw initial screen
        wrapper._extract_raw({"raw": "\x1b[H\x1b[2J\x1b[1;1HOLD VALUE"})
        # Second message: overwrite at same position
        result = wrapper._extract_raw({"raw": "\x1b[1;1HNEW VALUE"})
        lines = result.split("\n")
        assert lines[0] == "NEW VALUE"
        assert "OLD" not in lines[0]

    def test_clear_line_erases_content(self) -> None:
        wrapper = _make_wrapper()
        wrapper._extract_raw({"raw": "\x1b[1;1HFull line of text"})
        result = wrapper._extract_raw({"raw": "\x1b[1;1H\x1b[2K"})
        lines = result.split("\n")
        # Line 1 should be empty after clear
        assert lines[0] == "" if lines else True

    def test_stream_mode_not_activated_by_plain_text(self) -> None:
        wrapper = _make_wrapper()
        wrapper._extract_raw({"raw": "no escape codes here"})
        assert wrapper._screen_mode is False
        assert wrapper._screen is None


# ------------------------------------------------------------------
# _VT100Screen unit tests
# ------------------------------------------------------------------
class TestVT100Screen:
    """Direct tests for the _VT100Screen class."""

    def test_simple_text(self) -> None:
        s = _VT100Screen(rows=5, cols=20)
        s.feed("Hello")
        assert s.render() == "Hello"

    def test_newline(self) -> None:
        s = _VT100Screen(rows=5, cols=20)
        s.feed("A\nB\nC")
        assert s.render() == "A\nB\nC"

    def test_carriage_return_newline(self) -> None:
        s = _VT100Screen(rows=5, cols=20)
        s.feed("A\r\nB")
        assert s.render() == "A\nB"

    def test_cursor_position(self) -> None:
        s = _VT100Screen(rows=5, cols=20)
        s.feed("\x1b[3;10Hx")
        lines = s.render().split("\n")
        assert len(lines) >= 3
        assert lines[2][9] == "x"

    def test_cursor_home(self) -> None:
        s = _VT100Screen(rows=5, cols=20)
        s.feed("AAAA\x1b[HB")
        lines = s.render().split("\n")
        assert lines[0].startswith("BAAA")

    def test_clear_screen(self) -> None:
        s = _VT100Screen(rows=5, cols=20)
        s.feed("old text\x1b[2Jnew")
        rendered = s.render()
        assert "old" not in rendered
        assert "new" in rendered

    def test_cursor_movement(self) -> None:
        s = _VT100Screen(rows=5, cols=20)
        s.feed("\x1b[1;1HABCDE")
        # Move back 3
        s.feed("\x1b[3DX")
        lines = s.render().split("\n")
        assert lines[0] == "ABXDE"

    def test_erase_to_end_of_line(self) -> None:
        s = _VT100Screen(rows=5, cols=20)
        s.feed("Hello World")
        s.feed("\x1b[1;6H\x1b[K")  # Position at col 6, erase to EOL
        assert s.render() == "Hello"

    def test_sgr_ignored(self) -> None:
        s = _VT100Screen(rows=5, cols=20)
        s.feed("\x1b[1;32mGreen\x1b[0m")
        assert s.render() == "Green"

    def test_null_bytes_ignored(self) -> None:
        s = _VT100Screen(rows=5, cols=20)
        s.feed("\x00Hello\x00")
        assert s.render() == "Hello"

    def test_render_trims_trailing_spaces_and_empty_lines(self) -> None:
        s = _VT100Screen(rows=5, cols=20)
        s.feed("A")
        rendered = s.render()
        assert rendered == "A"
        assert not rendered.endswith(" ")


# ------------------------------------------------------------------
# ws_error / ws_close_code (issue #29): let consumers distinguish a clean
# WebSocket completion from an errored / abnormal / never-started one.
# ------------------------------------------------------------------
class TestUtilResponseWsErrorDefaults:
    def test_defaults_are_none(self) -> None:
        r = UtilResponse()
        assert r.ws_error is None
        assert r.ws_close_code is None


class TestOnError:
    def test_records_first_error(self) -> None:
        w = _make_wrapper()
        w._on_error(Exception("boom"))
        assert w.util_response.ws_error == "boom"

    def test_does_not_overwrite_existing(self) -> None:
        w = _make_wrapper()
        w._on_error(Exception("first"))
        w._on_error(Exception("second"))
        assert w.util_response.ws_error == "first"


class TestOnClose:
    def test_normal_close_is_clean(self) -> None:
        w = _make_wrapper()
        w._on_close(1000, "")
        assert w.util_response.ws_close_code == 1000
        assert w.util_response.ws_error is None

    def test_abnormal_close_sets_error(self) -> None:
        w = _make_wrapper()
        w._on_close(1006, "abnormal closure")
        assert w.util_response.ws_close_code == 1006
        assert "1006" in (w.util_response.ws_error or "")

    def test_no_status_close_is_not_flagged(self) -> None:
        w = _make_wrapper()
        w._on_close(None, "")
        assert w.util_response.ws_close_code is None
        assert w.util_response.ws_error is None


class TestStartWithTriggerWsError:
    """A WS-backed command whose WebSocket never starts must record ws_error so it
    is not mistaken for a clean trigger-only completion."""

    @staticmethod
    def _trigger(status: int = 200, data=None):
        return Mock(status_code=status, data=data if data is not None else {})

    def test_ws_factory_returning_none_sets_ws_error(self) -> None:
        w = _make_wrapper()
        w.start_with_trigger(
            trigger_fn=lambda: self._trigger(),
            ws_factory_fn=lambda trigger: None,
        )
        w.util_response.wait(timeout=5)
        assert w.util_response.done
        assert w.util_response.ws_required is False  # WS never started
        assert w.util_response.ws_error == "WebSocket factory returned None"

    def test_ws_factory_raising_sets_ws_error(self) -> None:
        def boom(trigger):
            raise RuntimeError("factory kaboom")

        w = _make_wrapper()
        w.start_with_trigger(trigger_fn=lambda: self._trigger(), ws_factory_fn=boom)
        w.util_response.wait(timeout=5)
        assert w.util_response.done
        assert "factory kaboom" in (w.util_response.ws_error or "")
