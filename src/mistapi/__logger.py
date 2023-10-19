'''
--------------------------------------------------------------------------------
------------------------- Mist API Python CLI Session --------------------------

    Written by: Thomas Munzer (tmunzer@juniper.net)
    Github    : https://github.com/tmunzer/mistapi_python

    This package is licensed under the MIT License.

--------------------------------------------------------------------------------
'''
import logging
import os
os.system("")

def magenta(text):
    return '\033[0;35m' + text + '\033[0m'
def red(text):
    return '\033[0;31m' + text + '\033[0m'
def yellow(text):
    return '\033[0;33m' + text + '\033[0m'
def green(text):
    return '\033[0;32m' + text + '\033[0m'
def white(text):
    return '\033[0;37m' + text + '\033[0m'
def cyan(text):
    return '\033[0;36m' + text + '\033[0m'
def blue(text):
    return '\033[0;34m' + text + '\033[0m'

class Console:

    def __init__(self, level:int=20):
        self.level = level

    def critical(self, message:str) -> None:
        if self.level <= 50 and self.level > 0:
            print(f"[{magenta('CRITICAL ')}] {message}")

    def error(self, message:str) -> None:
        if self.level <= 40 and self.level > 0:
            print(f"[{red('  ERROR  ')}] {message}")

    def warning(self, message:str) -> None:
        if self.level <= 30 and self.level > 0:
            print(f"[{yellow(' WARNING ')}] {message}")

    def info(self, message:str) -> None:
        if self.level <= 20 and self.level > 0:
            print(f"[{green('  INFO   ')}] {message}")

    def debug(self, message:str) -> None:
        if self.level <= 10 and self.level > 0:
            print(f"[{white('DEBUG  ')}] {message}")


    def _set_log_level(self,console_log_level:str=20, logging_log_level:int=10) -> None:
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


console = Console()
logger = logging.getLogger("mistapi")
logger.setLevel(logging.DEBUG)



