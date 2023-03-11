"""
    default_logger.py
    -------

    This module configure logging service if not configured and return logger.
"""
from ngp.core.services.logging.abs_logging import AbsLogger, BorgLogger
from ngp.utils.navigation import get_path
import logging
import logging.config


class DefaultLogger(AbsLogger, BorgLogger):
    """
    Fetch configuration from file based configuration repository.
    NOTE:
        1. Configuration file should be present.
    """

    def __init__(self):
        BorgLogger.__init__(self)
        if not self._logger_config:
            ngp_log_cfg_file = get_path('ngp/core/services/config/static/logging.ini')
            logging.config.fileConfig(
                ngp_log_cfg_file,
                disable_existing_loggers=False
            )
            self._logger_config = {"log_file": ngp_log_cfg_file}

    def get_logger(self) -> logging:
        """
        Returns logger.

        :return: Logger.
        """

        return logging.getLogger(__name__)
