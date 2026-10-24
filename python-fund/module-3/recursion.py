'''
Recursion is when a function calls itself to solve a smaller version of 
the same problem.
A recursive function needs:
1) A base case that stops the calls
2) A recursive call that moves toward the base case
'''

def factorial(n):
    if n == 0 or n == 1:  
        return 1
    return n * factorial(n - 1)

print(factorial(5))  