# ! for else loop in the python language 

'''
common construct is to run a loop until something is found and then to break out of the loop. The problem is that if I break out of the loop or the loop ends I need to determine which case happened. One method is to create a flag or store variable that will let me do a second test to see how the loop was exited.

For example assume that I need to search through a list and process each item until a flag item is found and then stop processing. If the flag item is missing then an exception needs to be raised.

Using the Python for...else construct you have

for i in mylist:
    if i == theflag:
        break
    process(i)
else:
    raise ValueError("List argument missing terminal flag.")

#######################

Compare this to a method that does not use this syntactic sugar:

flagfound = False
for i in mylist:
    if i == theflag:
        flagfound = True
        break
    process(i)

if not flagfound:
    raise ValueError("List argument missing terminal flag.")

In the first case the raise is bound tightly to the for loop it works with. In the second the binding is not as strong and errors may be introduced during maintenance.


for else  while else  break continue Keywords 
syntactic sugar is syntax within a programming language that is designed to make things easier to read or to express. It makes the language "sweeter" for human use: things can be expressed more clearly, more concisely, or in an alternative style that some may prefer.
'''



x = [34,3,1,2,5,65,89,90]

for i in x: 
    print(i)
    if i == 5:
        break   # Due to break statement the ELSE part is not executed in loop
else: 
    print("In the ELSE block of FOR loop")

for i in x: 
    print(i)
    if i ==5:
        continue  # ELSE Part of loop is executed 
else: 
    print("inside ELSE block of FOR loop")

x = len(x)

while x: 
    print(f"value of {x}")
    x -=1
    if x ==3:
        break
else:
    print("inside WHILE ELSE BLOCK part")

for i in range(55,80,2):
    print(f"hello {i}")


# try except else finally block parts 

try: 
    print(x)

except Exception as e: 
    print(e.args)

else: 
    print("Inside the TRY ELSE Block")
    print("Executed ONLY WHen there is no Exception in the TRY Block")
finally: 
    print("Always executed in the TRY BLOCK of FINALLY")

