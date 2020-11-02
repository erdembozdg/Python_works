
from collections import deque, Counter
from collections import defaultdict, OrderedDict, namedtuple
from operator import itemgetter
from itertools import groupby
import heapq
import os

# Get Previous Lines(Deque) 
def search_lines(lines, pattern, history=5):
    p_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, p_lines
        p_lines.append(line)

def get_lines(file_name):
    with open(file_name, 'r') as f:
        for line, p_lines in search_lines(f, 'python', 5):
            for line in p_lines:
                print(line, end='')
            print(line)
            print('-'*20)

# n-largest n-smallest
stocks = [
    {'name': 'IBM', 'price': 32},
    {'name': 'Sony', 'price': 31},
    {'name': 'LG', 'price': 30},
    {'name': 'Google', 'price': 29},
    {'name': 'AWS', 'price': 28},
    {'name': 'Microsoft', 'price': 27},
    {'name': 'Sony', 'price': 26}
]
tech_names = ['IBM', 'AWS', 'Sony']

# Mapping keys to multiple values
dic = {
    'x': [1, 2, 3],
    'y': [4, 5]
}

# Removing Dublicates for unhashable types (e.g. dicts)
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield val
            seen.add(val)

# filter a list
def is_int(item):
    try:
        item = int(item)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    data_dir = os.getcwd() + '\\files'
    if any(f.endswith('.txt') for f in os.listdir(data_dir)):
        fpath = os.path.join(data_dir, 'data.txt')

    # Get Previous Lines(Deque) 
    get_lines(fpath)

    # n-largest n-smallest
    print(heapq.nlargest(2,stocks, key=lambda s: s['price']))
    print(heapq.nsmallest(2,stocks, key=lambda s: s['price']))

    # Mapping keys to multiple values
    new_dic = defaultdict(list)
    for k, v in dic.items():
        new_dic[k].append(v)

    # zip calculations
    print(min(zip(dic.values(), dic.keys())))
    print(max(zip(dic.values(), dic.keys())))
    print(sorted(zip(dic.values(), dic.keys())))

    # New dic with removed keys
    print({k:dic[k] for k in dic.keys() - {'y'}})
    print({k:v for k, v in new_dic.items()})

    # Removing Dublicates for unhashable types (e.g. dicts)
    print(list(dedupe(stocks, key = lambda s: s['name'])))

    # Most common words
    print(Counter(['w1', 'w1', 'w2', 'w2', 'w3']).most_common(2))

    # Sorting, min, max dict with common keys
    print(sorted(stocks, key=itemgetter('name')))
    print(min(stocks, key=itemgetter('name')))

    # Using groupby for a dict, noted that it only works for consecutive itmes
    stocks.sort(key=itemgetter('name'))
    for name, items in groupby(stocks, key=itemgetter('name')):
        print(name)
        print('\t', list(items))

    # filter a list
    li = [23, 56, 22, 98, 33] 
    print([l for l in li if l > 23])
    print(list(l for l in li if l > 23))
    li.append('N/A')
    print(list(filter(is_int, li)))

    # subset of a dict
    print({k:v for k,v in dic.items() if k in ['x', 'y']})
    print(dict((k,v) for k,v in dic.items() if k in ['x']))

    # Using nametuble, noted that it is immutable unlike dict
    Stock = namedtuple('Stock', ('name', 'shares', 'price'))
    records = [
        ('IBM', 3, 1.25),
        ('IBM', 2, 2.25)
    ]

    for record in records:
        stock = Stock(*record)
        print(stock.shares * stock.price)

    # merge dict
    merge_dics = dict(dic)
    merge_dics.update(new_dic)
    print(merge_dics['x'])




