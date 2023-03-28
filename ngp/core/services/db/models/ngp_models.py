"""
    ngp_models.py
    -------

    This module define all NGP DB Models.
"""
import json

from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db
from sqlalchemy.orm import validates
from datetime import datetime

Base = declarative_base()


class NGPAudits(Base):
    """
    NGP Audit Model.
    .. admonition:: Note
        Defines NGP Audit record instance represented as a SQLAlchemy Model class
    """
    __tablename__ = 'ngp_audits'
    audit_id = db.Column(db.Integer(), primary_key=True)
    audit_dag_id = db.Column(db.String(50), nullable=False)
    audit_task_id = db.Column(db.String(50), nullable=False)
    audit_run_id = db.Column(db.String(50), nullable=False)
    audit_record_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    audit_job_start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    audit_job_status = db.Column(db.String(10), nullable=False, default="FAILURE")
    audit_detail = db.Column(db.String(500))

    @validates("audit_job_status")
    def validate_audit_job_status(self, key, value):
        """
        Validates audit object status.

        :param key: audit_job_status field
        :param value: audit_job_status value set
        :return: audit_job_status value if no error
        """
        if value not in ["FAILURE", "SUCCESS", "WARN"]:
            raise ValueError("Invalid audit record. Status provided {} but can be FAILURE/SUCCESS/WARN".format(value))
        return value

    # Representation
    def __repr__(self):
        """
        String representation of :class:`NGPAudits`
        .. admonition:: Note
            Used for printing

        :return: String
        """
        return "<NGPAudits: Id={}, DAG={}, Task={}, Run={}, Status={}>".format(
            self.audit_id, self.audit_dag_id, self.audit_task_id, self.audit_run_id, self.audit_job_status)


class NGPJob(Base):
    """
    NGP Job Model.
    .. admonition:: Note
        Defines NGP Job record instance represented as a SQLAlchemy Model class.
        NGP Job record will also be used for NGP framework job status maintenance.
    """
    __tablename__ = 'ngp_job'
    job_id = db.Column(db.Integer(), primary_key=True)
    job_dag_id = db.Column(db.String(50), nullable=False)
    job_task_id = db.Column(db.String(50), nullable=False)
    job_run_id = db.Column(db.String(50), nullable=False)
    job_status = db.Column(db.String(10), nullable=False, default="FAILURE")
    job_detail = db.Column(db.String(500))

    @validates("job_status")
    def validate_audit_job_status(self, key, value):
        """
        Validates job object status.

        :param key: job_status field
        :param value: job_status value set
        :return: job_status value if no error
        """
        if value not in ["FAILURE", "SUCCESS", "WARN"]:
            raise ValueError("Invalid job record. Status provided {} but can be FAILURE/SUCCESS/WARN".format(value))
        return value

    # Representation
    def __repr__(self):
        """
        String representation of :class:`NGPJob`
        .. admonition:: Note
            Used for printing

        :return: String
        """
        return "<NGPJob: Id={}, DAG={}, Task={}, Run={}, Status={}>".format(
            self.job_id, self.job_dag_id, self.job_task_id, self.job_run_id, self.job_status)

    # JSON Serializer
    def job_json_dump(self):
        """
        String encoded JSON representation of :class:`NGPJob`

        :return: String encoded JSON
        """
        return json.dumps({
            "job_dag_id": self.job_dag_id,
            "job_task_id": self.job_task_id,
            "job_run_id": self.job_run_id
        })

