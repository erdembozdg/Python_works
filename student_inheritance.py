class Student:

    def __init__(self, first_name, last_name, courses=None):
        self.first_name = first_name
        self.last_name = last_name
        if courses is None:
            self.courses = []
        else:
            self.courses = courses

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f"{self.first_name} is already \
            enrolled in the {course} course" )

class StudentAthlete(Student):

    def __init__(self, first_name, last_name, sport, courses=None):
        super().__init__(first_name, last_name, courses)
        self.sport = sport


courses_1 = ['python','ruby','javascript']
erdem = StudentAthlete("erdem", "hossain",  "hockey", courses_1)
print(erdem.sport)
print(isinstance(erdem, Student))
