import abc


class BorgLogger:

    _logger_config = dict()

    def __init__(self):
        self.__dict__ = self._logger_config


class AbsLogger(abc.ABC):

    @abc.abstractmethod
    def get_logger(self):
        pass
