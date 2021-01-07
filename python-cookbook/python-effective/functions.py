
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        raise ValueError('Input errors') from e

try:
    result = divide(2, 0)
except ValueError:
    print('Input errors')
else:
    print('Result: %.1f' % result)


def sort_priority(values, group):
    found = False
    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found

values = [8, 3, 1, 2, 5, 4, 7, 6]
group = {3, 6, 8, 2}
result = sort_priority(values, group)
print(values, result)

class Sort(object):
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)

sorter = Sort(group)
values.sort(key=sorter)
print(values)
assert sorter.found is True


from itertools import islice
def index_word(f):
    offset = 0
    for line in f:
        if line:
            yield offset
        for index, letter in enumerate(line):
            offset +=1
            if letter == ' ':
                yield offset

with open('python-cookbook/files/data.txt', 'r') as f:
    it = index_word(f)
    result = islice(it, 3, 4)
    print(list(result))

import time, datetime
def normalize(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percentage = 100 * value / total
        result.append(percentage)
    return result
print(normalize(lambda: values))


import json
def decode(data, default=None, when=None, ignore=False):
    if default == None:
        default = {}
    when = datetime.datetime.now() if when is None else when
    try:
        print("%s %s" % (json.loads(data), when))
    except ValueError:
        if ignore:
            return 0
        print("%s %s" % (default, when))
decode("Hello World", ignore = True)

