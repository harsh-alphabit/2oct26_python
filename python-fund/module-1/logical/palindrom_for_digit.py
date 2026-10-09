number = int(input("Enter a number: "))

original = number
reversed_number = 0

while number > 0:
	digit = number % 10
	reversed_number = reversed_number * 10 + digit
	number //= 10

if original == reversed_number:
	print("palindrome number")
else:
	print("not a palindrome number")
