"""Concept: assigning an object to another name does not copy the object."""


class Toy:
    def __init__(self, name):
        self.name = name


first_name = Toy("Rocket")
second_name = first_name  # Both names refer to the same Toy object.

second_name.name = "Blue Rocket"
print(first_name.name)  # The change is visible through both names.
print(first_name is second_name)  # True: same object.

# Calling the class again creates a separate object.
third_name = Toy("Robot")
print(first_name is third_name)  # False: separate objects.
