
class A:
    def spam(self, x):
        self.x = x
        print('Printing spam..')

    def foo(self):
        print(f'Printing foo...{self.x}')

class B:
    def __init__(self):
        self._a = A()

    # def spam(self, x):
    #     return self._a.spam(x)

    # def foo(self):
    #     return self._a.foo()

    def __getattr__(self, name):
        return getattr(self._a, name)

class Proxy:
    def __init__(self, obj):
        self._obj = obj
    
    def __getattr__(self, name):
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)

    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            delattr(self._obj, name)

a = A()
b = B()
print(b.spam(22))
print(b.foo())

p = Proxy(a)
p.spam(23)
print()

