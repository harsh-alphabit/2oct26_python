# ============================================

#        Custom Exception Handling in Python
# ============================================

# To create a custom exception:
#   1. Create a class
#   2. Inherit from Exception (or any built-in exception)
#   3. Use 'raise' keyword to trigger it


# ----- Case 1: Simple Custom Exception -----

class TooYoungError(Exception):
    pass  # simplest custom exception — just a name

age = int(input("Enter your age: "))

if age < 18:
    raise TooYoungError("You must be 18 or older!")
else:
    print("Welcome! You are eligible.")


# ----- Case 2: Custom Exception with __init__ -----

class InvalidMarksError(Exception):
    def __init__(self, marks):
        self.marks = marks
        self.message = f"Invalid marks: {marks}. Marks must be between 0 and 100."

try:
    marks = int(input("Enter your marks: "))
    if marks < 0 or marks > 100:
        raise InvalidMarksError(marks)
    print(f"Your marks: {marks}")
except InvalidMarksError as e:
    print(e.message)


# ----- Case 3: Custom Exception with try-except -----

class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Cannot withdraw ₹{amount}. Your balance is only ₹{balance}."

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(balance, amount)
    return balance - amount

try:
    balance = 5000
    amount = int(input("Enter amount to withdraw: "))
    remaining = withdraw(balance, amount)
    print(f"Withdrawal successful! Remaining balance: ₹{remaining}")
except InsufficientBalanceError as e:
    print(e.message)


# ----- Case 4: Multiple Custom Exceptions -----

class EmptyNameError(Exception):
    pass

class NameTooShortError(Exception):
    pass

def validate_name(name):
    if name == "":
        raise EmptyNameError("Name cannot be empty!")
    if len(name) < 3:
        raise NameTooShortError(f"Name '{name}' is too short. Minimum 3 characters required.")

try:
    name = input("Enter your name: ")
    validate_name(name)
    print(f"Hello, {name}!")
except EmptyNameError as e:
    print(e)
except NameTooShortError as e:
    print(e)


# ----- Case 5: Custom Exception with Inheritance Hierarchy -----
# You can create a base exception and child exceptions

class AppError(Exception):
    """Base exception for our application"""
    pass

class DatabaseError(AppError):
    """Raised when database operation fails"""
    pass

class AuthenticationError(AppError):
    """Raised when login fails"""
    pass

try:
    logged_in = False
    if not logged_in:
        raise AuthenticationError("Login failed! Invalid username or password.")
except AppError as e:
    # This catches both DatabaseError and AuthenticationError
    print(f"Application Error: {e}")


# ============================================
#  Summary:
#  - Custom exceptions = class that inherits Exception
#  - Use 'raise' to trigger them
#  - Use try-except to handle them
#  - You can add __init__ for custom messages
#  - You can create a hierarchy (parent → child)
# ============================================

