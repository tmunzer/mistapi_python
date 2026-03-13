# tests/unit/test_logger.py
"""
Unit tests for the Console logger and LogSanitizer.

These tests cover sensitive-field redaction, log-level gating,
the LogSanitizer filter, and the _set_log_level helper.
"""

import logging

import pytest

from mistapi.__logger import Console, LogSanitizer, SENSITIVE_FIELDS, logger


# ---------------------------------------------------------------------------
# Sanitization
# ---------------------------------------------------------------------------
class TestConsoleSanitize:
    """Tests for Console.sanitize() redaction logic."""

    def test_redacts_password_double_quotes(self) -> None:
        """A plain 'password' field in double quotes is redacted."""
        c = Console()
        raw = '{"password": "s3cret!"}'
        result = c.sanitize(raw)
        assert "s3cret!" not in result
        assert '******' in result

    def test_redacts_password_single_quotes(self) -> None:
        """A 'password' field wrapped in single quotes is redacted."""
        c = Console()
        raw = "{'password': 'mysecret'}"
        result = c.sanitize(raw)
        assert "mysecret" not in result
        assert '******' in result

    @pytest.mark.parametrize(
        "field",
        SENSITIVE_FIELDS,
        ids=SENSITIVE_FIELDS,
    )
    def test_redacts_every_sensitive_field(self, field: str) -> None:
        """Every entry in SENSITIVE_FIELDS must be redacted."""
        c = Console()
        raw = f'{{"{field}": "topSecret123"}}'
        result = c.sanitize(raw)
        assert "topSecret123" not in result
        assert '******' in result

    def test_redacts_case_insensitively(self) -> None:
        """Field matching is case-insensitive."""
        c = Console()
        raw = '{"PASSWORD": "abc"}'
        result = c.sanitize(raw)
        assert "abc" not in result
        assert '******' in result

    def test_redacts_multiple_fields_in_one_string(self) -> None:
        """Multiple sensitive fields in the same string are all redacted."""
        c = Console()
        raw = '{"password": "pw1", "apitoken": "tok1", "key": "k1"}'
        result = c.sanitize(raw)
        assert "pw1" not in result
        assert "tok1" not in result
        assert "k1" not in result

    def test_no_sensitive_data_unchanged(self) -> None:
        """A string with no sensitive fields is returned unchanged."""
        c = Console()
        raw = '{"name": "Alice", "age": "30"}'
        result = c.sanitize(raw)
        assert result == raw

    def test_non_string_input_dict(self) -> None:
        """A dict is JSON-serialised before sanitisation."""
        c = Console()
        data = {"password": "hunter2", "user": "admin"}
        result = c.sanitize(data)
        assert "hunter2" not in result
        assert "admin" in result
        assert '******' in result

    def test_non_string_input_list(self) -> None:
        """A list containing a dict with sensitive data is sanitised."""
        c = Console()
        data = [{"apitoken": "secret_tok"}]
        result = c.sanitize(data)
        assert "secret_tok" not in result
        assert '******' in result

    def test_non_string_input_int(self) -> None:
        """An integer is serialised and returned as-is (no sensitive data)."""
        c = Console()
        result = c.sanitize(42)
        assert result == "42"

    def test_empty_string(self) -> None:
        """An empty string returns an empty string."""
        c = Console()
        assert c.sanitize("") == ""

    def test_empty_value_still_redacted(self) -> None:
        """A sensitive field whose value is empty is still redacted."""
        c = Console()
        raw = '{"password": ""}'
        result = c.sanitize(raw)
        assert '******' in result


# ---------------------------------------------------------------------------
# Log-level methods (print gating)
# ---------------------------------------------------------------------------
class TestConsoleLogLevelMethods:
    """Each log method should print only when the level threshold is met."""

    # Mapping: (method_name, method_threshold)
    # critical prints at level <= 50
    # error    prints at level <= 40
    # warning  prints at level <= 30
    # info     prints at level <= 20
    # debug    prints at level <= 10
    LOG_METHODS = [
        ("critical", 50),
        ("error", 40),
        ("warning", 30),
        ("info", 20),
        ("debug", 10),
    ]

    @pytest.mark.parametrize("method_name,threshold", LOG_METHODS, ids=[m for m, _ in LOG_METHODS])
    def test_prints_when_level_equals_threshold(self, capsys, method_name, threshold) -> None:
        """Method prints when console level == method threshold."""
        c = Console(level=threshold)
        getattr(c, method_name)("hello")
        captured = capsys.readouterr()
        assert "hello" in captured.out

    @pytest.mark.parametrize("method_name,threshold", LOG_METHODS, ids=[m for m, _ in LOG_METHODS])
    def test_prints_when_level_below_threshold(self, capsys, method_name, threshold) -> None:
        """Method prints when console level is below the method threshold."""
        c = Console(level=max(threshold - 10, 1))
        getattr(c, method_name)("below")
        captured = capsys.readouterr()
        assert "below" in captured.out

    @pytest.mark.parametrize("method_name,threshold", LOG_METHODS, ids=[m for m, _ in LOG_METHODS])
    def test_silent_when_level_above_threshold(self, capsys, method_name, threshold) -> None:
        """Method is silent when console level exceeds the method threshold."""
        c = Console(level=threshold + 10)
        getattr(c, method_name)("nope")
        captured = capsys.readouterr()
        assert captured.out == ""

    @pytest.mark.parametrize("method_name,threshold", LOG_METHODS, ids=[m for m, _ in LOG_METHODS])
    def test_silent_when_level_is_zero(self, capsys, method_name, threshold) -> None:
        """No output at all when level is 0 (disabled)."""
        c = Console(level=0)
        getattr(c, method_name)("disabled")
        captured = capsys.readouterr()
        assert captured.out == ""

    def test_output_sanitised(self, capsys) -> None:
        """Print output has sensitive data redacted."""
        c = Console(level=20)
        c.info('{"password": "oops"}')
        captured = capsys.readouterr()
        assert "oops" not in captured.out
        assert '******' in captured.out

    def test_output_has_bracket_prefix(self, capsys) -> None:
        """All log lines are wrapped with a bracket prefix."""
        c = Console(level=10)
        c.debug("test_msg")
        captured = capsys.readouterr()
        assert captured.out.startswith("[")
        assert "test_msg" in captured.out


# ---------------------------------------------------------------------------
# Default level
# ---------------------------------------------------------------------------
class TestConsoleDefaults:
    """Verify constructor defaults."""

    def test_default_level_is_20(self) -> None:
        c = Console()
        assert c.level == 20

    def test_custom_level(self) -> None:
        c = Console(level=40)
        assert c.level == 40


# ---------------------------------------------------------------------------
# _set_log_level
# ---------------------------------------------------------------------------
class TestSetLogLevel:
    """Tests for _set_log_level() which adjusts both console and logging levels."""

    @pytest.fixture(autouse=True)
    def _restore_logger_level(self):
        """Save and restore the module-level logger level between tests."""
        original = logger.level
        yield
        logger.setLevel(original)

    def test_sets_console_level(self) -> None:
        c = Console(level=20)
        c._set_log_level(console_log_level=40, logging_log_level=10)
        assert c.level == 40

    def test_sets_logging_level(self) -> None:
        c = Console(level=20)
        c._set_log_level(console_log_level=20, logging_log_level=30)
        assert logger.level == 30

    def test_default_arguments(self) -> None:
        c = Console(level=50)
        c._set_log_level()
        assert c.level == 20
        assert logger.level == 10

    def test_set_level_to_zero_disables_console(self, capsys) -> None:
        c = Console(level=20)
        c._set_log_level(console_log_level=0)
        c.critical("should_not_appear")
        captured = capsys.readouterr()
        assert captured.out == ""


# ---------------------------------------------------------------------------
# LogSanitizer filter
# ---------------------------------------------------------------------------
class TestLogSanitizer:
    """Tests for the logging.Filter subclass that redacts sensitive data."""

    def _make_record(self, msg: str, *args) -> logging.LogRecord:
        """Create a minimal LogRecord for testing."""
        record = logging.LogRecord(
            name="mistapi",
            level=logging.INFO,
            pathname="",
            lineno=0,
            msg=msg,
            args=args if args else None,
            exc_info=None,
        )
        return record

    def test_filter_returns_true(self) -> None:
        """The filter never drops records; it always returns True."""
        f = LogSanitizer()
        record = self._make_record("safe message")
        assert f.filter(record) is True

    def test_filter_sanitises_message(self) -> None:
        """Sensitive data inside the message is replaced."""
        f = LogSanitizer()
        record = self._make_record('{"password": "leak"}')
        f.filter(record)
        assert "leak" not in record.msg
        assert '******' in record.msg

    def test_filter_clears_args(self) -> None:
        """record.args is set to None after filtering."""
        f = LogSanitizer()
        record = self._make_record("value is %s", "something")
        assert record.args is not None
        f.filter(record)
        assert record.args is None

    def test_filter_handles_format_args(self) -> None:
        """getMessage() expands %-formatting; filter sees the expanded string."""
        f = LogSanitizer()
        record = self._make_record(
            '{"apitoken": "%s"}', "my_secret_token"
        )
        # Before filtering, getMessage() should expand the arg
        expanded = record.getMessage()
        assert "my_secret_token" in expanded

        f.filter(record)
        assert "my_secret_token" not in record.msg
        assert '******' in record.msg

    def test_filter_safe_message_unchanged(self) -> None:
        """A record without sensitive data passes through with its message intact."""
        f = LogSanitizer()
        record = self._make_record("just a normal log line")
        f.filter(record)
        assert record.msg == "just a normal log line"
        assert record.args is None


# ---------------------------------------------------------------------------
# Module-level singletons
# ---------------------------------------------------------------------------
class TestModuleLevelObjects:
    """The module exposes pre-built console and logger objects."""

    def test_module_console_exists(self) -> None:
        from mistapi.__logger import console as mod_console
        assert isinstance(mod_console, Console)

    def test_module_logger_name(self) -> None:
        assert logger.name == "mistapi"

    def test_module_logger_has_sanitizer_filter(self) -> None:
        filters = logger.filters
        assert any(isinstance(f, LogSanitizer) for f in filters)

    def test_module_logger_level_is_integer(self) -> None:
        """Logger level is always a valid integer (may be mutated by other tests)."""
        assert isinstance(logger.level, int)
        assert logger.level >= 0
