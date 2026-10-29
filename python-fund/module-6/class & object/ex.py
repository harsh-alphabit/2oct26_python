class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

students = []

n = int(input("How many students do you want to add: "))

for i in range(n):
    print("\nEnter details for student", i + 1)

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    s = Student(name, age, marks)

    students.append(s)

for student in students:
    student.display()