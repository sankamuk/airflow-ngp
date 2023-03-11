"""
    ngp_environment.py
    -------

    This module helps in different functionality related to get/set of NGP environment property.
"""
import os
import configparser


def init_environment():
    """
    Setup NGP environment.

    :return: None
    """
    config = configparser.ConfigParser()
    ngp_cfg_file = os.path.join(os.environ.get('NGP_HOME', None), 'ngp/config/defaults.cfg')
    config.read(ngp_cfg_file)
    for sec in config.sections():
        for ky in config[sec]:
            os_environ_key = "{}.{}".format(sec, ky).replace('.', '_').upper()
            os_environ_value = config[sec][ky]
            os.environ[os_environ_key] = os_environ_value


def lookup_environment(env_key: str) -> str:
    """
    Lookup in environment for configuration.

    :param env_key: Environment configuration key
    :return: Environment configuration value for the key supplied, else None
    """
    # return os.environ.get(env_key, None)
    if env_key == 'NGP_SERVICE_CONFIG_BACKEND':
        return 'local_cfg'
    elif env_key == 'NGP_SERVICE_NOTIFICATION_CFG':
        return 'email_config'
    elif env_key == 'NGP_HOME':
        return 'C:\\Users\\HP\\OneDrive\\Desktop\\work\\airflow-ngp'
    elif env_key == 'NGP_SERVICE_NOTIFICATION_ALLOW':
        return 'INFO,WARNING,ERROR'


def dump_environment(file_name: str):
    """
    Dump environment into a config file.

    :param file_name: File name to dump the NGP environment.
    :return: None
    """
    with open(file_name, 'w') as f:
        for env_key in os.environ:
            if env_key.startswith("NGP_"):
                f.writelines("{}={}".format(env_key, os.environ[env_key]))

