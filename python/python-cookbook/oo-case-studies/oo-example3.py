import abc

class BaseFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid File Format")
        self.filename = filename

class X(BaseFile):
    ext = 'x'
    def play(self):
        print('Playing {} as X'.format(self.filename))


class Y(BaseFile):
    ext = 'y'
    def play(self):
        print('Playing {} as Y'.format(self.filename))

x = X('aaa.x')
x.play()

class Loader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractproperty
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Loader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        
        return NotImplemented

class SubLoader:
    ext = '.x'
    def play(self):
        print('This will play')

print(isinstance(SubLoader(), Loader))

# Monkey Patching
class A:
    def __init__(self, num):
        self.num = num
        
    def __add__(self, other):
        return self.num + other.num 
def get_num(self):
    return self.num

a = A(3)
A.get_num = get_num
print(a.get_num())
        
        
    

