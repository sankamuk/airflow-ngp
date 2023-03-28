"""
    spark_runner_factory.py
    -------

    This module creates Spark execution service object
"""
from ngp.utils.navigation import get_module, init_class


def get_spark_runner_service(runner_type: str = 'spark_local_runner') -> object:
    """
    Creates a Spark executor which can be used to execute application

    :param runner_type: String representing type of Spark execution engine, example::
        spark_local_runner
    :return: Object implementing :class:`ngp.core.services.spark.spark_abs_runner.AbsSparkRunner`
    """
    cls_name = get_module("services", "spark")[runner_type]
    return init_class("services", "spark", runner_type, cls_name)
