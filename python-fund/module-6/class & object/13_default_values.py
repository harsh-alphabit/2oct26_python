"""Concept: __init__ parameters can have default values."""


class Student:
    def __init__(self, name, marks=0):
        self.name = name
        self.marks = marks


student_with_marks = Student("Ravi", 82)
student_without_marks = Student("Mina")  # marks uses its default: 0.

print(student_with_marks.name, student_with_marks.marks)
print(student_without_marks.name, student_without_marks.marks)
