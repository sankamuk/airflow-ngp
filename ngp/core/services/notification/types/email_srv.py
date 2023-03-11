"""
    email_srv.py
    -------

    This module contains the implementation of Email notification service.
"""
from ngp.core.services.notification.abs_notification import AbsNotification, BorgNotify
from ngp.core.models.ngp_enums import NotificationType, JobStatus
from ngp.core.services.config.static.email_template import NGP_EMAIL_TEMPLATE
from ngp.core.services.config.config_factory import get_config_service
from ngp.utils.ngp_environment import lookup_environment
from datetime import datetime
from jinja2 import Template
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailSrv(AbsNotification, BorgNotify):
    """
    It allow framework to send email notifications.
    NOTE:
        1. Configuration should be present.
        2. Based on configuration only specific type of notification will be send.
    """

    def __init__(self):
        BorgNotify.__init__(self)
        if not self._notify_config:
            self._notify_config = {
                "smtp_host": None,
                "smtp_port": None,
                "smtp_ssl": True,
                "smtp_password": None,
                "email_to": None,
                "email_from": None
            }
            cfg_backend = lookup_environment('NGP_SERVICE_CONFIG_BACKEND')
            cfg_key = lookup_environment('NGP_SERVICE_NOTIFICATION_CFG')
            email_config = get_config_service(cfg_backend).get_cfg(cfg_key)
            self._notify_config.update(email_config)

    def notify(self,
               notification_type: NotificationType = NotificationType.INFO,
               job_detail: dict = None,
               message: str = None,
               audience: str = None):
        """
        Send Email notification.

        :param notification_type:
        :param job_detail:
        :param message:
        :param audience:
        """
        check_applicable = lookup_environment('NGP_SERVICE_NOTIFICATION_ALLOW')
        if NotificationType(notification_type).name in check_applicable.split(','):
            email_body = Template(NGP_EMAIL_TEMPLATE).render(
                ngp_job_color=(
                    "FF6433"
                    if notification_type == NotificationType.ERROR else "FFE033"
                    if notification_type == NotificationType.WARNING else "9CFF33"
                ),
                ngp_job_status=JobStatus(job_detail["status"]).name,
                ngp_job_time=datetime.today().strftime("%Y-%m-%d:%H-%M"),
                ngp_job_dag=job_detail["dag_id"],
                ngp_job_task=job_detail["task_id"],
                ngp_job_run=job_detail["run_id"],
                ngp_job_remark=message
            )
            email_subject = "NGP {} : DAG {} : TASK {}".format(NotificationType(notification_type).name,
                                                               job_detail["dag_id"],
                                                               job_detail["task_id"])
            email_to = audience if audience else self._notify_config["email_to"]

            message = MIMEMultipart('alternative')
            message['subject'] = email_subject
            message['To'] = email_to
            message['From'] = self._notify_config["email_from"]
            message.preamble = """Your mail reader does not support the report format. Please visit us online!"""
            message.attach(MIMEText(email_body, 'html'))
            server = (smtplib.SMTP(self._notify_config["smtp_host"], self._notify_config["smtp_port"])
                      if self._notify_config["smtp_port"] else smtplib.SMTP(self._notify_config["smtp_host"]))
            # server.set_debuglevel(1)
            if self._notify_config["smtp_ssl"]:
                context = ssl.create_default_context()
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()
            if self._notify_config["email_from"]:
                try:
                    server.login(self._notify_config["email_from"], self._notify_config["smtp_password"])
                except Exception as e:
                    print(e)
            server.sendmail(self._notify_config["email_from"], email_to.split(','), message.as_string())
            server.quit()
