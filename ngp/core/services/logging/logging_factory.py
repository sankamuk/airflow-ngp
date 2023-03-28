"""
    logging_factory.py
    -------

    This module setup logging service
"""
from ngp.utils.navigation import get_module, init_class


def get_logger_service(log_type: str = 'default_logger'):
    """
    Creates a Logging Service which can be used to return logger

    :param log_type: String representing type of Logging backend, example::
        default_logger
    :return: Object implementing :class:`ngp.core.services.logging.abs_logging.AbsLogger`
    """
    cls_name = get_module("services", "logging")[log_type]
    log_service = init_class("services", "logging", log_type, cls_name)
    return log_service.get_logger()
