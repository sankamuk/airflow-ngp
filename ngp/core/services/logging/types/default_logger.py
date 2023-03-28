"""
    default_logger.py
    -------

    This module configure logging service if not configured and return logger
"""
from ngp.core.services.logging.abs_logging import AbsLogger, BorgLogger
from ngp.utils.navigation import get_path
import logging
import logging.config


class DefaultLogger(AbsLogger, BorgLogger):
    """
    Logger which uses Python's logging framework

    .. admonition:: Note
        * Logger can be configured using file ngp/core/services/config/static/logging.ini
        * Default setting allows console logging of verbosity INFO
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
        Returns logger object, this can be used to log

        :return: Logger object of type :module:`logging`
        """

        return logging.getLogger(__name__)
