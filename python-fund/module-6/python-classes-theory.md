# Python Classes and Objects — Beginner Theory

> **For Module 6:** This lesson introduces classes and objects before we move on to file handling. Read the ideas, type the examples yourself, and change the values to see what happens.

## Learning goals

By the end, you should be able to:

- explain why a class is useful and what problem it solves;
- distinguish a class, an object, an attribute, and a method;
- create objects using `__init__()`;
- explain what `self` refers to and why it appears in methods;
- understand, at a beginner level, how variables refer to objects in memory;
- decide when a list, dictionary, or class is a sensible choice.

## 1. Start with a familiar problem

Suppose a program must keep information about many students. Each student has a name, age, and marks. We also want to calculate that student's result.

With separate variables, one student might look like this:

```python
student1_name = "Ravi"
student1_age = 19
student1_marks = 82

student2_name = "Asha"
student2_age = 20
student2_marks = 91
```

This is manageable for two students. With 100 students, there could be 300 separate variables. It is also easy to accidentally combine Ravi's name with Asha's marks.

We could put each student's information in a dictionary:

```python
student1 = {"name": "Ravi", "age": 19, "marks": 82}
student2 = {"name": "Asha", "age": 20, "marks": 91}

print(student1["name"])
```

This is already much better organized. But if many functions work with students, those functions and the student data still live separately. We must also remember the exact dictionary keys, such as `"marks"`.

A **class** gives us a way to describe a student once: what information every student should have, and what actions a student can perform. Then we make one **object** for each student.

## 2. What is a class?

A **class** is a description for creating objects of a particular kind. It groups related data and the functions that work with that data.

Think of a class as a form or plan:

- A blank student registration form says which details to collect.
- Each completed form contains the details of one particular student.
- The form design is like the class; each completed form is like an object.

Another familiar comparison is a recipe and the dish made from it. The recipe describes how to make something; it is not itself the dish.

In programming, a class can describe both:

- **Attributes:** information an object stores, such as a student's name or marks.
- **Methods:** actions or behavior, written as functions inside the class, such as showing the student's result.

## 3. What is an object?

An **object** is one particular value created using a class. It is also called an **instance** of that class. The act of making an object is called **creating an instance** or **instantiation**.

```python
class Student:
    pass


student_a = Student()
student_b = Student()

print(type(student_a))
print(student_a is student_b)  # False: these are two different objects
```

`Student` is the class. `student_a` and `student_b` refer to two different objects made from it. `pass` means “there is no class code here yet”; it lets us introduce the class syntax before adding details.

By convention, Python class names use **CapitalizedWords**, such as `Student`, `BankAccount`, and `SchoolBus`. Variable and method names usually use lowercase words with underscores, such as `student_name` and `show_result`.

## 4. Our first useful class

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

The class describes the information students have. Each call to `Student(...)` makes a new student object with its own values.

## 5. `__init__()` in detail

`__init__` is a special method Python calls to **initialize** a new object's starting information. It is called automatically when we create an object by calling the class.

```python
student_a = Student("Ravi", 19, 82)
```

For now, follow this simplified sequence:

1. Python creates a new `Student` object.
2. Python calls `Student.__init__` for that object.
3. The new object is supplied as the first argument (`self`).
4. The other values, `"Ravi"`, `19`, and `82`, are supplied as `name`, `age`, and `marks`.
5. The assignments store those values as attributes on that particular object.
6. The completed object is returned by the class call and `student_a` refers to it.

In everyday beginner explanations, people sometimes call `__init__` a constructor. More precisely, `__new__` creates the object and `__init__` initializes it. For this course, remember: **`__init__` runs automatically when an object is made and sets up its initial data.**

Break down this line:

```python
self.name = name
```

- `name` on the right is the value received by the method, such as `"Ravi"`.
- `self.name` on the left means the `name` attribute belonging to this particular object.
- The assignment stores the received value on the object.

The two names do not have to match. For example, `self.name = student_name` would also work if the parameter were named `student_name`.

### What `__init__` does not do

An `__init__` method should not return the object. Python handles the class call and object creation. Normally, `__init__` has no `return` statement; returning a non-`None` value from it causes an error.

### Parameters and defaults

An object can receive different starting values. Optional parameters can have defaults:

```python
class Student:
    def __init__(self, name, age, marks=0):
        self.name = name
        self.age = age
        self.marks = marks


new_student = Student("Mina", 18)
print(new_student.marks)  # 0
```

Here, `marks` is `0` if the caller does not provide it. Required parameters must be provided; otherwise Python reports a `TypeError`.

## 6. `self` in detail

`self` means **the particular object that is currently using the method**. It is how a method can read or change that object's attributes.

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

When `dog_a.bark()` runs, `self` refers to `dog_a`. When `dog_b.bark()` runs, `self` refers to `dog_b`. The same method works with either object because `self` identifies the one currently calling it.

You can picture the call this way:

```python
dog_a.bark()
```

is roughly equivalent to:

```python
Dog.bark(dog_a)
```

Python supplies the object for `self` when we use the usual `dog_a.bark()` form. We do not write `dog_a.bark(dog_a)`.

### Rules to remember about `self`

1. Write `self` as the first parameter of a regular instance method, including `__init__`.
2. Do not pass `self` yourself when calling the method through an object.
3. Use `self.attribute` to store or access data that belongs to the object.
4. `self` is a naming convention, not a Python keyword. The code could technically use another name, but Python programmers use `self` so the code is easy to recognize.

### A common `self` mistake

```python
class Student:
    def __init__(self, name):
        name = name  # Incorrect: this only assigns a local variable to itself
```

That code does not save the name on the object. Use an attribute on `self`:

```python
class Student:
    def __init__(self, name):
        self.name = name  # Correct: save it on this object
```

## 7. Attributes and methods

An **attribute** is a value associated with an object. We access it with a dot: `student_a.name`.

A **method** is a function defined inside a class. A regular instance method receives `self`, so it can use the data belonging to the object.

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
print(student.show_result())  # Ravi passed
```

`name` and `marks` are attributes. `show_result` is a method. Notice the method reads `self.marks` and `self.name`, so it works with the object that called it.

A function outside a class can also work with student data. A method is useful when the behavior is naturally part of the object and uses that object's information. Classes do not make every function better; they give us another way to organize code.

## 8. Each object keeps its own data

Attributes created with `self` belong to a particular object. They are often called **instance attributes**.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


account_a = BankAccount("Ravi", 5000)
account_b = BankAccount("Asha", 8000)

account_a.balance = 6000

print(account_a.balance)  # 6000
print(account_b.balance)  # 8000: account_b was not changed
```

Both objects were made from `BankAccount`, but each has its own `owner` and `balance`. Changing one object's attribute does not automatically change the other object's attribute.

## 9. Where do objects get stored?

When Python creates an object, the object exists in the program's memory (often informally called RAM while the program is running). A variable such as `account_a` is a **name that refers to the object**; it is helpful to imagine it as a label or reference pointing to the object.

```python
account_a = BankAccount("Ravi", 5000)
account_b = account_a

account_b.balance = 6500
print(account_a.balance)  # 6500
```

In this example, Python did **not** create a second account. Both names refer to the same object. Updating that object's balance can therefore be seen through either name.

To make another account object, call the class again:

```python
account_a = BankAccount("Ravi", 5000)
account_b = BankAccount("Asha", 8000)
```

Now the names refer to separate objects.

When no part of a running program can reach an object anymore, Python can reclaim its memory. Beginners do not normally need to manually free ordinary Python objects. Also, an object in memory is not automatically saved to a file: it normally exists only while the program is running unless we deliberately save its data.

## 10. What problem do classes solve?

Classes help when a program has many related things that each have their own data and behavior.

Without a class, you might pass several separate values to functions:

```python
def show_student_result(name, marks):
    if marks >= 40:
        print(f"{name} passed")
    else:
        print(f"{name} needs to try again")


show_student_result("Ravi", 82)
```

This is perfectly reasonable for a small task. As the program grows, you may pass the same student's name, marks, age, and other details to many functions. It becomes easy to mix up which values belong together.

With a class, the student data travels together and related behavior can use it:

```python
student = Student("Ravi", 82)
print(student.show_result())
```

Classes can help with:

- **Organization:** related attributes and methods are kept together.
- **Consistency:** every object is created according to the same class design.
- **Multiple records:** create many objects without inventing new variable names for every field.
- **Clearer operations:** `account.deposit(500)` says what the account does.
- **Validation:** methods can check whether an operation or value makes sense.

Classes do not automatically make a program shorter, faster, safer, or more correct. The benefit is clearer organization when the problem has meaningful objects with data and behavior.

## 11. Why use a class if we already have lists and dictionaries?

Lists and dictionaries are useful. A class is not a replacement for them; it serves a different purpose. Many programs use all three together.

### Use a list for a group of values

```python
marks = [82, 91, 76]
print(marks[0])  # 82
```

A list is a good choice when you want an ordered group of items, such as marks, names, or a queue of tasks.

### Use a dictionary for labeled values

```python
student_data = {"name": "Ravi", "age": 19, "marks": 82}
print(student_data["name"])  # Ravi
```

A dictionary is a good choice for a simple record of key-value pairs, especially when the fields may vary or when you are working with data from JSON or an API.

### Use a class when the record also has behavior or rules

```python
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def has_passed(self):
        return self.marks >= 40


student = Student("Ravi", 19, 82)
print(student.name)          # Ravi
print(student.has_passed())  # True
```

| Need | A natural starting point |
|---|---|
| Keep an ordered collection of items | `list` |
| Keep a few labeled values together | `dict` |
| Create many similar entities with their own data and related behavior | `class` |

The class version does not mean a dictionary is bad. For a small, temporary record, a dictionary can be simpler. A class becomes helpful when the same kind of entity appears repeatedly and the program needs consistent structure, behavior, or rules.

### A class and a list can work together

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

Here, each student is an object and the list holds the collection of student objects. This is a common pattern.

## 12. Validation: make an object start in a sensible state

A class can check data as it is initialized. This example rejects marks outside the range 0–100:

```python
class Student:
    def __init__(self, name, marks):
        if not 0 <= marks <= 100:
            raise ValueError("Marks must be from 0 to 100")

        self.name = name
        self.marks = marks


student = Student("Ravi", 82)  # Valid
# student = Student("Asha", 120)  # Raises ValueError
```

`raise ValueError(...)` tells the caller that the supplied value is not acceptable. We will study exceptions in more detail in the exception-handling lesson. A check in `__init__` validates the starting value; if attributes are later changed directly, extra design is needed to validate those changes too.

## 13. Real-world example: a bank account

A bank account is a useful example because it has both **data** (owner and balance) and **behavior** (deposit and withdraw). The same ideas apply to a shopping cart, library book, game character, or employee record.

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

Expected output:

```text
Deposited 500. Balance: 1500
Withdrew 200. Balance: 1300
Ravi's balance is 1300
Asha's balance is 3000
```

What does the class represent here?

- `BankAccount` is the design for accounts.
- `ravi_account` and `asha_account` are separate account objects.
- `owner` and `balance` are each account's data.
- `deposit`, `withdraw`, and `show_balance` are actions an account can perform.
- `self` makes each action work on the account that called it.

In a real banking system, important financial rules and stored balances need much stronger safeguards. This classroom example teaches the organization idea; it is not banking software.

## 14. Another real-world example: a library book

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

The `is_available` value changes on this book object. A different `LibraryBook` object has its own availability value.

## 15. A method can return a value

Methods can print a message, return a value, or do both. Returning a value usually makes a method easier to reuse:

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

`return` sends the calculated area back to the caller. We can print it, store it, or use it in another calculation.

## 16. Object state: what does “state” mean?

An object's **state** is the current set of values in its attributes. A bank account with balance `1000` has a different state after a successful withdrawal changes the balance to `800`.

```python
account = BankAccount("Ravi", 1000)  # Starting state: balance is 1000
account.withdraw(200)                # The method changes the state
account.show_balance()                # Current state: balance is 800
```

Methods are often useful because they let us describe an operation on an object and update its state in one clear place.

## 17. Common beginner errors

### Forgetting `self` in a method definition

```python
class Student:
    def show_name():
        print("Ravi")
```

Calling `student.show_name()` passes the student object automatically. If the method has no `self` parameter to receive it, Python reports an argument error. Write `def show_name(self):` for a regular instance method.

### Forgetting `self.` when saving an attribute

`name = name` only deals with a local variable. Use `self.name = name` to store the value on this object.

### Calling an attribute like a method, or a method like an attribute

```python
student.name          # attribute: no parentheses
student.show_result() # method: parentheses call it
```

### Mixing up class and object names

`Student` is the class. `student_a` is a variable referring to an object. Python convention uses a capitalized class name and a lowercase object variable name to make the difference visible.

### Expecting two names to mean two objects

`second = first` gives a second name for the same object. Call the class again to create another object.

## 18. The main idea in one picture

```text
Class (design)
    |
    | call the class with values
    v
Object (one actual instance)
    ├── attributes: this object's data
    └── methods: actions that can use/change this object's data

self = the object currently using a regular instance method
__init__ = the setup method Python calls when the object is initialized
```

## 19. Practice questions

Try these before looking at the examples again:

1. Create a `MobilePhone` class with `brand`, `model`, and `price` attributes. Create two phone objects and print each model.
2. Add a `show_details()` method that returns the phone's brand, model, and price in one sentence.
3. Create a `Movie` class with `title` and `rating`. Add an `is_recommended()` method that returns `True` when the rating is at least 8.
4. Create two `BankAccount` objects. Deposit into one and show that the other balance stays the same.
5. Make a list containing three `Student` objects. Use a loop to print each student's name and whether they passed.
6. In your own words, explain why `self.name = name` has `self.name` on the left and `name` on the right.
7. If `second = first`, did Python create another object? Explain what both names refer to.
8. For each need, choose a list, dictionary, or class and explain why: (a) store today's temperatures in order; (b) store one person's name and city; (c) represent many library books, each with a title and a borrow action.

## 20. Quick review

| Term | Beginner meaning |
|---|---|
| Class | A description used to make objects of a kind |
| Object / instance | One particular thing created from a class |
| Attribute | Data associated with an object |
| Method | A function defined in a class, often acting on an object |
| `__init__` | The method Python calls to initialize an object's starting data |
| `self` | The current object passed to a regular instance method |
| State | The current values stored in an object's attributes |

### Final takeaway

Use a **list** to collect items, a **dictionary** to label simple values, and a **class** when you want a reusable design for similar objects that have their own data and related actions. An object keeps its own state; `self` lets its methods work with that state; and `__init__` sets the object up when it is created.
