"""
    spark_config_service.py
    -------

    This module contains utility module related to fetching configuration for a Spark application.
"""
import os
import json

from ngp.core.services.db.models.ngp_models import NGPJob
from ngp.utils.navigation import get_path
from ngp.utils.genaral_utils import load_dict_from_json_file
from ngp.utils.ngp_environment import return_environment


def get_launcher_module_file() -> str:
    """
    Returns the fully qualified path to the Spark application launcher module file

    :return: String local file path
    """
    spark_app_fl = get_path("ngp/core/services/spark/app/spark_main.py")
    if os.path.isfile(spark_app_fl):
        return spark_app_fl
    else:
        raise Exception("NGP Spark Application launcher missing! Expecting - {}".format(spark_app_fl))


def get_spark_task_config(dag_id: str, task_id: str) -> dict:
    """
    Returns a dictionary corresponding to a Spark Application task

    :param dag_id: String representing DAG id
    :param task_id: String representing DAG id
    :return: Dictionary representing task config
    """

    dag_cfg_fl = get_path("ngp/config/dags/{}.json".format(dag_id))
    if not os.path.isfile(dag_cfg_fl):
        raise Exception("No DAG configuration file identified! Expecting - {}".format(dag_cfg_fl))

    dag_cfg = load_dict_from_json_file(dag_cfg_fl)
    if "tasks" not in dag_cfg:
        raise Exception("DAG config {} does not contain any task configuration! ".format(dag_cfg_fl))

    _task_cfg = dag_cfg["tasks"].get(task_id, None)
    if not _task_cfg:
        raise Exception("DAG config {} does not contain any task configuration for task {}! ".format(
            dag_cfg_fl, task_id))

    if isinstance(_task_cfg, str):
        return load_dict_from_json_file(get_path("ngp/config/tasks/{}".format(_task_cfg)))
    else:
        return _task_cfg


def get_spark_submit_command(spark_command: list, ngp_job: NGPJob) -> list:
    """
    Create NGP Spark Submit Command

    :param spark_command: List with command prefix will be appended to complete the command
    :param ngp_job: NGPJob object
    :return: String representing complete command
    """
    spark_command.append(get_launcher_module_file())
    spark_command.append(ngp_job.job_json_dump())
    spark_command.append(json.dumps(return_environment()))

