"""
    abs_notification.py
    -------

    This module contains parent class for defining Notification handler
"""
import abc
from ngp.core.models.ngp_enums import NotificationType


class BorgNotify:
    """
    Singleton parent for Notification handler
    """
    _notify_config = dict()

    def __init__(self):
        self.__dict__ = self._notify_config


class AbsNotification(abc.ABC):
    """
    Abstract Notification Handler
    """
    @abc.abstractmethod
    def notify(self,
               notification_type: NotificationType = NotificationType.INFO,
               job_detail: dict = None,
               message: str = None,
               audience: list = None):
        pass
