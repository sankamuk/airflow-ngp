"""
    spark_local_runner.py
    -------

    This module contains the implementation for executing Spark in local mode
"""
from ngp.core.services.config.config_factory import get_config_service
from ngp.core.services.spark.spark_abs_runner import BorgSparkRunner, AbsSparkRunner
from ngp.core.services.db.models.ngp_models import NGPJob
from ngp.utils.ngp_environment import lookup_environment
from ngp.core.services.spark.utils.spark_config_service import get_spark_submit_command
from ngp.utils.genaral_utils import run_host_command


class SparkLocalRunner(BorgSparkRunner, AbsSparkRunner):
    """
    This class is a wrapper for Spark in Local mode execution functionality

    .. admonition:: Note
        * Spark should be installed in the host executing the function
        * Spark CLI should be in path

    """
    def __init__(self):
        BorgSparkRunner.__init__(self)
        if not self._spark_config:
            self._spark_config = dict()

    def setup_runner(self):
        """
        Code to setup Spark instance in Local mode

        :return: None
        """
        pass

    def get_job_for_runner(self, ngp_job: NGPJob):
        """
        Code to get a handle to execute Spark in local mode

        :param ngp_job: Object typed :class:`ngp.core.services.db.models.ngp_models.NGPJob`
        :return: None
        """
        self._spark_config["ngp_job"] = ngp_job

    def teardown_runner(self):
        """
        Code to cleanup Spark instance in Local mode

        :return:
        """
        pass

    def submit_task_to_runner(self) -> dict:
        """
        Code to execute Spark application in Local mode

        :return: None
        """
        cfg_backend = lookup_environment("NGP_SERVICE_CONFIG_BACKEND")
        cfg_key = lookup_environment("NGP_SERVICE_SPARK_CONF")
        spark_cfg = get_config_service(cfg_backend).get_cfg(cfg_key)
        spark_command = spark_cfg["spark_local_mode_submit_prefix"]
        get_spark_submit_command(spark_command, self._spark_config["ngp_job"])

        return run_host_command(spark_command)

