
class MyBaseClass():
    def __init__(self, value):
        self.value = value

class Explicit(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value * 2)

class Implicit(MyBaseClass):
    def __init__(self, value):
        super().__init__(value * 2)

assert Explicit(5).value == Implicit(5).value

# Only consider using private attributes to avoid naming conflicts with subclasses.
class MyObject:
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10

    def get_private_field(self):
        return self.__private_field

    @classmethod
    def get_private_field_of_instance(cls, instance):
        return instance.__private_field

class MyChildObject(MyObject):
    def __init__(self):
        super().__init__()
        self._private_field = 11

foo = MyObject()
baz = MyChildObject()
print(foo.public_field)
assert MyObject.get_private_field_of_instance(foo) == foo.get_private_field()
assert baz._MyObject__private_field == 10
assert baz._private_field != baz.get_private_field()


class flist(list):
    def __init__(self, li):
        super().__init__(li)

    def frequency(self):
        counts = {}
        for item in self:
            counts.setdefault(item, 0)
            counts[item] += 1
        return counts

li = flist([1, 2, 3])
li.pop()
print(li.frequency())
