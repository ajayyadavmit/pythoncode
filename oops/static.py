'''
Static method are class methods that can access class methods variables .... 
static method works on external data to operate.. NOT on the Class Variables and Objects Variables.. 
static method has NO CONNECTION with objcts.. but logically connection with Class. 
static method is used when some processing is related to CLASS BUT does NOT need the Instance or objects to perform. 
Static method has LOGICAL connection with Class. 
when we want to work on external data by passing values from outside and process it in methods. 
Decorator @staticmethod is used to define. 

NOrmal FUncction with no Parameter SELF / CLS...  
instance method  >> self keywrod on instance variables. 
class method >> cls on Class variable 
static method >> No use of Object and Class variables, only logical connection with Class. 
'''


class Bank(object):
    roi = 8.45

    @staticmethod
    def interest(p,yr):
        print(Bank.roi * p *yr) 

    def instanceInterest(self,roi):
        self.roi = roi
        print(self.roi)
    @classmethod
    def classInterest(cls):
        roi = cls.roi
        print("class",roi)


b1 = Bank()
b1.instanceInterest(5)
b1.classInterest()
Bank.interest(2,3)

# Instance Method (SELF), Class Method (CLS) CLS.variableName, @staticmethod Static Method (workon External data's)  @staticmethod 
# Parent class Base Class Existing class Super class >> OLD Class  >> Super Class >> Parent class Base Class 
# Child Class > Sub Class >  child >> Derived class 
# Method can be class static instance COnstructors  methods.. 

'''

Inherithance method in 

Class EmployeeBankAccount  
methods >> Reusable types.. 
Class Customer : 
methods >> Reusable 

Keywords  === Reserved words  == special meaning & special Operations in Pythons... 
22 Keywords 


import keyword
print(len(keyword.kwlist))

python memory allcoaion is for Values  Not variables.. for VALUES not a VARIABLES... 
EFFICIENT MEORY MANAGEMENT.. >> GARBAGE COLLECTORS. >>
variable >> name // Tag to Values.. 

id() function returns the UNIQUER IDENTIFIER FOR the OBJECT.. PYTHON IS OBJECT ORIENT LANGU. 
id() func returns the unique identificer for object.. id()  unique identifier of object. 
'''
print(bin(7))
x = 5
print(id(x))

# variale name should be in LOwer Case letter.. Class name should be in Upper Case Letter. 
# meaningful name should be there. Separated by Underscore letter fruits_mangoes fruits_orange 
x,y,z = 5,4,"ram" # multiple variable assignments here.... Multiple Values for Variables Assignment's... 
print(x,y,z)
x=y=z=10
print(z)
x =y=z = 40
print(y)

function & function call in python ... 
Printer >> inputs >> Text & Images >> Process'es  Text & Images and then Printers the Outputs.. 

function ( input >> Parameters... )  >> Process & Computations  >> Output or Return Values.. in Function.. 

function_name(parameters/ arguments )
python everything is considered as object... function is also as OBJECT.. 

print(function_name)  ## Returns the Memory Address .. it gives the function name address object... 
id(function)

data type is the Category of the Data .... 
a = 5  # integer category of data ... 

5 is python object.. 
inbuilt data types ,,, user defined datat ypes.. Python Object  object 
data types are Classes  and variables are Object of Class... 


class a(object):  # Multi Level Inheritances....   
