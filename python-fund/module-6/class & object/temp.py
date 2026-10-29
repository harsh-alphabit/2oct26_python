class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self,name,age):
        self.name=name
        self.age=age

        print(f"name = {name}")





student_a = Student("Ravi", 19, 82)
student_b = Student("Asha", 20, 91)

print(student_a.name)   # Ravi
print(student_b.marks)  # 91


student_a.display('harsh',23)