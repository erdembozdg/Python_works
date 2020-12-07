#!/user/bin/env python3

import fileinput
import sys
import getpass
import os
import subprocess
import shutil
import time
from configparser import ConfigParser
import logging
import logging.config
import webbrowser
import send2trash

with fileinput.input() as f_input:
    for line in f_input:
        print(line, end="")

sys.stderr.write('It failed \n')
raise SystemExit(1)
raise SystemExit("It failed")

user = getpass.getuser()
passwd = getpass.getpass()

out_bytes = subprocess.check_output(['netstat', '-a'])
print(out_bytes.decode('utf-8'))

try:
    out_bytes = subprocess.check_output(['cmd', 'arg1', 'arg2'], sterr=subprocess.STDOUT, timeout=5)
except subprocess.CalledProcessError as e:
    out_bytes = e.output
    code = e.returncode
except subprocess.TimeoutExpired as e:
    out_bytes = e.output
    code = e.returncode  

out_bytes = subprocess.check_output('grep python | wc > out', shell=True)

text = b'hello world'\
p = subprocess.Popen(['wc'], stdout = subprocess.PIPE, stdin = subprocess.PIPE)
stdout, stdin = p.communicate(text)
out = stdout.decode('utf-8')
err = stderr.decode('utf-8')

shutil.move(src, dst)
shutil.copy(src, dest)
shutil.copy2(src, dest) # cp -p src dst
shutil.copy2(src, dst, follow_symlinks=False)
shutil.copytree(src, dest) # cp -R src dst
shutil.copytree(src, dst, symlinks=True)

shutil.copytree(src, dst, ignore=shutil.ignore_patterns('*~','*.pyc'))

shutil.make_archive('py33','zip','Python-3.3.0')
shutil.unpack_archive('Python-3.3.0.tgz')

def findfile(start, name):
    for path, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, path, name)
            print(os.path.normpath(os.path.abspath(full_path)))

def modified_within(top, seconds):
    now = time.time()
    for path, dirs, files in os.walk(top):
        if name in files:
            full_path = os.path.join(path, files)
            if os.path.exists(full_path):
                mtime = os.path.getmtime(full_path)
                if mtime > (now - seconds):
                    print(full_path)

def main():
    log = logging.getLogger(__name__)
    log.addHandler(logging.NullHandler())
    logging.basicConfig(
        filename='app.log',
        level=logging.ERROR,
        format='%(levelname)s:%(asctime)s:%(message)s'
    )
    logging.info('Openning file: %r, mode: %r', 'test1', 'mode')

    # logging.config.fileConfig('config.ini')

    log.debug('A debug message')


class Timer:
    def __init__(self, func=time.perf_counter):
        self._elabsed = 0.0
        self._start = None
        self._func = func

    def start(self):
        if self._start is not None:
            raise RuntimeError('Already started')
        self._start = self._func

    def stop(self):
        if self._start is None:
            raise RuntimeError('Not started')
        end = self._func
        self._elabsed = end - self._start
        self._start = None

    def reset(self):
        self._elabsed = 0.0

    def running(self):
        return self._start is not None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop


if __name__ == '__main__':
    # if len(sys.argv) != 3:
    #     print('Usage: {} dir seconds'.format(sys.argv[0]))
    #     raise SystemExit(1)
    # findfile(sys.argv[1], sys.argv[2])
    # modified_within(sys.argv[1], float(sys.argv[2]))

    # cfg = ConfigParser()
    # cfg.read('config.ini')
    # cfg.read(os.path.expanduser('~/.config.ini'))
    # cfg.write(sys.stdout)
    main()








