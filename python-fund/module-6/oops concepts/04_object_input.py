"""Collect user input and pass it into a new object's constructor."""


class Student:
    def __init__(self, name, age):
        # Save the values received from the user on the new object.
        self.name = name  # Save the name on this particular Student object.
        self.age = age  # Save the age on this particular Student object.

    def introduce(self):
        # Build a readable message from this object's saved data.
        return f"I am {self.name}, age {self.age}."


# BASIC EXAMPLE: the user types values used to create the object.
if __name__ == "__main__":
    # This block runs only when this file is started directly.
    # input() displays a prompt and waits for the learner to type a response.
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))  # input() gives text; convert to a number.
    student = Student(name, age)  # Pass the typed values into the class to make an object.
    print("Basic:", student.introduce())

    # REAL-WORLD EXAMPLE: collect details for a course registration.
    course = input("Enter course name: ")  # Collect one more value for registration.
    registration = Student(name, age)  # Build a student object from the earlier answers.
    print(f"Real world: {registration.name} registered for {course}.")
