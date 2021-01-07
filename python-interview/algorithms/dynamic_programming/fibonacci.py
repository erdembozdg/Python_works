
import time

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

cache = {}
def dynamic_fibonacci(n):
    if n in cache:
        return cache[n]
    else:
        if n < 2:
            return n
        else:
            cache[n] = dynamic_fibonacci(n-1) + dynamic_fibonacci(n-2)
            return cache[n]

t1 = time.time()
print(fibonacci(300))
t2 = time.time()
print(t2-t1)

t1 = time.time()
print(dynamic_fibonacci(300))
t2 = time.time()
print(t2-t1)