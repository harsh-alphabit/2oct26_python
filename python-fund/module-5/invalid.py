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