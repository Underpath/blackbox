import configparser
import os
from sys import exit


BLACKBOX_DIR = os.path.abspath(os.path.join(os.getenv("HOME"), '.blackbox/'))
CONFIG_FILE = os.path.join(BLACKBOX_DIR, 'config.cfg')
BLOCKSIZE = 65536


def get_option(option, section, option_type='str'):
    """
    Grabs the value of the option from the config file and returns it in the
    format requested.
    """

    try:
        option_value = config.get(section, option)
    except configparser.NoOptionError:
        return False
    if option_type == 'str':
        return option_value
    elif option_type == 'str_list':
        return option_value.split(',')
    elif option_type == 'int_list':
        return map(int, option_value.split(','))


def get_path(path_type, section, filename=None):
    path = get_option(path_type, section)

    if not path or not os.path.isdir(path):
        path = BLACKBOX_DIR

    if filename:
        path = os.path.join(path, filename)

    return path


def check_config_file():
    """
    Check if the config file exists, exits otherwise.
    """
    if not os.path.isfile(CONFIG_FILE):
        print('Config file not found. Exiting...')
        exit()


check_config_file()
config = configparser.ConfigParser()
config.read(CONFIG_FILE)

COMPRESSED_FILENAME = '{}.tar.gz'.format(get_option('filename', 'General'))
ENCRYPTED_FILENAME = '{}.gpg'.format(COMPRESSED_FILENAME)
COMPRESSED_FILE_PATH = get_path('staging_path', 'General', COMPRESSED_FILENAME)
ENCRYPTED_FILE_PATH = '{}.gpg'.format(COMPRESSED_FILE_PATH)
