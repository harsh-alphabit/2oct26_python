"""Beginner lesson for __str__, __name__, and __main__.

First run this file. Then run run_import_example.py to see the import case.
"""


# 1. __str__ lets us choose what a printed object looks like.
class Course:
    def __init__(self, title, duration_weeks):
        self.title = title
        self.duration_weeks = duration_weeks

    def __str__(self):
        # print(course) will show the text returned here.
        return f"{self.title} course ({self.duration_weeks} weeks)"


python_course = Course("Python Basics", 6)

print("__str__ example:", python_course)
print("str() example:", str(python_course))


# 2. __name__ tells Python's name for this file.
print("This file's __name__ value is:", __name__)

# When you run this file, __name__ is "__main__" and this message appears.
# When run_import_example.py imports it, this block is skipped.
if __name__ == "__main__":
    print("This file was run directly.")
else:
    print("This file was imported by another file.")


# Remember: __str__ describes an object; __name__ tells how this file is being used.
