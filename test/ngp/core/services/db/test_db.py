"""
    Test NGP Database Operations
"""
import pytest
from ngp.core.services.db.ngp_db import (get_engine,
                                         get_session,
                                         create_all_objects,
                                         close_session,
                                         add_audit,
                                         search_audit,
                                         update_audit,
                                         add_job,
                                         update_job,
                                         search_job,
                                         delete_job)
from ngp.core.services.db.models.ngp_models import NGPAudits, NGPJob


@pytest.fixture(scope="class")
def prepare_db(request):
    test_engine = get_engine()
    test_session = get_session(test_engine)
    create_all_objects(test_engine)
    request.cls.test_session = test_session
    yield
    close_session(test_session)


@pytest.mark.usefixtures("prepare_db")
class TestDBClass:
    def test_create_audit_table(self):
        """Test table exist"""
        assert len(self.test_session.query(NGPAudits).all()) == 0

    def test_create_audit_record(self):
        """Test Audit record creation"""
        a1 = NGPAudits(
            audit_dag_id="dummy_dag_01",
            audit_task_id="dummy_task_01",
            audit_run_id="dummy_run_01"
        )
        a2 = NGPAudits(
            audit_dag_id="dummy_dag_02",
            audit_task_id="dummy_task_02",
            audit_run_id="dummy_run_02"
        )
        try:
            add_audit(self.test_session, a1)
            add_audit(self.test_session, a2)
        except Exception as exc:
            assert False, f"'NGPAudits' creation raised an exception {exc}"

    def test_query_audit_table_all(self):
        """Test Audit record creation status in RDBMS"""
        assert len(search_audit(self.test_session)) == 2

    def test_query_audit_table_by_run_id(self):
        """Test query Audit record but Run id"""
        assert len(search_audit(self.test_session, (NGPAudits.audit_run_id == "dummy_run_01", ))) == 1

    def test_query_audit_table_by_dag_and_task_id(self):
        """Test query Audit record by DAG id and Task id"""
        filter_cond = (NGPAudits.audit_dag_id == "dummy_dag_02", NGPAudits.audit_task_id == "dummy_task_02")
        assert len(search_audit(self.test_session, filter_cond)) == 1

    def test_audit_table_update(self):
        """Test update Audit record"""
        filter_cond = (NGPAudits.audit_run_id == "dummy_run_01", )
        update_dict = {NGPAudits.audit_detail: "dummy"}
        update_audit(self.test_session, filter_cond, update_dict)
        get_updated_rec = search_audit(self.test_session, filter_cond)
        assert (get_updated_rec[0]).audit_detail == "dummy"

    def test_create_job_table(self):
        """Test table exist"""
        assert len(self.test_session.query(NGPJob).all()) == 0

    def test_create_job_record(self):
        """Test Job record creation"""
        j1 = NGPJob(
            job_dag_id="dummy_dag_01",
            job_task_id="dummy_task_01",
            job_run_id="dummy_run_01"
        )
        j2 = NGPJob(
            job_dag_id="dummy_dag_02",
            job_task_id="dummy_task_02",
            job_run_id="dummy_run_02"
        )
        try:
            add_job(self.test_session, j1)
            add_job(self.test_session, j2)
        except Exception as exc:
            assert False, f"'NGPJob' creation raised an exception {exc}"

    def test_query_job_table_all(self):
        """Test Job record creation status in RDBMS"""
        assert len(search_job(self.test_session)) == 2

    def test_query_job_table_by_run_id(self):
        """Test query Job record but Run id"""
        assert len(search_job(self.test_session, (NGPJob.job_run_id == "dummy_run_01", ))) == 1

    def test_query_job_table_by_dag_and_task_id(self):
        """Test query Job record by DAG id and Task id"""
        filter_cond = (NGPJob.job_dag_id == "dummy_dag_02", NGPJob.job_task_id == "dummy_task_02")
        assert len(search_job(self.test_session, filter_cond)) == 1

    def test_job_table_update(self):
        """Test update Job record"""
        filter_cond = (NGPJob.job_run_id == "dummy_run_01", )
        update_dict = {NGPJob.job_detail: "dummy"}
        update_job(self.test_session, filter_cond, update_dict)
        get_updated_rec = search_job(self.test_session, filter_cond)
        assert (get_updated_rec[0]).job_detail == "dummy"

    def test_job_table_delete(self):
        """Test delete Job record"""
        filter_cond = (NGPJob.job_run_id == "dummy_run_01", )
        delete_job(self.test_session, filter_cond)
        assert len(search_job(self.test_session)) == 1
