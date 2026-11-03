class Course:
    def __init__(self, title, weeks):
        self.title = title
        self.weeks = weeks

    def __str__(self):
        # Python expects this method to return text.
        return f"{self.title} course, {self.weeks} weeks long"


course = Course("Python Basics", 6)
print(course)       # Python Basics course, 6 weeks long
course_text = str(course)
print(course_text)  # Python Basics course, 6 weeks long