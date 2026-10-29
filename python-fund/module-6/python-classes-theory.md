# 🐍 Python Classes and Objects — Complete Beginner Guide

> **Module 6 lesson:** Learn how classes group related data and actions. Type each example, run it, and change the values yourself.

---

## 📌 Table of Contents

1. [Why Do We Need Classes?](#1--why-do-we-need-classes)
2. [What Problem Does a Class Solve?](#2--what-problem-does-a-class-solve)
3. [List vs Dictionary vs Class](#3--list-vs-dictionary-vs-class)
4. [What Is a Class?](#4--what-is-a-class)
5. [What Is an Object?](#5--what-is-an-object)
6. [Create Your First Class](#6--create-your-first-class)
7. [`__init__()` in Detail](#7--__init__-in-detail)
8. [`self` in Detail](#8--self-in-detail)
9. [Attributes and Methods](#9--attributes-and-methods)
10. [How Each Object Keeps Its Own Data](#10--how-each-object-keeps-its-own-data)
11. [Where Are Objects Stored?](#11--where-are-objects-stored)
12. [Object State](#12--object-state)
13. [Real-Time Example: Bank Account](#13--real-time-example-bank-account)
14. [Real-Time Example: Library Book](#14--real-time-example-library-book)
15. [Validation and Object Rules](#15--validation-and-object-rules)
16. [Methods That Return Values](#16--methods-that-return-values)
17. [When Should We Use a Class?](#17--when-should-we-use-a-class)
18. [Common Beginner Mistakes](#18--common-beginner-mistakes)
19. [Quick Revision](#19--quick-revision)
20. [Practice Questions](#20--practice-questions)

---

## 1. 🤔 Why Do We Need Classes?

Imagine we are building a **Student Management System**. Every student has a name, age, and marks. We may also want to calculate a result for each student.

Without a class, we might write:

```python
# Student 1
student1_name = "Ravi"
student1_age = 19
student1_marks = 82

# Student 2
student2_name = "Asha"
student2_age = 20
student2_marks = 91
```

This works for two students. But imagine storing 100 students. We would need 300 separate variables just for name, age, and marks. It would be easy to mix up which marks belong to which student.

We could also write a function that calculates a result:

```python
def get_result(name, marks):
    if marks >= 40:
        return f"{name} passed"
    return f"{name} needs to try again"


print(get_result("Ravi", 82))
```

This function works, but the function and the student's information are separate. As a program grows, we may pass the same student's information to many functions.

> **A class lets us keep the information about one kind of thing, and the actions related to it, together.**

---

## 2. 🧩 What Problem Does a Class Solve?

A class helps organize a program when it contains many similar things. Each thing has its own data, but the things share the same general structure and actions.

| Everyday example | Programming idea |
|---|---|
| A student has a name, age, marks, and can show a result | Student object has attributes and methods |
| Many students follow the same registration form | Student class is the shared design |
| Ravi and Asha have different marks | Each object stores its own values |

The basic idea is:

```text
Class  = design / template
Object = one particular thing made from that design
```

Think of a class like a blank registration form. The form says which details to collect. Each completed form represents one particular student.

Classes are especially helpful when related information and actions belong together. They are not needed for every small program; a few variables or a dictionary may be simpler for a small task.

---

## 3. 🆚 List vs Dictionary vs Class

Lists, dictionaries, and classes are all useful. A class is not automatically “better”; each one is suited to a different job.

### Use a list for a collection of items

```python
marks = [82, 91, 76]
print(marks[0])  # 82
```

A list keeps an ordered group of values. It is a good fit for marks, names, or a queue of tasks.

### Use a dictionary for labeled values

```python
student_data = {
    "name": "Ravi",
    "age": 19,
    "marks": 82,
}

print(student_data["name"])  # Ravi
```

A dictionary keeps key-value pairs. It is a good fit for a simple record or data received from a JSON file or an API.

### Use a class when similar things have data and actions

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def has_passed(self):
        return self.marks >= 40


student = Student("Ravi", 82)
print(student.name)          # Ravi
print(student.has_passed())  # True
```

| Situation | A natural choice |
|---|---|
| Keep an ordered collection of items | `list` |
| Keep a few labeled values together | `dict` |
| Represent many similar things with their own data and actions | `class` |

### Is a class better than a dictionary?

Not always. A dictionary may be simpler for one small record. A class is useful when we have many objects of the same kind, want each object to have the same design, and want actions or rules connected to that data.

One benefit is that we can write `student.has_passed()` instead of remembering to pass the right dictionary into a separate function. The class can also give a consistent place for operations and checks.

### Classes and lists can be used together

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


students = [
    Student("Ravi", 82),
    Student("Asha", 91),
    Student("Mina", 76),
]

for student in students:
    print(student.name, student.marks)
```

Here, each student is an object, and the list stores the group of student objects. This is a common pattern in real programs.

---

## 4. 📦 What Is a Class?

A **class** is a description used to create objects. It describes what information its objects can hold and what actions they can perform.

```python
class Student:
    pass
```

- `class` is the Python keyword that begins a class definition.
- `Student` is the class name. Class names conventionally use **CapitalizedWords**.
- `pass` means “there is no code here yet.” It lets us define an empty class temporarily.

A class by itself is only the design. We need to create an object from it to work with one particular student.

---

## 5. 🏗️ What Is an Object?

An **object** is one particular thing created from a class. It is also called an **instance** of the class.

```python
class Student:
    pass


student_a = Student()
student_b = Student()

print(type(student_a))          # <class '__main__.Student'>
print(student_a is student_b)   # False: they are different objects
```

| Word | Meaning |
|---|---|
| Class | The design used to create objects |
| Object / instance | One particular thing created from the class |
| Create an instance | Make an object by calling the class |

`student_a` and `student_b` were made from the same class, but they are two separate objects.

---

## 6. 🛠️ Create Your First Class

Let’s create students with their own names, ages, and marks:

```python
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks


student_a = Student("Ravi", 19, 82)
student_b = Student("Asha", 20, 91)

print(student_a.name)   # Ravi
print(student_b.marks)  # 91
```

`Student("Ravi", 19, 82)` creates one student object and gives it its starting information. Calling `Student(...)` again creates another object.

---

## 7. 🔧 `__init__()` in Detail

`__init__` is a special method Python calls automatically to **initialize** an object with its starting data.

```python
student_a = Student("Ravi", 19, 82)
```

For a beginner, think of the process like this:

1. Python creates a new `Student` object.
2. Python calls `__init__` for that object.
3. Python supplies the new object as the first argument, `self`.
4. The other values are supplied to `name`, `age`, and `marks`.
5. The assignments save those values on the new object.
6. The class call gives the finished object back, and `student_a` refers to it.

This is what the method receives conceptually:

```python
# Conceptually, Python calls something like:
Student.__init__(student_a, "Ravi", 19, 82)
```

We do not normally make this call ourselves. We simply write `Student("Ravi", 19, 82)`.

### Understand the assignment

```python
self.name = name
```

- `name` on the right is the value received by the method, such as `"Ravi"`.
- `self.name` on the left means the `name` attribute on this particular object.
- The assignment saves the received value on the object.

The names on the left and right can be different:

```python
def __init__(self, student_name):
    self.name = student_name
```

### What does the name `__init__` mean?

The double underscores on both sides are often called **dunder** (double underscore). The name `__init__` is short for initialize: it sets up an object's initial state.

In beginner lessons, `__init__` is often called a constructor. More precisely, Python's `__new__` method creates the object and `__init__` initializes it. For now, remember: **`__init__` runs automatically when we create an object and sets up its starting data.**

### `__init__` does not return the object

Python handles returning the object from the class call. Do not write `return self` in `__init__`. Usually there is no `return` statement in it. Returning a non-`None` value from `__init__` causes an error.

### Default values

We can make an argument optional by giving it a default:

```python
class Student:
    def __init__(self, name, age, marks=0):
        self.name = name
        self.age = age
        self.marks = marks


new_student = Student("Mina", 18)
print(new_student.marks)  # 0
```

If marks are not provided, they start at `0`. Required values such as `name` and `age` still need to be supplied.

---

## 8. 🪞 `self` in Detail

`self` refers to **the current object**: the object that is using the method right now. It lets a method access or change the correct object's information.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")


dog_a = Dog("Milo")
dog_b = Dog("Coco")

dog_a.bark()  # Milo says woof!
dog_b.bark()  # Coco says woof!
```

When `dog_a.bark()` runs, `self` means `dog_a`. When `dog_b.bark()` runs, `self` means `dog_b`. The same method can work with both objects because Python supplies the current object.

### How does Python supply `self`?

This call:

```python
dog_a.bark()
```

is roughly equivalent to:

```python
Dog.bark(dog_a)
```

The object is passed automatically when a method is called using `dog_a.bark()`. Do not pass it again:

```python
dog_a.bark()       # Correct
# dog_a.bark(dog_a)  # Incorrect: passes an extra argument
```

### Rules for `self`

1. Write `self` as the first parameter in a regular method, including `__init__`.
2. Do not pass `self` yourself when calling a method through an object.
3. Use `self.attribute` to save or access data belonging to that object.
4. `self` is not a reserved Python keyword; it is the standard naming convention. Always use it so other Python programmers can read your code easily.

### Common mistake: forgetting `self.`

```python
class Student:
    def __init__(self, name):
        name = name  # Incorrect: this does not save the name on the object
```

Correct version:

```python
class Student:
    def __init__(self, name):
        self.name = name  # Correct: save it on this object
```

---

## 9. ⚙️ Attributes and Methods

An **attribute** is information associated with an object. We access an attribute using a dot, such as `student.name`.

A **method** is a function defined inside a class. A regular instance method has `self` as its first parameter, so it can work with the object that called it.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_result(self):
        if self.marks >= 40:
            return f"{self.name} passed"
        return f"{self.name} needs to try again"


student = Student("Ravi", 82)
print(student.name)            # Ravi: attribute
print(student.show_result())   # Ravi passed: method call
```

| In this example | Kind | Purpose |
|---|---|---|
| `name`, `marks` | Attributes | Store this student's information |
| `show_result()` | Method | Uses the student's marks to find a result |

Parentheses call a method: `student.show_result()`. An attribute such as `student.name` is accessed without parentheses.

---

## 10. 📊 How Each Object Keeps Its Own Data

Attributes assigned using `self` belong to one particular object. These are called **instance attributes**.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


account_a = BankAccount("Ravi", 5000)
account_b = BankAccount("Asha", 8000)

account_a.balance = 6000

print(account_a.balance)  # 6000
print(account_b.balance)  # 8000: unchanged
```

Both accounts use the same class design, but each object has its own owner and balance. Changing `account_a.balance` does not change `account_b.balance`.

---

## 11. 🧠 Where Are Objects Stored?

While a Python program is running, its objects exist in the program's **memory**. A variable name such as `account_a` is best understood as a name that **refers to** an object.

```python
account_a = BankAccount("Ravi", 5000)
account_b = account_a

account_b.balance = 6500
print(account_a.balance)  # 6500
```

`account_b = account_a` does **not** create a second account. Both names refer to the same object. Changing the object's balance can therefore be seen through either name.

To create a separate account, call the class again:

```python
account_a = BankAccount("Ravi", 5000)
account_b = BankAccount("Asha", 8000)
```

Now there are two separate account objects, each with its own balance.

When an object is no longer reachable by the running program, Python can reclaim the memory it used. Beginners usually do not need to free ordinary Python objects themselves.

> **Important:** An object in memory is not automatically saved to a file. It normally exists while the program runs. To keep information after the program closes, we must deliberately save it, for example by writing it to a file. We will study file handling after this module.

---

## 12. 🔄 Object State

An object's **state** means the current values of its attributes. A bank account with a balance of `1000` has one state. After a successful withdrawal, it may have a balance of `800`, which is a new state.

```python
account = BankAccount("Ravi", 1000)  # Balance starts at 1000
account.balance -= 200               # Balance is now 800
print(account.balance)               # 800
```

Methods often change an object's state. For example, a `deposit()` method changes the balance of the account that called it.

---

## 13. 🏦 Real-Time Example: Bank Account

A bank account has **data** (owner and balance) and **actions** (deposit and withdraw). This makes it a useful example of a class.

```python
class BankAccount:
    def __init__(self, owner, starting_balance=0):
        if starting_balance < 0:
            raise ValueError("Starting balance cannot be negative")

        self.owner = owner
        self.balance = starting_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero")
            return

        self.balance += amount
        print(f"Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero")
        elif amount > self.balance:
            print("Not enough money in the account")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Balance: {self.balance}")

    def show_balance(self):
        print(f"{self.owner}'s balance is {self.balance}")


ravi_account = BankAccount("Ravi", 1000)
ravi_account.deposit(500)
ravi_account.withdraw(200)
ravi_account.show_balance()

asha_account = BankAccount("Asha", 3000)
asha_account.show_balance()
```

Output:

```text
Deposited 500. Balance: 1500
Withdrew 200. Balance: 1300
Ravi's balance is 1300
Asha's balance is 3000
```

| Part | Meaning |
|---|---|
| `BankAccount` | Class: the design for accounts |
| `ravi_account`, `asha_account` | Variables referring to separate objects |
| `owner`, `balance` | Each account's attributes |
| `deposit()`, `withdraw()`, `show_balance()` | Methods: actions related to an account |
| `self` | The account currently using a method |

This is a classroom example to teach organization. A real banking system needs much stronger security and safeguards.

---

## 14. 📚 Real-Time Example: Library Book

A library book has information, such as a title and author. It also has actions, such as being borrowed and returned.

```python
class LibraryBook:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"You borrowed: {self.title}")
        else:
            print(f"{self.title} is already borrowed")

    def return_book(self):
        self.is_available = True
        print(f"Returned: {self.title}")


book = LibraryBook("The Blue Umbrella", "Ruskin Bond")
book.borrow()
book.borrow()
book.return_book()
```

`borrow()` changes the availability of this particular book object. Another book object has its own `is_available` value.

Other real-world things we could model with classes include:

- a shopping cart, with items and an `add_item()` action;
- a game player, with a name, health, and a `take_damage()` action;
- an employee, with a name, role, and a `show_details()` action;
- a bus, with a route, passenger count, and a `board_passenger()` action.

---

## 15. ✅ Validation and Object Rules

A class can check starting information before storing it. This example makes sure marks are between 0 and 100:

```python
class Student:
    def __init__(self, name, marks):
        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100")

        self.name = name
        self.marks = marks


student = Student("Ravi", 82)  # Valid
# student = Student("Asha", 120)  # Raises ValueError
```

`raise ValueError(...)` reports that the supplied value is not acceptable. We will study exceptions in more detail in the exception-handling lesson.

This check validates the marks when the object is created. If someone later writes `student.marks = 120`, this simple class does not check that new value. More advanced ways to control later changes can be learned after the basics.

---

## 16. ↩️ Methods That Return Values

A method can print something, return a value, or do both. Returning a value makes it possible to reuse the answer elsewhere.

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


room = Rectangle(5, 4)
room_area = room.area()
print(room_area)  # 20
```

`return` sends the calculated area back to the caller. The caller can print it, save it in a variable, or use it in another calculation.

---

## 17. 🎯 When Should We Use a Class?

Consider a class when:

- your program represents many similar things, such as students or products;
- each thing needs its own group of related values;
- actions naturally use or change those values;
- you want objects to follow a consistent structure;
- the program needs rules for creating or changing those objects.

Use a simpler structure when it fits better:

| Your task | A good first choice |
|---|---|
| Store three temperatures in order | List |
| Store a person's name and city once | Dictionary |
| Represent many library books with titles and borrow actions | Class, often with a list of book objects |

> **Remember:** A class is a way to organize related data and behavior. It is a tool, not a rule that every program must use.

---

## 18. ⚠️ Common Beginner Mistakes

### 1. Forgetting `self` in a method

```python
class Student:
    def show_name():
        print("Ravi")
```

When we call `student.show_name()`, Python supplies the student object automatically. The method needs a first parameter to receive it:

```python
class Student:
    def show_name(self):
        print(self.name)
```

### 2. Forgetting `self.` when saving data

`name = name` only assigns a local variable to itself. Use `self.name = name` to store it on the object.

### 3. Mixing up an attribute and a method

```python
student.name          # Attribute: read a value
student.show_result() # Method: call an action
```

### 4. Thinking `second = first` creates a new object

It creates another name for the same object. Call the class again to create another object.

### 5. Thinking every value must be inside a class

A small script may only need variables, lists, dictionaries, and functions. Choose a class when it makes the program easier to understand or organize.

---

## 19. 📋 Quick Revision

```text
Class      → design used to create objects
Object     → one particular thing made from a class
Attribute  → data associated with an object
Method     → function defined in a class
self       → the current object using a regular method
__init__   → initializes an object's starting data
State      → the current values stored in an object's attributes
```

```python
class Example:
    def __init__(self, value):
        self.value = value

    def show(self):
        return self.value


item = Example("Hello")
print(item.show())  # Hello
```

### Final takeaway

Use a **list** to collect items, a **dictionary** to label simple values, and a **class** when you want a reusable design for similar objects that have their own data and related actions. `__init__` sets an object up, and `self` lets its methods work with the correct object.

---

## 20. ✍️ Practice Questions

Try these yourself before checking the examples above:

1. Create a `MobilePhone` class with `brand`, `model`, and `price`. Make two phone objects and print their models.
2. Add a `show_details()` method that returns the phone's brand, model, and price in one sentence.
3. Create a `Movie` class with `title` and `rating`. Add an `is_recommended()` method that returns `True` when the rating is at least 8.
4. Create two `BankAccount` objects. Deposit money into one and show that the other account's balance is unchanged.
5. Make a list with three `Student` objects. Loop through it and print each student's name and marks.
6. Explain in your own words why `self.name = name` has `self.name` on the left and `name` on the right.
7. If `second = first`, did Python make a second object? What do the two names refer to?
8. Choose a list, dictionary, or class for each task and explain your choice:
   - Store today's temperatures in order.
   - Store one person's name and city.
   - Represent many library books, each with a title and a borrow action.

---

> 💡 **Teacher note:** This guide intentionally focuses on the foundations students need first: classes, objects, `__init__`, `self`, attributes, methods, object references, and practical examples. Topics such as inheritance, encapsulation, class methods, and polymorphism can be taught after students are comfortable creating and using simple objects.
