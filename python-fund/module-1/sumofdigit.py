n=int(input("enter number for sum of 4 digit= "))
sum_of_digits=0
r=0
for i in range(4):
    r = n % 10
    sum_of_digits += r
    n //= 10

print(sum_of_digits)