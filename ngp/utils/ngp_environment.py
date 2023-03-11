"""
    ngp_environment.py
    -------

    This module helps in different functionality related to get/set of NGP environment property.
"""
import os


def init_environment():
    pass


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
    pass
