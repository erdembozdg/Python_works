
import datetime
from collections import namedtuple
from collections import defaultdict
from collections import Counter
import string
from functools import total_ordering

stock = ("FB", 75.00, 75.03, 74.90)

def middle(stock, date):
    x, y , z, t = stock
    return (x, date)

value, date = middle(stock, datetime.date(2010, 10, 3))
print(stock[2:3])

Stock = namedtuple('Stock', 'a b c')
stock = Stock(1, 2, c=3)
print(stock.a)

stocks = {'x': (1,2,3,4),
'y': (3,4,5,6)}

print(stocks.get('x'))

keys = {}
keys['x'] = 'Y'
keys[5] = 'ee'
keys[('c', 'y')] = 11

for k,v in keys.items():
    print(k)

keys.setdefault('xx', 'eee')
print(keys['xx'])

def letter_frequency(sentence):
    frequencies = defaultdict(int)
    for item in sentence.split(' '):
        frequencies[item] += 1
    return frequencies

sentence = 'erdem dddd'
for x, v in letter_frequency(sentence).items():
    print(x, v)

def letter_frequency2(sentence):
    return Counter(sentence).most_common()

for x in letter_frequency2(sentence):
    print(x)

ch = string.ascii_letters

def letter_frequency3(sentence):
    frequency = [(c,0) for c in ch]
    for s in sentence:
        index =  ch.index(s)
        frequency[index] = (s, frequency[index][1] + 1)
    return frequency

@total_ordering
class Sortee:
    def __init__(self, num, string, num2):
        self.num = num
        self.string = string
    
    def __lt__(self, other):
        return self.num < other.num

    def __repr__(self):
        return '{}:{}'.format(self.num, self.string)

    def __eq__(self, obj):
        return all((
            self.num == obj.num,
            self.string == obj.string
        ))

a = Sortee(2, '3', 3)
b = Sortee(0, '3', 4)
c = Sortee(2, '3', 3)
l = [a, b, c]
print(l)
print(a == b)

from operator import itemgetter

l = [("hello",3), ("HELP", 33), ("Helo", 1)]
# l.sort(key=str.lower)
l.sort(key=itemgetter(1))
print(l)

song_library = [("Phantom Of The Opera", "Sarah Brightman"),
("Knocking On Heaven's Door", "Guns N' Roses"),
("Captain Nemo", "Sarah Brightman"),
("Patterns In The Ivy", "Opeth"),
("November Rain", "Guns N' Roses"),
("Beautiful", "Sarah Brightman"),
("Mal's Song", "Vixy and Tony")]

artists = set()
for x,y in song_library:
    artists.add(y)
print("All {}".format(artists.union(artists)))
artists = list(artists)  
artists.sort()
print(artists)
bands = {'Opeth', 'Vixy and Tony'}
print(dir(list))

from queue import Queue, LifoQueue, PriorityQueue

line = LifoQueue(maxsize=3)
line.put('one')
line.put('two')
print(line.empty())
print(line.get())
print(line.get())

line2 = PriorityQueue()
line2.put((22, 'e'))
line2.put((221, 'e1'))
line2.put((223, 'e3'))

while not line2.empty():
    print(line2.get())

import sys

filename = "data.txt"

with open(filename) as f:
    for index, line in enumerate(f):
        print("{} {}".format(index+1, line), end='')

class Joiner(list):
    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.result = '.'.join(self)

import random, string

with Joiner() as j:
    for i in range(10):
        j.append(random.choice(string.ascii_letters))

print(j.__class__.__name__, j.result)

def xyz(a,b, c=True, d=''):
    pass

xyz(b=1,a=2,d='qq')

def get_x(*x):
    pass

get_x()
get_x(3,3,3,4)

class Opt:
    default_options = {
        'ip': 123,
        'port': 90,
        'name': 'erdem',
        'pass': 123
    }

    def __init__(self, **kwargs):
        self.options = Opt.default_options
        self.options.update(kwargs)

    def __getitem__(self, index):
        return self.options[index]

opt = Opt(name='fff')
print(opt['name'])
print(opt['pass'])

def show_args(a1, a2, a3 = 'aa'):
    print(a1, a2, a3)

x = range(3)
y = {
    'a1': 11,
    'a2': 12
}
show_args(*x)
show_args(**y)

def my_f():
    print("My Function")
my_f.dec = 'aaaaaaaaaaaaa'

def my_f2():
    print("My Function2")
my_f2.dec = 'bbbbbbbbbbbbbb'

def my_f3(f):
    print('Dec: ', end=' ')
    print(f.dec)
    print(f.__class__.__name__)
    print(f.__name__)
    f()

my_f3(my_f)
my_f3(my_f2)

class A:
    def op(self):
        print('ddddddddd')

a = A()
a.op()
a.op = show_args
a.op(*x)

class CapitalIterable:
    def __init__(self, string):
        self.string = string

    def __iter__(self):
        return CapitalIterator(self.string)

class CapitalIterator:

    def __init__(self, string):
        self.words = [s.capitalize() for s in string.split()]
        self.index = 0

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()

        word = self.words[self.index]
        self.index += 1
        return word

    def __iter__(self):
        return self

iterable = CapitalIterable('the quick brown fox jumps over the lazy dog')
# iterable = iter(iterable)

# while True:
#     try:
#         print(next(iterable))
#     except StopIteration:
#         break

for i in iterable:
    print(i)



from collections import namedtuple

Book = namedtuple('Book', 'author title genre')

books = {
    Book('Erdem', 'Nightwatch', 'fantasy'),
    Book('Tom', 'The thief', 'western'),
    Book('Bob', 'Twice', 'fantasy')
}

f_authors = {book.author for book in books if book.genre == 'fantasy'}
print(f_authors)
f_titles = {book.title: book.author for book in books if book.genre == 'fantasy'}
print(f_titles)

# inname. outname = sys.argv[1:3]

def warning_filter():
    with open("data.txt") as inline:
        for line in inline:
            if 'er' in line:
                yield line.replace('er', '')

def warning_filter2():
    with open("data.txt") as inline:
        yield from (
            line.replace('er', '')
            for line in inline
            if 'er' in line
        )

with open("data.txt", "w") as outline:
    warnings = warning_filter()
    for w in warnings:
        outline.write(w)
    warnings = warning_filter2()
    for w in warnings:
        outline.write(w)

with open("data.txt") as inline:
    with open("data.txt", "w") as outline:
        warnings = (line.replace('er', '') for line in inline if 'er' in line)
        for w in warnings:
            outline.write(w)

print(warning_filter())


s = 'hello world'

template = """
public class {0} {{
public static void main(String[] args) {{
System.out.println("{label2}");
}}
}}"""
print(template.format('Dusty', label2 = 'writing'))

subtotal = 12.32
tax = subtotal * 0.07
total = subtotal + tax

print("Sub: ${0} Tax: ${1} Total: ${total}".format(
subtotal, tax, total=total))

ch = b'clinic\x63'
print(ch.decode('utf-8'))
print(s.encode('utf-8'))
b = bytearray(b'xyxyiu')

import re


match = re.match('hello', s)

if match:
    print('matches')


import pickle
import json

some_data = ["a list", "containing", 5,
"values including another list",
["inner", "list"]]

with open('test_seriliaze', 'wb') as f:
    pickle.dump(some_data, f)

with open('test_seriliaze', 'rb') as f:
    load_data = pickle.load(f)

assert some_data == load_data

class Contact:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return ("{} {}".format(self.name, self.surname))

c = Contact("John", "Smith")
print(json.dumps(c.__dict__))

class ContactEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Contact):
            return {
                'isContact': True,
                'name': obj.name,
                'surname': obj.surname,
                'fullname': obj.full_name
            }
        return super().default(obj)

print(json.dumps(c, cls=ContactEncoder))

def decode_contact(dic):
    if dic.get('isContact'):
        return Contact(dic['name'], dic['surname'])
    else:
        return dic

data = '{"isContact": true, "name": "John", "surname": "Smith", "fullname": "John Smith"}'
c = json.loads(data, object_hook=decode_contact)
print(c.full_name)
