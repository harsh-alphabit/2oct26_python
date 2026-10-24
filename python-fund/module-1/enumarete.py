
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

print("\nWith start=1:")
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
