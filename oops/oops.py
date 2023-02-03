''' 
python is both COMPILER AND INTERPRETED language. 
it is mentioned that python language is interpreted. But that is half correct the python program is first compiled and then interpreted. The compilation part is hidden from the programmer thus, many programmers believe that it is an interpreted language. The compilation part is done first when we execute our code and this will generate byte code and internally this byte code gets converted by the python virtual machine(p.v.m) according to the underlying platform(machine+operating system).

$ python3 -m py_compile first.py 
the extension .PYC is the PYTHON COMPILER. 
$ cd __pycache__  # Change the Folder here. 
$ python3 first.cpython-39.pyc

Thus it has COMPILER and INTERPRETER both. 

'''
# !Data Types in Python
'''
Numeric Type >> Int, Float, Complex
Text type >> String (str)
Sequence type >> List , Tuple, Range . 
Set type >> set, Frozenset 
Boolean type >> bool 
None Type >> None  ( having NO Data Value's )
'''
# ? int, float, complex, bool, none, str, tuple(), set(), dict(), list(), bool, str() 
# type() function with python object type(python_object)  
''''
object oriented is the Programming Paradigms in Python. Programing Paradigm is the way of approach of programming technique in python. 
Python supports Multiple paradigm techniques.

1. Procedural 
2. Functional   >> foucs on ACTION Action based ( less on Data TIDE )
3. Object oriented   >> focus on DATA based and its ACTIONS>  
Real world scenarios have both the ACTION's and DATA on the scenarios So OOP is required. 

Procedural Program >> writing program LINE by LINE techniques.. Line by Line writing the program in Python. 
                Procedural >> Line By Line Execution of Program's  >> Problme is Reusability Type... 
So function Came into Picture.. Functional Programming... 

from procedural to FUnctonal approach >> it Solves the ReUSABILITY Problem in program.. you cna Reuse the problme of code re-writing in program. 

Object Oriented Program << functional << Procedural approach 

What are Objects ?  Any Real life scnearios are object. 2 properties..  Attributes ( variabls )  and Behaviour ( Action - Function)

EMail Object

attributes >> variables 
<<<  subject, contents, heading, contact_to_list >>> 
<<   Behaviours >> actions / Functions like:::   Send Email, Compose Email. 

eMail oBject >>  attributes  &&& >>  actions / Behaviours / Functions 

OOP is the approach paradigm to write the program. Focused on the Data part more. 
in Functional >> focus on the LOGIC part more...

Writing Program by Creating Classes && Objects..  
Class is the Templates.. Blueprint ...

Objects are Real for working Methods...

OOP is to solve the REAL WORLD problem...   
Inheritance >> Reusability Code
Encapsulation >> Security of Data 
Abstraction >> Data Hiding.. >> Data Hiding (Abstraction)  >> Data Security ( Encapsulation)  >> Reusablity ( Inheritance )

inheritance >> Reusablity  / Encapsulation >> Data Security   / Abstraction >> data Hiding feature of Object Oriented program 

paradigm for program 
Procedural ( Line by Line ) 
FUnction ( ReUsablity)  >> foucs on Action 
Object ( Real problem solving)  >> foucs on Data Part 

Class is a  TEMPLATE for creating an object in a program. Object represents the Real World Entity in a program. 

class == Template 
object == Real world Entity in a Program. 
Every Object belongs to certain Specific Class.  
for eg - Email Class >> object's are email1 , email 2, 3email, 4_email, 5_Email >> these are the Object for the Class Email. 

Class >> (has)  2 parts >> 1. Attributes (data)  >> 2. Methods  (Functions)

why class as Templates ?
 class represents the Plan / Structures for creating the an object. 
class collection of Objects. 
 class collection of attributes and methods. Class is User Defined data Types. UDDT. 
User Defined Data Types is Class. 

'''

x = 200 
print(type(x))
print(x)
class Apple: 
    pass

class Orange(Apple):
    pass

o = Orange()

print(type(o))  # Show the <Class ## Name   '__main__.orange'

# class is organge inside the module Name __name__  == _'_main_'_

# class Instantiation is the Object.  Object are the INSTANT Variable of Class in Python programming. 

# User defined Data Types in pythion is Class.  

# main represents that This Class Organge is prresent in current Module only. Not at Any Other Module files. 

# __main__  represents that class is present in same modulrl



# CONSTRUCTOR IS MAGIC SPECIAL METHOD THAT IS CALLED AUTOMATICALLY WHILE OBJECT IS CREATED. 
# ALL OBJECT HAS SOME PROPERTIES AND METHOD.. 

# MEMORY REPRESENTATON AND WORKIGN OF SELF VARIABLES.. 

# EMPLOYEE IS THE CLASSS .. E1 , E2 ARE OBJECT OF CLASS. 

# 1ST CLASS DEINTIONS... 
# UNTIL IT SEES OBJECTS IT WONT ALLOCATE MEMORY.. 

# OBJECT IS ALLOCATED IN HEAP MEMORY IN THE PYTHON... 

# HEAP MEMORY AT LOCATION H1 ADDRESSS... 

# SELF IS THE VARIABLE THAT CONTATIS THE MEMORY LOCATION OF CURRENT OBJECTS. PYTHON WONT ALLOCATE MEMORY UNTIL OBJECTS ARE CREATED... 

# CLASS DEFINTION NO MEMORY. HEAP MEMORY LOCATON. 

'''
1. Memory allocation to the OBJECT 
2. memory reference Returned to the object 
3. memory reference automaticllay passed to the object
4. constructor creates / initializes the variables in the memory locations. 

what is self ?
self is variable for the memory location object of address that contatins variables. 

class members = attributes ( variables ) + methods ( action / functions)
SYNTAX for Class Members Access: 
object_name.DOTnotation_attributes. 
ojbect_name.MethodName()  >> class Member's can be ACCESSED in the CLASS DEFINITION. 


BUILT- IN CLASS FUNCTIONS.. 
getattr, setattr, delattr, hasattr ( class BUILT IN functions.. )

'''

'''
4 BUILT - IN METHODS IN CLASS. 
getattr() setattr() hasattr() delattr() 

class == attributes (variables ) + mehtods / functions (actions )

__dict__ (property) shows the List of Values in the Functions.. 

'''


class Exam: 
    ''' documenation of Exam here '''
    def __init__(self,subject, marks) -> None:
        self.subject = subject
        self.marks= marks

    def display(self):
        print(f"the subject name is {self.subject} and the obtained Marks is {self.marks}")

ex1 = Exam("english", 800)
print(type(ex1))
print(getattr(ex1,'subject'))
print(getattr(ex1,'marks'))
setattr(ex1,'subject','Mathematics subject')  #Setattribute >> setattr()   getattr() functions. < #
print(ex1.display())
print(ex1.__dict__)  ##NAMESPACE OF OBJECT
delattr(ex1,'marks')  #Deletes the Attributes of the Object in Python... 
print(ex1.__dict__)
print(hasattr(ex1,"dkd"))  # Returns the BOOLEAN value to the functions 
# can be used to check the CONDITION Values with TRUE / FALSE Boolean Outcomes.. 
# if statement can be USED in the conditions... 

'''
Built in class Attributes 
__doc__  >> documentation String >> Gives the Purpose of Class (used for IMPORT Class Defintion)
__dict__  >> NAMESPACE OF CLASS 
__name__   >> Class Name 
__module__  >> Class Module Name in which class is Defined... 
__bases__  >> list of Base Class for Inheritances.. 
'''

print(Exam.__dict__)  ## Namespace of the Class Here 
print(Exam.__doc__)
print(Exam.__name__)
print(Exam.__module__)  ## can check the module name 


class one():
    '''sdfsf 23423423432 3w32423'''
    pass

print(one.__dict__)

o2 = one()
print(isinstance(o2, one))

print(isinstance(o2,one))  # this returns the value of the object ... 

class Laptop():
    ''' laptop class'''
    def __init__(self, brand, size, color) -> None:
        self.brand = brand
        self.size = size
        self.color = color 

    def display(self):
        print(f"the laptop brand is {self.brand} and size = {self.size} and has color of {self.color}")

sony = Laptop("Sony Vaio", "16 inch", "Violet")
sony.display()

print(getattr(sony, "brand"))
setattr(sony,"brand","HP")
print(sony.__dict__)
print(hasattr(sony,"brnd"),"######")  # return Boolean True or False ... 
print(delattr(sony,"color"))
print(hasattr(sony, 'color'),"####")

print(isinstance(sony,one)) # if statement with the conditions .. then only perform some operations with Conditions MATCHING VALUES... 

# OBJECT METHODS 
print(dir(sony))

print(sony.__dict__)
print(sony.__doc__)
print(sony.__module__)

print(dir(Laptop))
print("#####",Laptop.__dict__, Laptop.__doc__, Laptop.__module__, Laptop.__name__, sep='\n')

# Attributes of the Class  # attributes of the OBJECTS  
#  in functional programming , you have seen the types of variables Local variable, Global variable, Non-Local variables. 
# in OOPS programing concept, we can see the INSTANCE variables, CLASS variables... 

class Camera(object):
    photosize = "4X3 frame size"
    location = "KTM"

    def __init__(self) -> None:
        self.box = "new camera"
        self.status1 = "unopened"
        print(self.box, self.status1)
    def display(self):
        print(f"box name is {self.box} and status is {self.status1}")

    @staticmethod
    def createCamera():
        name = input("Enter the camera Name")
        range1 = input("Enter the cost range")
        print(name,range1)

    @classmethod
    def style(cls):
       return  cls.photosize, cls.location




c1 = Camera()
# Camera.createCamera()
# c1.createCamera()
# print(c1.style())
# print(c1.box)
c1.display()
# static method works with External data.. It is refered with Class NAME referecnce. Variable name in static method. 

'''
Encapsulation >> like a CAPSULE >> wrapping up data and method in a SINGLE unit is encapsulation. 
class >> CAPSULE STRUCTUR E
data >> ATTRIBUTE  , method >> FUNCTIONS ( CAPSULED in a SINGLE UNIT ) >> FORMS >> ENCAPSULATIONS 
THAT SINGLE UNIT IS  a class CLASS TYPE.... 
encapasualtion >> data cant be accessed from outside object.. object_name.variablename >> Data Hidings. types.. 



'''

class Finance(object):
    def __init__(self) -> None:
        self.__revenue = 5555
        print(self.__revenue)
    def display(self): 
        print(f"the value of reveneu{self.__revenue}")  ##Now Private variable can be accessed with METHODS here... DIRECTLY... 

f1 = Finance()
print(f1.__dict__)
f1.display()
# class HR(object):
#     def __init__(self):  ## Init is a Constructor functio that DOES not return ANYDATYPES.. 
#         # f1.__revenue = 888  ##SInce these Classes are UNRELATED then why does it access other class data and Modidfies it .. Its property of Encapsulation data types.. 
#         print(f1.__revenue)  #Creaed new varible with HR class Names.. 
#         print(f1.__dict__)
# h1 = HR()

## data member as Private so it can't be accessed.. 
# revenue was Public variale.. Only you need to have the Object Referenced to access variables.. Then you can access from ANY PLACE value. 
# public, private ,, proctected  SETTER AND getter method.. to modify the private variables.. here.. 
# Name mangling for the private variables. is stored with _classname__variableNamePrivateVariables. 
'''
Python does not have PURE encapsulation.. Only restric the data access directly.. 
Indirectly modificiation of Data access .. >> 
Python gives modules for data access.. 
polymorphism >> poly == many phism == form several 
polymorphism in python is the abilit of python OBJECT to take several different forms. 
+ operator >> Python object >> Forms different behaviours as per scenaris.. 
as per inputs it performs different behaviours.. + PLUS Operator in python.. + Operator is Python Objects.. 
len() sort () + operator  >> Polymorphism types.. 
Polymorphism example with the INheritance .. Inheritiance classes... 
polymorphisn in INBUITL methods of Python...  
you can moidfy your requriemnts for the object programming types.. 

'''
print(5+5)
print("df"+"34") 


class Car(object):
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b
    def __str__(self) -> str: # this is called Internally of the python classes.. 
        return "Ths is Car object inside CAR CAR "
    def __len__(self):  ## Now the Len function works on the Object creations values.. 
        return len(self.a) + len(self.b)

c1 = Car([3,4,5],[9,45,23])
print(c1)  # calls internally the built-ins function __str__()  STRING Representations. 
print(len(c1))  ##len function would RETURN the LENGTH number of the COLLECTIONS data Types.. 
#Ethi sis example of polymorphism.. types..  
# magic method checks the object categories to check the Length number in the list collections. 

# function taking Argument as an OBjects Types.. Object passing types.. 

class BMW(object):
    def maxspeed(self):
        print("BMW max speed")
    def fueltype(self):
        print("Diseal")

class Ferrai(object):
    def maxspeed(self):
        print("Ferari 180 ")
    def fueltype(self):
        print("Electric")
    @classmethod
    def hero(cls,one,two ):
        return one+two     

bmw = BMW()
ferrai = Ferrai()
print(type(bmw),"$$$$")
print(Ferrai.hero("one","Two"))

def callFunction(obj):
    obj.maxspeed()
    obj.fueltype()

callFunction(bmw)
callFunction(ferrai)  # function can take OBJect as an ARGUMENT Parameters... 

# passing object as an ARGUMENT to the function 

# return object as an argument to function 

def add(value):
    if value == '4':
        return bmw
    else: 
        return ferrai

n1 = '4'
n2 = add(n1)
print(n2.maxspeed())

##Returning object as an Argument from FUNCTION.. 
# Passign Object as a Parameter to function (). 
'''
opeator overloading >> assign a NEW Meaning to the operators like ADD + object , Subract - object, 
'''
x1 = 55
x2 = 45

print(x1 + x2)
# python does this operations in the 3 steps. 
# 1. check the data type of 1st operand (its INT type so then it will call the add operations __add__)
# x1 is the object thus it will call funtion beloinging of that object.. 
print(x1.__add__(x2))
print(x2.__add__(x1))
# objectName.functionName(parameterValue)
print(type(x1))
print(int.__add__(x1,x2))  #this is with CLASSNAME calling directly.... 

s1 = "dkf"
s2 = "ktm values "

print(s1.__add__(s2)) ## objecname.functionname(parameter)

# classname.functionname(par1, par2)
# dataTYPe of the lEFT SIDE funtion, GO inside the CLassName and then pass it to functions.. 

class Book(object):
    def __init__(self, title,cost) -> None:
        self.title = title
        self.cost = cost 
    def __add__(self, b): # Passes Object here with Parameters of SELF COST .. obj1.cost + PLUS obj2.cost 
        total =  self.cost + b.cost
        return Book("good", total)
    def __mul__(self,x):
        return self.cost * x.cost
    def __str__(self) -> str:  #String representation of the function cost data Values... 
        return str(self.cost)

        # __gt__ >> Greater than operator >>  


b1 = Book("Muna Madan",400)
b2 = Book("Nepali Guide",678)
b3 = Book("df",450000000)

print(b1.cost + b2.cost +b3.cost)
print(b1+b2+b3)  #Here the cost is printed like an OBJECT returned THen again the PLUS function is Called on the Python object.add() funcs 
# print(b1 * b2)