# Create a seperate initializer
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = self.first_name + " " + self.last_name
        
    @classmethod
    def from_full_name(cls, full_name, age):
        if not " " in full_name:
            raise ValueError
        first_name, last_name = full_name.split(" ", 2)
        return cls(first_name, last_name, age)            

    def greet(self):
        print("Hello my name is {0}".format(self.full_name))
        
e1 = Person("Erdem", "Bozdag", 39)
e2 = Person.from_full_name("Erdem Bozdag", 39)
assert e1.greet() == e2.greet()

# Inheritance
class Foo(object):
    def __init__(self):
        print("foo init")
    
    def foo_method(self):
        print("foo method")
    
    foo = 'attr foo of Foo'

class Bar(object):
    def __init__(self):
        print("bar init")
        
    def bar_method(self):
        print("bar method")

    foo = 'attr foo of Bar' # we won't see this.
    bar = 'attr bar of Bar'

class FooBar(Foo, Bar):
    def __init__(self):
        print("foobar init")
        super(FooBar, self).__init__()
        
    def foo_method(self):
        print("foobar method")
        super(FooBar, self).foo_method()
            
    foobar = 'attr foobar of FooBar'
    
fb = FooBar()
print(fb.foo)
print(FooBar.mro())
