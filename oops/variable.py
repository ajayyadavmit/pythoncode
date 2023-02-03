'''
Access Specifier for the Variables in Python... 

Private >> __Double underscore ( Name Managing will be there >> can be accessed with _ClassName__PrivatevariableName)
Protected >> _singleUnderscore ( Single Underscore will be used for the Protected variable)
Protected variable can be accessed in the Class.. 
Public >> as it is Normal.. can be accessed from anywhere 

NAME MANGLING for private variables in python..  objectName._classname__privatevariablename  (Name Mangling)

'''
'''

funcdamental concept of Object oriented programming 

Encapsulation >> any Data in object and Method to perform the functionality >> should be written in 1 place.. 
You encapsulated the data & method is OOP... 

Encapsulation should be written at 1 place only.. 
Data Abstracton >> Hiding the complex functionality 
Inheritance >> Reusablity of Code 
Polymorphism >> tkaing more than 1 Form of Code Behaviours 


DocString and Purpose in Class and Function.. 
* Function >> Function purpose bheaviours, arguments in the docstring 
Class >> attributes and Methods in Docstring 
Module >> list of classes and Functions in Modules. 
Packages >> list of Modules and Functionality 

Q. whats difference DocString vs Comments 
Comments are IGNORED by the Interpreter / Conpiler where are DOCSTRING are executed .. 
Docstrign are in Meory of pgroms.. 
COmments - purpose of statment Descriptons of Code Statement LINE BY LINE level's. 
Docstring - Purpose of Class and Fucntion actions... 


'''

class Employee(object):
    compnayName = "Tech Digits"
    _exp = "Software Engineer"
    __year = 5.5   ## Name Manging for the object varaibles... 

    def __init__(self, gender, place) -> None:
        self.gender = gender
        self.__place = place 
    
    def emp(self):
        print(f"{self.gender}, {self.__year}")

print(Employee.compnayName)
print(Employee._exp)
# print(Employee._Employee.__year)  # name mangling for the private __ double Underscore variable. 

##  Class Method for the oBject creations to make simple 
e1 = Employee("Male","Pokhara Fewa Tal")
e1.emp()

def add():
    return
x = add()
print(add())

if  x:
    print("F ONE")

'''
@classmethod decorator (relationship with CLass cls)
instance method (self) >> relationship with Object INSTANCE's 
@staticmethod (relationship) >> with External Variables data inputs.. 

absctracion hides the complex functinality with users... eg- len() len(string tuple, list etc. )
sort() len()
'''

l = [4,1,89,0]
print(l)
l.sort()
print(l)

m = ["b","a","d"]
m.sort()
print(m)  ##For soritng there are n numbe of Algorithms >> to Use these Algorithms different techniues

# Abstraction >> to hide COMPLEXITY from the user .. Encapsulation then only >> Abstractions can be achieved.. 
''''
DUNDER METHOD / MAGIC Method __name__ __len__ __sort__ 
Name Mangling >> destroy the name of variables. 
'''

print(e1.__dict__)  # objectname.__dict__ >> Gives the dictionary based output (key: value ) (pairs) () function 
# Name Mangled >> Destroyed in the object _ClassName__VariableName = Value 

print(type(e1))
# obj.__dict__ 
l = [34,22,11,788]
print(max(l,[4444,3]))


