"""Class and object: a class is a design; objects are items made from it."""


# BASIC EXAMPLE: one class can describe different student objects.
# A class is the design; each object is one actual student made from it.
class Student:
    def __init__(self, name):  # __init__ runs when we create a new Student.
        # The value passed as name is saved on this particular student object.
        self.name = name  # self.name is data (an attribute) stored on this object.

    def introduce(self):
        # This method uses the object's saved name and returns a sentence.
        return f"My name is {self.name}."  # A function inside a class is called a method.


student = Student("Mina")  # Create an object and give it a starting name.
print("Basic:", student.introduce())


# REAL-WORLD EXAMPLE: create several student records from one class.
class CourseStudent:
    def __init__(self, name, course):
        # Store each student's details separately; every object gets its own values.
        self.name = name
        self.course = course

    def introduce(self):
        # Return a short summary using this object's attributes.
        return f"{self.name} is learning {self.course}."


students = [CourseStudent("Mina", "Python"), CourseStudent("Arun", "Web Design")]  # Two separate objects.
for student in students:
    # Repeat the same method call for each object in the list.
    print("Real world:", student.introduce())
