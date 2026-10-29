# 🐍 Python Classes — Complete Theory Guide

---

## 📌 Table of Contents

1. [Why Do We Need Classes?](#1--why-do-we-need-classes)
2. [What Problem Does It Solve?](#2--what-problem-does-it-solve)
3. [Why Not Just Use List / Dict?](#3--why-not-just-use-list--dict)
4. [What is a Class?](#4--what-is-a-class)
5. [What is an Object (Instance)?](#5--what-is-an-object-instance)
6. [`__init__()` — The Constructor](#6--__init__--the-constructor)
7. [`self` — The Current Object](#7--self--the-current-object)
8. [Instance Variables](#8--instance-variables)
9. [Methods (Functions Inside a Class)](#9--methods-functions-inside-a-class)
10. [Class Variables vs Instance Variables](#10--class-variables-vs-instance-variables)
11. [Encapsulation (Data Hiding)](#11--encapsulation-data-hiding)
12. [Inheritance (Parent → Child)](#12--inheritance-parent--child)
13. [`super()` — Call Parent's Method](#13--super--call-parents-method)
14. [Method Overriding](#14--method-overriding)
15. [Polymorphism](#15--polymorphism)
16. [`__str__` and `__repr__`](#16--__str__-and-__repr__)
17. [`@staticmethod` and `@classmethod`](#17--staticmethod-and-classmethod)
18. [Private Variables (`_` and `__`)](#18--private-variables-_-and-__)
19. [`@property` Decorator](#19--property-decorator)
20. [Multiple Inheritance](#20--multiple-inheritance)
21. [Abstract Class](#21--abstract-class)
22. [Quick Cheat Sheet](#22--quick-cheat-sheet)

---

## 1. 🤔 Why Do We Need Classes?

Imagine you're building a **Student Management System**. Each student has a name, age, marks, and you need functions like `get_grade()`, `is_pass()`, etc.

**Without classes**, you'd write something like this:

```python
# Student 1
student1_name = "Ravi"
student1_age = 20
student1_marks = 85

# Student 2
student2_name = "Priya"
student2_age = 21
student2_marks = 72

def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    else:
        return "C"

print(get_grade(student1_marks))  # B
```

### ❌ Problems with this approach:

| Problem | Explanation |
|---------|-------------|
| **Too many variables** | For 100 students, you'd create 300 variables! |
| **No connection** | `student1_name` and `get_grade()` are not linked — they're floating around separately |
| **Easy to mess up** | You might accidentally pass `student2_marks` when you meant `student1_marks` |
| **Hard to maintain** | Adding a new field (like phone number) means changing code everywhere |

> **Classes solve all of these problems by bundling data + functions together into one unit.**

---

## 2. 🧩 What Problem Does It Solve?

Classes solve the problem of **organizing related data and behavior together**.

Think of it like this:

| Real World | Programming |
|------------|------------|
| A **car** has color, speed, fuel — and it can **start**, **stop**, **accelerate** | A **class** has variables (data) — and it has **methods** (functions) |
| Each **specific car** (your Honda, my Toyota) is different | Each **object** is a different instance of the same class |

### The core idea:

```
Class = Blueprint (template)
Object = Actual thing made from that blueprint
```

A class is like a **cookie cutter** 🍪 — you use the same cutter to make many cookies, but each cookie can have different toppings (data).

---

## 3. 🆚 Why Not Just Use List / Dict?

Good question! Let's try to manage students with a dict:

### Attempt with Dict:

```python
student1 = {
    "name": "Ravi",
    "age": 20,
    "marks": 85
}

student2 = {
    "name": "Priya",
    "age": 21,
    "marks": 72
}

def get_grade(student):
    if student["marks"] >= 90:
        return "A"
    elif student["marks"] >= 75:
        return "B"
    return "C"

print(get_grade(student1))  # B
```

### This works! But here are the problems:

| Problem | Dict | Class |
|---------|------|-------|
| **Typos** | `student["nme"]` → `KeyError` at runtime 💥 | `student.nme` → your editor warns you immediately |
| **No rules** | Anyone can do `student["marks"] = -500` (invalid!) | Class can **validate** data inside `__init__` |
| **Functions are separate** | `get_grade(student1)` — function is NOT part of the student | `student1.get_grade()` — function BELONGS to the student |
| **No structure enforcement** | One dict might have `"marks"`, another might have `"score"` — no consistency | Every object follows the same blueprint |
| **No inheritance** | Can't create a `ScienceStudent` that extends a `Student` | Easy! `class ScienceStudent(Student)` |

### Same thing with a Class:

```python
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        return "C"

s1 = Student("Ravi", 20, 85)
print(s1.get_grade())  # B

# s2 = Student("Priya", 21, -50)  # ❌ ValueError! Class protects the data
```

> **Summary**: Use **dict** for simple key-value data. Use **class** when your data has **behavior** (functions) and needs **rules/structure**.

---

## 4. 📦 What is a Class?

A class is a **blueprint** or **template** for creating objects.

```python
class Car:
    pass  # empty class — but it's valid!
```

- `class` → keyword to define a class
- `Car` → name of the class (always **CamelCase** by convention)
- `pass` → placeholder (means "nothing here yet")

Think of it like an **architect's plan** — it describes what a house will look like, but it's not a house itself.

---

## 5. 🏗️ What is an Object (Instance)?

An **object** is a **real thing** created from the class blueprint.

```python
class Car:
    pass

car1 = Car()  # object 1
car2 = Car()  # object 2

print(type(car1))  # <class '__main__.Car'>
print(car1 == car2)  # False — they are two DIFFERENT objects
```

| Term | Meaning |
|------|---------|
| **Class** | The blueprint / template |
| **Object** | A real thing created from the class |
| **Instance** | Same as object (used interchangeably) |
| **Instantiation** | The act of creating an object from a class |

```
Car  → class (blueprint)
car1 = Car()  → object / instance (actual car)
car2 = Car()  → another object / instance (another car)
```

---

## 6. 🔧 `__init__()` — The Constructor

`__init__` is a **special method** that runs **automatically** when you create an object. It **initializes** (sets up) the object's data.

```python
class Student:
    def __init__(self, name, age):
        self.name = name  # store name inside the object
        self.age = age    # store age inside the object

s1 = Student("Ravi", 20)  # __init__ runs automatically here
print(s1.name)  # Ravi
print(s1.age)   # 20
```

### Breaking it down:

```
Student("Ravi", 20)
   │
   ▼
Python does two things:
   1. Creates a new empty object
   2. Calls __init__(self, "Ravi", 20)
      │
      ▼
   self.name = "Ravi"   →  saves "Ravi" inside this object
   self.age  = 20       →  saves 20 inside this object
```

### Key points:

- `__init__` is called **constructor** (it constructs/builds the object)
- The double underscores `__` are called **dunder** (double underscore)
- It does NOT return anything (no `return` statement)
- It runs **every time** you create a new object

### Common mistake:

```python
class Student:
    def __init__(self, name):
        name = name  # ❌ WRONG! This is just a local variable, NOT saved in object

    # Correct way:
    def __init__(self, name):
        self.name = name  # ✅ self.name saves it INSIDE the object
```

---

## 7. 🪞 `self` — The Current Object

`self` is a **reference to the current object**. It's how the object talks about **itself**.

```python
class Dog:
    def __init__(self, name):
        self.name = name  # "Hey object, YOUR name is ___"

    def bark(self):
        print(f"{self.name} says: Woof!")  # "Hey object, what's YOUR name?"

dog1 = Dog("Tommy")
dog2 = Dog("Bruno")

dog1.bark()  # Tommy says: Woof!
dog2.bark()  # Bruno says: Woof!
```

### How `self` works behind the scenes:

```python
dog1.bark()
# Python secretly converts this to:
Dog.bark(dog1)
# So self = dog1

dog2.bark()
# Python secretly converts this to:
Dog.bark(dog2)
# So self = dog2
```

### Key rules about `self`:

| Rule | Explanation |
|------|-------------|
| `self` must be the **first parameter** in every method | Python passes the object automatically |
| You **don't pass** `self` when calling | `dog1.bark()` NOT `dog1.bark(dog1)` |
| `self` is not a keyword | You could name it `this` or `abc`, but **always use `self`** (convention) |
| Use `self.___` to access/set object data | Without `self`, it's just a local variable |

### Visualizing `self`:

```
dog1 (object in memory)          dog2 (object in memory)
┌──────────────────┐             ┌──────────────────┐
│ name = "Tommy"   │             │ name = "Bruno"   │
└──────────────────┘             └──────────────────┘
       ▲                                ▲
       │                                │
  self refers                      self refers
  to dog1 when                     to dog2 when
  dog1.bark()                      dog2.bark()
  is called                        is called
```

---

## 8. 📊 Instance Variables

Instance variables are **data that belongs to a specific object**. Each object has its own copy.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner      # instance variable
        self.balance = balance  # instance variable

acc1 = BankAccount("Ravi", 5000)
acc2 = BankAccount("Priya", 8000)

print(acc1.balance)  # 5000
print(acc2.balance)  # 8000

acc1.balance = 6000  # only acc1 changes
print(acc1.balance)  # 6000
print(acc2.balance)  # 8000 — acc2 is NOT affected
```

### Key point:
> Each object has its **own separate copy** of instance variables. Changing one object doesn't affect the other.

---

## 9. ⚙️ Methods (Functions Inside a Class)

A **method** is simply a **function defined inside a class**. It describes what the object can **do**.

```python
class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        return self.num ** 2

    def cube(self):
        return self.num ** 3

    def is_even(self):
        return self.num % 2 == 0

c = Calculator(4)
print(c.square())   # 16
print(c.cube())     # 64
print(c.is_even())  # True
```

### Methods with parameters:

```python
class Calculator:
    def __init__(self, num):
        self.num = num

    def add(self, other):
        return self.num + other

    def multiply(self, other):
        return self.num * other

c = Calculator(10)
print(c.add(5))       # 15
print(c.multiply(3))  # 30
```

### Methods that modify the object:

```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def reset(self):
        self.count = 0

c = Counter()
c.increment()
c.increment()
c.increment()
print(c.count)  # 3

c.decrement()
print(c.count)  # 2

c.reset()
print(c.count)  # 0
```

---

## 10. 🏷️ Class Variables vs Instance Variables

| Feature | Class Variable | Instance Variable |
|---------|---------------|-------------------|
| **Where defined** | Inside class, outside any method | Inside `__init__` with `self.` |
| **Shared?** | Shared by ALL objects | Each object has its OWN copy |
| **Accessed via** | `ClassName.var` or `self.var` | `self.var` only |
| **Use case** | Data common to all objects | Data unique to each object |

```python
class Employee:
    # Class variable — shared by ALL employees
    company = "TCS"
    employee_count = 0

    def __init__(self, name, salary):
        # Instance variables — unique to EACH employee
        self.name = name
        self.salary = salary
        Employee.employee_count += 1  # increment shared counter

e1 = Employee("Ravi", 50000)
e2 = Employee("Priya", 60000)
e3 = Employee("Amit", 55000)

print(e1.company)              # TCS (accessing class var through object)
print(Employee.company)        # TCS (accessing class var through class)
print(Employee.employee_count) # 3 (shared — counts ALL employees)

print(e1.name)  # Ravi (instance var — unique to e1)
print(e2.name)  # Priya (instance var — unique to e2)
```

### ⚠️ Tricky behavior — modifying class variable through object:

```python
class Student:
    school = "ABC School"  # class variable

s1 = Student()
s2 = Student()

# This does NOT modify the class variable!
# It creates a NEW instance variable on s1
s1.school = "XYZ School"

print(s1.school)       # XYZ School (s1's own instance variable)
print(s2.school)       # ABC School (still using class variable)
print(Student.school)  # ABC School (class variable unchanged)

# To actually change the class variable:
Student.school = "New School"
print(s2.school)  # New School (now s2 sees the change)
```

---

## 11. 🔒 Encapsulation (Data Hiding)

Encapsulation means **hiding the internal data** of an object and only allowing access through methods. This **protects** the data from being misused.

### The problem without encapsulation:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

acc = BankAccount(5000)
acc.balance = -10000  # 😱 Anyone can set a negative balance!
print(acc.balance)    # -10000 — this should NOT be allowed
```

### The solution with encapsulation:

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # __ makes it "private"

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Withdrawal amount must be positive!")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

acc = BankAccount(5000)
acc.deposit(2000)      # Deposited 2000. New balance: 7000
acc.withdraw(1000)     # Withdrew 1000. New balance: 6000
print(acc.get_balance())  # 6000

# Trying to access directly:
# print(acc.__balance)  # ❌ AttributeError!
```

> **Think of it like an ATM**: You can deposit and withdraw through the machine (methods), but you can't directly open the vault and take money (access private data).

---

## 12. 👨‍👦 Inheritance (Parent → Child)

Inheritance lets you **create a new class based on an existing class**. The child class gets everything from the parent class and can add its own stuff.

### Why inheritance?

```
Without inheritance:
  - Student class: name, age, get_info()
  - Teacher class: name, age, get_info(), subject
  
  → name, age, get_info() are REPEATED in both! 😫

With inheritance:
  - Person class: name, age, get_info()
  - Student(Person): inherits everything + adds student-specific stuff
  - Teacher(Person): inherits everything + adds teacher-specific stuff
  
  → No repetition! 🎉
```

```python
# Parent class (also called Base class / Super class)
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}!")

    def info(self):
        print(f"I am {self.name}")

# Child class (also called Derived class / Sub class)
class Dog(Animal):  # Dog INHERITS from Animal
    def fetch(self):  # new method only for Dog
        print(f"{self.name} fetches the ball!")

class Cat(Animal):  # Cat INHERITS from Animal
    def purr(self):  # new method only for Cat
        print(f"{self.name} purrs...")

# Using them:
dog = Dog("Tommy", "Woof")
dog.speak()   # Tommy says Woof!    ← inherited from Animal
dog.info()    # I am Tommy          ← inherited from Animal
dog.fetch()   # Tommy fetches the ball!  ← Dog's own method

cat = Cat("Kitty", "Meow")
cat.speak()   # Kitty says Meow!    ← inherited from Animal
cat.purr()    # Kitty purrs...      ← Cat's own method

# cat.fetch()  # ❌ Error! Cat doesn't have fetch()
```

### Terminology:

| Term | Meaning |
|------|---------|
| **Parent / Base / Super class** | The class being inherited FROM |
| **Child / Derived / Sub class** | The class that INHERITS |
| `class Dog(Animal)` | Dog inherits from Animal |
| `isinstance(dog, Animal)` | Returns `True` — Dog IS an Animal |

---

## 13. 🔗 `super()` — Call Parent's Method

`super()` lets the **child class call the parent's method**. Most commonly used in `__init__` to initialize the parent's data.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)  # call Person's __init__
        self.grade = grade  # add Student-specific data

    def info(self):
        super().info()  # call Person's info() first
        print(f"Grade: {self.grade}")  # then add more info

s = Student("Ravi", 20, "A")
s.info()
# Output:
# Name: Ravi, Age: 20
# Grade: A
```

### What happens WITHOUT `super()`?

```python
class Student(Person):
    def __init__(self, name, age, grade):
        # ❌ Forgot to call super().__init__()
        self.grade = grade

s = Student("Ravi", 20, "A")
print(s.grade)  # A ✅
print(s.name)   # ❌ AttributeError! name was never set
```

> **Rule**: If your child class has `__init__`, always call `super().__init__()` to properly initialize the parent's data.

---

## 14. 🔄 Method Overriding

When a child class **defines a method with the same name** as the parent, the child's version **replaces** (overrides) the parent's version.

```python
class Shape:
    def area(self):
        return 0

    def description(self):
        return "I am a shape"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # OVERRIDES Shape's area()
        return 3.14 * self.radius ** 2

    def description(self):  # OVERRIDES Shape's description()
        return f"I am a circle with radius {self.radius}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):  # OVERRIDES Shape's area()
        return self.width * self.height

    def description(self):
        return f"I am a rectangle ({self.width}x{self.height})"

c = Circle(5)
r = Rectangle(4, 6)

print(c.area())         # 78.5
print(c.description())  # I am a circle with radius 5
print(r.area())         # 24
print(r.description())  # I am a rectangle (4x6)
```

> The child class **replaces** the parent's method with its own version. The parent's method still exists — you can access it with `super()`.

---

## 15. 🎭 Polymorphism

**Polymorphism** = "many forms". The **same method name** behaves **differently** for different objects.

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"

# Polymorphism in action — same function works with different types!
def animal_sound(animal):
    print(animal.speak())  # calls speak() — but which one? Depends on the object!

animals = [Dog(), Cat(), Duck()]

for animal in animals:
    animal_sound(animal)

# Output:
# Woof!
# Meow!
# Quack!
```

### Why is this powerful?
The `animal_sound()` function **doesn't care** what type of animal it receives. It just calls `.speak()` and trusts that the object knows what to do. This is called **Duck Typing** in Python:

> *"If it walks like a duck and quacks like a duck, it's a duck."*
> — Python doesn't check the type, it just checks if the method exists.

---

## 16. 📝 `__str__` and `__repr__`

These special methods control **how your object looks when printed**.

### Without `__str__`:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Ravi", 20)
print(s)  # <__main__.Student object at 0x7f2b3c>  😕 Useless!
```

### With `__str__`:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"

    def __repr__(self):
        return f"Student('{self.name}', {self.age})"

s = Student("Ravi", 20)
print(s)        # Student(name=Ravi, age=20)       ← uses __str__
print(repr(s))  # Student('Ravi', 20)               ← uses __repr__
print([s])      # [Student('Ravi', 20)]              ← lists use __repr__
```

| Method | Purpose | When called |
|--------|---------|-------------|
| `__str__` | Human-readable, user-friendly output | `print(obj)`, `str(obj)`, f-strings |
| `__repr__` | Developer-friendly, detailed output | `repr(obj)`, in lists, in debugger |

> **Tip**: Always define at least `__repr__`. If you define only `__repr__`, Python uses it as a fallback for `__str__` too.

---

## 17. 🏷️ `@staticmethod` and `@classmethod`

### Regular Method (uses `self`):
- Needs an **object** to be called
- Can access instance data via `self`

### `@classmethod` (uses `cls`):
- Receives the **class** itself as the first argument
- Can access/modify **class variables**
- Often used as **alternative constructors**

### `@staticmethod` (no `self`, no `cls`):
- Doesn't need the object OR the class
- Just a regular function that **logically belongs** to the class

```python
class Pizza:
    total_pizzas = 0  # class variable

    def __init__(self, size, toppings):
        self.size = size          # instance variable
        self.toppings = toppings  # instance variable
        Pizza.total_pizzas += 1

    # Regular method — needs an object (self)
    def describe(self):
        return f"{self.size} pizza with {', '.join(self.toppings)}"

    # Class method — needs the class (cls)
    @classmethod
    def get_total(cls):
        return f"Total pizzas made: {cls.total_pizzas}"

    # Alternative constructor using classmethod
    @classmethod
    def margherita(cls):
        return cls("Medium", ["cheese", "tomato", "basil"])

    # Static method — needs nothing
    @staticmethod
    def validate_size(size):
        return size in ["Small", "Medium", "Large"]

# Using regular method (needs object):
p1 = Pizza("Large", ["pepperoni", "mushroom"])
print(p1.describe())  # Large pizza with pepperoni, mushroom

# Using class method (through class name):
p2 = Pizza.margherita()  # alternative constructor!
print(p2.describe())     # Medium pizza with cheese, tomato, basil

print(Pizza.get_total())  # Total pizzas made: 2

# Using static method (no object needed):
print(Pizza.validate_size("Medium"))  # True
print(Pizza.validate_size("Huge"))    # False
```

### Summary table:

| Type | First Param | Can access instance data? | Can access class data? |
|------|-------------|--------------------------|----------------------|
| Regular method | `self` | ✅ Yes | ✅ Yes |
| `@classmethod` | `cls` | ❌ No | ✅ Yes |
| `@staticmethod` | None | ❌ No | ❌ No |

---

## 18. 🔐 Private Variables (`_` and `__`)

Python uses **naming conventions** to indicate access levels:

| Prefix | Meaning | Example | Accessibility |
|--------|---------|---------|--------------|
| No prefix | Public | `self.name` | Accessible from anywhere |
| `_` (single underscore) | Protected (convention) | `self._name` | "Please don't touch this from outside" (but you still CAN) |
| `__` (double underscore) | Private (name mangling) | `self.__name` | Hard to access from outside (Python renames it) |

```python
class Employee:
    def __init__(self, name, salary, password):
        self.name = name          # public — anyone can access
        self._salary = salary     # protected — "internal use, don't touch"
        self.__password = password  # private — Python hides this

e = Employee("Ravi", 50000, "secret123")

print(e.name)       # ✅ Ravi
print(e._salary)    # ✅ 50000 (works, but you SHOULDN'T do this)
# print(e.__password)  # ❌ AttributeError!

# But Python doesn't truly hide it — it renames it (name mangling):
print(e._Employee__password)  # ✅ secret123 (not recommended!)
```

> **Python's philosophy**: "We're all adults here." Python doesn't enforce strict privacy — it just uses conventions to **signal intent**.

---

## 19. 🏠 `@property` Decorator

`@property` lets you **access a method like a variable**. It's useful for:
- Adding **validation** when setting values
- Computing values **on the fly**
- Making code **cleaner**

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius  # store internally

    @property
    def radius(self):
        """Getter — called when you READ circle.radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter — called when you WRITE circle.radius = ___"""
        if value <= 0:
            raise ValueError("Radius must be positive!")
        self._radius = value

    @property
    def area(self):
        """Computed property — calculated on the fly"""
        return 3.14 * self._radius ** 2

    @property
    def diameter(self):
        return self._radius * 2

c = Circle(5)

# These LOOK like variable access, but they're actually calling methods!
print(c.radius)    # 5       ← calls the getter
print(c.area)      # 78.5    ← calls the area property
print(c.diameter)  # 10      ← calls the diameter property

c.radius = 10      # ← calls the setter (validates!)
print(c.area)      # 314.0

# c.radius = -5    # ❌ ValueError: Radius must be positive!
# c.area = 100     # ❌ AttributeError: can't set (no setter defined for area)
```

---

## 20. 🌳 Multiple Inheritance

A class can inherit from **more than one parent class**.

```python
class Flyable:
    def fly(self):
        print(f"{self.name} is flying! 🦅")

class Swimmable:
    def swim(self):
        print(f"{self.name} is swimming! 🏊")

class Walkable:
    def walk(self):
        print(f"{self.name} is walking! 🚶")

# Duck inherits from ALL THREE!
class Duck(Flyable, Swimmable, Walkable):
    def __init__(self, name):
        self.name = name

d = Duck("Donald")
d.fly()   # Donald is flying! 🦅
d.swim()  # Donald is swimming! 🏊
d.walk()  # Donald is walking! 🚶
```

### Method Resolution Order (MRO):

When two parents have the same method name, Python follows a specific order:

```python
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):  # inherits from both B and C
    pass

d = D()
d.greet()  # Hello from B  (B comes first in the inheritance list)

# Check the MRO:
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

> **MRO Rule**: Python checks left to right → D → B → C → A → object

---

## 21. 🎨 Abstract Class

An abstract class is a class that **cannot be instantiated** (you can't create objects from it). It serves as a **template** that forces child classes to implement certain methods.

```python
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract Base Class
    @abstractmethod
    def area(self):
        """Every shape MUST implement area()"""
        pass

    @abstractmethod
    def perimeter(self):
        """Every shape MUST implement perimeter()"""
        pass

    def description(self):  # regular method — NOT abstract
        return "I am a shape"

# s = Shape()  # ❌ TypeError: Can't instantiate abstract class!

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # MUST implement this
        return 3.14 * self.radius ** 2

    def perimeter(self):  # MUST implement this
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

c = Circle(5)
r = Rectangle(4, 6)

print(c.area())        # 78.5
print(c.perimeter())   # 31.4
print(c.description()) # I am a shape  ← inherited from Shape

print(r.area())        # 24
print(r.perimeter())   # 20
```

### What if you forget to implement an abstract method?

```python
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    # ❌ Forgot to implement perimeter()!

# t = Triangle(3, 4)
# TypeError: Can't instantiate abstract class Triangle
# with abstract method perimeter
```

> Abstract classes are like a **contract**: "If you want to be a Shape, you MUST have `area()` and `perimeter()`."

---

## 22. 📋 Quick Cheat Sheet

```python
# ─── DEFINE A CLASS ───
class MyClass:
    class_var = "shared"                # class variable

    def __init__(self, x):              # constructor
        self.x = x                      # instance variable

    def method(self):                   # regular method
        return self.x

    @classmethod
    def class_method(cls):              # class method
        return cls.class_var

    @staticmethod
    def static_method():               # static method
        return "I don't need self or cls"

    def __str__(self):                  # print-friendly string
        return f"MyClass(x={self.x})"

    def __repr__(self):                 # developer string
        return f"MyClass({self.x})"


# ─── CREATE OBJECTS ───
obj = MyClass(10)
print(obj.x)            # 10
print(obj.method())     # 10
print(obj)              # MyClass(x=10)


# ─── INHERITANCE ───
class Child(MyClass):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y


# ─── KEY CONCEPTS ───
# self          → refers to the current object
# __init__      → runs when object is created (constructor)
# super()       → call parent class method
# @property     → access method like a variable
# @classmethod  → method that gets the class, not the object
# @staticmethod → method that gets nothing (utility function)
# __str__       → what print() shows
# __repr__      → what the debugger / lists show
# ABC           → abstract base class (can't instantiate)
# __var         → private (name mangled)
# _var          → protected (convention only)
```

---

### 🎯 When to Use What?

| Situation | Use |
|-----------|-----|
| Simple key-value data, no behavior | `dict` |
| Ordered collection of same-type items | `list` |
| Data with behavior (functions) | `class` |
| Data with rules/validation | `class` with `@property` |
| Multiple similar types sharing behavior | `class` + inheritance |
| Blueprint that forces child to implement methods | Abstract class |

---

> 💡 **Final takeaway**: A class is just a way to **group related data and functions together**. Start simple — use a dict. When you find yourself passing the same dict to many functions, that's when a class would make your code cleaner.
