# --- Example 2: When an error DOES occur ---

try:
    result = 10 / 0
    print("try: This line will NOT run")
except ZeroDivisionError:
    print("except: Caught division by zero!")
else:
    print("else: This will NOT run because there was an error")
finally:
    print("finally: This ALWAYS runs — cleanup happens here.")

# Output:
#   except: Caught division by zero!
#   finally: This ALWAYS runs — cleanup happens here.
