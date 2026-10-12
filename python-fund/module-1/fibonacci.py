n=int(input("enter range for fibonacci  series = "))

a=0
b=1
for i in range(n):
    print(a, end=" ")
    c=a+b
    a=b
    b=c
