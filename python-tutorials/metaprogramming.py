
from abc import ABCMeta, abstractmethod
import operator
from contextlib import contextmanager

class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError('Cannot instantiate directly')

class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance

class test1(metaclass=NoInstance):
    @staticmethod
    def grok():
        print('No instance')


class test2(metaclass=Singleton):
    def __init__(self):
        print('Creating Singleton pattern')

print("----------------")
class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxsize=None):
        pass

    @abstractmethod
    def write(self, data):
        pass

print("----------------")
# Extend Metadata
class MyMeta(type):
    def __new__(cls, clsname, bases, clsdict, *, debug=False, synchronize=False):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError('Bad attribute name', name)
        return super().__new__(cls, clsname, bases, clsdict)

    def __init__(self, clsname, bases, ns, *, debug=False, synchronize=False):
        return super().__init__(clsname, bases, ns)

class Root(metaclass=MyMeta, debug=True, synchronize=True):
    pass

class child(Root):
    def foobar(self):
        pass

print("----------------")

class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))

class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []
    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise TypeError('{} arguments required'.format(len(cls._fields)))
        return super().__new__(cls, args)

class Stock(StructTuple):
    _fields = ['name', 'shares', 'price']

print("----------------")

def type_property(name, expected_type):
    _name = '_' + name

    @property
    def prop(self):
        return getattr(self, __name)

    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError('{}  must be a {}'.format(name, expected_type))
        setattr(self, _name, value)
    
    return prop

class Person:
    name = type_property('name', str)
    age = type_property('age', int)
    def __init__(self, name, age):
        self.name = name
        self.age = age

print("----------------")
# Context Manager

@contextmanager
def list_transaction(items):
    li = list(items)
    yield li
    items[:] = li

print("----------------")

def test3():
    a = 10
    loc = locals()
    exec('b = a + 3')
    b = loc['b']
    print(b)



test1.grok()
x1 = test2()
x2 = test2()
print(x1 is x2)
s = Stock('xxx', 33, 2.3)
print(s[1])

items = [1, 2, 3]
with list_transaction(items) as l:
    l.append(4)

print(items)

test3()
exec('for i in range(10): print(i, end=\'\')')

