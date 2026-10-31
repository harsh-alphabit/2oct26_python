# Python OOP Concepts for Beginners

Object-oriented programming (OOP) is a way to organize a program around **objects**. An object keeps related data and the actions that use that data together.

This guide uses plain language, small examples, and practical situations. You can read it after learning Python variables, functions, lists, and dictionaries. The class-and-object lesson in this module covers those basics in more detail.

## Contents

1. [What is OOP?](#1-what-is-oop)
2. [Why use OOP?](#2-why-use-oop)
3. [POP and OOP](#3-pop-and-oop)
4. [Class and object basics](#4-class-and-object-basics)
5. [The four main OOP concepts](#5-the-four-main-oop-concepts)
   - [Encapsulation](#51-encapsulation)
   - [Inheritance and its types](#52-inheritance-and-its-types)
   - [Polymorphism, overloading, and overriding](#53-polymorphism-overloading-and-overriding)
   - [Abstraction](#54-abstraction)
6. [Combined example: notifications](#6-combined-example-notifications)
7. [When to use OOP](#7-when-to-use-oop)
8. [Common beginner mistakes](#8-common-beginner-mistakes)
9. [Quick revision and practice](#9-quick-revision-and-practice)

---

## 1. What is OOP?

Think of a **bicycle**. It has information, such as its color and gear, and actions, such as changing gear and braking. In a program, we can represent a bicycle as an object with data and actions.

OOP gives us a way to describe that kind of thing once, then create as many separate examples of it as we need.

| Everyday idea | Python idea |
|---|---|
| A design for all bicycles | Class |
| One particular bicycle | Object |
| Its color or current gear | Attribute (data) |
| Braking or changing gear | Method (action) |

OOP is useful when a program has groups of similar things, each with its own data and related actions. It is one way to organize code; small scripts often work perfectly well with functions and dictionaries.

## 2. Why use OOP?

For a very small task, a few variables and functions are easy to understand. As a program grows, it may have many similar things to track. Keeping every value separate and passing it to many functions can make the code harder to update and easier to mix up.

For example, a shop program may need to manage hundreds of products. Each product has a name, price, and stock count. It may also need actions such as checking stock or applying a discount. A `Product` class keeps the data and related actions in one clear place, and each product object keeps its own values.

OOP can help us:

- **Organize related code:** keep an object's data and its actions together.
- **Reuse a design:** create many objects from one class instead of writing the same structure repeatedly.
- **Keep objects' data separate:** changing one product's stock does not change another product's stock.
- **Make changes easier to manage:** a clear class can own the rules for its data and actions.
- **Extend a program:** new object types can reuse or provide their own behavior when that makes sense.

OOP does not automatically make every program better. It is most useful when the program has enough related objects and behavior to benefit from that organization.

## 3. POP and OOP

**POP** is commonly expanded as **procedure-oriented programming**; the style is also called **procedural programming**. It organizes a program around procedures (in Python, usually functions) and the steps they perform on data. **OOP** means **object-oriented programming**. It organizes a program around objects, which hold data and provide related methods.

Both approaches can solve the same problem. Python supports functions and procedural code as well as OOP, and real projects often use a mix.

| | POP (procedural-oriented programming) | OOP (object-oriented programming) |
|---|---|---|
| Main focus | Steps and functions (procedures) | Objects that hold data and provide behavior |
| Where data lives | Often in separate variables or data structures passed to functions | In attributes belonging to objects |
| How actions are organized | Functions are called with the data they need | Methods are called on the related object |
| A natural fit | Short scripts or tasks that follow a clear sequence | Programs with many similar things, each with its own data and actions |

### One small example in each style

Suppose we want to add money to a wallet.

**Procedural style (POP):** the function receives the balance and amount, then returns the new balance.

```python
def add_money(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be greater than zero")
    return balance + amount


wallet_balance = 100
wallet_balance = add_money(wallet_balance, 50)
print(wallet_balance)  # 150
```

**Object-oriented style (OOP):** the wallet object stores its balance, and its method updates that balance.

```python
class Wallet:
    def __init__(self, balance=0):
        self.balance = balance

    def add_money(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        self.balance += amount


wallet = Wallet(100)
wallet.add_money(50)
print(wallet.balance)  # 150
```

In the procedural example, the balance is passed into a function. In the OOP example, the wallet object keeps its balance and the method that updates it together. For one wallet, either approach is straightforward. If a program manages many wallets, each with its own balance and operations, objects can make it clearer which balance is being changed.

### Which one should I choose?

- Use **POP** when the task is small and reads naturally as a sequence of steps or a few functions.
- Consider **OOP** when you have many similar entities with their own data and related operations.
- Use a **mix** when it helps: for example, objects can represent customers while regular functions handle general calculations.

Neither style is always best. Choose the structure that makes the program easiest to read, explain, and change.

## 4. Class and object basics

Here is a small class. Read it from the top: `class` defines the design, `__init__` sets up a new object, and methods describe actions.

```python
class Bicycle:
    def __init__(self, color):
        self.color = color
        self.gear = 1

    def change_gear(self, new_gear):
        self.gear = new_gear

    def describe(self):
        return f"A {self.color} bicycle in gear {self.gear}"


city_bike = Bicycle("blue")
city_bike.change_gear(3)
print(city_bike.describe())  # A blue bicycle in gear 3
```

- **Class:** `Bicycle` is the reusable design that describes what a bicycle object stores and can do.
- **Object:** `city_bike` is one bicycle created from the class. Each object has its own values.
- **Attribute:** `color` and `gear` are values stored on an object.
- **Method:** `change_gear()` and `describe()` are functions defined in the class for its objects to use.
- **`__init__()`:** the setup method Python calls when a new object is created. It gives the object starting values.
- **`self`:** the current object. `self.color` means the color stored on this particular bicycle.

## 5. The four main OOP concepts

The four commonly taught OOP concepts are **encapsulation, inheritance, polymorphism, and abstraction**. These words sound formal, but each describes a practical way to organize code.

### 5.1 Encapsulation

**Simple meaning:** Keep an object's data and the methods that use it together. Use those methods to apply the object's rules.

For example, a wallet has a balance. Instead of having every part of a program change the balance however it wants, we can provide methods that apply simple rules.

```python
class Wallet:
    def __init__(self, starting_balance=0):
        if starting_balance < 0:
            raise ValueError("Starting balance cannot be negative")
        self._balance = starting_balance

    def add_money(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        self._balance += amount

    def get_balance(self):
        return self._balance


wallet = Wallet(100)
wallet.add_money(50)
print(wallet.get_balance())  # 150
```

In Python, a leading underscore in `_balance` is a **convention** that says “this is intended for internal use.” It does not make the value truly private or impossible to change. The methods provide a clear, rule-aware way to use the balance.

**Real-world use:** A shopping cart can keep its item list together with `add_item()`, `remove_item()`, and `total_price()` methods. Those methods can make sure the cart is updated consistently.

### 5.2 Inheritance and its types

**Simple meaning:** Make a new class from an existing class so it can reuse or customize behavior.

Imagine a company app with several kinds of employees. All employees have a name, but a manager also has a team size.

```python
class Employee:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hello, I am {self.name}."


class Manager(Employee):
    def __init__(self, name, team_size):
        super().__init__(name)  # Set up the name using the parent class
        self.team_size = team_size

    def describe_team(self):
        return f"{self.name} manages {self.team_size} people."


manager = Manager("Asha", 5)
print(manager.introduce())    # Hello, I am Asha.
print(manager.describe_team())  # Asha manages 5 people.
```

`Employee` is the **parent class** (also called base class). `Manager` is the **child class** (also called derived class). `Manager` inherits `introduce()` and adds `describe_team()`. `super()` lets the child use the parent's setup or behavior.

**Real-world use:** In a delivery app, `Delivery` might hold shared details such as an order number, while `BikeDelivery` and `VanDelivery` add details specific to each delivery type.

**Beginner tip:** Use inheritance when the new type really is a kind of the old type. If two things merely use one another, composition (keeping an object inside another object) may be a clearer fit.

#### Common inheritance types

These names describe how parent and child classes are connected. Python supports all of these patterns.

**1. Single inheritance — one child inherits from one parent.**

```python
class Animal:
    def eat(self):
        return "Eating"


class Dog(Animal):
    def bark(self):
        return "Woof!"
```

`Dog` inherits from one parent, `Animal`.

**2. Multilevel inheritance — a child inherits from a class that is already a child.**

```python
class Animal:
    def breathe(self):
        return "Breathing"


class Mammal(Animal):
    pass


class Dog(Mammal):
    pass
```

`Dog` inherits `breathe()` through `Mammal` from `Animal`.

**3. Hierarchical inheritance — multiple children inherit from the same parent.**

```python
class Animal:
    def eat(self):
        return "Eating"


class Dog(Animal):
    pass


class Cat(Animal):
    pass
```

Both `Dog` and `Cat` inherit from `Animal`.

**4. Multiple inheritance — one child inherits from more than one parent.**

```python
class Camera:
    def take_photo(self):
        return "Photo taken"


class Phone:
    def make_call(self):
        return "Calling"


class CameraPhone(Camera, Phone):
    pass


device = CameraPhone()
print(device.take_photo())  # Photo taken
print(device.make_call())   # Calling
```

`CameraPhone` inherits behavior from both `Camera` and `Phone`. When parent classes define methods with the same name, Python follows its **method resolution order (MRO)** to decide which implementation it finds first. Multiple inheritance can be useful, but keep it simple and learn about MRO when you need it.

**5. Hybrid inheritance — a combination of two or more inheritance patterns.**

For example, a design may combine multilevel and multiple inheritance. Hybrid inheritance is a name for the combined shape; it is not a separate Python keyword or feature.

```python
class Device:
    pass


class Camera(Device):
    pass


class Phone(Device):
    pass


class SmartCameraPhone(Camera, Phone):
    pass
```

Here, `Camera` and `Phone` inherit from `Device`, and `SmartCameraPhone` inherits from both. This combines hierarchical and multiple inheritance.

### 5.3 Polymorphism, overloading, and overriding

**Simple meaning:** Different kinds of objects can use the same method name and do the action in their own way.

For example, different payment options can all provide a `pay()` method. The checkout code can call `pay()` without needing to know each payment type's internal steps.

```python
class CardPayment:
    def pay(self, amount):
        return f"Paid {amount} using a card"


class WalletPayment:
    def pay(self, amount):
        return f"Paid {amount} using a digital wallet"


def checkout(payment_method, amount):
    print(payment_method.pay(amount))


checkout(CardPayment(), 500)    # Paid 500 using a card
checkout(WalletPayment(), 500)  # Paid 500 using a digital wallet
```

Both classes have a `pay()` method, but each one handles the call in its own way. This example uses Python's flexible approach: the objects do not need to share a parent class as long as they provide the method the code expects.

**Real-world use:** A report can have `export()` methods for PDF, CSV, and Excel output. The rest of the program can ask each report exporter to `export()` without repeating the export-selection logic everywhere.

#### Method overloading

**Method overloading** means using one method name for different input counts or types. Some languages let you write multiple methods with the same name but different parameter lists. Python does not support that form directly: if a class defines the same method name more than once, the last definition replaces earlier ones.

In Python, optional parameters are a simple way to handle a few different call patterns:

```python
class Greeter:
    def greet(self, name="there"):
        return f"Hello, {name}!"


greeter = Greeter()
print(greeter.greet())        # Hello, there!
print(greeter.greet("Mina")) # Hello, Mina!
```

One method handles both calls. This is a simple Python way to accept different call patterns; it is not the same as defining multiple methods with the same name. Python also supports **operator overloading**: a class can define special methods such as `__add__()` to give an operator like `+` a meaning for its objects.

#### Method overriding

**Method overriding** happens when a child class replaces an inherited method with its own version. Calls on child objects use the child's version.

```python
class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):  # Overrides Animal.speak()
        return "Woof!"


class Cat(Animal):
    def speak(self):  # Overrides Animal.speak()
        return "Meow!"


for animal in [Dog(), Cat()]:
    print(animal.speak())
```

Output:

```text
Woof!
Meow!
```

The same method call, `speak()`, gives behavior suited to each object's type. That is also an example of **polymorphism**. A child method can call the parent's version with `super()` when it wants to extend the inherited behavior.

### 5.4 Abstraction

**Simple meaning:** Show what an object can do while hiding the details of how it does it.

When you use an ATM, you choose “withdraw cash.” You do not need to manage every internal communication step yourself. Programs can offer a similarly clear operation.

Python's `abc` module lets us define an abstract base class. A child class must provide any abstract methods before it can be used to create objects.

```python
from abc import ABC, abstractmethod


class ReportExporter(ABC):
    @abstractmethod
    def export(self, report_text):
        """Save or send the report in a particular format."""
        pass


class TextExporter(ReportExporter):
    def export(self, report_text):
        return f"Text report: {report_text}"


exporter = TextExporter()
print(exporter.export("Monthly sales"))
```

`ReportExporter` describes the operation every exporter must provide. `TextExporter` supplies the actual steps. We cannot create a `ReportExporter` object directly because its `export()` method is abstract.

**Real-world use:** A delivery service can define a common `calculate_fee()` operation while each delivery type supplies the way its fee is calculated.

**Relationship to polymorphism:** Abstraction defines a clear operation to use; polymorphism lets different object types carry out that operation in different ways.

## 6. Combined example: notifications

This small example brings together the four ideas. A notification system can send a message by email or text. The shared interface is `send()`, while each service handles sending in its own way.

```python
from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, recipient):
        self._recipient = recipient  # Encapsulated implementation detail

    @abstractmethod
    def send(self, message):
        """Send a message using this notification type."""
        pass


class EmailNotification(Notification):
    def send(self, message):
        return f"Email to {self._recipient}: {message}"


class TextNotification(Notification):
    def send(self, message):
        return f"Text to {self._recipient}: {message}"


def notify_customer(notification, message):
    print(notification.send(message))


email = EmailNotification("sam@example.com")
text = TextNotification("555-0100")

notify_customer(email, "Your order is ready")
notify_customer(text, "Your order is ready")
```

What the example demonstrates:

| Concept | Where it appears |
|---|---|
| Encapsulation | Each notification keeps its recipient and sending behavior together. `_recipient` signals an internal-use convention. |
| Inheritance | `EmailNotification` and `TextNotification` inherit from `Notification`. |
| Polymorphism | `notify_customer()` calls `send()` on different notification objects. |
| Abstraction | `Notification` says that a notification must have `send()`, without defining the service-specific steps. |

This is a learning example. A real application would connect to email or messaging services, handle failures, protect personal data, and avoid printing private recipient information.

## 7. When to use OOP

OOP can help when:

- you need to represent many similar things, such as products, students, or orders;
- each thing has its own data and actions that use that data;
- you want new types to share behavior but customize some operations;
- a large program is easier to understand when split into objects with clear jobs.

Choose a simpler approach when it fits. A list is often enough for a group of numbers, and a dictionary can be a good choice for one simple record. Too many tiny classes can make a program harder to follow.

## 8. Common beginner mistakes

1. **Thinking a class and an object are the same.** The class is the design; an object is one instance created from it.
2. **Forgetting `self` in an instance method.** Python passes the current object as the first argument automatically.
3. **Forgetting `self.` when saving an attribute.** Use `self.name = name` to store a value on the object.
4. **Using inheritance just to avoid repeating one line.** Inheritance should describe a meaningful “is a kind of” relationship.
5. **Treating a leading underscore as real privacy.** In Python, `_value` is a convention for internal use, not an access lock.
6. **Trying to use all four concepts in every program.** They are tools; use the ones that make the code easier to understand.
7. **Putting everything into one large class.** Give a class one clear responsibility and use functions or other classes where appropriate.

## 9. Quick revision and practice

### Quick revision

| Term | Remember it as |
|---|---|
| Term | Simple definition |
|---|---|
| Class | A design for creating objects |
| Object | One item created from a class |
| Attribute | A value stored on an object |
| Method | A function defined in a class |
| Encapsulation | Keep data and related methods together, and use methods to apply rules |
| Inheritance | Create a class that reuses or customizes another class's behavior |
| Polymorphism | The same method call can work differently for different object types |
| Overloading | Use one method name for different inputs; Python handles this differently from some languages |
| Overriding | A child class supplies its own version of an inherited method |
| Abstraction | Show the needed operation and hide its implementation details |

### Practice questions

1. Create a `Book` class with a title and author. Add a method that returns a short description.
2. Create a `Vehicle` class and a `Bus` child class. Give the bus a seat count and a method that reports it.
3. Make `EmailAlert` and `AppAlert` classes that each have a `send()` method. Write one function that can use either alert.
4. In your own words, explain the difference between inheritance and polymorphism.
5. For a library system, identify one example of encapsulation and one possible abstract operation.
6. In the notification example, what would happen if a child class did not implement `send()`?

### One-line memory aid

> **Encapsulation** groups and protects usage, **inheritance** reuses and specializes, **polymorphism** gives one call different behaviors, and **abstraction** presents a simple operation while hiding its steps.
