import time
from functools import wraps, partial
import logging
from inspect import signature
import types

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n:int):
    while n > 0:
        n -= 1

print("----------------")
# logging decorator
def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    log_name = name if name else func.__module__
    log = logging.getLogger(log_name)
    log_msg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, log_msg)
        return func(*args, **kwargs)
    return wrapper

@logged(level=logging.DEBUG, name='example', message='example message')
def test2():
    print('test logging decorator')

@logged
def add(x, y):
    return x + y

print("----------------")

class A:

    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)
        return wrapper

    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper

a = A()
@a.decorator1
def spam():
    pass

@A.decorator2
def spam():
    pass

print("----------------")
# Optional debug

def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling ', func.__name__)
        return func(*args, **kwargs)
    return wrapper

@optional_debug
def debug_test(a, b, c):
    print(a, b, c)

print("----------------")
# Class decorator
class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)

@Profiled
def add(x, y):
    return x + y

class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)

print("----------------")
# change class definition
def log_attribute(cls):

    orig_attr = cls.__getattribute__

    def new_attribute(self, name):
        print('getting: ', name)
        return orig_attr(self, name)

    cls.__getattribute__ = new_attribute
    return cls

@log_attribute
class A:
    def __init__(self, x):
        self.x =x

if __name__ == '__main__':

    countdown(100000)
    logging.basicConfig(level=logging.DEBUG)
    test2()
    print(add(2, 3))
    print(debug_test(1, 2, 4, debug=True))

    a = A(11)
    print(a.x)



