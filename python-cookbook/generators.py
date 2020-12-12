import itertools
from itertools import islice

def x(n):
    while True:
        yield n
        n += 1
          
start = x(1)
start2 = itertools.count(1)
print([next(start) for _ in range(5)])
print(next(islice(start, 5)))
print(list(islice(start, 2)))
print([next(start2) for _ in range(5)])

def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b      
print(list(islice(fibonacci(), 8)))

def foo(x):
    yield from range(x**2)  
print(list(foo(5)))   




    