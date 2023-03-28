from ngp.core.services.notification.types.email_srv import EmailSrv
from ngp.core.models.ngp_enums import NotificationType
from ngp.core.services.db.models.ngp_models import NGPJob


def test_send_email():
    try:
        e = EmailSrv()
        j = NGPJob(
            job_dag_id="dummy_dag_01",
            job_task_id="dummy_task_01",
            job_run_id="dummy_run_01"
        )
        e.notify(NotificationType.INFO, j, "Good", "iam.san.muk@gmail.com")
    except Exception as exc:
        assert False, f"'EmailSrv' raised an exception {exc}"
