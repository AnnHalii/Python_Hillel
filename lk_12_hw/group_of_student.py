import uuid


class Student:
    def __init__(self, name, age, grades, group):
        self.name = name
        self.age = age
        self.grades = grades or {}
        self.group = group
        self._id = uuid.uuid4()

    def leave_group(self):
        self.group.delete_student(self)

    def change_group(self, other_group):
        self.group.delete_student(self)
        other_group.add_student(self)

    @property
    def avg_rate(self):
        return sum(self.grades.values()) / len(self.grades)


class Group:
    def __init__(self, name):
        self.name = name
        self.students = {}

    @property
    def avg_rate(self):
        return sum([student.avg_rate for student in self.students.values()]) / len(self.students)

    def add_student(self, student):
        self.students.setdefault(student._id, student)
        student.group = self

    def delete_student(self, student: Student):
        self.students.pop(student._id, None)
        student.group = None


def chek_its_ok():
    new_group = Group(name='new_group')
    other_group = Group(name='other_group')
    oleg = Student(name='Oleg', age=21, grades={'math': 4, 'bio': 4, 'history': 5}, group=new_group)
    andrey = Student(name='Andrey', age=22, grades={'math': 5, 'bio': 3, 'history': 5}, group=new_group)
    print(oleg.name, oleg._id, oleg.avg_rate)
    print(andrey.name, andrey._id, andrey.avg_rate)
    new_group.add_student(andrey)
    new_group.add_student(oleg)
    new_group.add_student(oleg)
    print(new_group.students)
    print(new_group.avg_rate)
    print(oleg.name, oleg.group.name)
    print(andrey.name, andrey.group.name)
    oleg.change_group(other_group)
    print(oleg.name, oleg.group.name)
    print(other_group.students)
    print(new_group.students)
    print(andrey.name, andrey.group.name)
    new_group.delete_student(andrey)
    print(new_group.students)
    new_group.delete_student(oleg)


chek_its_ok()