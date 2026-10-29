"""Concept: __init__ runs when an object is created and sets its first data."""


class Student:
    def __init__(self, name, age, marks):
        # self.name, self.age, and self.marks are attributes on this object.
        self.name = name
        self.age = age
        self.marks = marks


student = Student("Ravi", 19, 82)
student2 = Student("harsh", 23, 100)

print("Name:", student.name)
print("Age:", student.age)
print("Marks:", student.marks)

print("Name:", student2.name)
print("Age:", student2.age)
print("Marks:", student2.marks)
