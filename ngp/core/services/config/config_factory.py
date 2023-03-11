"""
    config_factory.py
    -------

    This module creates configuration service object.
"""
from ngp.utils.navigation import get_module, init_class


def get_config_service(cfg_type: str = 'local_cfg'):
    """
    Creates a Configuration Service which can be used to return configuration value with a key.

    :param cfg_type: Type of configuration backend. default -> local_cfg (file based config)
    :return: Configuration Service Object.
    """
    cls_name = get_module("services", "config")[cfg_type]
    return init_class("services", "config", cfg_type, cls_name)
