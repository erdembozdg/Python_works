"""
Generate a fibonnaci sequence up to n
"""
def fib1(num):
    if num == 0 or num == 1:
        return num
    else:
        return fib1(num-1) + fib1(num-2)

def fib2(num=7):
    a, b = 0, 1
    for n in range(num):
        yield a
        a, b = b, a + b

assert [fib1(i) for i in range(9)] == list([i for i in fib2(9)])

def fib3(num):
    def step(a, b):
        return b, a + b
    a, b = 0, 1
    for _ in range(num):
        a, b = step(a, b)
    return a
print(fib3(10))
