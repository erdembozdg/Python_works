from collections import defaultdict

m1 = {'x': 1, 'y': 2}
l1 = [ ('a', 3), ('b', 4) ]

#  a stateful closure.
def combine(m1, l1):
    count = 0
    def log():
        nonlocal count
        count += 1
        return 0
    d1 = defaultdict(log, m1)
    for key, value in l1:
        d1[key] += value
    return count
assert combine(m1, l1) == 2

# Using a helper class is a better solution than
class logging:
    def __init__(self):
        self.count = 0
    def __call__(self):
        self.count +ou= 1
        return 0

log = logging()
assert callable(log)

d1 = defaultdict(log, m1)
for key, value in l1:
    d1[key] += value
assert log.count == 2
