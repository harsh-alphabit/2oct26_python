"""Real-world practice: an account has data and deposit/withdraw actions."""


class BankAccount:
    def __init__(self, owner, starting_balance=0):
        if starting_balance < 0:
            raise ValueError("Starting balance cannot be negative")

        self.owner = owner
        self.balance = starting_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Enter a deposit amount greater than zero.")
            return

        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a withdrawal amount greater than zero.")
        elif amount > self.balance:
            print("There is not enough money in the account.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def show_balance(self):
        print(f"{self.owner}'s balance is {self.balance}")


ravi_account = BankAccount("Ravi", 1000)
ravi_account.deposit(500)
ravi_account.withdraw(200)
ravi_account.show_balance()

asha_account = BankAccount("Asha", 3000)
asha_account.show_balance()  # Asha's balance is separate from Ravi's.
