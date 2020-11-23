"""
Generate a fibonnaci sequence up to n
"""
def fib1(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fib1(num-1) + fib1(num-2)

def fib2(num):
    a, b = 1, 1
    for n in range(num):
        yield a
        a, b = b, a + b

assert [fib1(i) for i in range(2,10)] == list([i for i in fib2(8)])
