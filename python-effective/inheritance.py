
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
