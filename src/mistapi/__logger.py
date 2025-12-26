"""
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
"""

import json
import logging
import os
import re

os.system("")  # nosec bandit B605 B607

SENSITIVE_FIELDS = [
    "secret",
    "mesh_psk",
    "psk",
    "default_psk",
    "broadnet_password",
    "gupshup_password",
    "lte_password",
    "password",
    "poser_password",
    "puzzel_password",
    "authentication_password",
    "encryption_password",
    "root_password",
    "mist_password",
    "apitoken",
    "cp_api_key",
    "ecm_api_key",
    "key",
    "fips_zeroize_password",
    "passphrase",
    "old_passphrase",
    "oauth2_client_secret",
    "oauth2_password",
    "splunk_token",
    "conductor_token",
]


def magenta(text):
    """
    Docstring for magenta

    :param text: Description
    """
    return "\033[0;35m" + text + "\033[0m"


def red(text):
    """
    Docstring for red

    :param text: Description
    """
    return "\033[0;31m" + text + "\033[0m"


def yellow(text):
    """
    Docstring for yellow

    :param text: Description
    """
    return "\033[0;33m" + text + "\033[0m"


def green(text):
    """
    Docstring for green

    :param text: Description
    """
    return "\033[0;32m" + text + "\033[0m"


def white(text):
    """
    Docstring for white

    :param text: Description
    """
    return "\033[0;37m" + text + "\033[0m"


def cyan(text):
    """
    Docstring for cyan

    :param text: Description
    """
    return "\033[0;36m" + text + "\033[0m"


def blue(text):
    """
    Docstring for blue

    :param text: Description
    """
    return "\033[0;34m" + text + "\033[0m"


class Console:
    """
    Console class for logging messages to the console with different log levels
    and sanitizing sensitive fields in the messages.
    """

    def __init__(self, level: int = 20) -> None:
        self.level: int = level
        self.sensitive_fields = SENSITIVE_FIELDS
        # compile regex pattern to match sensitive fields
        # example pattern: r'("password"\s*:\s*)"(.*?)"'
        # matches "password": "value"
        # and captures "password": and "value" separately
        # to replace "value" with "******"
        # case insensitive
        self.sensitive_pattern = re.compile(
            r'(["\']('
            + "|".join(self.sensitive_fields)
            + r')["\']?\s*:\s*)["\']([^"\']*)["\']',
            re.IGNORECASE,
        )

    def sanitize(self, data) -> str:
        """
        sanitize sensitive fields in a dictionary or string

        PARAMS
        -----------
        data : str

        RETURNS
        -----------
        sanitized data : str
        """
        if not isinstance(data, str):
            data_str = json.dumps(data)
        else:
            data_str = str(data)
        sanitized_data = self.sensitive_pattern.sub(r'\1"******"', data_str)
        return sanitized_data

    def critical(self, message) -> None:
        """
        Docstring for critical

        :param self: Description
        :param message: Description
        :type message: str
        """
        if self.level <= 50 and self.level > 0:
            print(f"[{magenta('CRITICAL ')}] {self.sanitize(message)}")

    def error(self, message) -> None:
        """
        Docstring for error

        :param self: Description
        :param message: Description
        :type message: str
        """
        if self.level <= 40 and self.level > 0:
            print(f"[{red('  ERROR  ')}] {self.sanitize(message)}")

    def warning(self, message) -> None:
        """
        Docstring for warning

        :param self: Description
        :param message: Description
        :type message: str
        """
        if self.level <= 30 and self.level > 0:
            print(f"[{yellow(' WARNING ')}] {self.sanitize(message)}")

    def info(self, message) -> None:
        """
        Docstring for info

        :param self: Description
        :param message: Description
        :type message: str
        """
        if self.level <= 20 and self.level > 0:
            print(f"[{green('  INFO   ')}] {self.sanitize(message)}")

    def debug(self, message) -> None:
        """
        Docstring for debug

        :param self: Description
        :param message: Description
        :type message: str
        """
        if self.level <= 10 and self.level > 0:
            print(f"[{white('DEBUG  ')}] {self.sanitize(message)}")

    def _set_log_level(
        self, console_log_level: int = 20, logging_log_level: int = 10
    ) -> None:
        """
        set console and logging log level

        PARAMS
        -----------
        console_log_level : int, default: 20
        logging_log_level : int, default: 10

        Values:
        50 -> CRITICAL
        40 -> ERROR
        30 -> WARNING
        20 -> INFO
        10 -> DEBUG
        0  -> DISABLED
        """
        self.level = console_log_level
        logger.setLevel(logging_log_level)


class LogSanitizer(logging.Filter):
    """
    Logging filter that sanitizes sensitive fields in log messages
    """

    def __init__(self):
        super().__init__()
        self.console = Console()

    def filter(self, record):
        record.msg = self.console.sanitize(record.msg)
        return True


console = Console()
logger = logging.getLogger("mistapi")
logger.setLevel(logging.DEBUG)
logger.addFilter(LogSanitizer())
