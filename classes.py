
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
        self.sport = sport


class Node:

    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({})'.format(self._value)

    def add_children(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)
    
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


if __name__ == '__main__':
    
    root = Node(12)
    child_1 = Node(111)
    child_2 = Node(222)
    root.add_children(child_2)
    root.add_children(child_1)
    child_1.add_children(Node(44))
    child_2.add_children(Node(440))

    for r in root.depth_first():
        print(r)


    file_name = "data.txt"
    courses_1 = ['python','ruby','javascript']
    erdem = Student("erdem", "hossain", courses_1)
    print(erdem.add_to_file(file_name))

    courses_1 = ['python','ruby','javascript']
    erdem = StudentAthlete("erdem", "hossain",  "hockey", courses_1)
    print(erdem.sport)
    print(isinstance(erdem, Student))
