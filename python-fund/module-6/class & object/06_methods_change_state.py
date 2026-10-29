"""Concept: an object's state is its current data; methods can change it."""


class Counter:
    def __init__(self):
        self.value = 0

    def increase(self):
        self.value += 1

    def show(self):
        print("Current value:", self.value)


counter = Counter()
counter.show()  # State starts at 0.
counter.increase()
counter.increase()
counter.show()  # State is now 2.
