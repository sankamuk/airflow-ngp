import abc


class BorgLogger:
    """
    Singleton parent for Log Handler
    """
    _logger_config = dict()

    def __init__(self):
        self.__dict__ = self._logger_config


class AbsLogger(abc.ABC):
    """
    Abstract Log Handler
    """
    @abc.abstractmethod
    def get_logger(self):
        pass
