try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    print("Sum:",A+b)
except Exception as e:
    print(e)
else:
    print("This is else block!")