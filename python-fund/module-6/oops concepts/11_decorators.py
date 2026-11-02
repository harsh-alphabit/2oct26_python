"""Decorator examples for beginners.

A decorator is a function that wraps another function to add behavior around it.
Run this file to see a simple decorator and a practical login-check example.
"""


# BASIC EXAMPLE
def announce(function):
    """Wrap a function so messages appear before and after its normal work."""

    def wrapper():
        # This runs before the original function.
        print("Starting the task")

        # Call the original function that was passed into announce().
        function()

        # This runs after the original function finishes.
        print("Task finished")

    # Give the wrapped function back to Python.
    return wrapper


@announce  # Same idea as: greet = announce(greet)
def greet():
    """The original function; its job is just to greet the class."""
    print("Hello, students!")


print("Basic decorator example:")
greet()  # Python calls wrapper(), which also calls the original greet().


# PRACTICAL EXAMPLE: check login before showing a student's report.
def requires_login(function):
    """Only call the decorated function when the first value says logged in."""

    def wrapper(is_logged_in, *args, **kwargs):
        # Stop before running the report when the user is not logged in.
        if not is_logged_in:
            return "Please log in to view this report."

        # Pass the remaining inputs through to the original function.
        return function(*args, **kwargs)

    return wrapper


@requires_login
def show_report(student_name):
    """Return the report message for one student."""
    return f"Showing the report for {student_name}."


print("\nPractical decorator example:")
print(show_report(False, "Mina"))  # Not logged in: the report is not shown.
print(show_report(True, "Mina"))   # Logged in: show_report() does its normal work.

# This login check is only for learning decorator flow. Real applications need
# proper authentication; this simple Boolean is not a security system.
