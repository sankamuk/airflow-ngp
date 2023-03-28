"""
    spark_abs_runner.py
    -------

    This module contains parent class for defining Spark execution handler
"""
import abc


class BorgSparkRunner:
    """
    Singleton parent for Spark Runner
    """

    _spark_config = dict()

    def __init__(self):
        self.__dict__ = self._spark_config


class AbsSparkRunner(abc.ABC):
    """
    Abstract Spark Runner
    """
    @abc.abstractmethod
    def setup_runner(self):
        pass

    @abc.abstractmethod
    def get_job_for_runner(self, ngp_job):
        pass

    @abc.abstractmethod
    def teardown_runner(self):
        pass

    @abc.abstractmethod
    def submit_task_to_runner(self):
        pass
