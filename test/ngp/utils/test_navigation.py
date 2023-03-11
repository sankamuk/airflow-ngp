import os
from ngp.core.services.config.types.local_cfg import LocalCfg
from ngp.utils.navigation import get_path, get_module, init_class


def test_get_path():
    file_abs_path = os.path.join(
        (os.getcwd()),
        "ngp", "core", "services", "config", "static", "ngp.json"
    )
    assert get_path('ngp/core/services/config/static/ngp.json') == file_abs_path


def test_get_module():
    assert get_module("services", "config") == {"local_cfg": "LocalCfg"}


def test_init_class():
    assert isinstance(
        init_class("services", "config", "local_cfg", "LocalCfg"),
        LocalCfg
    )
