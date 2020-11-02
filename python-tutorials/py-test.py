
# pytest py_test.py --capture=no
# by passing the -s or --capture=no flag

import tempfile
import shutil
import os.path
import py.test
import sys

def setup_module(module):
    print('Setting up Module {}'.format(module.__name__))

def teardown_module(module):
    print('Tearing down Module {}'.format(module.__name__))

def test_X():
    print("Running Instances")


class BaseTest:
    def setup_class(cls):
        print("Setting up Class {0}".format(cls.__name__))
        cls.dir = tempfile.mkdtemp()

    def teardown_class(cls):
        print("Tearing down Class {0}".format(cls.__name__))
        shutil.rmtree(cls.dir)

    def setup_method(self, method):
        print("Setting up Method {0}".format(method.__name__))

    def teardown_method(self, method):
        print("Tearing down Method {0}".format(method.__name__))

class TestClass(BaseTest):
    def test_method_1(self):
        print("Running Method 1")
        os.mkdir(os.path.join(self.dir, 'a'))
        os.mkdir(os.path.join(self.dir, 'b'))
        contents = os.listdir(self.dir)
        assert len(contents) == 2

    @py.test.mark.skipif(sys.platform.startswith('linux'), reason='This test is useless')
    def test_method_2(self):
        assert b"hello".decode() == "hello"


