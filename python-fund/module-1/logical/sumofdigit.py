n=int(input("enter number for sum of 4 digit= "))
sum_of_digits=0
r=0
for i in range(4):
    r = n % 10  # 1234 -> 123.4 and takes 4 in r
    sum_of_digits += r  
    n //= 10   # 123.4 = 123

print(sum_of_digits)