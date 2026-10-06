a=int(input("enter value of a = "))
b=int(input("enter value of b = "))

print("="*20)
print("1) press 1 for addition")
print("2) press 2 for sub")
print("3) press 3 for div")
print("4) press 4 for multi")
print("5) press 5 for divi")
choice=int(input("enter your choice : "))



if choice==1:
    print(f"addition for {a} + {b} = {a+b}")

elif choice==2:
    print(f"subtraction for {a} - {b} = {a-b}")

elif choice==3:
    print(f"division for {a} / {b} = {a/b}")

elif choice==4:
    print(f"multiplication for {a} * {b} = {a*b}")

elif choice==5:
    print(f"modulo for {a} % {b} = {a%b}")

else:
    print("enter valid number")



