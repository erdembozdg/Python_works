from urllib.request import urlopen
import time
import sys
import shutil
import zipfile
from pathlib import Path

class Color:
    def __init__(self, name, value):
        self._name = name
        self._value = value

    def _set_name(self, name):
        if not name:
            raise Exception('Invalid name')
        self._name = name

    def _get_name(self):
        return self._name

    def _del_name(self):
        del self._name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not value:
            raise Exception('Invalid value')
        self._value = value

    @value.deleter
    def value(self):
        del self._value

    name = property(_get_name, _set_name, _del_name, 'This is a property')

class AverageList(list):
    @property
    def average(self):
        return sum(self) / len(self)

class WebPage():
    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if self._content is None:
            self._content = urlopen(self.url).read()
        return self._content

a = AverageList([1, 56, 22])
print(a.average)

c = Color('e', 'c')
c.name = 'erdem'





