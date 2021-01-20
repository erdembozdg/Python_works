from collections import namedtuple
import collections
'''
Avoid manking dictionaries with values that are other dictionaries or long tuples.
'''
class SimpleGradeBook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, score, weight, comment):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append((score, weight, comment))

    def average_grade(self, name):
        by_subject = self._grades[name]
        for subject, grades in by_subject.items():
            total, total_weight = 0, 0
            total = sum(score * weight for score, weight, _ in grades)
            total_weight = sum(weight for _, weight, _ in grades)
            yield (subject, total/total_weight)

grade = SimpleGradeBook()
grade.add_student("erdem")
grade.report_grade("erdem", "math", 83, 0.3, "Good")
grade.report_grade("erdem", "math", 93, 0.7, "Great")
print(list(grade.average_grade("erdem")))

'''
Multiple helper classes when your internal state dictionaries get complicated
'''
Grade = collections.namedtuple('Grade', ('score', 'weight', 'comment'))

class Subject:
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight, comment):
         self._grades.append(Grade(score, weight, comment))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight

class Student:
    def __init__(self):
        self._subjects = {}

    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count

class GradeBook:
    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name] 

book = GradeBook()
erdem = book.student("erdem")
math = erdem.subject("Math")
math.report_grade(83, 0.3, "Good")
math.report_grade(93, 0.7, "Great")
print(erdem.average_grade())






            

    


