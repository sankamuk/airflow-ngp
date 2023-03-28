"""
    navigation.py
    -------

    This module helps in different functionality related to navigation.
"""
import os
import glob
from importlib import import_module
from inspect import getmembers, isabstract, isclass
from ngp.utils.ngp_environment import lookup_environment


def get_path(rel_path: str = None) -> str:
    """
    Returns absolute path corresponding to relative path.

    :param rel_path: String representing relative path from project root, example::
        ngp/core/services/config/static/ngp.json
    :return: String representing absolute file path, example::
        /opt/software/airflow-ngp/ngp/core/services/config/static/ngp.json
    """
    ngp_home = lookup_environment("NGP_HOME")
    return os.path.join(ngp_home, *(rel_path.split('/')))


def get_module(family: str = 'services', mod_type: str = None) -> dict:
    """
    List the modules with classes of specific type. This will be used by factory method to invoke the functionality.

    :param family: String representing kind of module to look, example::
        services
    :param mod_type: String representing module type, example::
        config
    :return: Dictionary of modules and corresponding classes, example::
        {
            "local_cfg": "LocalCfg"
        }
    """
    module_rel_path = "ngp/core/{}/{}/types".format(family, mod_type)
    module_abs_path = get_path(module_rel_path)
    modules = glob.glob(os.path.join(module_abs_path, "*.py"))
    module_list = dict()
    for mod_file in modules:
        if not mod_file.endswith('__init__.py'):
            mod_name = os.path.basename(mod_file)[:-3]
            mod_path = "{}.{}".format(module_rel_path.replace('/', '.'), mod_name)
            py_module = import_module(mod_path)
            classes = [
                c[0]
                for c in getmembers(py_module, lambda m: isclass(m) and not isabstract(m))
                if c[1].__module__ == mod_path
            ]
            if len(classes) == 1:
                module_list[mod_name] = classes[0]
    return module_list


def init_class(family: str = 'services',
               mod_type: str = 'config',
               mod_name: str = 'local_cfg',
               cls_name: str = 'LocalCfg') -> object:
    """
    List the modules with classes of specific type. This will be used by factory method to invoke the functionality

    :param family: String representing kind of module to look, example::
        services
    :param mod_type: String representing module type, example::
        config
    :param mod_name: String representing module name, example::
        local_cfg
    :param cls_name: String representing class name, example::
        LocalCfg
    :return: Initiated object of type class named :attr:`cls_name`
    """
    mod_path = "ngp.core.{}.{}.types.{}".format(family, mod_type, mod_name)
    py_module = import_module(mod_path)
    cls_object_list = [
        c[1]
        for c in getmembers(py_module, lambda m: isclass(m) and not isabstract(m))
        if c[0] == cls_name
    ]
    if len(cls_object_list) != 1:
        return None

    return (cls_object_list[0])()
