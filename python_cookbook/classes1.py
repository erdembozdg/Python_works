import os
from abc import ABCMeta, abstractmethod
import io
import time
import math
import weakref
from functools import total_ordering

class Student():

    def __init__(self, first_name, last_name, courses=None):
        self._first_name = first_name
        self._last_name = last_name
        if courses is None:
            self.courses = []
        else:
            self.courses = courses

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError('Cannot delete attribute')

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')

    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    def get_last_name(self):
        return self._first_name

    def del_first_name(self):
        raise AttributeError('Cannot delete attribute')

    name = property(set_first_name, get_last_name, del_first_name)

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f"{self.first_name} is already \
            enrolled in the {course} course" )

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{course} is not found")

            def __len__(self):
                return len(self.courses)

    def find_in_file(self, file_name):
        with open(file_name) as f:
            for line in f:
                first_name, last_name, courses = Student.prep_recod(line)
                student_read_in = Student(first_name, last_name, courses)
                if self == student_read_in:
                    return True
                return False

    def add_to_file(self, file_name):
        if self.find_in_file(file_name):
            return "Record is alread existed"
        else:
            record_to_append = Student.prep_to_write(self.first_name, self.last_name, self.courses)
            with open(file_name, "a+") as write_to_file:
                write_to_file.write(record_to_append+"\n")
            return "Record is added"

    @staticmethod
    def prep_recod(line):
        line = line.split(":")
        first_name, last_name = line[0].split(",")
        courses = line[1].rstrip().split(",")
        return first_name, last_name, courses

    @staticmethod
    def prep_to_write(first_name, last_name, courses):
        full_name = first_name + ',' + last_name
        courses = ', '.join(courses)
        return full_name + ':' + courses

    def __eq__(self, other):
        return self.first_name == other.first_name \
        and self.last_name == other.last_name

    def __repr__(self):
        return f"Student('{self.first_name}', '{self.last_name}')"

    def __str__(self):
        return f"First name: {self.first_name.capitalize()}\n\
        Last Name: {self.last_name.capitalize()}\
        \nCourse: {', '.join(map(str.capitalize ,self.courses))}"

class StudentAthlete(Student):

    def __init__(self, first_name, last_name, sport, courses=None):
        super().__init__(first_name, last_name, courses)
        self._sport = sport
    
    @property
    def first_name(self):
        print("Getting name")
        return super().first_name

    @first_name.setter
    def first_name(self, value):
        print("Setting name to", value)
        super(StudentAthlete, StudentAthlete).first_name.__set__(self, value)
    
    @first_name.deleter
    def first_name(self, value):
        print("Deleting name")
        super(StudentAthlete, StudentAthlete).first_name.__delete__(self)

print("----------------")

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

    file_name = open("data.txt", "w")
    folder = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(folder, 'data.txt')

    courses_2 = ['python','ruby','javascript']
    erdem = Student("erdem", "hossain", courses_2)
    erdem.first_name = "Tom"
    print(erdem.add_to_file(file_name))

    erdem2 = StudentAthlete("erdem", "hossain", "", courses_2)
    erdem2.first_name = "xxx"
    print(erdem2.add_to_file(file_name))

    d = Date(2019, 12, 120)
    d2 = Date.today()
    print(format(d, 'mdy'))
    print(format(d2))
    print('{:mdy}'.format(d))

    p = SubStructure(2,3, n = "erdem")
    print(p.x, p.y, p.n)

    p = Point(2, 3)
    print(getattr(p, 'distance')(0,0))

