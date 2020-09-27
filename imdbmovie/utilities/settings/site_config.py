from yaml import safe_load
from os.path import join, dirname, abspath


class SiteConfig:
    """
    Manage configurations as per the environment
    """

    def __init__(self, config_file='development.yaml'):
        self.config = None
        self.config_file = config_file

        if config_file.startswith('/') is False:
            self.config_file = join(dirname(abspath(__file__)), config_file)

        with open(self.config_file, 'rt') as f:
            self.config = safe_load(f.read())

    def get_config(self):
        """
        Get all configuration
        :return:
        """
        return self.config
