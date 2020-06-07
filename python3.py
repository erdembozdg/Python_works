
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

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{course} is not found")

    def __len__(self):
        return len(self.courses)

    def __repr__(self):
        return f"Student('{self.first_name}', '{self.last_name}')"

    def __str__(self):
        return f"First name: {self.first_name.capitalize()}\n\
        Last Name: {self.last_name.capitalize()}\
        \nCourse: {', '.join(map(str.capitalize ,self.courses))}"


courses_1 = ['python', 'rails']
erdem = Student("erdem", "bozdag")
erdem.add_course("rails")
erdem.add_course("java")

print(len(erdem))
print(repr(erdem))
print(erdem.__dict__)
