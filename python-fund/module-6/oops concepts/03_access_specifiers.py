"""Python visibility styles and the important difference between _ and __.

Python does not enforce public/protected/private access like some languages.
One underscore is a convention. Two leading underscores cause name mangling.
See access_specifiers_flow.svg in this folder for a visual summary.
"""


class Example:
    def __init__(self):
        # These three attributes show Python's common naming styles.
        self.public_name = "Anyone can use this normally"  # Public: ordinary attribute.
        self._internal_note = "One underscore: please treat as internal"  # Convention only; still directly accessible.
        self.__private_like = "Two underscores: name mangling is applied"  # Renamed internally to reduce accidental clashes.

    def read_private_like(self):
        # This method provides a normal way to read the double-underscore value.
        return self.__private_like  # Class methods can use the private-like attribute.


# BASIC EXAMPLE: make an object, then look at its differently named attributes.
item = Example()
print("Basic public:", item.public_name)
print("Basic internal convention:", item._internal_note)  # Accessible, but treat as internal.
print("Basic private-like via method:", item.read_private_like())
# You can technically reach the mangled name, but normally use the class method instead.
print("Name-mangled form (for learning only):", item._Example__private_like)

# Remember the difference:
# _name  -> Python leaves the name alone; the underscore is a polite warning.
# __name -> Python changes it to _ClassName__name to help avoid accidental clashes.
# Neither form is a security barrier. Do not put secrets in either attribute.


# REAL-WORLD EXAMPLE: expose a safe operation for the bank PIN.
class BankAccount:
    def __init__(self, owner, pin):
        # Save the provided account details on this new account object.
        self.owner = owner       # Public: other code can normally read the owner's name.
        self._attempts = 0       # One underscore: internal-use hint; still accessible as account._attempts.
        self.__pin = pin         # Two underscores: name becomes _BankAccount__pin inside Python.

    def check_pin(self, entered_pin):
        # Compare the typed PIN with the saved value and return True or False.
        self._attempts += 1  # Update an internal-use counter each time the method is called.
        return entered_pin == self.__pin


account = BankAccount("Leela", "2468")  # Create a sample account for this lesson.
print("Real world:", account.owner, "PIN correct?", account.check_pin("2468"))
# Python naming conventions are not security. Never keep real PINs as plain text.
