a=int(input("enter value for a: "))
b=int(input("enter value for b: "))
c=int(input("enter value for c: "))

if a>b and a>c:
    print("a is max")
elif b>a and b>c:
    print("b is max")
else:
    print("c is max")