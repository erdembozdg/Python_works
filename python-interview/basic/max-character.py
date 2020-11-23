
from collections import defaultdict

def max_char1(string):
    map_char = defaultdict(int)
    for i in string:
        map_char[i] = 1 if map_char[i] is None else map_char[i] + 1
    maximum = 0
    for key, value in map_char.items():
        if maximum < value:
            maximum = value
            max_char = key
    return (max_char, maximum)

def max_char2(string):
    maximum = 0
    for i in set(string):
        value = string.count(i)
        if maximum < value:
            maximum = value
            max_char = i
    return (max_char, maximum)
assert max_char1("Hello World!!") == max_char2("Hello World!!")
