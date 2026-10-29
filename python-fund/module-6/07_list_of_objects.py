"""Concept: a list can hold many objects made from the same class."""


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_result(self):
        if self.marks >= 40:
            return "Pass"
        return "Try again"


students = [
    Student("Ravi", 82),
    Student("Asha", 91),
    Student("Mina", 35),
]

for student in students:
    print(student.name, "-", student.show_result())
