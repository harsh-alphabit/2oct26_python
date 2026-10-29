"""Concept: a method can return an answer for the caller to use."""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Return the answer instead of printing inside the method.
        return self.length * self.width


room = Rectangle(5, 4)
room_area = room.area()

print("Room area:", room_area)
print("Twice the room area:", room_area * 2)
