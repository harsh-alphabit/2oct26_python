menu = {
	1: ("Burger", 120),
	2: ("Pizza", 300),
	3: ("Salad", 90.50),
	4: ("Fries", 450),
}

total = 0


while True:
	for number, (item, price) in menu.items():
		print(f"{number}) {item} - {price}")
	print("(0) = finish order")

	try:
		choice = int(input("choose an item number: "))

		if choice == 0:
			break
		if choice not in menu:
			print("please choose a number from the menu")
			continue

		quantity = int(input("how many would you like? "))
		if quantity <= 0:
			print("quantity must be greater than zero")
			continue

		item, price = menu[choice]
		item_total = price * quantity
		total += item_total
		print(f"added {quantity} {item}(s): {item_total}")

	except ValueError:
		print("Please enter a valid number")

print(f"\nYour total is: {total}")

