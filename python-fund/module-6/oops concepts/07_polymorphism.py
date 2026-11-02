"""Polymorphism: the same call works with different object types."""


# BASIC EXAMPLE: different report types respond to the same method call.
class TextReport:
    def show(self):
        # This report's version of show() returns text-report behavior.
        return "Showing a text report"


class SalesReport:
    def show(self):
        # Same method name, but this report supplies different behavior.
        return "Showing a sales report"


for report in [TextReport(), SalesReport()]:
    print("Basic:", report.show())  # Same call; the object decides what it does.


# REAL-WORLD EXAMPLE: checkout can use different payment objects.
class CardPayment:
    def pay(self, amount):
        # Return a message describing how this payment object handles the amount.
        return f"Paid ${amount:.2f} by card"


class WalletPayment:
    def pay(self, amount):
        # The same operation is implemented for a different payment type.
        return f"Paid ${amount:.2f} from digital wallet"


def checkout(payment_method, amount):
    # This function can work with either payment object because both have pay().
    # It doesn't need to know the payment object's internal steps.
    print("Real world:", payment_method.pay(amount))


checkout(CardPayment(), 25)  # Try checkout with a card payment object.
checkout(WalletPayment(), 25)
