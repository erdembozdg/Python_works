
import os

def simple_function():
    return "You have called simple_function"

class SimpleClass(object):
    def explode(self):
        return "KABOOM!"

def work_on():
    path = os.getcwd()
    print({f'Working on {path}'})
    return path

class Helper:
    def __init__(self, path):
        self._path = path

    def get_path(self):
        base_path = os.getcwd()
        return os.path.join(base_path, self._path)

class Worker:
    def __init__(self):
        self._helper = Helper('db')

    def work_on(self):
        path = self._helper.get_path()
        print({f'Working on {path}'})
        return path
