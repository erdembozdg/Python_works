from io import StringIO
from io import TextIOWrapper
import gzip
import bz2
from functools import partial
import os
from fnmatch import fnmatch
import glob
import urllib.request
import sys
from tempfile import NamedTemporaryFile, TemporaryDirectory
import pickle

dirpath = os.getcwd()
filename = "data.txt"
path = os.path.join(dirpath, filename)
os.chmod(path, 0o777)

with open('data.txt', 'rt', encoding='latin-1') as f:
    data = f.read()
    print(data)
    # for line in f:

with open('write_data.txt', 'wt') as f:
    f.write('text1.txt\n')
    print("xxxx", file=f, end='!!\n')

row = ('xyz', 33)
print(*row)
print(' '.join(str(x) for x in row))
print("----------------")

with open('xyz.bin', 'wb') as f:
    text = 'Hello '
    f.write(text.encode('utf-8'))
    f.write(b'Erdem')

with open('xyz.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')
    print(text)

print("----------------")

s = StringIO()
s.write('Test: ')
print('file-like object example', file=s)
print(s.read())
print("----------------")

with gzip.open('data.gz', 'wt') as f:
    f.write('test gzip')

with bz2.open('data.bz2', 'wt') as f:
    f.write('test gzip')

with gzip.open('data.gz', 'rt') as f:
    print(f.read())

with bz2.open('data.bz2', 'rt') as f:
    print(f.read())
print("----------------")

RECORD_SIZE = 32
with open('xyz.bin', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for record in records:
        print(record)
print("----------------")
def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        return f.readinto(buf)
print(read_into_buffer('xyz.bin'))
print("----------------")

print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.join('tmp', 'data', os.path.basename(path)))
print(os.path.expanduser(path))
print(os.path.splitext(path))
print(os.path.isfile(path))
print(os.path.isdir(path))
print(os.path.exists(path))
print(os.path.islink(path))
print(os.path.realpath(path))
print(os.path.getsize(path))
print(os.path.getmtime(path))

print("----------------")

names = [name for name in os.listdir(os.path.dirname(path))]
for name in names:
    if os.path.isfile(name):
        print(f'{name} is file')
    if os.path.isdir(name):
        print(f'{name} is directory')
    if name.endswith('.py'):
        print(f'{name} is python file')
    if fnmatch(name, '*.py'):
        print(f'{name} is python file')

print("----------------")

pyfiles = glob.glob('*.py')
names = [(name, os.path.getsize(name), os.path.getmtime(name)) for name in pyfiles]
for name, size, time in names:
    print(name, size, time)

names = [(name, os.stat(name)) for name in pyfiles]
for name, metadata in names:
    print(name, metadata.st_size, metadata.st_mtime)

print("----------------")

u = urllib.request.urlopen('http://www.python.org')
f = TextIOWrapper(u, encoding='utf-8')

print(sys.stdout.encoding)
sys.stdout = TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
print(sys.stdout.encoding)
sys.stdout.buffer.write(b'Hello Erdem')

print("----------------")

with NamedTemporaryFile('w+t') as f:
    f.write('Hello World\n')
    f.write('Erdem')

    f.seek(0)
    print(f"file names is {f.name}\n{f.read()}")

with TemporaryDirectory() as dirname:
    print(dirname)

print("----------------")

data = object()
f = open(filename, 'wb')
pickle.dump(data, f)
s = pickle.dumps(data)

f = open(filename, 'rb')
data = pickle.load(f)
data = pickle.loads(s)



