
# with expression as target_var: 
#     do_something(target_variable)

# f = open("sqlite1.py","r")  # fileopen("filename","mode r, w, r+ read and write")
# print(f.read())
# f.close()
# a = input("What is your name")
# b= int(input("Enter value for B"))

# A context manager usually takes care of setting up some resource, e.g. opening a connection, and automatically handles the clean up when we are done with it. 

# A Context manager usually takes care of the resources (opening the file ) doing some operations and closing the file . 

# RAISE ERROR IN PYTHON 
# if b == 0:
#     raise ZeroDivisionError("Zeor divisino eroror")

# if a.isnumeric():
#     raise Exception("Nubers are not allowed")

# print(f"the vlaue of AA {a}")

# print(f" the B BB Value {b}")

# l = [34,55,90,"df",12,87,98]
# for i in l: 
#     print(i)
#     print(type(i))
#     if l.isalpha():
#         raise IndexError("Index Error is Raised Here ")



# Raise Error will Raise the Exception in the Program # 
## the benefit of raising Exception is to STOP the program only >>  # 
# Raise exception to STOP Program Values # 


# x = input("Enter the value")

# try:
#     print(x)
#     y = 1/0
# except ZeroDivisionError as ze:
#     print("Value is ZERO")
#     raise ZeroDivisionError(" This is divisin Error")
# except NameError as ne: 
#     print(ne)
# except Exception as e:
#     print(e)
#     print('Something went wrong')
#     if c == "harry":
#         raise ValueError("No value here")
# finally:
#     print('The try except is finished')



'''
    Try: This block will test the excepted error to occur
    Except:  Here you can handle the error
    Else: If there is no exception then this block will be executed
    Finally: Finally block always gets executed either exception is generated or not

try >> this block executes as trying the code to execute 
except >> When the exception occurs then this block of code will execute 
else >> if no exception then this block of code will be executed 
finally >> always this block of code will be executed irregards of the exceptions 
raise Keyword >> raise will be executed with the Exception name as the paramters values . This will Interrupts the Program to Stop 

Exception Types 
1. ZeroDivision Error
2. ValueError (at the run time INPUT)
3. NameError (No variable defined)
4. IndexError ( List Index Error)
5. KeyError ( Dictionary Key Error)
6. ModuleNotFoundError ( No Module Import in the file)
7. ImportError ( while importing no module found )
8. TypeError ( Type Casting doing error occurs  STR + INT ) 

'''

# l1 = [34,55,89,4,33,45,89]
# try: 
#     print(l1[5])
# except IndexError as ie: 
#     print(ie)
#     print("#"*33, "Index Error ")
# else: 
#     d = input("Ebnter the value")
#     print(f"the input value is {d}")
# finally: 
#     print("<< The program EXITS Here >>")
#     raise Exception("This is new one Exceptions")


# try except else finally  (These are BLOCK of Code to be Executed Here >>)


# with open("sqlite1.py","r+") as f: 
#     print(f.read())
#     print(f.writelines("\n\n  TEST TEST TEST HERE TEST TEST"))
#     print(f.seek(8))
#     print(f.tell())

'''

try:
    print("Starting the PRogram Execution")
    # raise IndexError # Raise will Forefully Stop the Program here 
    a = int(input("Enter the value"))
    print(a)
    print(4/a)
except ValueError as ve: 
    print("not a right values here")
else: 
    print(f" the square of the value {a*a}")
finally: 
    print("Exiting the Program BLock")

'''


value_list = [45,33,2,5,89,67]
value_dict = {'name' :"ravi", "marks" : [34,67,89]}

def list_value(*args):
    for i in args: 
        print(i)

list_value(*value_list)

def dict_value(**kwargs):
    for key, value in kwargs.items():
        print(key,value)

dict_value(**value_dict)

# function with the LIST values and the DICTIONARY values ( Key value pairs)



