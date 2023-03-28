import abc


class BorgCFG:
    """
    Singleton parent for Configuration Handler
    """
    _cfg_config = dict()

    def __init__(self):
        self.__dict__ = self._cfg_config


class AbsCFG(abc.ABC):
    """
    Abstract Configuration Handler
    """

    @abc.abstractmethod
    def get_cfg(self,
                cfg_key: str = None) -> dict:
        pass
