n=int(input("enter your number= "))

if n%2==0 and n%3==0 and n%5==0 and n%7==0 and n%9==0:
    print(f"{n} is prime number")

else:
    print("not prime")