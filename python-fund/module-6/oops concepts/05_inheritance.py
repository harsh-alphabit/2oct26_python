"""Inheritance and its common types, with simple examples."""


# Inheritance means a child class can reuse methods from a parent class.
# BASIC: SINGLE inheritance has one child class and one parent class.
class Employee:
    def clock_in(self):
        # A shared action that child employee types can reuse.
        return "Employee clocked in"


class Intern(Employee):  # Intern is a kind of Employee, so it inherits clock_in().
    def learn(self):
        # This action belongs only to the Intern child class.
        return "Intern is learning"


intern = Intern()  # This object can use methods from both Intern and Employee.
print("Single:", intern.clock_in(), "and", intern.learn())


# BASIC: MULTILEVEL inheritance passes through a chain: parent -> child -> grandchild.
class Organization:
    def follow_policy(self):
        # This method will be inherited through multiple levels.
        return "Following company policy"


class Department(Organization):  # Department inherits follow_policy from Organization.
    pass


class SupportTeam(Department):  # SupportTeam gets the method through Department.
    pass


print("Multilevel:", SupportTeam().follow_policy())


# BASIC: HIERARCHICAL inheritance means multiple child classes share one parent.
class EmployeeBase:
    def describe(self):
        # Shared method for all employee types below.
        return "I am an employee"


class Developer(EmployeeBase):
    pass


class Designer(EmployeeBase):
    pass


print("Hierarchical:", Developer().describe(), ";", Designer().describe())


# BASIC: MULTIPLE inheritance means one child class inherits from two parent classes.
class Camera:
    def take_photo(self):
        # Camera feature that CameraPhone will inherit.
        return "Photo taken"


class Phone:
    def call(self):
        # Phone feature that CameraPhone will inherit.
        return "Calling"


class CameraPhone(Camera, Phone):  # It gets take_photo() and call() from both parents.
    pass


device = CameraPhone()
print("Multiple:", device.take_photo(), "and", device.call())


# BASIC: HYBRID inheritance combines patterns (here hierarchical and multiple).
# Device is the shared parent; two child classes lead to one class with both parents.
class Device:
    def power_on(self):
        # The shared base class provides a method to both device branches.
        return "Powered on"


class CameraDevice(Device):
    pass


class PhoneDevice(Device):
    pass


class SmartCameraPhone(CameraDevice, PhoneDevice):
    pass


print("Hybrid:", SmartCameraPhone().power_on())


# REAL-WORLD EXAMPLE: delivery types share common order details and status.
class Delivery:
    def __init__(self, order_number):
        # Save the order number once in the parent so all delivery types can use it.
        self.order_number = order_number

    def status(self):
        # Return a status message using the saved order number.
        return f"Order {self.order_number} is on the way"


class BikeDelivery(Delivery):  # BikeDelivery inherits the order number and status method.
    def vehicle(self):
        # Add information specific to bike deliveries.
        return "Bicycle"


delivery = BikeDelivery("A104")  # Child object receives its order number through inherited setup.
print("Real world:", delivery.status(), "by", delivery.vehicle())
