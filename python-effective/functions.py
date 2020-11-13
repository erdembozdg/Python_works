
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

