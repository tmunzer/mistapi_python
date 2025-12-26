import logging

import mistapi
from mistapi.__logger import LogSanitizer

LOG_FILE = "./log.txt"
logging.basicConfig(filename=LOG_FILE, filemode="w")
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
LOGGER.addFilter(LogSanitizer())
a = mistapi.APISession(env_file="~/.mist_env")
a.login()
b = mistapi.api.v1.self.apitokens.createApiToken(a, body={"name": "mistapi_test"})

LOGGER.debug("This is a debug message")
LOGGER.debug(b.data)
