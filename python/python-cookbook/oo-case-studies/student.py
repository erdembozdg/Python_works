import os
class Student:

    def __init__(self, first_name, last_name, courses=None):
        self._first_name = first_name
        self._last_name = last_name
        if courses is None:
            self.courses = []
        else:
            self.courses = courses

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError('Cannot delete attribute')

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._last_name = value

    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    def get_last_name(self):
        return self._first_name

    def del_first_name(self):
        raise AttributeError('Cannot delete attribute')

    name = property(set_first_name, get_last_name, del_first_name)

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

    def find_in_file(self, file_name):
        with open(file_name) as f:
            for line in f:
                first_name, last_name, courses = Student.prep_recod(line)
                student_read_in = Student(first_name, last_name, courses)
                if self == student_read_in:
                    return True
                return False

    def add_to_file(self, file_name):
        if self.find_in_file(file_name):
            return "Record is alread existed"
        else:
            record_to_append = Student.prep_to_write(self.first_name, self.last_name, self.courses)
            with open(file_name, "a+") as write_to_file:
                write_to_file.write(record_to_append+"\n")
            return "Record is added"

    @staticmethod
    def prep_recod(line):
        line = line.split(":")
        first_name, last_name = line[0].split(",")
        courses = line[1].rstrip().split(",")
        return first_name, last_name, courses

    @staticmethod
    def prep_to_write(first_name, last_name, courses):
        full_name = first_name + ',' + last_name
        courses = ', '.join(courses)
        return full_name + ':' + courses

    def __eq__(self, other):
        return self.first_name == other.first_name \
        and self.last_name == other.last_name

    def __repr__(self):
        return f"Student('{self.first_name}', '{self.last_name}')"

    def __str__(self):
        return f"First name: {self.first_name.capitalize()}\n\
        Last Name: {self.last_name.capitalize()}\
        \nCourse: {', '.join(map(str.capitalize ,self.courses))}"

class StudentAthlete(Student):

    def __init__(self, first_name, last_name, sport, courses=None):
        super().__init__(first_name, last_name, courses)
        self._sport = sport
    
    @property
    def first_name(self):
        print("Getting name")
        return super().first_name

    @first_name.setter
    def first_name(self, value):
        print("Setting name to", value)
        super(StudentAthlete, StudentAthlete).first_name.__set__(self, value)
    
    @first_name.deleter
    def first_name(self, value):
        print("Deleting name")
        super(StudentAthlete, StudentAthlete).first_name.__delete__(self)


if __name__ == '__main__':
    
    file_name = open("data.txt", "w")
    folder = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(folder, 'data.txt')

    courses_2 = ['python','ruby','javascript']
    erdem = Student("erdem", "hossain", courses_2)
    erdem.first_name = "Tom"
    print(erdem.add_to_file(file_name))

    erdem2 = StudentAthlete("erdem", "hossain", "", courses_2)
    erdem2.first_name = "xxx"
    print(erdem2.add_to_file(file_name))