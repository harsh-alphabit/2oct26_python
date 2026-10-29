"""Concept: check starting data before saving it on an object."""


class Student:
    def __init__(self, name, marks):
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")

        self.name = name
        self.marks = marks


good_student = Student("Ravi", 82)
print(good_student.name, "has", good_student.marks, "marks")

# Uncomment the next line to see the ValueError for invalid starting marks.
# bad_student = Student("Asha", 120)
