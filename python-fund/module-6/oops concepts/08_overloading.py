"""Overloading: handle different inputs with one method name."""


# Overloading means using one method name for different kinds or amounts of input.
# BASIC EXAMPLE: Python doesn't keep multiple same-named definitions in one class.
# An optional value lets one method handle two simple call patterns.
class Greeter:
    def greet(self, name="there"):
        # If no name is supplied, Python uses the default value "there".
        return f"Hello, {name}!"


greeter = Greeter()  # Make one Greeter object and call greet in two ways.
print("Basic:", greeter.greet())
print("Basic:", greeter.greet("Mina"))


# REAL-WORLD EXAMPLE: optional quantity and discount let one method calculate different bills.
class Bill:
    def total(self, price, quantity=1, discount=0):
        # Optional parameters let callers give only a price or add quantity/discount.
        return price * quantity - discount


bill = Bill()
print("Real world, one item:", bill.total(10))
print("Real world, several items with discount:", bill.total(10, 3, 5))


# Operator overloading gives operators such as + a meaning for our own objects.
# Python calls __add__ when it sees Points object + Points object.
class Points:
    def __init__(self, value):
        # Store the numeric point value on this object.
        self.value = value

    def __add__(self, other):
        # Python calls this method for left_point + right_point.
        # Return a new Points object whose value is the sum.
        return Points(self.value + other.value)


print("Operator overloading:", (Points(2) + Points(3)).value)
