'''
'__getattr__' is useful for use cases like lazily accessing schemales data, which is only called for missing attributes.
'__getattribute__' and '__setattr__' are called every time an attribute is accessed on an object.
'''
class LazyDB:
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = 'Value for %s is missing' % name
        setattr(self, name, value)
        return value

class LoggingDB1(LazyDB):
    def __getattr__(self, name):
        print('Called __getattr__(%s)' % name)
        return super().__getattr__(name)

    def __setattr__(self, name, value):
        print('Called __setattr__(%s, %s)' % (name, value))
        return super().__setattr__(name, value)

class LoggingDB2(LazyDB):
    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)
        try:
            return super().__getattribute__(name)
        except AttributeError:
            print('Called __getattr__(%s)' % name)
            return super().__getattr__(name)


data1 = LoggingDB1()
data2 = LoggingDB2()
data1.exists = 10
print(data1.foo)
print(f'exists: {data1.exists}')
print(data2.foo)
print(f'exists: {data2.exists}')
