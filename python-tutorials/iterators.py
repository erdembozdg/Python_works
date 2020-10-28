import os
from itertools import dropwhile, islice, chain
from collections import defaultdict, Iterable
import heapq

dirpath = os.getcwd()
filename = 'data.txt'
path = os.path.join(dirpath, filename)
os.chmod(path, 0o777)

# test1
with open(path) as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass
print("----------------")

# test2
with open(path) as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')
print("----------------")

# test3
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

for item in frange(1, 5, 0.5):
    print(item)
print("----------------")

# test4: iterating in reverse
with open(path) as f:
    for line in reversed(list(f)):
        print(line, end="")
print("----------------")

# test5: Taking a slice of an iterator
c = "zxcvbnmasdfghjklqwertyui"
print([x for x in islice(c, 10, 20)])
print("----------------")

# test6: Skipping lines
with open(path) as f:
    lines = [line for line in f if not line.startswith('erdem')]
    for line in lines:
        print(line, end='')
print("----------------")

# test7: Index-value pairs
word_summary = defaultdict(list)
with open(path, 'rt') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    try:
        words = [w.strip().lower() for w in line.split()]
        for word in words:
            word_summary[word].append(idx)
    except ValueError as e:
        print('Line: {} parse error: {}'.format(idx, e))
print(word_summary)
print("----------------")

# test8: zip
xpts = [1, 5, 6, 7, 2, 7]
ypts = [11, 33, 567, 99, 45, 354]
for i in zip(xpts, ypts):
    print(i)
for i in chain(xpts, ypts):
    print(i)
print("----------------")

# test9: Nested Sequence
def flatten(items, ignore_types = (str, bytes)):
    for item in items:
        if isinstance(item, Iterable) and not isinstance(item, ignore_types):
            yield from item
        else:
            yield item
nested_items = [2, 45, [33, 66, 5, 7]]
for item in flatten(nested_items):
    print(item)
