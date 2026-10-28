## WHAT IS AN EXCEPTION?

An exception is an ERROR that happens DURING the execution of a program. When Python encounters an error, it "raises" an exception and the program STOPS immediately — unless we handle it.

Think of it like this:
Syntax Error  → Python can't even READ your code (typo)
Exception     → Python can read your code, but something goes WRONG while running it

```

 --- Example : ZeroDivisionError ---
 Dividing any number by zero is mathematically undefined
 Uncomment below to see the error:
 result = 10 / 0   # ZeroDivisionError: division by zero

```

# other examples
1) NameError
2) TypeError
3) ValueError
4) IndexError
5) KeyError
6) FileNotFoundError


# note
Without exception handling, even ONE error will crash your entire program That's why we use try/except to handle errors gracefully and keep the program running


### CATCHING SPECIFIC EXCEPTIONS ###

Using bare "except:" catches ALL errors --> which is bad
because it hides bugs you didn't expect

ALWAYS catch the SPECIFIC exception you expect

# ex
```
try:
    number = int("hello")
except:
    print("Something went wrong!")

```

insteadf do this

```

try:
    number = int("hello")
except ValueError:
    print("ValueError: You entered text instead of a number!")

```

## --- Using "as e" to get the error message ---
 "as e" stores the error details in variable 'e'

```
try:
    marks = [85, 90, 78]
    print(marks[10])
except IndexError as e:
    print(f"IndexError occurred: {e}")
    # Output: IndexError occurred: list index out of range

```



### COMPLETE try / except / else / finally EXPLAINED

try:       → Code that MIGHT cause an error
except:    → Runs ONLY if an error occurs in try
else:      → Runs ONLY if NO error occurred in try
finally:   → Runs ALWAYS — error or no error

Flow diagram:

  try block runs
       |
       ├── Error?  YES → except runs → finally runs
       |
       └── Error?  NO  → else runs   → finally runs

```
# --- Example 1: When NO error occurs ---
try:
    result = 10 + 5
    print(f"try: Calculation successful! Result = {result}")
except Exception as e:
    print(f"except: Error occurred — {e}")
else:
    print("else: No error! We can safely use the result.")
finally:
    print("finally: This ALWAYS runs — cleanup happens here.")

# Output:
#   try: Calculation successful! Result = 15
#   else: No error We can safely use the result.
#   finally: This ALWAYS runs — cleanup happens here.

```

```
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

```

## WHEN TO USE WHAT?

else    → Put code that should run ONLY on success(keeps try block small and focused)

finally → Put CLEANUP code here (closing files, closing database connections, 
          releasing resources) It runs even if you use "return" inside try



### NESTED try / except BLOCKS

You can put a try/except INSIDE another try/except.
The inner block handles its own errors. If it can't handle
an error, the error "bubbles up" to the outer block.


```
students_data = [
    {"name": "Ravi", "marks": "85", "total": "100"},
    {"name": "Priya", "marks": "abc", "total": "100"},    # Bad marks
    {"name": "Amit", "marks": "90", "total": "0"},         # Division by zero
    {"name": "Sneha", "marks": "78", "total": "100"},
]

try:
    print("Processing all student records...\n")

    for student in students_data:
        try:
            name = student["name"]
            marks = int(student["marks"])      # Could raise ValueError
            total = int(student["total"])
            percentage = (marks / total) * 100  # Could raise ZeroDivisionError

            print(f"  ✅ {name}: {percentage:.1f}%")

        except ValueError:
            print(f"  ❌ {student['name']}: Invalid marks data!")
        except ZeroDivisionError:
            print(f"  ❌ {student['name']}: Total marks is zero!")

    print("\nAll records processed successfully!")

except Exception as e:
    # Catches any unexpected error in the overall process
    print(f"\nFatal error in processing: {e}")
    
```

KEY POINTS:
1. Inner try/except handles errors at a GRANULAR level
2. Outer try/except acts as a SAFETY NET
3. If inner block can't handle it, it bubbles UP
4. This pattern is great for processing LISTS of items
   — one bad item doesn't stop the whole process


