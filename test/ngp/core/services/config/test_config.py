from ngp.core.services.config.config_factory import get_config_service
from ngp.core.services.config.types.local_cfg import LocalCfg


def test_get_config_service_return():
    assert isinstance(get_config_service('local_cfg'), LocalCfg)


def test_get_config_service_lookup():
    assert (get_config_service('local_cfg').get_cfg('email_config')
            ==
            {'smtp_host': 'dummy', 'smpt_user': 'dummy', 'smpt_password': 'dummy'})
