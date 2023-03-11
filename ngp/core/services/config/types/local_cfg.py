"""
    local_cfg.py
    -------

    This module interacts with local file based configuration repo.
"""
from ngp.core.services.config.abs_config import BorgCFG, AbsCFG
from ngp.utils.navigation import get_path
import os
import json


class LocalCfg(AbsCFG, BorgCFG):
    """
    Fetch configuration from file based configuration repository.
    NOTE:
        1. Configuration file should be present.
    """

    def __init__(self):
        BorgCFG.__init__(self)
        if not self._cfg_config:
            ngp_cfg_file = get_path('ngp/core/services/config/static/ngp.json')
            if not os.path.isfile(ngp_cfg_file):
                raise Exception("Local NGP configuration file {} does not exist.".format(ngp_cfg_file))
            with open(ngp_cfg_file) as fh:
                self._cfg_config = json.load(fh)

    def get_cfg(self, cfg_key: str = None) -> dict:
        """
        Returns configuration item for key passed as argument.

        :param cfg_key: Configuration key.
        :return: Configuration value or None.
        """

        return self._cfg_config.get(cfg_key, None)

