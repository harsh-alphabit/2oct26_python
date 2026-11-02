"""Overriding: a child class replaces an inherited method's behavior."""


# BASIC EXAMPLE: a child class can provide its own version of a method.
class Employee:
    def role(self):
        # Parent/default behavior used by a general employee.
        return "General employee"


class Developer(Employee):  # Developer is an Employee and inherits its role method.
    def role(self):  # This replaces Employee.role for Developer objects.
        # Specialized behavior: a Developer object gives a more specific role.
        return "Software developer"


print("Basic:", Employee().role())
print("Basic:", Developer().role())


# REAL-WORLD EXAMPLE: delivery types estimate travel time differently.
class Delivery:
    def __init__(self, distance_km):
        # Save distance so each delivery type can calculate its own estimate.
        self.distance_km = distance_km

    def estimate_minutes(self):
        # Default estimate supplied by the parent class.
        return self.distance_km * 10


class BikeDelivery(Delivery):  # This child replaces the parent's ETA calculation.
    def estimate_minutes(self):
        # The bike uses its own example speed rule to estimate travel time.
        return self.distance_km * 6


class VanDelivery(Delivery):  # This child provides another version of the same method.
    def estimate_minutes(self):
        # The van uses a different example speed rule.
        return self.distance_km * 4


for delivery in [BikeDelivery(5), VanDelivery(5)]:
    # Same method call; the object's class selects the matching calculation.
    print("Real world:", type(delivery).__name__, "ETA:", delivery.estimate_minutes(), "minutes")
