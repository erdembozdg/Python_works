import os
from abc import ABCMeta, abstractmethod
import io
import time
import math
import weakref
from functools import total_ordering


class Node():
    def __init__(self, value):
        self._value = value
        self._children = []
        self._parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = weakref.ref(value)

    def __repr__(self):
        return 'Node({})'.format(self._value)

    def add_children(self, node):
        self._children.append(node)
        node.parent = self

    def __iter__(self):
        return iter(self._children)
    
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

print("----------------")

_formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}'
}

class Date:
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)
    
    def __format__(self, code):
        if code == "":
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

def func():
    return "datacamp"


print("----------------")
# Descriptors
class Integer:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, cls):
        if instance is None:
            instance = self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected ')
        instance.__dict__[self.name] = value


    def __delete__(self, instance):
        del instance.__dict__[self.name]

print("----------------")

class Structure:
    _fields = []
    def __init__(self, *args, **kwargs):
        if len(self._fields) != len(args):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))

class SubStructure(Structure):
    _fields = ['x','y']

print("----------------")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({} {})'.format(self.x, self.y)
    
    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)

print("----------------")

class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.square_feet = self.width * self.length

@total_ordering
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()

    def add_room(self, room):
        self.rooms.append(room)

    def living_space(self):
        return sum(r.square_feet for r in self.rooms)
    
    def __str__(self):
        return '{}: {} square foot {}'.format(self.name,
                                              self.living_space,
                                              self.style)
    def __eq__(self, other):
        return self.living_space == other.living_space

    def __lt__(self, other):
        return self.living_space < other.living_space 
        
print("----------------")

if __name__ == '__main__':
    
    root = Node(12)
    child_1 = Node(111)
    child_2 = Node(222)
    root.add_children(child_2)
    root.add_children(child_1)
    child_1.add_children(Node(44))
    child_2.add_children(Node(440))

    for r in root.depth_first():
        print(r)

    print(child_1.parent)
    del root
    print(child_1.parent)

    d = Date(2019, 12, 120)
    d2 = Date.today()
    print(format(d, 'mdy'))
    print(format(d2))
    print('{:mdy}'.format(d))

    p = SubStructure(2,3, n = "erdem")
    print(p.x, p.y, p.n)

    p = Point(2, 3)
    print(getattr(p, 'distance')(0,0))

