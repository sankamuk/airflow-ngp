"""
    spark_runner_factory.py
    -------

    This module creates Spark execution service object.
"""
from ngp.utils.navigation import get_module, init_class


def get_spark_runner_service(runner_type: str = 'spark_local_runner') -> object:
    """
    Creates a Spark executor which can be used to execute application.

    :param runner_type: Type of Spark execution engine. default -> spark_local_runner (Spark in local mode)
    :return: Spark Runner Object.
    """
    cls_name = get_module("services", "spark")[runner_type]
    return init_class("services", "spark", runner_type, cls_name)
