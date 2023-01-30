# import pdb Module 

# print(locals())

# print(globals())

# def add(a,b):
#     return a+b

# a = input("Enter A Value")
# b = input("Enter B value")


# c = add(a,b)

# print(c)

'''
Debuggin >>  De + Bug  ( Dig  BUG find out )
Debugging is the PROCESS of finding BUGS or ERRORS in the program CODE. 

BreakPoint allows you to STOP the PROGRAM at certain POINT so you can DEBUG your Code well.  

Debug Types >> 
a. Breakpoint >> Just Stop the program Code running at Certain STEPS factor. 
b. Conditional Breakpoint >> Stop the program with Some Condition  condition can be like 
i. Variable name   (    a == 45 )  ( {a}  {self.name} )
c. Log Message >> This is used to incase to STOP the PRINT() command factor. Log will give the message in 
DEBUG CONSOLE OUTPUT Window.

Area Types: 
Variables ( Local / Global ) options >> Give the "Variable Definitions" & its Values. 
WATCH ( you can see the SPECIFIC Value of Variable)
BREAKPOINTS  ( you can call breakpoints when EXCEPTIONS are RAISED or occured in program)

import pdb   # python Debugging Module 
Module contains Python Class and Function related by the Developer. 

'''

# l1 = []

# for i in range(5):
#     a = input("Enter the value")
#     l1.append(a)

# print(l1)

# for i in l1:
#     print(i + "df")

# try:
#   print(x)
# except:
#   print('An exception occurred')

''' 
class User: 
    v2 = "new"
    _v3 = "hero"
    def __init__(self, name, place) -> None:
       self. __name = name
       self.__place = place
    def getname(self):
        return self.__name

    def getplace(self):
        return self.__place
    def setvalue(self):
        v1 = 54
        return v1, v2
    def __str__(self) -> str:
        return f"the name of person {self.__name} and palce is {self.__place}"

user1 = [User("Ram","KTM"), User("shyam","np"),User("hari","pk")]

u1 = User("Ram","KTM")
print(u1)

print(u1.getname())
# u1.__name
print(u1.v2)
print(u1._v3)

'''


'''
CALL STACK >>  maintains the RECORD of the FUNCTION. 
Call Stack helps to Maintain the MEMORY of the Function for the ORDER of EXECUTION of function (). 

Without Call Stack >> Python Can NOT maintain the order of execution of function. 

>> AREA IS CALLED >> FUNCTION STACK 

'''

# def fn1():
#     print("fn 1111")

# def fn2():
#     print("fn 2222")

# def fn3():
#     fn1()
#     fn2()
#     fn1()
#     fn2()

# fn3()

# 5!  =5  x 4 x 3 x 2 x 1 

# Call stack can be simulated well with RECURSIVE example where first 1st it calls the fileName.py then Function (). 

# def recursion(n):
#     if n == 1:
#         return 1 
#     else:
#         return n * recursion(n-1)

# print(recursion(5))

'''

LOCAL & GLOBAL Variables >> they are SUPPOSED to function placeholder for Values of Variables.

'''

import pdb


g1 = 5 
pdb.set_trace()
l1 = 10
def g11():
    global g1 
    g1 = 15
    l1 = 1111
    a = input("Enter a value")
    print(g1,l1)

# print(g11)


g11()
print(g1)


'''
python has several INBUILD Variable NAME's That will help to DEFINE the variable Name and its VALUE. 

__name__
__file__


'''

'''
pdb.settrace()  >> to pause the command for debug with PDB module 

commands types: 

l  >>  line no of code shows 
n  >> next line 

c >> continue execution 
q  >> quit the program 


'''