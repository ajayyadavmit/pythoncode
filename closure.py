# # python CLOSURE allocates the FUNTION Variable CODE to some outpute Numbers.. 
# since function will be destroyed once it is called out . thus the value of function will NOT be stored in the memory. 
# This is done by the CLOSURE techniques. 
# Which will allocate the function output number to the certain CODE base value. 
# ALIAS / Function / Function name / CLOSURE 
# Used in the Decorators 
# Decorators are the FUNCTION only  which takes the Parameter as the FUnction FN() defined. 

# with the Closure Techniques you can do assign variables to the Code Number Outputs. 

def outer(f1):
    def inner():
        f1()
        print("Inside Inner")
        print(id(inner) ,"inner")
    return inner

# using the Decorators for the functions 
@outer
def one():
    print("Inside One function")

# aone = outer(one)  # creating the ALIAS functio with the Output variables. 
# aone()  # calling the Alias function 
# print(id(aone), "alias function")
# print(id(outer), "outer func")
# # print(type(outer(one)))

one()

