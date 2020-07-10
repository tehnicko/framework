from six.moves import configparser
from os import path
import sys
import os

from run_test import CONFIG_PATH

current_dir = path.dirname(path.realpath(__file__))


class EnvConfiguration():
    def __init__(self, CONFIG_PATH, section):
        parser = configparser.ConfigParser()
        found = parser.read(CONFIG_PATH)
        self.section = section
        if not found:
            sys.exit('Error: Config file not found: %s' % (CONFIG_PATH))
        self.config = configparser.ConfigParser()
        self.config.read(CONFIG_PATH)

    def get(self, option):
        if self.config.has_option(self.section, option):
            return self.config.get(self.section, option)
        else:
            sys.exit(
                'Error: Option \'%s\' not found in configuration.' % (option)
            )


# Get TEST_ENV environment variable
try:
    env = os.environ["TEST_ENV"]
except KeyError:
    env = "tst"

# Read configuration for env
env_config = EnvConfiguration(CONFIG_PATH, env)
