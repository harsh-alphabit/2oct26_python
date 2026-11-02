"""Encapsulation: keep data and its rule-following methods together."""


# BASIC EXAMPLE: the counter keeps its number and the methods that use it together.
class Counter:
    def __init__(self):
        # Give every new counter its own starting value.
        self._value = 0  # Attribute stores the count; _ suggests internal use by convention.

    def increase(self):
        # The object changes its own count instead of requiring outside code to calculate it.
        self._value += 1  # Method changes the value in a controlled way.

    def get_value(self):
        # Return the count so other code can read it through a clear method.
        return self._value


counter = Counter()  # Create a counter object; its value starts at zero.
counter.increase()  # Ask the object to update its own value.
print("Basic:", counter.get_value())


# REAL-WORLD EXAMPLE: the cart checks prices and calculates its own total.
class ShoppingCart:
    def __init__(self):
        self._items = []  # The cart keeps its own list of item names and prices.

    def add_item(self, name, price):
        # Add one (name, price) pair. First reject invalid prices to keep the cart sensible.
        if price < 0:
            raise ValueError("Price cannot be negative")
        # A tuple keeps this item's name and price together in the list.
        self._items.append((name, price))

    def total(self):
        # Add the price from every (name, price) pair and give the result back.
        return sum(price for name, price in self._items)


cart = ShoppingCart()  # Start with a new, empty cart.
cart.add_item("Notebook", 3.50)  # Call the cart's method to add an item.
cart.add_item("Pen", 1.25)
print("Real world: cart total =", cart.total())
