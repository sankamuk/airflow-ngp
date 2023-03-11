from ngp.core.services.notification.types.email_srv import EmailSrv
from ngp.core.models.ngp_enums import NotificationType


def test_send_email():
    try:
        e = EmailSrv()
        e.notify(NotificationType.INFO, {"dag_id": "s", "task_id": "t", "run_id": "d", "status": 1}, "Good", "iam.san.muk@gmail.com")
    except Exception as exc:
        assert False, f"'EmailSrv' raised an exception {exc}"
