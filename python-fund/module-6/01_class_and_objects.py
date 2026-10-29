"""Concept: a class is a design; objects are individual things made from it."""


class Student:
    pass  # We will add information and actions to this class in later examples.


# Calling the class creates two separate Student objects.
student_one = Student()
student_two = Student()

print(type(student_one))
print(student_one is student_two)  # False: they are different objects.
