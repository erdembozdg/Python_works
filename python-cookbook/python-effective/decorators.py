from contextlib import contextmanager
import logging
logging.basicConfig(level=logging.INFO)

@contextmanager
def log_level(name, level):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)

with log_level('my-log', logging.INFO) as logger:
    logger.debug('This is my message')
    logger.setLevel(logging.DEBUG)
    logger.debug('This is my message')

print("\n")

def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("%s(%r,%r) -> %s" % (func.__name__, args, kwargs, result))
        return result
    return wrapper

@trace
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n-2) + fibonacci(n-1)
print(fibonacci(6))
