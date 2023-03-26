from ngp.core.services.spark.infra.utils.spark_config_service import get_launcher_module_file, get_spark_task_config
from ngp.utils.navigation import get_path
import os


def test_get_launcher_module_file():
    assert get_launcher_module_file() == get_path("ngp/core/services/spark/app/spark_main.py")


def test_get_spark_task_config():
    test_dict = {"dummy_task_cfg":  12345}
    assert get_spark_task_config("dummy_dag", "dummy_task_01") == test_dict
    assert get_spark_task_config("dummy_dag", "dummy_task_02") == test_dict
