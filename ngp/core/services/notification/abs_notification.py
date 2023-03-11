import abc
from ngp.core.models.ngp_enums import NotificationType


class BorgNotify:

    _notify_config = dict()

    def __init__(self):
        self.__dict__ = self._notify_config


class AbsNotification(abc.ABC):

    @abc.abstractmethod
    def notify(self,
               notification_type: NotificationType = NotificationType.INFO,
               job_detail: dict = None,
               message: str = None,
               audience: list = None):
        pass
