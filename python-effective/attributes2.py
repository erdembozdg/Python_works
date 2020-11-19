
'''
Descriptor Classes
'''
import weakref

class Grade:
    def __init__(self):
        self._values = weakref.WeakKeyDictionary()
    def __get__(self, instance, instance_type):
        if instance is None: return self
        return self._values.get(instance, 0)
    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")
        self._values[instance] = value

class Exam():
    writing_grade = Grade()

exam1  = Exam()
exam1.writing_grade = 82
exam2  = Exam()
exam2.writing_grade = 82
assert exam1.writing_grade == exam2.writing_grade
