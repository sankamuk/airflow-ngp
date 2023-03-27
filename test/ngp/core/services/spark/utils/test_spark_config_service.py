from ngp.core.services.db.models.ngp_models import NGPJob
from ngp.core.services.spark.utils.spark_config_service import get_launcher_module_file, get_spark_task_config, \
    get_spark_job_config
from ngp.utils.navigation import get_path


def test_get_launcher_module_file():
    assert get_launcher_module_file() == get_path("ngp/core/services/spark/app/spark_main.py")


def test_get_spark_task_config():
    test_dict = {"dummy_task_cfg":  12345}
    assert get_spark_task_config("dummy_dag", "dummy_task_01") == test_dict
    assert get_spark_task_config("dummy_dag", "dummy_task_02") == test_dict


def test_get_spark_job_config():
    ngp_job = NGPJob(
        job_dag_id="dummy_dag",
        job_task_id="dummy_task_01",
        job_run_id="dummy_run_01"
    )
    assert get_spark_job_config(ngp_job) == ["--driver-memory", "2g"]
    ngp_job = NGPJob(
        job_dag_id="dummy_dag",
        job_task_id="dummy_task_02",
        job_run_id="dummy_run_03"
    )
    assert get_spark_job_config(ngp_job) == ["--driver-memory", "5g"]
