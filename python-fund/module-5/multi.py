try:
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    result = num1 / num2
    print(f"result: {num1} / {num2} = {result}")

except ValueError:
    print("error: enter valid numbers only")

except ZeroDivisionError:
    print("error: cannot divide by zero")

except Exception as e:
    print(f"Unexpected error: {e}")