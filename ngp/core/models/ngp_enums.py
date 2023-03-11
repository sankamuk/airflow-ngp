"""
    ngp_enums.py
    -------

    This module contains all ENUM types for NGP framework.
"""
import enum


# Notification Type
class NotificationType(enum.Enum):
    """
    Notification Types

    INFO        - Information based notification
    WARNING     - Warning based notification
    ERROR       - Error based notification
    """
    INFO = 0
    WARNING = 1
    ERROR = 2


# NGP Job Status
class JobStatus(enum.Enum):
    """
    Job Status

    SUCCESS     - Successful execution
    FAILURE     - Failure
    WARN        - Though job can be flagged as complete but there were warning on the way
    """
    SUCCESS = 0
    FAILURE = 1
    WARN = 2

