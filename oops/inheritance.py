'''
@property  // Decorator for the making the behavirou of function as variables.. 
@price.setter  // setter()  Getter() properties .. >> for seting the function names.. 
@ is for the decorators symbol.s..  

constructor == init() function method inside the class. COnstructor function init() are called AUTOMATICALLY in the class when the object is CREATED. 

Child >> Constructor >> if NOT present >> then Python Interpreter would call the Parent COnstructor
__dict__  >> shows the child DICTIONARY details functions (). 
'''
'''
class Father():
    def __init__(self) -> None:
        self.caste = "yadav"
        self.location = "Kathamndu"
#Constructor priority of exection is SON class then only it looks for the Father constructor class. 

class Son(Father):
    def __init__(self) -> None:
        print(super())
        self.price = 4000

class grandson(Son):
    pass
## Here the SON class would by DEFAULT call the Father Constructor function () for INITIALIZATION techniques. 

class Father2: 
    pass 
s1 = Son()
print(s1.__dict__)  ## Son Constructor is Executed Here if there is NO Father Constructore then Only.. .  
f1 = Father()
print(f1.__dict__)
g1= grandson()
print(g1.__dict__)
print(isinstance(g1,Father2))
print(hasattr(g1,"nskd"))
'''

'''
super() function returns the Parent object. then you can call the function name on that objects to execute it. 
with super() function , we can call the Parent class Properties.. ( attibutes , methods )
super().functioname >> SIMILAR >> objectName.functionName()  
this function returns a Temporary object that will call other functions.. 
'''

# class Computer(object):
#     def __init__(self,weight,color) -> None:
#         self.storage = weight
#         self.ram = color
#     def display(self):
#         print(f"the storage is {self.storage} and color is {self.ram}")

# class Mobile(Computer):
#     def __init__(self,wt,c) -> None:
#         super().__init__(wt,c)  ## super Passes the FUnctional Object of Parent Class and Initi is Constructor of object. 
#         self.size = "4x55"
#         self.price = 3400

# c1 = Computer(54,"redpurple")
# m1= Mobile(34,44)
# print(c1.__dict__)
# print(m1.__dict__)

# OBject >> Parent >> Child >> Grandchild 
# Default constructor of OBJECT class INherited on Parent Basis. 
# class variables in Inheritance prpeorty & Methods.. 
# LEGB rule >> local enclosed nonlocal global builtin variables. 

# Single multilevel inheritance hieararchical inheretiance.. 
# 1 paretn class >> creates multiple CHILD class is called as HIERARCHICAL inheritances. 

# child 1 cannot access child 2 properties in inhieritances.. 
'''
Hierarchical inhertiance Multiple child Single inheiri Multilevelinher Hiearchical inehr

multiple inhericancr >> multiple Parent class and 1 CHILD class is there. 
Multiple Inheritance >> multiple parent class (dervied from OBJECT Class)  >> has >> 1 Child Class inheritances. 
order is importanct . L to R ..   Left to Right order for attritubtes , prpeprty 

'''

class Country(object):
    place = "Nepal"
    def __init__(self) -> None:
        super().__init__()
        print("Country class contutru")
        self.office = "Country"

class Home(object):
    place = "janakpur"
    def __init__(self) -> None:
        super().__init__()
        self.office = "HOme"
        print("HOme Class Constructor ")

# order of execution is from Left to Right >> Super().init() passes from l to right CONTROL..  
class Person(Country, Home): # ORder of priority is from Left to Rigth for Class variables, Class Method, Static Method, Instance method etc... 
    def __init__(self) -> None:
        super().__init__()
        # self.office ="Person"
        print("Person Class Constructure")

p1 = Person()
print(p1.place)
print(p1.office)
print(p1.__dict__)

c1 = Country()
print(c1.office)
print(Country.place)
print(c1.place)

'''
MRO >> METHOD RESOLUTION ORDER in INHERITANCE.. HOW THE PROPERTIES AD METHOD , ATTRIBUTES ARE SEARCHEDNI IN INHERITANCES. 
HYBRID inhertances ( P1, p2 >> Child >> GrandChild1   , GrandChild2  Classes )
for these resolution order, we have MRO (Method Resoltion order inheritance properties...)
method resoultion order mro 
1st rule >> 1st rule in Child class 
2nd rule >> Depth first from LEFT TO right order 


Cyclic inheritance  >> Class inhertis from same class. is cyclic inheritances.. 

Encapsulation >> OOP >> Definting attribute & method workign Together single UNIT 
Encapsultioant >> OOP >> Method + Attributes Wrapped in a Single Unit .. >> leads to ABSTRATIONS> 

capsule == class  & in capsule Method || Attributes 

method resoution order mro () in the class to know the rule of inheritance types in pgrogma. 

'''

class A(object):
    pass
class B(X):
    pass
class C(object):
    pass
class X(A,B,C):
    pass
class Y(B,C):
    pass
class P(X,Y):
    pass

class M(X,A,C):
    pass

print(A.mro())
print(M.mro())
print(B.mro())