"""
    ngp_db.py
    -------

    This module controls NGP backend database interaction
"""
import os
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from ngp.core.services.db.models.ngp_models import Base
from ngp.core.services.db.models.ngp_models import NGPAudits, NGPJob


def get_engine():
    """
    Creates SQLAlchemy Engine

    :return: SQLAlchemy DB Engine object
    """
    """Create SQLAlchemy Engine"""
    if "NGP_SERVICE_DB_URL" in os.environ:
        ngp_db_url = os.environ["NGP_SERVICE_DB_URL"]
    elif "AIRFLOW_CORE_SQL_ALCHEMY_CONN" in os.environ:
        ngp_db_url = os.environ["AIRFLOW_CORE_SQL_ALCHEMY_CONN"]
    else:
        ngp_db_url = "sqlite://"  # Default in memory database
    return db.create_engine(ngp_db_url)


def get_session(db_engine):
    """
    Returns an Session

    :param db_engine: SQLAlchemy DB Engine object
    :return: SQLAlchemy DB Session
    """
    ssn = sessionmaker()
    ssn.configure(bind=db_engine)
    return ssn()


def create_all_objects(db_engine):
    """
    Create Database Objects

    :param db_engine: SQLAlchemy DB Engine object
    :return: None
    """
    Base.metadata.create_all(db_engine)


def _check_uncommitted_object(db_session):
    """
    Check uncommitted object in SQLAlchemy Session

    :param db_session: SQLAlchemy DB Session
    :return: SQLAlchemy Model Objects
    """
    return db_session.new


def commit_session(db_session):
    """
    Commit and SQLAlchemy Session

    :param db_session: SQLAlchemy DB Session
    :return: None
    """
    db_session.commit()


def rollback_session(db_session):
    """
    Rollback and SQLAlchemy Session

    :param db_session: SQLAlchemy DB Session
    :return: None
    """
    db_session.rollback()


def close_session(db_session):
    """
    Close and SQLAlchemy Session

    :param db_session: SQLAlchemy DB Session
    :return: None
    """
    db_session.close()


def _add_single_object_in_session(db_session, obj):
    """
    Adding an object to SQLAlchemy Session

    :param db_session: SQLAlchemy DB Session
    :param obj: SQLAlchemy Model Object
    :return: None
    """
    db_session.add(obj)


def _add_multiple_object_in_session(db_session, obj_list):
    """
    Adding list of object to SQLAlchemy Session

    :param db_session: SQLAlchemy DB Session
    :param obj_list: List of SQLAlchemy Model Object
    :return: None
    """
    db_session.add_all(obj_list)


def add_audit(db_session, audit: NGPAudits):
    """
    Persist an audit record

    :param db_session: SQLAlchemy DB Session returned from :meth:`get_session`
    :param audit: Object typed :class:`ngp.core.services.db.models.ngp_models.NGPAudits`
    :return: None
    """
    _add_single_object_in_session(db_session, audit)
    commit_session(db_session)


def search_audit(db_session, audit_filter: tuple = None):
    """
    Search audit record(s)

    :param db_session: SQLAlchemy DB Session returned from :meth:`get_session`
    :param audit_filter: Tuple representing NGPAudits object search filter, example::
        (NGPAudits.audit_dag_id == "dummy", NGPAudits.audit_task_id == "dummy")
    :return: List of NGPAudits objects of type :class:`ngp.core.services.db.models.ngp_models.NGPAudits`
    """
    return db_session.query(NGPAudits).filter(*audit_filter).all() if audit_filter \
        else db_session.query(NGPAudits).all()


def update_audit(db_session, audit_filter: tuple = None, update_dict: dict = None):
    """
    Update an audit record(s)

    :param db_session: SQLAlchemy DB Session returned from :meth:`get_session`
    :param audit_filter: Tuple representing NGPAudits object search filter, example::
        (NGPAudits.audit_dag_id == "dummy", NGPAudits.audit_task_id == "dummy")
    :param update_dict: NGPAudits object update dictionary, example::
        {NGPAudits.audit_detail: "dummy"}
    :return: None
    """
    search_result = db_session.query(NGPAudits).filter(*audit_filter) if audit_filter else db_session.query(NGPAudits)
    search_result.update(update_dict, synchronize_session=False)
    commit_session(db_session)


def add_job(db_session, ngp_job: NGPJob):
    """
    Persist an job record

    :param db_session: SQLAlchemy DB Session returned from :meth:`get_session`
    :param ngp_job: Object typed :class:`ngp.core.services.db.models.ngp_models.NGPJob`
    :return: None
    """
    _add_single_object_in_session(db_session, ngp_job)
    commit_session(db_session)


def search_job(db_session, job_filter: tuple = None):
    """
    Search job record(s)

    :param db_session: SQLAlchemy DB Session returned from :meth:`get_session`
    :param job_filter: NGPJob object search filter, example::
        (NGPJob.job_id == "dummy", )
    :return: List of object typed :class:`ngp.core.services.db.models.ngp_models.NGPJob`
    """
    return db_session.query(NGPJob).filter(*job_filter).all() if job_filter \
        else db_session.query(NGPJob).all()


def update_job(db_session, job_filter: tuple = None, update_dict: dict = None):
    """
    Update an job record(s)

    :param db_session: SQLAlchemy DB Session returned from :meth:`get_session`
    :param job_filter: NGPJob object search filter, example::
        (NGPJob.job_id == "dummy", )
    :param update_dict: NGPJob object update dictionary, example::
        {NGPJob.job_detail == "dummy", }
    :return: None
    """
    search_result = db_session.query(NGPJob).filter(*job_filter) if job_filter else db_session.query(NGPJob)
    search_result.update(update_dict, synchronize_session=False)
    commit_session(db_session)


def delete_job(db_session, job_filter: tuple = None):
    """
    Delete an job record(s)

    :param db_session: SQLAlchemy DB Session
    :param job_filter: NGPJob object search filter, example::
        (NGPJob.job_id == "dummy", )
    :return: None
    """
    search_result = db_session.query(NGPJob).filter(*job_filter) if job_filter else db_session.query(NGPJob)
    search_result.delete()
    commit_session(db_session)
