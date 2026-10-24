#Use *args when you want a function to accept any number of positional arguments. 
# Python collects them into a tuple.

def add_all(*args):
    total = 0
    for number in args:
        total += number
    return total

print(add_all(2, 3))       # 5
print(add_all(2, 3, 4, 5)) # 14



#Use **kwargs when you want a function to accept any number of keyword arguments.
#  Python collects them into a dictionary.

def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

show_details(name="harsh", age=23)