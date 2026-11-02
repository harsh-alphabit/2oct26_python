"""Abstraction: define what an object must do; hide how it does it."""

from abc import ABC, abstractmethod  # Tools for defining a class with required methods.


# BASIC EXAMPLE
class Appliance(ABC):  # ABC marks this as a base design, not a directly usable appliance.
    @abstractmethod
    def turn_on(self):
        pass  # The base class says this method is required; a child writes the steps.


class Fan(Appliance):  # Fan supplies the required turn_on method.
    def turn_on(self):
        # This is the Fan-specific implementation of the required operation.
        return "Fan is spinning"


print("Basic:", Fan().turn_on())
# Appliance() itself cannot be created until turn_on is implemented.


# REAL-WORLD EXAMPLE: each delivery type calculates a fee in its own way.
class DeliveryFee(ABC):  # This rule says every fee calculator needs calculate().
    @abstractmethod
    def calculate(self, distance):
        pass  # Each concrete delivery fee class must fill in this calculation.


class BikeFee(DeliveryFee):
    def calculate(self, distance):
        # Example rule: a base charge plus a charge for every kilometer.
        return 20 + distance * 5


fee_rule = BikeFee()  # Create a usable fee calculator that implements the abstract method.
print("Real world: delivery fee =", fee_rule.calculate(3))
