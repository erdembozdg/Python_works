
import os

class InputData:
    def read(self):
        raise NotImplementedError

class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path, 'r').read()


# Python only allows for single constructor method. @classmethod polymorphizm solve this problem.
class GenericInputData:
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError

class PathInputData(GenericInputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path, 'r').read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config('data_dir')
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))