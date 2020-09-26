# File Name: yaml_reader.py
# Author: Ankit Goswami
# Creation Date[DD/MM/YY]: 02/04/2020

from yaml import safe_load, load
from os.path import join, dirname, abspath


class YAMLFileReader:
    """
    Manipulating YAML files.
    """

    def __init__(self, filename=None):
        self.data = None
        self.filename = filename

        if filename.startswith('/') is False:
            self.filename = join(dirname(dirname(dirname(abspath(__file__)))), filename)

    def safe_read(self):
        """
        If you need data in json format you must use this method
        """

        with open(self.filename, 'rt') as f:
            self.data = safe_load(f.read())

        return self.data

    def read(self):
        """
        In case of dynamic object creation of python class, method, function etc. use this method.
        """

        with open(self.filename, 'rt') as f:
            self.data = load(f.read())

        return self.data
