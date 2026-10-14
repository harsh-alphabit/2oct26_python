budget = 3000

items = [
    {"id": 1, "name": "Pencil", "price": 10, "available": True},
    {"id": 2, "name": "Eraser", "price": 5, "available": True},
    {"id": 3, "name": "Notebook", "price": 50, "available": True},
    {"id": 4, "name": "Pen", "price": 20, "available": True},
    {"id": 5, "name": "Geometry Box", "price": 120, "available": True}
]

print("===== STATIONERY SHOP =====")

for item in items:
    if item["available"] == True:
        status = "Available"
    else:
        status = "Not available"

    print(item["id"], "-", item["name"], "- Rs.", item["price"], "-", status)

print("===========================")

customer_name = input("Enter customer name: ")

order = []
subtotal = 0

while True:
    item_id = int(input("Enter item ID (0 to finish): "))

    if item_id == 0:
        if len(order) == 0:
            print("Order is empty. Add an item first.")
        else:
            break

    elif item_id < 1 or item_id > len(items):
        print("Wrong item ID.")

    else:
        selected_item = items[item_id - 1]
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be more than zero.")
        else:
            order.append({
                "name": selected_item["name"],
                "price": selected_item["price"],
                "quantity": quantity
            })

            line_total = selected_item["price"] * quantity
            subtotal = subtotal + line_total

            print(selected_item["name"], "x", quantity, "=", "Rs.", line_total)
            print("Subtotal so far: Rs.", subtotal)

print("Subtotal: Rs.", subtotal)

payment = input("Pay by cash or online? ").lower()

if payment == "cash":
    discount = 0
else:
    if payment == "online":
        discount = subtotal * 5 / 100
    else:
        print("Invalid choice. No discount will be given.")
        discount = 0

after_discount = subtotal - discount
tax = after_discount * 5 / 100
final_bill = after_discount + tax

if final_bill > budget:
    print("Can't pay: bill is over the Rs.", budget, "budget.")
else:
    print("===== RECEIPT =====")
    print("Customer:", customer_name)

    for item in order:
        line_total = item["price"] * item["quantity"]
        print(item["name"], "x", item["quantity"], "=", "Rs.", line_total)

    print("Subtotal: Rs.", subtotal)
    print("Online discount: Rs.", discount)
    print("Tax: Rs.", tax)
    print("Final bill: Rs.", final_bill)
    print("Paid: Rs.", final_bill)
    print("Thank you!")

print("--- SUMMARY ---")

total_quantity = 0

for item in order:
    total_quantity = total_quantity + item["quantity"]

print("Different items:", len(order))
print("Total quantity:", total_quantity)
print("Total bill: Rs.", final_bill)

most_expensive = items[0]

for item in items:
    if item["price"] > most_expensive["price"]:
        most_expensive = item

print("Most expensive item:", most_expensive["name"], "- Rs.", most_expensive["price"])