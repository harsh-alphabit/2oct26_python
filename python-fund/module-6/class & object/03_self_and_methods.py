"""Concept: self is the current object; methods can use its own data."""


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        # self.name means the name belonging to the dog calling bark().
        print(f"{self.name} says woof!")


dog_one = Dog("Milo")
dog_two = Dog("Coco")

dog_one.bark()  # In this call, self refers to dog_one.
dog_two.bark()  # In this call, self refers to dog_two.
