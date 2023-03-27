from ngp.core.services.spark.spark_runner_factory import get_spark_runner_service
from ngp.core.services.db.models.ngp_models import NGPJob


def test_get_spark_runner_service():
    spark_runner = get_spark_runner_service()
    ngp_job = NGPJob(
            job_dag_id="dummy_dag",
            job_task_id="dummy_task_01",
            job_run_id="dummy_run_01"
        )
    spark_runner.get_job_for_runner(ngp_job)
    result = spark_runner.submit_task_to_runner()
    assert result["status"] == 0
