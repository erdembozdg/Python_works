import html
from functools import partial

def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

print(avg(2,4,5,6,7))

def make_element(name, value, **attr):
    items = [' %s="%s"' % item for item in attr.items()]
    attr_str = ''.join(items)
    return '<{name}{attrs}>{value}</{name}>'.format(name=name, attrs=attr_str, value=html.escape(value))

print(make_element('x', 'y', size=23, id=11))

print("----------------")

def find_min(*values:int, clip=None) -> int:
    m = min(values)
    if clip is not None:
        m = clip if clip < m else m
    return m, f'clip: {clip}'

print(find_min(44,22,77,clip=10))

print("----------------")

items = lambda x,y: (x+y)
print(items(2,3))

items = [lambda x, n=n: (n+x) for n in range(5)]
print([item(20) for item in items])

print(sorted(["Erdem Bozdag","Kelly Amstrong", "Richard Gere"], key=lambda name: name.split()[-1].lower()))

print("----------------")
# partial function
def x(a,b,c,d):
    print(a,b,c,d)

y = partial(x, d=22)
print(y(1, 2, 3))

print("----------------")
# Closure function
def outside_f(text):
    def inside_f(x,y):
        return text.format(x,y)
    return inside_f

out = outside_f("My name is {}, and {} is my surname")
print(out("Erdem", "Bozdag"))
# Closure function, inner variables
def sample():
    n = 0
    def func():
        print('n =', n)

    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    func.set_n = set_n
    func.get_n = get_n
    return func

f = sample()
f.set_n(10)
f()

print("----------------")
# callback functios
def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)

class ResultHandler:
    def __init__(self):
        self.sequence = 0
    def handler(self, result):
        self.sequence += 1
        print('[{}] Got {}'.format(self.sequence, result))

def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence 
        sequence += 1
        print('[{}] Got {}'.format(sequence, result))
    return handler


def add(x,y):
    return x+y

r = ResultHandler()
apply_async(add, ("Hello ","World"), callback=r.handler)

r = make_handler()
apply_async(add, ("Hello ","World"), callback=r)


