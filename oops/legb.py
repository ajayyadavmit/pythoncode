# LEGB rules.  >> local  , enclosed, global , built-IN rules for variables.. 
# local enclosed global builtin variables. 

# LEGB RULES IN THE PYTHON FOR THE VARIABLES SCOPE IN THE FUNCTIONAL PROGRAMMING APPROACH..... 

# THIS is SCOPE where you can access the variables in the programming. 


def output():
    a = print
    a("gnene")  # Another name for the print functions to make SHORTCUT variables.. 

output()

## you can use the GLOBAL VARAIBLE inside the function code. 

x = 111

## global access types.. 
def variable():  ## non local 
    '''sdfsf'''
    # global x  # Indicates the variables to be used inside the functional programming parts. 
    x = 34
    print(x)  # access the global variables 
    x = x + 50 
    print(x)
    def inner():   ##Local function >> Local variables Generations 
        # nonlocal x
        global x
        x = x+121
        print(x)
    inner()
    # x = 50  # local variables Inside the Function. 
    
# print(x)  # Gives the NAMEERROR since variable is DEFINED inside the function.. so it does NOT have GLOBAL SCOPE part. 

variable()

# local variable >> inside the function defintions 
# non - local  >> also called ENCLOSED variables.. non -local === ENCLOSED 
# global variable 
# built -in >> Overall scope part 
# global nonlocal builtins >> LEGB rules  local non-local (Enclosed variables) global BuiltINS 

# LEGB rules decides the scope of the variables in the program.. which variables program should have ACCESS... on what basis.. >>
'''
2 types of variables in OOP 
Instance variable 
class variables 

class has Namespace and in that namespace memory location it will have variables inside present. 
Instance variables are ASSOCIATED with the OBJECTS... These objects will have specific individual memory
location for the variables allocations types. 

instance variables can be accessed, set, deleted outside the class.. So one variables won't be affecting the othe variables types. 

instance variable >> instance METHOD >> can be allocated by the SELF keyword. SELF is used 
for the memory location accessing. 

'''

class student():
    collegeName = "Tribhuwan University"
    yearOfExperience = 1
    def __init__(self, name, course) -> None:
        self.name = name 
        self.course = course
    def display(self): 
        print(f"{self.name} and {self.course}")

    def change(self):  # self is marketed for the INSTANCE method / function . 
        self.name = input("Enter the Name of Student")
        self.course = input("Enter the COURSE details of Student")

    @classmethod
    def classvariable(cls):
        print(f"the Name of College {cls.collegeName}")
    @classmethod   ## class Method has to take the INPUT's parameters from the Class structure list.
    def onetwo(cls):
        print(" ONE TWO TWO ")
        print(cls.collegeName)
    @classmethod 
    def three(cls):
        cls.yearOfExperience = 4
        print(cls.yearOfExperience)


s4 = student("hari Bahadur","Electronic Communication Engineering")
s4.display()
print(s4.__dict__)
print(s4.collegeName)
## class variable can be accessed by all objects through SAME DOT notations parts. 
student.collegeName = "Kathmandu UNIVERSTIY College"
print(s4.__dict__)
print(s4.collegeName)
s4.collegeName = "Pokhara"  # creation of INStance variable NOT class variables.. 
print(s4.__dict__)
print(student.collegeName)
student.classvariable()
student.onetwo()
student.three()
# s1 = student("ram", "CSE")  # instance constructor called here ...  
# s1.display()  # instance method called 
# print(s1.__dict__)

# for _ in range(5):
#     s1.change()
#     s1.display()
#     print(s1.__dict__)  ##Namespace for th Object Memory details allocations... 

## instance method , instance variable ( worked with SELF keyword )
## class variables declared at Class Level's.. only 1 COPY for the Class variables is there. . 
# class variables is there for all the Objects in  class scope level. 
# modification of class variables can impact all the objects there. 
# example  of class variables >> Bonus percentage, YearofserviceInCompany, companyname, location.. 
# class variable >> className.classVariable  >> className_classVariable. cls 

# @classmethod  # decorator for the class Method inside the CLass Types. @classmethod 
# first argument is the class / cls  in the class method... && for instance method first argument is SELF keyword... 

#instance method class method instance variable  class variable 
# local enclosed nonlocal global variable builtins variables.. 
# instance methods >> are of two types >> Setter method  && Getter Method.. Setter method >> set values of Variables..   >> Getter method -- GET values of Variables.. 



class Home():
    __amount = 55
    bike = 453
    def setname(self,name): # SETTER FUNCTION NAME 
        self.name = name
    
    def getname(self):  # GETTER FUNCTION NAME >>> 
        print(f"the name details is {self.name}")
    def privatevariable(self):
        self.__location = input("Enter locaton")
        self.__age = int(input("Enter age"))
        self.__amount = int(input("Enter Amount Values"))
    def displayprivate(self):
        print(f"{self.__amount}  and {self.__age}  age && location {self.__location}")

h1 = Home()
h1.setname(input("Enter the Name"))
h1.getname()

h2 = Home()
h2.setname(input("Enter the Name"))
h2.getname()
print(h1.__dict__)
print(h1.bike)
# print(h1.__amount)
h1.privatevariable()
h1.displayprivate()

## instance method (object data) , class method ( class data )
# static method ( external data ) >> does not belong on class or object 
# @staticmethod @classmethod 
# id(python OBJECT )  >> id for unique identifier ... 

print(id(h1))
print(id(Home))
print(bin(5))
