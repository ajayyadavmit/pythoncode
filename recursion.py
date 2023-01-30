# def recursion(n):
#     if n ==1: 
#         return 1
#     else:
#         return n* recursion(n-1)

# b = int(input("Enter the value for Fibanocci Calculations"))
# print(recursion(b))

# def iterative(b):
#     fact = 1
#     for i in range(b):
#         fact = fact * (i+1)
#     return fact

# print(f"The RECURSIVE Value {iterative(b)}")

# iterative is in the For loop with the Range() function value of 0 to (n-1) values. 
# factorial 5! = 5 x 4 x 3 x2 x1

a = int(input("Enter the number for FACTORIAL"))

''' 
import time
t1 = time.time()
def factorial(a):
    if a ==1:
        return 1
    else:
        return a * factorial(a-1)

print(f" the factoiral values are {factorial(a)}  and time calcuations {time.time() -t1} seconds")

t2 = time.time()
def iterations(a):
    fact = 1
    for i in range(a):
        fact = fact * (i+1)
    return fact

print(f"The value ITERATIONS are {iterations(a)} and the time calcuations {time.time() - t2} seconds")
print(f" t2 seconds {t2}")
'''
# 0 1 1 2 3 5 8 13 
# INDEX numbers 
# 1 2 3 4 5


def fibonacci(a):
    if a == 1 or a == 2:
        return a
    else:
        print(a)
        return fibonacci(a-1) + fibonacci(a-2)

print(fibonacci(a))


# recursion BASE COnditno should be there some Value as the Base Values. .. 

# Recursive Funtion are function which are executed by their call to itselfs values.. 

import sys 

print(sys.getrecursionlimit())  # Shows the Recursive Limit calling of the funtions .. in SYS module sys.getrecursionlimit()

sys.setrecursionlimit(300)

counter = 0
def demo():
    global counter
    counter += 1
    print("hellos", "counter", counter)
    demo()

# demo()  # RecursionError: maximum recursion depth exceeded while calling a Python object
# # Python has Maximum Recursive function limits depth of 1000.  

# Recursive function can call itself functions. 
