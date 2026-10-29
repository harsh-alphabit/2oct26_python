"""Concept: objects from one class keep their own instance attribute values."""


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


account_one = BankAccount("Ravi", 5000)
account_two = BankAccount("Asha", 8000)

account_one.balance = 6000  # Change only Ravi's account.

print(account_one.owner, "has", account_one.balance)
print(account_two.owner, "has", account_two.balance)  # Still 8000.
