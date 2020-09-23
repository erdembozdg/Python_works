import pkgutil
import sys
import subprocess
from os.path import abspath, join, dirname
import importlib

from a import A
from b import B

a = A()
a.spam()

b = B()
b.foo()

# data = pkgutil.get_data(__package__, 'data.txt')

# subprocess.run('env PYTHONPATH=/some/dir:/other/dir python',  shell=True, check=True, text=True)
print(sys.path)
sys.path.insert(0, abspath(dirname('__file__')))
math = importlib.import_module('math')
print(math.sin(2))

