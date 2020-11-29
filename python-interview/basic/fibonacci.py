"""
Generate a fibonnaci sequence up to n
"""
def fib1(num):
    if num == 0 or num == 1:
        return num
    else:
        return fib1(num-1) + fib1(num-2)

def fib2(num):
    a, b = 0, 1
    for n in range(num):
        yield a
        a, b = b, a + b

assert [fib1(i) for i in range(9)] == list([i for i in fib2(9)])
