n = int(input("enter your number= "))

if n < 2:
    print("not prime")
elif n == 2:
    print(f"{n} is prime number")
elif n % 2 == 0:
    print("not prime")
else:
    is_prime = True
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{n} is prime number")
    else:
        print("not prime")