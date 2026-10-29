"""Concept: lists, dictionaries, and classes solve different kinds of tasks."""


# A list is useful for an ordered collection of values.
temperatures = [28, 30, 29]
print("Today's temperatures:", temperatures)

# A dictionary is useful for a small group of labeled values.
student_record = {"name": "Ravi", "marks": 82}
print("Student name from dictionary:", student_record["name"])

# A class is useful when similar records also have related actions.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def passed(self):
        return self.marks >= 40


student = Student("Ravi", 82)
print("Student name from object:", student.name)
print("Did the student pass?", student.passed())
